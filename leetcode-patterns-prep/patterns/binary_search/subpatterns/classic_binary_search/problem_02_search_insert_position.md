# Search Insert Position

**Difficulty:** Easy
**Pattern:** Binary Search
**Subpattern:** Classic Binary Search
**Link:** https://leetcode.com/problems/search-insert-position/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a sorted array of distinct integers and a target, return the index if found. If not, return the index where it **would be inserted** to keep the array sorted.

### 2. Clarification Questions

- **Input constraints?** Array is sorted with distinct values. Length 1 to 10^4. Values from -10^4 to 10^4.
- **Edge cases?** Target smaller than all elements (insert at 0), target larger than all (insert at end), target already present.
- **Expected output?** Integer index (0-indexed).
- **Can input be modified?** Not needed — read-only search.

### 3. Brute Force Approach

- **Idea:** Linear scan — find the first element >= target and return its index.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- 💡 **Core Insight:** This is binary search where, if the target isn't found, `left` naturally lands on the correct insertion point. When the loop ends, `left` is the index of the **first element >= target**.
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Simple linear scan |
| Optimized | O(log n) | O(1) | Binary search — `left` is the answer |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Standard binary search with `left <= right`.
- If found, return `mid`.
- If not found, `left` is exactly the insertion index.

```python
def searchInsert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # WHY: insertion point is to the right
        else:
            right = mid - 1  # WHY: insertion point is to the left

    return left  # WHY: left is the first index where nums[left] >= target
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [1, 3, 5, 6]`, `target = 5`

| Step | left | right | mid | nums[mid] | Action |
|------|------|-------|-----|-----------|--------|
| 1 | 0 | 3 | 1 | 3 | 3 < 5 → left = 2 |
| 2 | 2 | 3 | 2 | 5 | Found! Return 2 |

**Input:** `nums = [1, 3, 5, 6]`, `target = 2`

| Step | left | right | mid | nums[mid] | Action |
|------|------|-------|-----|-----------|--------|
| 1 | 0 | 3 | 1 | 3 | 3 > 2 → right = 0 |
| 2 | 0 | 0 | 0 | 1 | 1 < 2 → left = 1 |
| 3 | left > right | — | — | — | Return left = 1 |

### Edge Case Testing

- **Empty input:** Not possible per constraints (length >= 1).
- **Single element:** `[3]`, target=3 → returns 0. Target=1 → returns 0. Target=5 → returns 1.
- **Typical case:** Target between elements → `left` lands at correct insertion point.
- **Extreme values:** Target < nums[0] → returns 0. Target > nums[-1] → returns `len(nums)`.

### Complexity

- **Time:** O(log n) — standard binary search.
- **Space:** O(1) — constant extra space.

### Optimization Discussion

Python's `bisect.bisect_left(nums, target)` does exactly this. In an interview, implementing it manually shows understanding.

### Follow-up Variations

- What if duplicates exist? (Use `bisect_left` vs `bisect_right` logic.)
- What if you need to actually insert and return the new array?

### Common Traps

- **Returning `mid` instead of `left` when not found:** After the loop, `left` is the answer, not `mid`.
- **Forgetting the case where target > all elements:** `left` correctly becomes `len(nums)`, which is a valid insertion index.
- **Using `left < right` instead of `left <= right`:** This changes the loop invariant and requires different handling.
