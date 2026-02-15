# Remove Duplicates from Sorted Array II

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Same Direction
**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a **sorted** array `nums`, remove duplicates in-place so that each element appears **at most twice**. Return the count `k` of valid elements. The first `k` positions must hold the result in sorted order.

### 2. Clarification Questions
- Input constraints? `1 <= nums.length <= 3 * 10^4`, `-10^4 <= nums[i] <= 10^4`, sorted non-decreasing
- Edge cases? Length 1 or 2 (always valid), all identical elements
- Expected output? Return integer `k`, modify array in-place
- Can input be modified? Yes

### 3. Brute Force Approach
- **Idea:** Count occurrences with a hash map, rebuild array allowing at most 2 per value.
- **Time:** O(n)
- **Space:** O(n)

### 4. Optimized Approach
- **Core Insight:** Compare `nums[read]` with `nums[write - 2]`. If they differ, this element is safe to include (at most 2 copies). This generalizes to "at most K" by comparing with `nums[write - K]`.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (counter) | O(n) | O(n) | Extra storage |
| Optimized (two pointers) | O(n) | O(1) | Elegant, generalizable |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- First 2 elements are always valid — start `write` at 2.
- For each `read` from index 2 onward, compare with `nums[write - 2]`.
- If different, this value hasn't appeared twice yet in the output — write it.

```python
def removeDuplicates(nums: list[int]) -> int:
    if len(nums) <= 2:
        return len(nums)

    write = 2  # first two elements always kept

    for read in range(2, len(nums)):
        # compare with element 2 positions back in the output
        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1

    return write
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `[1, 1, 1, 2, 2, 3]`

| Step | read | nums[read] | write | nums[write-2] | Action | Output portion |
|------|------|-----------|-------|--------------|--------|----------------|
| 0 | 2 | 1 | 2 | 1 (nums[0]) | equal, skip | [1,1] |
| 1 | 3 | 2 | 2 | 1 (nums[0]) | diff, write | [1,1,2] |
| 2 | 4 | 2 | 3 | 1 (nums[1]) | diff, write | [1,1,2,2] |
| 3 | 5 | 3 | 4 | 2 (nums[2]) | diff, write | [1,1,2,2,3] |

Return `5`. Result: `[1, 1, 2, 2, 3]`.

### Edge Case Testing
- **Empty input:** Length >= 1 per constraints
- **Single element:** `[1]` -> returns 1 (early return)
- **Typical case:** `[1,1,1,2,2,3]` -> `[1,1,2,2,3]`, returns 5
- **Extreme values:** All same `[5,5,5,5,5]` -> `[5,5]`, returns 2

### Complexity
- **Time:** O(n) — single pass
- **Space:** O(1) — in-place modification

### Optimization Discussion
The `nums[write - 2]` trick is the canonical solution. It generalizes elegantly:
- **At most K duplicates:** Compare with `nums[write - K]`
- This works because the output section is always sorted, so if `nums[read] == nums[write - K]`, there are already K copies.

### Follow-up Variations
- **Remove Duplicates I (LC 26)** — at most 1 occurrence (use `write - 1`)
- **Allow at most K duplicates** — generalized version
- **Remove duplicates from unsorted array** — requires hash set, O(n) space

### Common Traps
- Comparing with `nums[read - 2]` instead of `nums[write - 2]` — must compare against the **output** section, not the original array
- Forgetting the early return for length <= 2
- Off-by-one: starting `read` or `write` at the wrong index
