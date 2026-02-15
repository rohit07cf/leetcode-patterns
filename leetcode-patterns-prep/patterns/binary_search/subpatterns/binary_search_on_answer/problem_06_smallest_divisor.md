# Find the Smallest Divisor Given a Threshold

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Binary Search on Answer
**Link:** https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array `nums` and an integer `threshold`, find the **smallest positive integer divisor** such that the sum of `ceil(nums[i] / divisor)` for all elements is **<= threshold**.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 5 * 10^4`, `1 <= nums[i] <= 10^6`, `nums.length <= threshold <= 10^6`
- **Edge cases?** `threshold == n` means each element contributes at least 1, so divisor must be `max(nums)`. Large threshold means divisor = 1.
- **Expected output?** A single integer — the smallest valid divisor.
- **Can input be modified?** Yes, but no need.

### 3. Brute Force Approach

- **Idea:** Try every divisor from 1 to `max(nums)`. For each, compute the division sum. Return the first divisor where the sum <= threshold.
- **Time:** O(max(nums) * n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** Larger divisors produce smaller sums. The sum is **monotonically decreasing** as the divisor increases. Binary search on the divisor to find the smallest one where the sum fits within the threshold.

- **Time:** O(n * log(max(nums)))
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(max(nums) * n) | O(1) | TLE for large values |
| Optimized | O(n * log(max(nums))) | O(1) | ~20 iterations of binary search |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Binary search on divisor in `[1, max(nums)]`
- For each candidate divisor, compute `sum(ceil(num / divisor))` for all elements
- If sum <= threshold, divisor is valid — search left for a smaller one

```python
import math
from typing import List

def smallestDivisor(nums: List[int], threshold: int) -> int:
    lo, hi = 1, max(nums)

    while lo < hi:
        mid = (lo + hi) // 2
        # Compute division sum with divisor = mid
        total = sum(math.ceil(num / mid) for num in nums)

        if total <= threshold:
            hi = mid        # valid — try smaller divisor
        else:
            lo = mid + 1    # sum too large — need bigger divisor

    return lo
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [1, 2, 5, 9], threshold = 6`

`lo = 1, hi = 9`

| Divisor (mid) | ceil results | Sum | Feasible? |
|---------------|-------------|-----|-----------|
| mid=5 | [1,1,1,2] | 5 | Yes -> hi=5 |
| mid=3 | [1,1,2,3] | 7 | No -> lo=4 |
| mid=4 | [1,1,2,3] | 7 | No -> lo=5 |
| lo=5, hi=5 -> return 5 |

**Output:** `5` (correct)

### Edge Case Testing

- **Empty input:** Constraints guarantee n >= 1.
- **Single element:** `nums = [10], threshold = 1` -> divisor = 10 (ceil(10/10) = 1).
- **Typical case:** Shown above.
- **Extreme values:** All elements = 1 -> any divisor gives sum = n, so answer = 1 if n <= threshold.

### Complexity

- **Time:** O(n * log(max(nums))) — binary search over divisor range, each check is O(n).
- **Space:** O(1) — no extra storage.

### Optimization Discussion

**Integer ceiling trick:** `math.ceil(a / b)` can be replaced with `(a + b - 1) // b` to avoid float conversion. This is faster and avoids potential floating-point precision issues.

```python
total = sum((num + mid - 1) // mid for num in nums)
```

### Follow-up Variations

- What if we want the **largest** divisor such that the sum >= threshold? (Flip the search direction.)
- What if each element has a weight that multiplies its contribution?

### Common Traps

- **Divisor starts at 1, not 0.** Division by zero is undefined.
- **Using floor instead of ceiling.** The problem explicitly says division results are rounded **up**.
- **Constraint guarantee.** `threshold >= nums.length` ensures divisor = `max(nums)` always works (each element contributes at least 1), so a valid answer always exists.
