# Remove Element

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Same Direction
**Link:** https://leetcode.com/problems/remove-element/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` **in-place**. Return the count `k` of elements that are not equal to `val`. The first `k` elements of `nums` must contain those remaining values (order can change).

### 2. Clarification Questions
- Input constraints? `0 <= nums.length <= 100`, `0 <= nums[i] <= 50`, `0 <= val <= 100`
- Edge cases? Empty array, all elements equal to val, val not in array
- Expected output? Return count `k`; first `k` positions hold non-val elements
- Can input be modified? Yes, and order of remaining elements doesn't matter

### 3. Brute Force Approach
- **Idea:** Create a new array with elements != val, copy back.
- **Time:** O(n)
- **Space:** O(n)

### 4. Optimized Approach
- **Core Insight:** Use a `write` pointer to track where the next "kept" element goes. Scan with `read`; whenever `nums[read] != val`, write it at `write` and advance.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(n) | Extra array |
| Two Pointers (same direction) | O(n) | O(1) | In-place, preserves order |
| Two Pointers (swap with end) | O(n) | O(1) | Fewer copies when val is rare, doesn't preserve order |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- `write` tracks the insertion index for non-val elements.
- `read` scans every element; copy non-val elements forward.

```python
def removeElement(nums: list[int], val: int) -> int:
    write = 0

    for read in range(len(nums)):
        if nums[read] != val:
            # keep this element — place at write position
            nums[write] = nums[read]
            write += 1

    return write
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `nums = [3, 2, 2, 3], val = 3`

| Step | read | nums[read] | write | Action | Array |
|------|------|-----------|-------|--------|-------|
| 0 | 0 | 3 | 0 | skip (== val) | [3,2,2,3] |
| 1 | 1 | 2 | 0 | copy, write=1 | [2,2,2,3] |
| 2 | 2 | 2 | 1 | copy, write=2 | [2,2,2,3] |
| 3 | 3 | 3 | 2 | skip (== val) | [2,2,2,3] |

Return `2`. First 2 elements: `[2, 2]`.

### Edge Case Testing
- **Empty input:** `nums = []` -> loop doesn't execute, returns 0
- **Single element:** `[3], val=3` -> skip, returns 0. `[3], val=2` -> keep, returns 1
- **Typical case:** `[0,1,2,2,3,0,4,2], val=2` -> returns 5
- **Extreme values:** All equal to val -> returns 0. None equal to val -> returns n

### Complexity
- **Time:** O(n) — single pass
- **Space:** O(1) — in-place

### Optimization Discussion
If removals are **rare**, the "swap with last" approach avoids unnecessary copies:

```python
def removeElement(nums, val):
    i, n = 0, len(nums)
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1  # don't advance i — need to check swapped element
        else:
            i += 1
    return n
```

This does at most `k` assignments (where `k` = count of val) instead of `n - k`.

### Follow-up Variations
- **Move Zeroes (LC 283)** — same pattern but zeroes go to end
- **Remove Duplicates (LC 26)** — similar write pointer, different condition
- **Remove All Adjacent Duplicates (LC 1047)** — stack-based variant

### Common Traps
- Forgetting to return `write` (not `write + 1` here, since we increment **after** writing)
- Trying to delete elements mid-iteration with `del` or `pop` — O(n) per operation, O(n^2) total
- In the swap-with-end variant, advancing `i` after a swap before checking the swapped element
