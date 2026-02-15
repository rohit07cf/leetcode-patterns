# Koko Eating Bananas

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Binary Search on Answer
**Link:** https://leetcode.com/problems/koko-eating-bananas/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Koko has `n` piles of bananas. She can eat at most `k` bananas per hour (one pile at a time, even if she finishes early). Find the **minimum integer eating speed `k`** such that she can eat all bananas within `h` hours.

### 2. Clarification Questions

- **Input constraints?** `1 <= piles.length <= 10^4`, `1 <= piles[i] <= 10^9`, `piles.length <= h <= 10^9`
- **Edge cases?** `h == len(piles)` means she must eat each pile in 1 hour, so `k = max(piles)`. `h` is very large means `k = 1`.
- **Expected output?** A single integer — the minimum eating speed.
- **Can input be modified?** Yes, but no need to modify it.

### 3. Brute Force Approach

- **Idea:** Try every speed from `1` to `max(piles)`. For each speed, calculate total hours needed. Return the first speed that fits within `h`.
- **Time:** O(max(piles) * n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** The answer space `[1, max(piles)]` is **monotonic** — if speed `k` works, then `k+1` also works. Binary search on this monotonic answer space to find the minimum valid `k`.

- **Feasibility check:** For a given speed `k`, hours needed = `sum(ceil(pile / k))` for each pile. If total hours <= `h`, the speed is feasible.

- **Time:** O(n * log(max(piles)))
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(max(piles) * n) | O(1) | TLE when max(piles) is 10^9 |
| Optimized | O(n * log(max(piles))) | O(1) | ~30 iterations of binary search |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Binary search on speed `k` in range `[1, max(piles)]`
- For each candidate `k`, compute total hours using `ceil(pile / k)`
- If feasible (total <= h), search left for a smaller speed; otherwise search right

```python
import math
from typing import List

def minEatingSpeed(piles: List[int], h: int) -> int:
    # Answer lies in [1, max(piles)]
    lo, hi = 1, max(piles)

    while lo < hi:
        mid = (lo + hi) // 2
        # Feasibility: can Koko finish at speed mid within h hours?
        hours_needed = sum(math.ceil(p / mid) for p in piles)

        if hours_needed <= h:
            hi = mid        # feasible — try slower speed
        else:
            lo = mid + 1    # too slow — need faster speed

    return lo
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `piles = [3, 6, 7, 11], h = 8`

| Speed (mid) | Hours per pile | Total | Feasible? |
|-------------|---------------|-------|-----------|
| lo=1, hi=11, mid=6 | [1,1,2,2] | 6 | Yes -> hi=6 |
| lo=1, hi=6, mid=3 | [1,2,3,4] | 10 | No -> lo=4 |
| lo=4, hi=6, mid=5 | [1,2,2,3] | 8 | Yes -> hi=5 |
| lo=4, hi=5, mid=4 | [1,2,2,3] | 8 | Yes -> hi=4 |
| lo=4, hi=4 -> return 4 |

**Output:** `4` (correct)

### Edge Case Testing

- **Empty input:** Constraints guarantee at least 1 pile — not applicable.
- **Single element:** `piles = [5], h = 5` -> speed = 1. `piles = [5], h = 1` -> speed = 5.
- **Typical case:** Shown in dry run above.
- **Extreme values:** `piles = [10^9], h = 1` -> speed = 10^9. Binary search handles this in ~30 steps.

### Complexity

- **Time:** O(n * log(max(piles))) — binary search over `max(piles)` values, each check scans all `n` piles.
- **Space:** O(1) — no extra data structures.

### Optimization Discussion

Using `(p + mid - 1) // mid` instead of `math.ceil(p / mid)` avoids floating point issues and is slightly faster. Both are correct here since we work with positive integers.

### Follow-up Variations

- What if Koko can switch piles mid-hour? (Removes ceiling — becomes a simpler division problem.)
- What if there are multiple Kokos eating in parallel? (Divide total work among workers.)

### Common Traps

- **Lower bound of 1, not 0.** Dividing by 0 crashes. Minimum speed must be at least 1.
- **Using `math.ceil` with integer division.** `ceil(p / k)` with Python 3 int division truncates — must use `math.ceil(p / k)` or `(p + k - 1) // k`.
- **Setting `hi = max(piles)` not `sum(piles)`.** Eating faster than the largest pile gains nothing since she eats one pile per hour slot.
