# Search in Rotated Sorted Array

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Modified Binary Search — Rotated Arrays
**Link:** https://leetcode.com/problems/search-in-rotated-sorted-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a sorted array that has been rotated at some unknown pivot, search for a target value and return its index. Return -1 if not found. All elements are **unique**.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 5000`, values in `[-10^4, 10^4]`, all unique.
- **Edge cases?** Single element, target not present, no rotation (pivot at 0).
- **Expected output?** Index of target, or -1.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** Linear scan through the array.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** At any midpoint, **one half is always sorted**. Check if the target lies in the sorted half — if yes, search there; otherwise, search the other half.
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Simple linear scan |
| Optimized | O(log n) | O(1) | Modified binary search |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Compute `mid` and check if it's the target.
- Determine which half is sorted by comparing `nums[lo]` with `nums[mid]`.
- If the **left half is sorted**, check if target falls in `[lo, mid)` — narrow accordingly.
- Otherwise the **right half is sorted** — check if target falls in `(mid, hi]` — narrow accordingly.

```python
def search(nums, target):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1  # target in sorted left half
            else:
                lo = mid + 1  # target in right half
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1  # target in sorted right half
            else:
                hi = mid - 1  # target in left half

    return -1
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`

| Step | lo | hi | mid | nums[mid] | Action |
|------|----|----|-----|-----------|--------|
| 1 | 0 | 6 | 3 | 7 | Left sorted [4..7], 0 not in [4,7) -> lo=4 |
| 2 | 4 | 6 | 5 | 1 | Right sorted [1,2], 0 not in (1,2] -> hi=4 |
| 3 | 4 | 4 | 4 | 0 | Found! Return 4 |

### Edge Case Testing

- **Empty input:** Constraint says length >= 1, but loop won't execute if empty.
- **Single element:** `[5]`, target=5 -> mid=0, found. Target=3 -> return -1.
- **Typical case:** Demonstrated above.
- **Extreme values:** No rotation `[1,2,3]` -> left half always sorted, standard binary search behavior.

### Complexity

- **Time:** O(log n) — halving search space each iteration.
- **Space:** O(1) — only pointers.

### Optimization Discussion

This is already optimal for searching in a rotated sorted array with unique elements. No further optimization needed.

### Follow-up Variations

- What if duplicates are allowed? (See Problem 02 — LC 81)
- What if you need to find the rotation pivot first?
- Can you solve it by first finding the pivot, then doing standard binary search on the correct half?

### Common Traps

- **Using `nums[lo] < nums[mid]` instead of `<=`:** When `lo == mid` (two-element subarray), the left "half" is a single element. `<=` correctly identifies it as sorted.
- **Off-by-one in range checks:** Use `nums[lo] <= target < nums[mid]` (inclusive lo, exclusive mid) for the left half.
- **Forgetting the no-rotation case:** When the array isn't rotated, the algorithm still works because the left half is always sorted.
