# Squares of a Sorted Array

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction
**Link:** https://leetcode.com/problems/squares-of-a-sorted-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an integer array sorted in non-decreasing order, return an array of the **squares** of each number, also sorted in non-decreasing order.

### 2. Clarification Questions
- Input constraints? Array length 1 to 10^4. Values from -10^4 to 10^4. Already sorted.
- Edge cases? All negatives, all positives, mix of both. Single element.
- Expected output? New array of squared values in sorted order.
- Can input be modified? We return a new array; original can be left intact.

### 3. Brute Force Approach
- **Idea:** Square every element, then sort the result.
- **Time:** O(n log n) — due to sorting.
- **Space:** O(n) — for the output array (O(n log n) if sort uses extra space).

### 4. Optimized Approach
- 💡 **Core Insight:** The largest squares come from the **extremes** (most negative or most positive). Using two pointers at both ends, compare absolute values. The larger absolute value produces the next largest square. **Fill the result array from the back** (largest to smallest).
- **Time:** O(n)
- **Space:** O(n) — output array only (required by the problem).

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Square + Sort | O(n log n) | O(n) | Simple but suboptimal |
| Two Pointers | O(n) | O(n) | Optimal — leverages sorted input |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Initialize result array of same length.
- Use `left = 0`, `right = n - 1`, fill position `pos = n - 1` (back to front).
- Compare absolute values at both ends; the larger one gets squared and placed at `pos`.
- Decrement `pos` and move the chosen pointer inward.

```python
def sortedSquares(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1  # fill from the back (largest first)

    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2

        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1

        pos -= 1

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `nums = [-4, -1, 0, 3, 10]`

| Step | left | right | left_sq | right_sq | pos | Action | result |
|------|------|-------|---------|----------|-----|--------|--------|
| 1 | 0 | 4 | 16 | 100 | 4 | 100 > 16, place 100 | [_,_,_,_,100] |
| 2 | 0 | 3 | 16 | 9 | 3 | 16 > 9, place 16 | [_,_,_,16,100] |
| 3 | 1 | 3 | 1 | 9 | 2 | 9 > 1, place 9 | [_,_,9,16,100] |
| 4 | 1 | 2 | 1 | 0 | 1 | 1 > 0, place 1 | [_,1,9,16,100] |
| 5 | 2 | 2 | 0 | 0 | 0 | equal, place 0 | [0,1,9,16,100] |

Result: `[0, 1, 9, 16, 100]`

### Edge Case Testing
- **Empty input:** Not possible per constraints (length >= 1).
- **Single element:** `[-5]` -> `[25]`. Correct.
- **Typical case:** `[-4,-1,0,3,10]` -> `[0,1,9,16,100]`. Correct.
- **Extreme values:** All negatives `[-5,-3,-1]` -> `[1,9,25]`. All positives `[1,2,3]` -> `[1,4,9]`. Both work because extremes always have the largest squares.

### Complexity
- **Time:** O(n) — single pass through the array.
- **Space:** O(n) — for the output array (unavoidable since we must return a new array).

### Optimization Discussion
O(n) is optimal. We must read every element and write every output, so linear time is a lower bound. The output array is required, so O(n) space is also a lower bound.

### Follow-up Variations
- Can you do it **in place**? Not easily while maintaining sorted order, since squares of negatives go to different positions.
- **Merge two sorted arrays** (LeetCode 88): Similar two-pointer merge pattern, also filling from the back.
- What if the array has **duplicates**? No change needed — the algorithm handles duplicates naturally.

### ⚠️ Common Traps
- Filling the result **front to back** instead of back to front — you'd place the largest squares at the wrong end.
- Using `left < right` instead of `left <= right` — misses the middle element when the array has odd length.
- Forgetting to handle negative numbers — `(-4)^2 = 16` is larger than `3^2 = 9`.
