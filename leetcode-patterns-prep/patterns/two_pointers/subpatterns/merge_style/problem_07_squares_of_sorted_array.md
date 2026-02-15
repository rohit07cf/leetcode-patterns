# Squares of a Sorted Array

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Merge Style
**Link:** https://leetcode.com/problems/squares-of-a-sorted-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of integers sorted in non-decreasing order, return an array of the **squares** of each number, also sorted in non-decreasing order.

### 2. Clarification Questions
- Input constraints? `1 <= nums.length <= 10^4`, values in `[-10^4, 10^4]`, sorted non-decreasing
- Edge cases? All negative; all positive; mix of negative and positive; contains zeros
- Expected output? New sorted array of squared values
- Can input be modified? Yes, but we build a new output array

### 3. Brute Force Approach
- **Idea:** Square every element, then sort the resulting array.
- **Time:** O(n log n)
- **Space:** O(n) for the output

### 4. Optimized Approach
- **Core Insight:** After squaring, the **largest values come from the extremes** (most negative or most positive). Use two pointers at the left and right ends. Compare absolute values (or squared values), place the larger square at the **end** of the result array, and move that pointer inward. This is a **merge from two ends**.
- **Time:** O(n)
- **Space:** O(n) for output (O(1) extra beyond that)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n log n) | O(n) | Square then sort |
| Two Pointers | O(n) | O(n) | Merge from both ends |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Initialize `left = 0`, `right = n - 1`, and a result array.
- Fill result from the **back** (index `n-1` down to 0).
- At each step, compare `abs(nums[left])` vs `abs(nums[right])`. Place the larger square and move that pointer.

```python
def sortedSquares(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    write = n - 1  # fill from the back

    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2

        if left_sq >= right_sq:
            result[write] = left_sq
            left += 1   # consumed the left extreme
        else:
            result[write] = right_sq
            right -= 1  # consumed the right extreme
        write -= 1

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums = [-4, -1, 0, 3, 10]`

| Step | left | right | write | left_sq | right_sq | Action | result |
|------|------|-------|-------|---------|----------|--------|--------|
| 1 | 0 | 4 | 4 | 16 | 100 | 100 → pos 4 | [_,_,_,_,100] |
| 2 | 0 | 3 | 3 | 16 | 9 | 16 → pos 3 | [_,_,_,16,100] |
| 3 | 1 | 3 | 2 | 1 | 9 | 9 → pos 2 | [_,_,9,16,100] |
| 4 | 1 | 2 | 1 | 1 | 0 | 1 → pos 1 | [_,1,9,16,100] |
| 5 | 2 | 2 | 0 | 0 | 0 | 0 → pos 0 | [0,1,9,16,100] |

Result: `[0, 1, 9, 16, 100]`

### Edge Case Testing
- **Empty input:** Not possible per constraints (min length 1)
- **Single element:** `[-5]` → `[25]`
- **Typical case:** As shown above
- **Extreme values:** All negative `[-3,-2,-1]` → left pointer dominates; all positive `[1,2,3]` → right pointer dominates

### Complexity
- **Time:** O(n) — single pass, each element visited once
- **Space:** O(n) — for the output array; O(1) extra workspace

### Optimization Discussion

This is the **same idea as Merge Sorted Array (LeetCode 88)** — filling from the back to avoid overwriting. Here we treat the array as two sorted sequences (negatives reversed, positives) being merged.

### Follow-up Variations
- Merge Sorted Array (LeetCode 88) — same reverse-fill technique
- Sort an array with three distinct values (Dutch National Flag)
- Kth Largest Element in an Array (LeetCode 215)

### Common Traps
- Filling the result front-to-back instead of back-to-front (you'd need to reverse at the end)
- Forgetting that `left == right` is a valid case (the `<=` in the while condition)
- Using `abs()` comparison but then forgetting to actually **square** the value before storing
