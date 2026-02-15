# Find Peak Element

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Classic Binary Search
**Link:** https://leetcode.com/problems/find-peak-element/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array where `nums[i] != nums[i+1]` (no adjacent duplicates), find **any** peak element (an element strictly greater than its neighbors). The array boundaries are treated as negative infinity. Return the index of any peak.

### 2. Clarification Questions

- **Input constraints?** 1 <= n <= 1000. `nums[-1] = nums[n] = -infinity`. No adjacent duplicates.
- **Edge cases?** Single element (always a peak), strictly increasing array (last element is peak), strictly decreasing (first is peak).
- **Expected output?** Index of **any** peak element.
- **Can input be modified?** Not needed — read-only.

### 3. Brute Force Approach

- **Idea:** Linear scan — check each element to see if it's greater than both neighbors.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- 💡 **Core Insight:** If `nums[mid] < nums[mid + 1]`, the right side is **going up**, so a peak **must** exist on the right (because the array ends at -infinity). Conversely, if `nums[mid] < nums[mid - 1]`, a peak exists on the left. Binary search always moves toward the **ascending** direction.

- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Simple linear scan |
| Optimized | O(log n) | O(1) | Binary search — move toward ascending side |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use `left < right` template (converging to a single element).
- Compare `nums[mid]` with `nums[mid + 1]` to decide direction.
- When loop exits, `left == right` points to a peak.

```python
def findPeakElement(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1  # WHY: peak must be on the right (ascending slope)
        else:
            right = mid  # WHY: mid could be the peak, or peak is to the left

    return left  # WHY: left == right, converged to a peak
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [1, 2, 3, 1]`

| Step | left | right | mid | nums[mid] vs nums[mid+1] | Action |
|------|------|-------|-----|--------------------------|--------|
| 1 | 0 | 3 | 1 | 2 < 3 | left = 2 |
| 2 | 2 | 3 | 2 | 3 > 1 | right = 2 |
| 3 | left == right = 2 | — | — | — | Return 2 |

**Answer:** Index 2 (value 3 is a peak).

### Edge Case Testing

- **Empty input:** Constraints guarantee length >= 1.
- **Single element:** `[1]` → left = right = 0 immediately, return 0. Correct (boundary is -inf).
- **Typical case:** Multiple peaks → returns any one of them.
- **Extreme values:** Strictly increasing `[1,2,3,4]` → keeps going right, returns index 3. Strictly decreasing `[4,3,2,1]` → keeps going left, returns index 0.

### Complexity

- **Time:** O(log n) — halving search space each step.
- **Space:** O(1) — constant extra space.

### Optimization Discussion

This is optimal for a general unsorted array. The key insight that makes binary search work here: **a peak is guaranteed to exist on the ascending side** because the boundary is -infinity.

### Follow-up Variations

- **Peak Index in a Mountain Array (LC 852):** Guaranteed single peak — same approach.
- **Find Peak Element II (LC 1901):** 2D version — more complex.
- What if you need to find **all** peaks? (Must be O(n) — no binary search shortcut.)

### Common Traps

- **Comparing `nums[mid]` with `nums[mid - 1]` instead of `nums[mid + 1]`:** When `mid = 0`, accessing `nums[mid - 1]` is `nums[-1]` in Python (last element!). Safer to compare with `mid + 1` and use `left < right` so `mid` never equals `right`.
- **Using `left <= right`:** This template requires `left < right` to avoid infinite loops since we use `right = mid` (not `mid - 1`).
- **Assuming the array is sorted:** It is NOT sorted. Binary search works here because of the peak **existence guarantee**, not sorted order.
