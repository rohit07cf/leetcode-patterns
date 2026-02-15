# Search in a Nearly Sorted Array

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Modified Binary Search — Rotated Arrays
**Link:** https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/ (variant — classic interview problem)

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a "nearly sorted" array where each element may be displaced by **at most one position** from its sorted location (i.e., element at index `i` in the sorted array could be at index `i-1`, `i`, or `i+1`), find the index of a target value. Return -1 if not found.

### 2. Clarification Questions

- **Input constraints?** Array of unique integers. Each element is at most 1 position away from its correct sorted position.
- **Edge cases?** Target at first/last position, target at a swapped position, target absent.
- **Expected output?** Index of target, or -1.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** Linear scan through the array.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** Standard binary search checks only `nums[mid]`. Since elements can be displaced by 1, we must also check `nums[mid - 1]` and `nums[mid + 1]` at each step. If none match, use `nums[mid]` vs `target` to decide direction — skip 2 positions (since we've already checked mid-1, mid, mid+1).
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Simple scan |
| Optimized | O(log n) | O(1) | Check mid-1, mid, mid+1 each step |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- At each step, check `mid - 1`, `mid`, and `mid + 1` (with bounds checking).
- If target found at any of these three positions, return that index.
- If `nums[mid] < target`, search right: `lo = mid + 2` (mid-1, mid, mid+1 are cleared).
- If `nums[mid] > target`, search left: `hi = mid - 2`.

```python
def search_nearly_sorted(nums, target):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        # Check mid and its neighbors (displaced by at most 1)
        if nums[mid] == target:
            return mid
        if mid - 1 >= lo and nums[mid - 1] == target:
            return mid - 1
        if mid + 1 <= hi and nums[mid + 1] == target:
            return mid + 1

        # Target not in {mid-1, mid, mid+1} — narrow search
        if nums[mid] < target:
            lo = mid + 2  # skip mid-1, mid, mid+1 (all checked)
        else:
            hi = mid - 2  # skip mid-1, mid, mid+1 (all checked)

    return -1
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums = [10, 3, 40, 20, 50, 80, 70]`, `target = 40`

Sorted would be `[3, 10, 20, 40, 50, 70, 80]` — each element displaced by at most 1.

| Step | lo | hi | mid | Check mid-1, mid, mid+1 | Action |
|------|----|----|-----|------------------------|--------|
| 1 | 0 | 6 | 3 | nums[2]=40, nums[3]=20, nums[4]=50 | nums[2]==40! Return 2 |

### Edge Case Testing

- **Empty input:** If length is 0, loop doesn't execute, return -1.
- **Single element:** `[5]`, target=5 -> mid=0, found. Target=3 -> return -1.
- **Typical case:** Shown above.
- **Extreme values:** Target at index 0 — could be found as `mid - 1` when mid=1. Bounds check `mid - 1 >= lo` ensures safety.

### Complexity

- **Time:** O(log n) — each iteration eliminates 3 elements and moves by 2, maintaining logarithmic behavior.
- **Space:** O(1) — only pointers.

### Optimization Discussion

The +2/-2 skip is the key optimization. Since we check three positions each iteration, we can safely skip past all three. This maintains the O(log n) guarantee despite the displacement.

### Follow-up Variations

- What if elements can be displaced by at most **k** positions? Check `2k + 1` positions around mid, skip by `k + 1`.
- What if the array is nearly sorted but could also be rotated?
- Nearly sorted with duplicates — how would you handle ties?

### Common Traps

- **Skipping by `mid + 1` / `mid - 1` instead of `mid + 2` / `mid - 2`:** If you only skip by 1, you might re-check positions. More importantly, skipping by 2 is safe because you've checked mid-1, mid, mid+1 — all three are cleared.
- **Bounds checking on `mid - 1` and `mid + 1`:** Always verify `mid - 1 >= lo` and `mid + 1 <= hi` before accessing. Using `>= lo` (not `>= 0`) and `<= hi` (not `< n`) ensures you stay within the active search range.
- **Assuming the array is perfectly sorted:** The displacement property means `nums[mid]` might not be the "right" element for that position. Always check neighbors.
