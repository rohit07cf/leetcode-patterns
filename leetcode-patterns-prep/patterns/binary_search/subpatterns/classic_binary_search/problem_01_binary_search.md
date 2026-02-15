# Binary Search

**Difficulty:** Easy
**Pattern:** Binary Search
**Subpattern:** Classic Binary Search
**Link:** https://leetcode.com/problems/binary-search/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a sorted array of integers `nums` and a target value, return the index of the target if found, otherwise return `-1`.

### 2. Clarification Questions

- **Input constraints?** Array is sorted in ascending order. All elements are unique. Length 1 to 10^4.
- **Edge cases?** Target not in array, single-element array, target at boundaries.
- **Expected output?** Integer index or `-1`.
- **Can input be modified?** Not needed — read-only search.

### 3. Brute Force Approach

- **Idea:** Linear scan through the array checking each element.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- 💡 **Core Insight:** The array is **sorted**, so we can eliminate half the search space each step. Compare the target with the middle element — if target is smaller, search left; if larger, search right.
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Linear scan, ignores sorted property |
| Optimized | O(log n) | O(1) | Classic binary search |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Initialize `left` and `right` pointers at array boundaries.
- While `left <= right`, compute `mid` and compare `nums[mid]` to target.
- Narrow the search window by half each iteration.

```python
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2  # WHY: avoid integer overflow

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # WHY: target is in right half
        else:
            right = mid - 1  # WHY: target is in left half

    return -1  # WHY: target not found
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9`

| Step | left | right | mid | nums[mid] | Action |
|------|------|-------|-----|-----------|--------|
| 1 | 0 | 5 | 2 | 3 | 3 < 9 → left = 3 |
| 2 | 3 | 5 | 4 | 9 | Found! Return 4 |

### Edge Case Testing

- **Empty input:** Constraint says length >= 1, but `left > right` immediately returns `-1`.
- **Single element:** `[5]`, target=5 → mid=0, found. Target=3 → returns `-1`.
- **Typical case:** Target in middle of array → logarithmic convergence.
- **Extreme values:** Target smaller than all elements or larger than all → loop exits, returns `-1`.

### Complexity

- **Time:** O(log n) — halving the search space each iteration.
- **Space:** O(1) — only three pointers used.

### Optimization Discussion

This is already the optimal solution. A recursive version exists but adds O(log n) stack space with no benefit.

### Follow-up Variations

- What if duplicates exist and you need the **first** or **last** occurrence?
- What if the array is sorted in **descending** order?

### Common Traps

- **Integer overflow on `mid`:** Use `left + (right - left) // 2` instead of `(left + right) // 2`. Not an issue in Python but critical in Java/C++.
- **Off-by-one with `left <= right`:** Using `<` instead of `<=` misses the case where the target is the last remaining element.
- **Moving pointers incorrectly:** Must use `mid + 1` and `mid - 1`, not `mid`. Otherwise infinite loop when `left == right`.
