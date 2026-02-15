# Squares of a Sorted Array

**Difficulty:** Easy
**Pattern:** Sorting
**Subpattern:** Merge Sort
**Link:** https://leetcode.com/problems/squares-of-a-sorted-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number, also sorted in non-decreasing order.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 10^4`, `-10^4 <= nums[i] <= 10^4`, array is sorted in non-decreasing order.
- **Edge cases?** All non-negative, all non-positive, mix of negative and positive, zeros.
- **Expected output?** New array of squared values in sorted order.
- **Can input be modified?** Yes, but we return a new array.

### 3. Brute Force Approach

- **Idea:** Square every element, then sort the resulting array.
- **Time:** O(n log n)
- **Space:** O(n) for the result (or O(1) extra if sorting in-place)

### 4. Optimized Approach

- **Core Insight:** The input is sorted, so the **largest squares** are at the **two ends** (large negatives or large positives). Use two pointers from both ends, compare absolute values, and fill the result array **from the back**. This is conceptually the **merge step** of merge sort — merging two sorted sequences (negatives reversed and positives) into one.
- **Time:** O(n)
- **Space:** O(n) for the result

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (square + sort) | O(n log n) | O(n) | Simple but doesn't use sorted property |
| Optimized (two pointers) | O(n) | O(n) | Merge-like, fills from back |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use two pointers: `left = 0`, `right = n - 1`.
- Fill the result from the **last index** backward (largest first).
- Compare `abs(nums[left])` vs `abs(nums[right])`, place the larger square, move that pointer inward.

```python
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        write = n - 1  # Fill from the back (largest squares first)

        while left <= right:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]

            if left_sq > right_sq:
                # Left end has larger absolute value
                result[write] = left_sq
                left += 1
            else:
                # Right end has larger (or equal) absolute value
                result[write] = right_sq
                right -= 1
            write -= 1

        return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [-4, -1, 0, 3, 10]`

| Step | left | right | write | left_sq | right_sq | Action | Result |
|------|------|-------|-------|---------|----------|--------|--------|
| 1 | 0 | 4 | 4 | 16 | 100 | 100 > 16, place 100 | [_,_,_,_,100] |
| 2 | 0 | 3 | 3 | 16 | 9 | 16 > 9, place 16 | [_,_,_,16,100] |
| 3 | 1 | 3 | 2 | 1 | 9 | 9 > 1, place 9 | [_,_,9,16,100] |
| 4 | 1 | 2 | 1 | 1 | 0 | 1 > 0, place 1 | [_,1,9,16,100] |
| 5 | 2 | 2 | 0 | 0 | 0 | equal, place 0 | [0,1,9,16,100] |

**Output:** `[0, 1, 9, 16, 100]`

### Edge Case Testing

- **Empty input:** Not possible (length >= 1).
- **Single element:** `[-5]` -> `[25]`.
- **Typical case:** `[-4, -1, 0, 3, 10]` -> `[0, 1, 9, 16, 100]`.
- **Extreme values:** All negative `[-3, -2, -1]` -> `[1, 4, 9]`. Left pointer sweeps all. All positive `[1, 2, 3]` -> `[1, 4, 9]`. Right pointer sweeps all.

### Complexity

- **Time:** O(n) — each element is visited exactly once.
- **Space:** O(n) — result array (required by the problem).

### Optimization Discussion

- This is already optimal. We cannot do better than O(n) since we must output n elements.
- The merge sort connection: the sorted array with negatives is like two sorted sequences — negative part (reversed) and positive part. The two-pointer technique is the **merge** of these two sequences by absolute value.

### Follow-up Variations

- Merge Sorted Array (LC 88) — similar backward merge technique.
- Two Sum II (LC 167) — two pointers on a sorted array.
- Sort an Array (LC 912) — full merge sort implementation.

### Common Traps

- **Filling from the front instead of the back.** The largest squares are at the ends, so filling from the back is natural. Filling from the front would require finding the smallest absolute value first, which is more complex.
- **Using `abs()` comparison but forgetting to square.** The result needs squared values, not absolute values. While `abs` comparison works for deciding which pointer to move, the stored value must be the square.
- **Off-by-one with `left <= right`.** Use `<=` not `<`, otherwise the middle element when `left == right` is skipped.
