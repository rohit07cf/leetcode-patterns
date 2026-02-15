# Find Minimum in Rotated Sorted Array

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Modified Binary Search — Rotated Arrays
**Link:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a sorted array of **unique** elements that has been rotated, find the minimum element. The minimum is the element right after the rotation pivot.

### 2. Clarification Questions

- **Input constraints?** `1 <= n <= 5000`, all unique, values in `[-5000, 5000]`.
- **Edge cases?** No rotation (already sorted), single element, rotated by n-1 positions.
- **Expected output?** The minimum value (not index).
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** Scan all elements, track minimum.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** The minimum is the **only element smaller than its predecessor**. Compare `nums[mid]` with `nums[hi]`: if `nums[mid] > nums[hi]`, the min is in the right half; otherwise it's in the left half (including mid).
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Linear scan |
| Optimized | O(log n) | O(1) | Compare mid with hi to decide direction |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use `lo, hi` pointers. Compare `nums[mid]` with `nums[hi]`.
- If `nums[mid] > nums[hi]` -> min is in `[mid+1, hi]` (right side of the "break").
- Else -> min is in `[lo, mid]` (mid could be the min, don't skip it).
- Loop until `lo == hi` — that's the answer.

```python
def findMin(nums):
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if nums[mid] > nums[hi]:
            # Min must be in (mid, hi] — mid is too large
            lo = mid + 1
        else:
            # Min could be mid itself — keep it in range
            hi = mid

    return nums[lo]
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums = [3, 4, 5, 1, 2]`

| Step | lo | hi | mid | nums[mid] vs nums[hi] | Action |
|------|----|----|-----|----------------------|--------|
| 1 | 0 | 4 | 2 | 5 > 2 | lo = 3 |
| 2 | 3 | 4 | 3 | 1 < 2 | hi = 3 |
| Done | lo == hi == 3 | | | | Return nums[3] = 1 |

### Edge Case Testing

- **Empty input:** Constraint guarantees length >= 1.
- **Single element:** `[7]` -> lo=hi=0 immediately, return 7.
- **Typical case:** Shown above.
- **Extreme values:** No rotation `[1,2,3,4]` -> `nums[mid]` always <= `nums[hi]`, hi shrinks to 0, return nums[0] = 1. Correct.

### Complexity

- **Time:** O(log n) — halving each step.
- **Space:** O(1) — two pointers.

### Optimization Discussion

Already optimal. The key design choice is comparing with `nums[hi]` rather than `nums[lo]`. Comparing with `nums[lo]` doesn't work because when the subarray is already sorted, `nums[mid] >= nums[lo]` is always true and doesn't tell you which direction to go.

### Follow-up Variations

- What if duplicates exist? (See Problem 04 — LC 154)
- Return the **index** of the minimum instead of the value.
- Find the **rotation count** (same as finding the index of the minimum).

### Common Traps

- **Comparing with `nums[lo]` instead of `nums[hi]`:** This fails for non-rotated arrays. `nums[mid] >= nums[lo]` when the array is sorted doesn't tell you where the min is.
- **Using `lo <= hi` with `hi = mid - 1`:** This can skip the minimum. Use `lo < hi` with `hi = mid` to keep the potential answer in range.
- **Off-by-one when `mid` is the min:** Setting `hi = mid` (not `mid - 1`) ensures we don't skip past the minimum element.
