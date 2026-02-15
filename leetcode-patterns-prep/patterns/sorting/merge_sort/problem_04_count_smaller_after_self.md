# Count of Smaller Numbers After Self

**Difficulty:** Hard
**Pattern:** Sorting
**Subpattern:** Merge Sort
**Link:** https://leetcode.com/problems/count-of-smaller-numbers-after-self/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums`, return an array `counts` where `counts[i]` is the number of elements to the **right** of `nums[i]` that are **strictly smaller** than `nums[i]`.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 10^5`, `-10^4 <= nums[i] <= 10^4`.
- **Edge cases?** Single element (count = 0), sorted ascending (all zeros), sorted descending (counts = n-1, n-2, ..., 0).
- **Expected output?** Array of integers, same length as input.
- **Can input be modified?** Yes, but we need to track original indices.

### 3. Brute Force Approach

- **Idea:** For each element, scan all elements to its right and count smaller ones.
- **Time:** O(n^2)
- **Space:** O(1) (beyond the output)

### 4. Optimized Approach

- **Core Insight:** During merge sort, when an element from the **left** half is placed into the merged array, all elements already placed from the **right** half are smaller and were originally to its right. This count equals the number of right-half elements merged so far. Track original indices alongside values to update the correct count.
- **Time:** O(n log n)
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | TLE for n = 10^5 |
| Merge Sort | O(n log n) | O(n) | Counts inversions during merge |
| BIT / Fenwick Tree | O(n log n) | O(n) | Alternative, coordinate compression needed |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Pair each element with its original index: `(value, index)`.
- During merge, when placing a left-half element, the count of right-half elements already placed tells us how many smaller-right elements exist.
- Track `right_count` — incremented each time a right-half element is placed before a left-half element.

```python
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        n = len(nums)
        counts = [0] * n
        # Pair each value with its original index
        indexed = [(nums[i], i) for i in range(n)]

        self._merge_sort(indexed, counts)
        return counts

    def _merge_sort(self, arr: list[tuple], counts: list[int]) -> list[tuple]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self._merge_sort(arr[:mid], counts)
        right = self._merge_sort(arr[mid:], counts)

        return self._merge(left, right, counts)

    def _merge(self, left: list[tuple], right: list[tuple],
               counts: list[int]) -> list[tuple]:
        merged = []
        i = j = 0
        right_count = 0  # How many right-half elements placed so far

        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                # Every right element already placed is smaller and was to the right
                counts[left[i][1]] += right_count
                merged.append(left[i])
                i += 1
            else:
                # Right element is smaller — increment counter
                right_count += 1
                merged.append(right[j])
                j += 1

        # Remaining left elements: all right elements were smaller
        while i < len(left):
            counts[left[i][1]] += right_count
            merged.append(left[i])
            i += 1

        # Remaining right elements: no left elements to update
        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [5, 2, 6, 1]`

Indexed: `[(5,0), (2,1), (6,2), (1,3)]`

1. **Split:** `[(5,0), (2,1)]` and `[(6,2), (1,3)]`
2. **Merge `[(5,0), (2,1)]`:**
   - 5 > 2: right_count=1, place (2,1)
   - Place (5,0): counts[0] += 1 -> `counts = [1,0,0,0]`
   - Merged: `[(2,1), (5,0)]`
3. **Merge `[(6,2), (1,3)]`:**
   - 6 > 1: right_count=1, place (1,3)
   - Place (6,2): counts[2] += 1 -> `counts = [1,0,1,0]`
   - Merged: `[(1,3), (6,2)]`
4. **Merge `[(2,1), (5,0)]` and `[(1,3), (6,2)]`:**
   - 2 > 1: right_count=1, place (1,3)
   - 2 <= 6: counts[1] += 1 -> `counts = [1,1,1,0]`, place (2,1)
   - 5 <= 6: counts[0] += 1 -> `counts = [2,1,1,0]`, place (5,0)
   - Place (6,2): counts[2] += 1 -> not here, remaining right
   - Final: `counts = [2, 1, 1, 0]`

### Edge Case Testing

- **Empty input:** Not possible (length >= 1).
- **Single element:** `[5]` -> `[0]`.
- **Typical case:** `[5, 2, 6, 1]` -> `[2, 1, 1, 0]`.
- **Extreme values:** Descending `[4, 3, 2, 1]` -> `[3, 2, 1, 0]`.

### Complexity

- **Time:** O(n log n) — standard merge sort with O(1) extra work per element during merge.
- **Space:** O(n) — temporary arrays during merge, plus the indexed pairs.

### Optimization Discussion

- **BIT / Fenwick Tree** approach: Traverse from right to left, query count of elements smaller than current, then update. Requires coordinate compression for negative values.
- **BST approach:** Insert from right to left, track subtree sizes. Degenerates to O(n^2) without balancing.
- Merge sort is the most reliable O(n log n) approach in interviews.

### Follow-up Variations

- Reverse Pairs (LC 493) — similar merge sort counting pattern.
- Count of Range Sum (LC 327) — counting within a range during merge.
- Global and Local Inversions (LC 775).

### Common Traps

- **Losing track of original indices.** You must carry the original index through all merge operations. Sorting rearranges elements, so without index tracking, you can't update the correct position in `counts`.
- **Using `<` instead of `<=` in the merge comparison.** When `left[i] == right[j]`, the left element should go first (equal elements aren't "smaller"), so use `<=`.
- **Forgetting to add `right_count` for remaining left elements** after the main merge loop. These left elements are larger than all right-half elements.
