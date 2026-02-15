# Maximum Candies Allocated to K Children

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Binary Search on Answer
**Link:** https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array `candies` where `candies[i]` is the number of candies in pile `i`, and `k` children, split piles into sub-piles of **equal size**. Find the **maximum number of candies** each child can get. Each child gets at most one sub-pile. Return `0` if not possible.

### 2. Clarification Questions

- **Input constraints?** `1 <= candies.length <= 10^5`, `1 <= candies[i] <= 10^7`, `1 <= k <= 10^12`
- **Edge cases?** If `k > sum(candies)`, return 0 (not enough candy). If `k == 1`, return `max(candies)` or `sum(candies)` depending on interpretation (it's `sum // 1` effectively max pile contribution).
- **Expected output?** A single integer — max candies per child (or 0).
- **Can input be modified?** Yes, but no need.

### 3. Brute Force Approach

- **Idea:** Try every possible allocation size from `max(candies)` down to 1. For each size, count how many sub-piles we can make. Return the first size that yields >= k sub-piles.
- **Time:** O(max(candies) * n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** If we can give each child `c` candies, we can also give them `c-1`. The count of sub-piles is **monotonically decreasing** as the allocation size increases. Binary search on the allocation size to find the **maximum** valid value.

- **Feasibility check:** For a given size `c`, each pile `candies[i]` produces `candies[i] // c` sub-piles. If total sub-piles >= k, it's feasible.

- **Time:** O(n * log(max(candies)))
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(max(candies) * n) | O(1) | TLE for large values |
| Optimized | O(n * log(max(candies))) | O(1) | ~24 binary search iterations |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Binary search on allocation size in `[1, max(candies)]`
- This is a **maximize** problem — use upper-mid to avoid infinite loops
- Feasibility: count total sub-piles via integer division
- Handle the edge case where total candies < k (return 0)

```python
from typing import List

def maximumCandies(candies: List[int], k: int) -> int:
    # Quick check: not enough total candy
    if sum(candies) < k:
        return 0

    lo, hi = 1, max(candies)

    while lo < hi:
        mid = (lo + hi + 1) // 2    # upper-mid for maximize
        # Feasibility: can we give k children mid candies each?
        sub_piles = sum(c // mid for c in candies)

        if sub_piles >= k:
            lo = mid        # feasible — try larger allocation
        else:
            hi = mid - 1    # not enough sub-piles — shrink allocation

    return lo
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `candies = [5, 8, 6], k = 3`

`sum = 19 >= 3`. `lo = 1, hi = 8`

| Size (mid) | Sub-piles per pile | Total | Feasible? |
|------------|-------------------|-------|-----------|
| mid=5 | [1, 1, 1] | 3 | Yes -> lo=5 |
| mid=7 | [0, 1, 0] | 1 | No -> hi=6 |
| mid=6 | [0, 1, 1] | 2 | No -> hi=5 |
| lo=5, hi=5 -> return 5 |

**Output:** `5` (correct: split [8] into [5,3], take [5],[5],[6])

### Edge Case Testing

- **Empty input:** Constraints guarantee n >= 1.
- **Single element:** `candies = [10], k = 3` -> 10//3 = 3 sub-piles of size 3, answer = 3.
- **Typical case:** Shown above.
- **Extreme values:** `k = 10^12` with small piles -> likely returns 0.

### Complexity

- **Time:** O(n * log(max(candies))) — binary search with O(n) feasibility check.
- **Space:** O(1) — constant extra space.

### Optimization Discussion

The `sum(candies) < k` early check avoids entering binary search when even allocating 1 candy per child is impossible. Without it, binary search still works but the early exit is cleaner.

### Follow-up Variations

- What if children can receive multiple sub-piles? (Sum up, answer = `sum(candies) // k`.)
- What if piles cannot be split? (Greedy assignment of whole piles.)
- Cutting Ribbons (LC 1891) — nearly identical problem structure.

### Common Traps

- **Returning 0 when impossible.** If total candies < k, no allocation works.
- **Using lower-mid for a maximize problem.** Causes infinite loop. Use `(lo + hi + 1) // 2` with `lo = mid`.
- **Division by zero.** Since `lo` starts at 1, `mid` is always >= 1, so `c // mid` is safe.
- **Large `k` (up to 10^12).** Make sure the sum comparison doesn't overflow in typed languages.
