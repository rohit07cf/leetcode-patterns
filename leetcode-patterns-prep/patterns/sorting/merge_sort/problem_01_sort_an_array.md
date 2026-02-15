# Sort an Array

**Difficulty:** Medium
**Pattern:** Sorting
**Subpattern:** Merge Sort
**Link:** https://leetcode.com/problems/sort-an-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of integers `nums`, sort the array in ascending order and return it. You must solve it without using any built-in sort functions, with O(n log n) time complexity and the smallest space complexity possible.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 5 * 10^4`, `-5 * 10^4 <= nums[i] <= 5 * 10^4`
- **Edge cases?** Single element array (already sorted), all identical elements, already sorted, reverse sorted.
- **Expected output?** The same array sorted in ascending order.
- **Can input be modified?** Yes, in-place modifications are acceptable.

### 3. Brute Force Approach

- **Idea:** Use a simple O(n^2) sort like insertion sort or selection sort. Compare every pair and swap as needed.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** Merge sort divides the array in half recursively, sorts each half, then merges two sorted halves in O(n). The divide-and-conquer structure guarantees O(n log n) in **all** cases (no worst-case degradation like quicksort).
- **Time:** O(n log n)
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (Insertion Sort) | O(n^2) | O(1) | TLE on large inputs |
| Optimized (Merge Sort) | O(n log n) | O(n) | Stable, guaranteed performance |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Recursively split the array at the midpoint until subarrays have length 1.
- Merge two sorted halves using a two-pointer technique into a temporary array.
- Copy merged results back into the original positions.

```python
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # Base case: single element is already sorted
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        # Recursively sort both halves
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # Merge two sorted halves
        return self._merge(left, right)

    def _merge(self, left: list[int], right: list[int]) -> list[int]:
        result = []
        i = j = 0

        # Two-pointer merge: always pick the smaller element
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Append remaining elements (only one side will have leftovers)
        result.extend(left[i:])
        result.extend(right[j:])
        return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [5, 2, 3, 1]`

1. Split: `[5, 2]` and `[3, 1]`
2. Split `[5, 2]` -> `[5]`, `[2]` -> merge -> `[2, 5]`
3. Split `[3, 1]` -> `[3]`, `[1]` -> merge -> `[1, 3]`
4. Merge `[2, 5]` and `[1, 3]`:
   - Compare 2 vs 1 -> pick 1
   - Compare 2 vs 3 -> pick 2
   - Compare 5 vs 3 -> pick 3
   - Append 5
   - Result: `[1, 2, 3, 5]`

### Edge Case Testing

- **Empty input:** Not possible per constraints (length >= 1), but returns `[]`.
- **Single element:** `[1]` -> returns `[1]` immediately (base case).
- **Typical case:** `[5, 2, 3, 1]` -> `[1, 2, 3, 5]`.
- **Extreme values:** All duplicates `[3, 3, 3]` -> `[3, 3, 3]` (stable, `<=` preserves order).

### Complexity

- **Time:** O(n log n) — log n levels of recursion, each level does O(n) work merging.
- **Space:** O(n) — temporary arrays during merge; recursion stack is O(log n).

### Optimization Discussion

- **In-place merge sort** can reduce auxiliary space to O(1) but is complex and has higher constant factors.
- **Bottom-up merge sort** avoids recursion overhead by iteratively merging subarrays of size 1, 2, 4, 8, ...
- For this problem, the standard top-down approach is clean and interview-preferred.

### Follow-up Variations

- Implement bottom-up (iterative) merge sort.
- Sort a linked list using merge sort (LC 148).
- Implement in-place merge sort with O(1) extra space.

### Common Traps

- **Using `<` instead of `<=` in merge comparison** breaks stability. Always use `<=` when picking from the left half to maintain stable sort order.
- **Forgetting to append remaining elements** after the main merge loop. One of the two halves will still have unprocessed elements.
- **Quicksort pitfall:** Interviewers ask for this problem specifically because quicksort has O(n^2) worst case. Merge sort is the safe choice here.
