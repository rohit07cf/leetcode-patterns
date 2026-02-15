# Minimum Operations to Reduce X to Zero

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Minimum Window Pattern
**Link:** https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an integer array `nums` and an integer `x`, return the minimum number of operations to reduce `x` to exactly zero. In one operation, you remove either the leftmost or rightmost element and subtract its value from `x`. Return `-1` if impossible.

### 2. Clarification Questions
- Input constraints? `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^4`, `1 <= x <= 10^9`.
- Edge cases? `x` equals total sum (remove everything), `x = 0` (zero operations), single element.
- Expected output? Minimum number of operations (removals), or -1.
- Can input be modified? Yes.

### 3. Brute Force Approach
- **Idea:** Try all combinations of taking elements from left and right using recursion/memoization.
- **Time:** O(n^2) with memoization on (left_count, right_count) states.
- **Space:** O(n^2)

### 4. Optimized Approach
- **Core Insight:** Removing elements from the edges is equivalent to **keeping a contiguous subarray in the middle**. If we remove elements summing to `x`, the remaining middle subarray sums to `total - x`. So we need the **longest** subarray with sum `total - x`. Minimizing removals = maximizing the kept middle.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(n^2) | Memoized recursion |
| Optimized | O(n) | O(1) | Longest subarray with target sum |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Compute `target = total_sum - x`. If `target < 0`, return -1. If `target == 0`, return `n`.
- Use a sliding window to find the **longest** subarray with sum exactly `target`.
- All values are positive, so the window sum is monotonically increasing as we expand — standard shrinkable window.
- Answer: `n - max_window_length`.

```python
def minOperations(nums: list[int], x: int) -> int:
    total = sum(nums)
    target = total - x

    # edge case: need to remove everything
    if target == 0:
        return len(nums)
    if target < 0:
        return -1

    # find longest subarray with sum == target
    max_len = -1
    current_sum = 0
    left = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        # shrink if sum exceeds target (all values positive)
        while current_sum > target and left <= right:
            current_sum -= nums[left]
            left += 1

        # check if we hit the target
        if current_sum == target:
            max_len = max(max_len, right - left + 1)

    return len(nums) - max_len if max_len != -1 else -1
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `nums = [1,1,4,2,3]`, `x = 5`

`total = 11`, `target = 11 - 5 = 6`

Find longest subarray summing to 6:

| right | nums[r] | sum | left | window | max_len |
|-------|---------|-----|------|--------|---------|
| 0 | 1 | 1 | 0 | [1] | -1 |
| 1 | 1 | 2 | 0 | [1,1] | -1 |
| 2 | 4 | 6 | 0 | [1,1,4] | 3 |
| 3 | 2 | 8→shrink: remove 1, sum=7→remove 1, sum=6 | 2 | [4,2] | 3 |
| 4 | 3 | 9→shrink: remove 4, sum=5 | 3 | [2,3] | 3 |

Longest subarray with sum 6 has length 3. Answer: `5 - 3 = 2`.

We remove `[1]` from left and `[3]` from right (or `[1,1]` from left... wait, that sums to 2, not 5). Actually: remove index 0 (value 1) and index 4 (value 3), total removed = 1+3 = 4 ≠ 5. Let me re-check: the middle subarray `[1,1,4]` sums to 6, so we keep indices 0-2 and remove indices 3,4 (values 2,3, sum=5). That's 2 operations.

**Output:** `2`

### Edge Case Testing
- **Empty input:** Not possible per constraints.
- **Single element:** `nums = [5]`, `x = 5` → target=0, return 1.
- **Typical case:** Shown in dry run.
- **Extreme values:** `x > total_sum` → target < 0, return -1.

### Complexity
- **Time:** O(n) — single pass with two pointers. All values positive ensures each element is added/removed from window at most once.
- **Space:** O(1) — only pointers and running sum.

### Optimization Discussion
- The key insight of **inverting the problem** (from "minimize edges removed" to "maximize middle kept") transforms an awkward two-sided problem into a standard sliding window.
- Prefix sum + hashmap would also work in O(n) time, O(n) space, but the sliding window is cleaner.

### Follow-up Variations
- What if `nums` can contain **negative** numbers? (Need prefix sum + hashmap instead of sliding window.)
- What if you can remove from one side only?
- Minimum operations to reduce `x` to at most zero (not exactly zero).

### Common Traps
- **Not recognizing the inversion trick** — trying to directly model "remove from left or right" leads to complex DP/recursion.
- **Forgetting `target == 0`:** If `x == total_sum`, we must remove all elements. The sliding window won't find a subarray of sum 0 that spans the whole array (it finds empty subarrays), so handle this as a special case.
- **Assuming negative values are possible** — the constraint says `nums[i] >= 1`, which is what makes the sliding window valid (monotonic sum).
