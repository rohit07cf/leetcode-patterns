# Minimum Size Subarray Sum

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Variable Window
**Link:** https://leetcode.com/problems/minimum-size-subarray-sum/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an array of **positive integers** `nums` and a positive integer `target`, return the **minimal length** of a contiguous subarray whose sum is greater than or equal to `target`. If no such subarray exists, return 0.

### 2. Clarification Questions
- Input constraints? `1 <= target <= 10^9`, `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^4`. **All positive**.
- Edge cases? No subarray sums to target — return 0. Single element >= target — return 1.
- Expected output? An integer — the minimum window length.
- Can input be modified? Yes, but we don't need to.

### 3. Brute Force Approach
- **Idea:** For every starting index, expand right accumulating the sum. Stop as soon as `sum >= target`. Track the minimum length.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** Since all values are **positive**, adding elements only increases the sum and removing elements only decreases it. This monotonic property lets us use a sliding window. **Expand** right to grow the sum, **shrink** left to minimize the window while the sum remains valid.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Try all starting positions |
| Sliding Window | O(n) | O(1) | Shrink when sum >= target |
| Binary Search | O(n log n) | O(n) | Prefix sums + binary search |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Expand `right` to grow `window_sum`.
- Once `window_sum >= target`, shrink from `left` as much as possible while maintaining the condition.
- Update `min_len` each time the condition holds.

```python
def minSubArrayLen(self, target: int, nums: list[int]) -> int:
    left = 0
    window_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        window_sum += nums[right]

        # Shrink window while sum is still valid
        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `target = 7`, `nums = [2,3,1,2,4,3]`

| right | nums[r] | window_sum | left | window | min_len |
|-------|---------|------------|------|--------|---------|
| 0 | 2 | 2 | 0 | [2] | inf |
| 1 | 3 | 5 | 0 | [2,3] | inf |
| 2 | 1 | 6 | 0 | [2,3,1] | inf |
| 3 | 2 | 8 | 0 | [2,3,1,2] | 4 |
| | | 6 | 1 | [3,1,2] | 4 |
| 4 | 4 | 10 | 1 | [3,1,2,4] | 4 |
| | | 7 | 2 | [1,2,4] | 3 |
| | | 6 | 3 | [2,4] | 3 |
| 5 | 3 | 9 | 3 | [2,4,3] | 3 |
| | | 7 | 4 | [4,3] | 2 |
| | | 3 | 5 | [3] | 2 |

Output: **2** (subarray `[4,3]`)

### Edge Case Testing
- **Empty input:** Constraint says `len >= 1`, not applicable.
- **Single element:** `nums = [7], target = 7` — sum meets target immediately, returns 1.
- **Typical case:** `target = 7, nums = [2,3,1,2,4,3]` — returns 2.
- **Extreme values:** `target = 10^9, nums = [1,1,1]` — sum never reaches target, returns 0.

### Complexity
- **Time:** O(n) — each element enters and leaves the window at most once, so `left` moves at most n times total.
- **Space:** O(1) — only pointers and running sum.

### Optimization Discussion
The O(n log n) binary search approach uses prefix sums: for each index, binary search for the smallest window where the prefix sum difference >= target. This is useful when elements can be **negative** (sliding window doesn't work with negatives). But here, O(n) sliding window is optimal.

### Follow-up Variations
- **What if the array contains negative numbers?** Sliding window fails — use prefix sums with a deque or binary search.
- **Find the subarray itself, not just the length** — track `best_left` and `best_right` indices.
- **Maximum Size Subarray Sum Equals K** (LC 325) — prefix sums with hash map.

### Common Traps
- This problem asks for **minimum** window — so shrink as much as possible (use `while`, not `if`).
- Forgetting to return 0 when no valid subarray exists (check `min_len == inf`).
- **Sliding window only works here because all numbers are positive.** With negatives, the monotonic shrink property breaks.
