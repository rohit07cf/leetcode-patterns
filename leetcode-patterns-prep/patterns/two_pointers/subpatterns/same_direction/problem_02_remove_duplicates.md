# Remove Duplicates from Sorted Array

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Same Direction
**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a **sorted** integer array `nums`, remove duplicates **in-place** so each element appears only once. Return the count `k` of unique elements. The first `k` elements of `nums` must hold the unique values in order.

### 2. Clarification Questions
- Input constraints? `1 <= nums.length <= 3 * 10^4`, `-100 <= nums[i] <= 100`, array is sorted in non-decreasing order
- Edge cases? Single element, all same elements, already unique
- Expected output? Return integer `k`; first `k` elements modified in-place
- Can input be modified? Yes, modify in-place

### 3. Brute Force Approach
- **Idea:** Use a set or extra array to collect unique values, then copy back.
- **Time:** O(n)
- **Space:** O(n)

### 4. Optimized Approach
- **Core Insight:** Since the array is **sorted**, duplicates are always adjacent. Use a `write` pointer for the next unique position and a `read` pointer scanning forward. When `nums[read] != nums[write]`, advance `write` and copy.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (set) | O(n) | O(n) | Extra storage |
| Optimized (two pointers) | O(n) | O(1) | Exploits sorted property |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Start `write` at index 0 (first element is always unique).
- Scan with `read` from index 1.
- When a new unique value is found, place it at `write + 1`.

```python
def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    write = 0  # last written unique position

    for read in range(1, len(nums)):
        if nums[read] != nums[write]:
            # found a new unique element — place it next
            write += 1
            nums[write] = nums[read]

    return write + 1  # count of unique elements
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `[1, 1, 2]`

| Step | read | nums[read] | write | nums[write] | Action | Array |
|------|------|-----------|-------|-------------|--------|-------|
| 0 | 1 | 1 | 0 | 1 | equal, skip | [1,1,2] |
| 1 | 2 | 2 | 0 | 1 | different, write=1 | [1,2,2] |

Return `2`. First 2 elements: `[1, 2]`.

### Edge Case Testing
- **Empty input:** Returns 0 (guard clause)
- **Single element:** `[5]` -> `write` stays 0, returns 1
- **Typical case:** `[0,0,1,1,1,2,2,3,3,4]` -> returns 5, first 5: `[0,1,2,3,4]`
- **Extreme values:** All same `[7,7,7,7]` -> returns 1

### Complexity
- **Time:** O(n) — single pass
- **Space:** O(1) — in-place modification

### Optimization Discussion
Already optimal for this problem. The sorted property guarantees we only need to compare adjacent unique values. No further optimization possible.

### Follow-up Variations
- **Remove Duplicates II (LC 80)** — allow at most 2 occurrences
- **Remove Element (LC 27)** — remove a specific value
- **Move Zeroes (LC 283)** — similar write/read pointer pattern

### Common Traps
- Starting `read` at 0 instead of 1 (wastes a comparison, or causes off-by-one)
- Returning `write` instead of `write + 1` (off-by-one on the count)
- Forgetting the array is **sorted** — comparing `nums[read]` with `nums[read-1]` works but comparing with `nums[write]` is cleaner
