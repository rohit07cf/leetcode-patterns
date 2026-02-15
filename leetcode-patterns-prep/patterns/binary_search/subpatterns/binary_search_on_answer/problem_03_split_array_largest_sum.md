# Split Array Largest Sum

**Difficulty:** Hard
**Pattern:** Binary Search
**Subpattern:** Binary Search on Answer
**Link:** https://leetcode.com/problems/split-array-largest-sum/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Split an integer array `nums` into `k` **non-empty contiguous subarrays** such that the **largest subarray sum** among the `k` subarrays is **minimized**. Return that minimized largest sum.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 1000`, `0 <= nums[i] <= 10^6`, `1 <= k <= min(50, nums.length)`
- **Edge cases?** `k == len(nums)` means each element is its own subarray, answer = `max(nums)`. `k == 1` means answer = `sum(nums)`.
- **Expected output?** A single integer — the minimized largest subarray sum.
- **Can input be modified?** Yes, but no need.

### 3. Brute Force Approach

- **Idea:** DP — `dp[i][j]` = min largest sum when splitting first `i` elements into `j` subarrays. Try all split points.
- **Time:** O(n^2 * k)
- **Space:** O(n * k)

### 4. Optimized Approach

- **Core Insight:** Binary search on the answer. If the max allowed subarray sum is `target`, greedily check if we can split into `<= k` subarrays where each sum <= `target`. The answer space `[max(nums), sum(nums)]` is **monotonic**: larger targets need fewer splits.

- **Time:** O(n * log(sum(nums)))
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| DP | O(n^2 * k) | O(n * k) | Exact but slower |
| Binary Search | O(n * log(sum(nums))) | O(1) | Elegant, interview favorite |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Binary search on the maximum allowed subarray sum in `[max(nums), sum(nums)]`
- Greedy feasibility: scan left-to-right, accumulate sum; when exceeding `target`, start a new subarray
- If splits needed <= `k`, the target is feasible — search left for a smaller target

```python
from typing import List

def splitArray(nums: List[int], k: int) -> int:
    lo, hi = max(nums), sum(nums)

    while lo < hi:
        mid = (lo + hi) // 2
        # Feasibility: can we split into <= k subarrays each with sum <= mid?
        splits = 1
        current_sum = 0

        for num in nums:
            if current_sum + num > mid:
                splits += 1       # start a new subarray
                current_sum = 0
            current_sum += num

        if splits <= k:
            hi = mid        # feasible — try smaller max sum
        else:
            lo = mid + 1    # too many splits — allow larger max sum

    return lo
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [7, 2, 5, 10, 8], k = 2`

`lo = 10, hi = 32`

| Target (mid) | Greedy splits | Splits | Feasible? |
|--------------|---------------|--------|-----------|
| mid=21 | [7,2,5] [10,8] | 2 | Yes -> hi=21 |
| mid=15 | [7,2,5] [10] [8] | 3 | No -> lo=16 |
| mid=18 | [7,2,5] [10,8] | 2 | Yes -> hi=18 |
| mid=17 | [7,2,5] [10] [8] | 3 | No -> lo=18 |
| lo=18, hi=18 -> return 18 |

**Output:** `18` (correct: `[7,2,5]` sum=14, `[10,8]` sum=18)

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `nums = [5], k = 1` -> returns 5.
- **Typical case:** Shown above.
- **Extreme values:** All zeros -> returns 0. One huge element -> that element is the answer.

### Complexity

- **Time:** O(n * log(sum(nums))) — binary search range is at most sum(nums), each check is O(n).
- **Space:** O(1) — greedy check uses constant space.

### Optimization Discussion

This problem is **identical in structure** to "Capacity to Ship Packages Within D Days" (LC 1011). The ship capacity = max subarray sum, and days = number of subarrays. Recognizing this equivalence is key.

### Follow-up Variations

- What if subarrays don't need to be contiguous? (Becomes a sorting + greedy problem.)
- What if we want to maximize the minimum subarray sum instead? (Flip the binary search condition.)
- Painter's Partition Problem — same problem with different flavor text.

### Common Traps

- **Forgetting that `lo = max(nums)`.** Every element must fit in some subarray, so the max sum must be at least the largest element.
- **Confusing this with "exactly k splits" vs "<= k splits."** Greedy with <= k works because using fewer splits with a given max is always possible by merging adjacent subarrays.
- **Not recognizing the equivalence** with shipping/allocation problems. Practice mapping between problem flavors.
