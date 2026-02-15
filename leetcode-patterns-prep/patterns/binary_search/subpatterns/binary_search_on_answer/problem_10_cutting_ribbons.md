# Cutting Ribbons

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Binary Search on Answer
**Link:** https://leetcode.com/problems/cutting-ribbons/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array `ribbons` where `ribbons[i]` is the length of ribbon `i`, and an integer `k`, cut ribbons into pieces of **equal length** such that you get at least `k` pieces. Find the **maximum possible length** of each piece. Return `0` if impossible.

### 2. Clarification Questions

- **Input constraints?** `1 <= ribbons.length <= 10^5`, `1 <= ribbons[i] <= 10^5`, `1 <= k <= 10^9`
- **Edge cases?** If `k > sum(ribbons)`, impossible even with length 1 -> return 0. Single ribbon of length `L` with `k = 1` -> answer = `L`.
- **Expected output?** A single integer — max piece length (or 0).
- **Can input be modified?** Yes, but no need.

### 3. Brute Force Approach

- **Idea:** Try every length from `max(ribbons)` down to 1. For each length, count pieces. Return the first length yielding >= k pieces.
- **Time:** O(max(ribbons) * n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** If we can get `k` pieces of length `L`, we can also get `k` pieces of length `L-1` (more pieces from each ribbon). The piece count is **monotonically non-increasing** as length increases. Binary search on the length to find the **maximum** valid value.

- **Time:** O(n * log(max(ribbons)))
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(max(ribbons) * n) | O(1) | Slow for large ribbon lengths |
| Optimized | O(n * log(max(ribbons))) | O(1) | ~17 iterations of binary search |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Binary search on piece length in `[1, max(ribbons)]`
- This is a **maximize** problem — use upper-mid
- Feasibility: count total pieces via `ribbons[i] // length`
- Return 0 if even length 1 doesn't yield k pieces

```python
from typing import List

def maxLength(ribbons: List[int], k: int) -> int:
    # Quick check: even cutting into 1-length pieces isn't enough
    if sum(ribbons) < k:
        return 0

    lo, hi = 1, max(ribbons)

    while lo < hi:
        mid = (lo + hi + 1) // 2    # upper-mid for maximize
        # Feasibility: can we get k pieces of length mid?
        pieces = sum(r // mid for r in ribbons)

        if pieces >= k:
            lo = mid        # feasible — try longer pieces
        else:
            hi = mid - 1    # not enough pieces — shorten length

    return lo
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `ribbons = [9, 7, 5], k = 3`

`sum = 21 >= 3`. `lo = 1, hi = 9`

| Length (mid) | Pieces per ribbon | Total | Feasible? |
|--------------|------------------|-------|-----------|
| mid=5 | [1, 1, 1] | 3 | Yes -> lo=5 |
| mid=7 | [1, 1, 0] | 2 | No -> hi=6 |
| mid=6 | [1, 1, 0] | 2 | No -> hi=5 |
| lo=5, hi=5 -> return 5 |

**Output:** `5` (correct: cut 9->5+4, keep 7->5+2, keep 5)

### Edge Case Testing

- **Empty input:** Constraints guarantee n >= 1.
- **Single element:** `ribbons = [10], k = 3` -> 10//3 = 3 pieces of length 3, answer = 3.
- **Typical case:** Shown above.
- **Extreme values:** `k = 10^9` with small ribbons -> likely returns 0. `k = 1` -> return `max(ribbons)`.

### Complexity

- **Time:** O(n * log(max(ribbons))) — binary search with O(n) feasibility check.
- **Space:** O(1) — constant extra space.

### Optimization Discussion

This problem is **structurally identical** to Maximum Candies Allocated to K Children (LC 2226). The ribbon = candy pile, pieces = sub-piles. Recognizing these equivalences speeds up interview problem-solving.

**Pattern family:** Cutting Ribbons, Maximum Candies, Koko Eating Bananas, Capacity to Ship — all use the same binary search on answer template with minor variations in the feasibility check.

### Follow-up Variations

- What if ribbons have different values per unit length? (Becomes a knapsack-like problem.)
- What if cuts have a cost? (Greedy or DP approach needed.)
- What if pieces don't need to be equal length but must be within a range `[L, R]`?

### Common Traps

- **Returning 0 when impossible.** The `sum(ribbons) < k` check catches this before binary search.
- **Using lower-mid for a maximize problem.** Use `(lo + hi + 1) // 2` with `lo = mid` to avoid infinite loops.
- **Off-by-one with `lo` and `hi`.** Since we search in `[1, max(ribbons)]`, `lo = 1` ensures no division by zero.
- **This is a premium (locked) problem.** Practice the identical free problem LC 2226 (Maximum Candies) instead if needed.
