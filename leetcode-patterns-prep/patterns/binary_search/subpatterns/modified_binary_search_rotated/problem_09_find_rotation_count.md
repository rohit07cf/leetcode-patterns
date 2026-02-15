# Find Rotation Count

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Modified Binary Search — Rotated Arrays
**Link:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/ (variant: return the index)

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a sorted array of **unique** elements that has been rotated `k` times, find the value of `k` — i.e., the **index of the minimum element**. The rotation count equals the number of positions the original sorted array was rotated to the right.

### 2. Clarification Questions

- **Input constraints?** Array of unique elements, at least 1 element, sorted then rotated.
- **Edge cases?** No rotation (k=0, array already sorted), single element, rotated n-1 times.
- **Expected output?** Integer — the rotation count (index of minimum element).
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** Linear scan to find where `nums[i] < nums[i-1]`. That index is the rotation count.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** This is **exactly** LC 153 (Find Minimum in Rotated Sorted Array), but we return the **index** instead of the value. The index of the minimum element equals the rotation count. Compare `nums[mid]` with `nums[hi]` to decide direction.
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Find the "drop" point |
| Optimized | O(log n) | O(1) | Binary search for min index |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Identical to LC 153 logic: compare `nums[mid]` with `nums[hi]`.
- If `nums[mid] > nums[hi]`, the pivot (min) is in `[mid+1, hi]`.
- Otherwise, the pivot is in `[lo, mid]`.
- When `lo == hi`, that index is the rotation count.

```python
def find_rotation_count(nums):
    lo, hi = 0, len(nums) - 1

    # If array is not rotated or has one element
    if nums[lo] <= nums[hi]:
        return 0

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if nums[mid] > nums[hi]:
            # Pivot (min) is to the right of mid
            lo = mid + 1
        else:
            # Pivot could be at mid
            hi = mid

    return lo  # index of min == rotation count
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums = [15, 18, 2, 3, 6, 12]` (rotated 2 times)

| Step | lo | hi | mid | nums[mid] vs nums[hi] | Action |
|------|----|----|-----|----------------------|--------|
| Check | nums[0]=15 > nums[5]=12 | | | | Array is rotated, proceed |
| 1 | 0 | 5 | 2 | 2 < 12 | hi = 2 |
| 2 | 0 | 2 | 1 | 18 > 2 | lo = 2 |
| Done | lo == hi == 2 | | | | Return 2 |

Rotation count = 2. Correct — the original array `[2, 3, 6, 12, 15, 18]` was rotated right 2 times.

### Edge Case Testing

- **Empty input:** Assume at least one element.
- **Single element:** `[5]` -> `nums[lo] <= nums[hi]` is true, return 0.
- **Typical case:** Shown above.
- **Extreme values:** No rotation `[1, 2, 3, 4]` -> early return 0. Full rotation (n rotations = no rotation) -> return 0.

### Complexity

- **Time:** O(log n) — standard binary search halving.
- **Space:** O(1) — only two pointers.

### Optimization Discussion

The early check `if nums[lo] <= nums[hi]: return 0` handles the non-rotated case in O(1) but isn't strictly necessary — the binary search would also converge to index 0. It improves clarity.

### Follow-up Variations

- What if **duplicates** are allowed? Same as LC 154 variant — worst case O(n).
- Given the rotation count, **reconstruct the original sorted array** in O(n).
- **Reverse the rotation** in-place using three reversals: reverse whole array, reverse first k, reverse rest.
- Binary search for a target using the rotation count: find pivot, then binary search on the correct half.

### Common Traps

- **Confusing rotation direction:** "Rotated k times" typically means the last k elements moved to the front. The rotation count = index of the minimum = number of elements that moved from the back to the front.
- **Returning the value instead of the index:** The problem asks for the count (index), not the minimum value.
- **Not handling the non-rotated case:** When `nums[0] < nums[n-1]`, the array is already sorted. Rotation count is 0. Without the early check, the loop still works but the intent is less clear.
