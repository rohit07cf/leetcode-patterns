# Magnetic Force Between Two Balls

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Binary Search on Answer
**Link:** https://leetcode.com/problems/magnetic-force-between-two-balls/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given `n` basket positions and `m` balls, place the balls into baskets such that the **minimum magnetic force** (distance) between any two balls is **maximized**. Return that maximized minimum distance.

### 2. Clarification Questions

- **Input constraints?** `2 <= n <= 10^5`, `2 <= m <= n`, `1 <= position[i] <= 10^9`
- **Edge cases?** `m == 2` means place at first and last sorted position. `m == n` means every basket gets a ball, answer = min gap between consecutive sorted positions.
- **Expected output?** A single integer — the maximized minimum distance.
- **Can input be modified?** Yes — we need to sort positions.

### 3. Brute Force Approach

- **Idea:** Try all combinations of `m` baskets from `n` positions. For each combination, compute the minimum pairwise distance. Return the max over all combinations.
- **Time:** O(C(n, m) * m)
- **Space:** O(m)

### 4. Optimized Approach

- **Core Insight:** Binary search on the answer (the minimum distance). If we can place `m` balls with minimum distance `d`, we can also place them with minimum distance `d-1`. This **monotonicity** enables binary search. Greedy placement validates each candidate distance.

- **Feasibility check:** Sort positions. Place the first ball at position[0]. Greedily place each subsequent ball at the first position that is >= `d` away from the last placed ball.

- **Time:** O(n * log(n) + n * log(max_dist))
- **Space:** O(1) (excluding sort)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(C(n,m) * m) | O(m) | Combinatorial explosion |
| Optimized | O(n log n + n log(max_dist)) | O(1) | Sort once, then binary search |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort positions first
- Binary search on minimum distance in `[1, position[-1] - position[0]]`
- Greedy feasibility: place balls left-to-right, skip positions too close to the last placed ball

```python
from typing import List

def maxDistance(position: List[int], m: int) -> int:
    position.sort()

    lo, hi = 1, position[-1] - position[0]

    while lo < hi:
        mid = (lo + hi + 1) // 2    # upper-mid because we maximize
        # Feasibility: can we place m balls with min distance >= mid?
        balls_placed = 1
        last_position = position[0]

        for i in range(1, len(position)):
            if position[i] - last_position >= mid:
                balls_placed += 1
                last_position = position[i]
                if balls_placed == m:
                    break

        if balls_placed >= m:
            lo = mid        # feasible — try larger distance
        else:
            hi = mid - 1    # can't place enough balls — shrink distance

    return lo
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `position = [1, 2, 3, 4, 7], m = 3`

Sorted: `[1, 2, 3, 4, 7]`, `lo = 1, hi = 6`

| Min dist (mid) | Placement | Balls placed | Feasible? |
|-----------------|-----------|--------------|-----------|
| mid=4 | [1, _, _, _, 7] | 2 | No -> hi=3 |
| mid=2 | [1, _, 3, _, 7] | 3 | Yes -> lo=2 |
| mid=3 | [1, _, _, 4, 7] | 3 | Yes -> lo=3 |
| lo=3, hi=3 -> return 3 |

**Output:** `3` (correct: balls at positions 1, 4, 7)

### Edge Case Testing

- **Empty input:** Not possible per constraints (n >= 2, m >= 2).
- **Single element:** Not possible (n >= 2).
- **Typical case:** Shown above.
- **Extreme values:** Two positions far apart with m=2 -> answer = distance between them.

### Complexity

- **Time:** O(n log n + n * log(max_pos - min_pos)) — sorting plus binary search with O(n) check.
- **Space:** O(1) — aside from sorting (language-dependent).

### Optimization Discussion

This is a **maximize the minimum** problem — a classic binary search on answer variant. The key difference from "minimize the maximum" problems: use **upper-mid** `(lo + hi + 1) // 2` and adjust `lo = mid` / `hi = mid - 1` to avoid infinite loops.

### Follow-up Variations

- What if balls have different sizes/weights affecting force?
- What if positions are on a 2D grid? (Distance metric changes, greedy may not work.)
- Aggressive Cows (SPOJ) — identical problem, classic competitive programming version.

### Common Traps

- **Forgetting to sort positions.** The greedy check assumes sorted order.
- **Using lower-mid for a maximize problem.** This causes an infinite loop. When searching for the maximum valid value, use `mid = (lo + hi + 1) // 2` with `lo = mid`.
- **Early termination.** Break out of the greedy loop once `m` balls are placed for a small speedup.
