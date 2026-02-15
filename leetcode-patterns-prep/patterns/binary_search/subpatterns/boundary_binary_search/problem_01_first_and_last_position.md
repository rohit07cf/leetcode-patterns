# Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Boundary Binary Search
**Link:** https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a sorted array of integers and a target value, find the starting and ending position of the target in the array. Return `[-1, -1]` if the target is not found. Must run in **O(log n)** time.

### 2. Clarification Questions

- **Input constraints?** Array is sorted in non-decreasing order. `0 <= nums.length <= 10^5`.
- **Edge cases?** Empty array, target not present, single element, all elements are the target.
- **Expected output?** A list of two integers `[first_index, last_index]`.
- **Can input be modified?** Yes, but no need to — we only read.

### 3. Brute Force Approach

- **Idea:** Linear scan from left to find first occurrence, then from right to find last occurrence.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** Run **two boundary binary searches** — one to find the **leftmost** position where `nums[mid] >= target`, and another to find the **rightmost** position where `nums[mid] <= target`. This is the quintessential boundary binary search problem.
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Simple linear scan |
| Optimized | O(log n) | O(1) | Two binary searches for boundaries |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use a helper `find_bound(is_left)` that performs boundary binary search.
- For the **left bound**, when `nums[mid] == target`, move `right = mid - 1` to keep searching left.
- For the **right bound**, when `nums[mid] == target`, move `left = mid + 1` to keep searching right.
- Track the answer index whenever we find the target.

```python
def searchRange(nums, target):
    def find_bound(is_left):
        lo, hi = 0, len(nums) - 1
        result = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                result = mid  # record candidate
                if is_left:
                    hi = mid - 1  # keep searching left for first occurrence
                else:
                    lo = mid + 1  # keep searching right for last occurrence
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return result

    left = find_bound(is_left=True)
    right = find_bound(is_left=False)
    return [left, right]
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [5, 7, 7, 8, 8, 10]`, `target = 8`

**Left bound search:**
- `lo=0, hi=5` -> `mid=2`, `nums[2]=7 < 8` -> `lo=3`
- `lo=3, hi=5` -> `mid=4`, `nums[4]=8 == 8` -> `result=4`, `hi=3`
- `lo=3, hi=3` -> `mid=3`, `nums[3]=8 == 8` -> `result=3`, `hi=2`
- `lo=3, hi=2` -> exit. **Left = 3**

**Right bound search:**
- `lo=0, hi=5` -> `mid=2`, `nums[2]=7 < 8` -> `lo=3`
- `lo=3, hi=5` -> `mid=4`, `nums[4]=8 == 8` -> `result=4`, `lo=5`
- `lo=5, hi=5` -> `mid=5`, `nums[5]=10 > 8` -> `hi=4`
- `lo=5, hi=4` -> exit. **Right = 4**

**Output:** `[3, 4]`

### Edge Case Testing

- **Empty input:** `nums=[]` -> `lo > hi` immediately, returns `[-1, -1]`.
- **Single element:** `nums=[8], target=8` -> returns `[0, 0]`.
- **Target not found:** `nums=[1,2,3], target=5` -> returns `[-1, -1]`.
- **Extreme values:** All elements are target -> returns `[0, n-1]`.

### Complexity

- **Time:** O(log n) — two binary searches, each O(log n).
- **Space:** O(1) — only pointers and variables.

### Optimization Discussion

This is already optimal for the constraint of O(log n). An alternative is using `bisect_left` and `bisect_right` from Python's `bisect` module, but interviewers typically want you to implement the binary search manually.

### Follow-up Variations

- Find the **count** of a target in a sorted array (right - left + 1).
- Extend to rotated sorted arrays.
- Search in a sorted matrix for first/last occurrence in a specific row.

### Common Traps

- **Using a single binary search** — finding one occurrence then scanning linearly degrades to O(n) in the worst case (e.g., all elements are the target).
- **Off-by-one in boundary logic** — forgetting to continue searching after finding a match (moving `hi = mid - 1` or `lo = mid + 1`) causes early termination.
- **Returning early on first match** — you must record the result and keep narrowing to find the true boundary.
