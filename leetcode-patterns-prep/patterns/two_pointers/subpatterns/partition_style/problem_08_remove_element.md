# Remove Element

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Partition Style
**Link:** https://leetcode.com/problems/remove-element/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Remove all occurrences of a given value `val` from an array **in-place** and return the new length `k`. The first `k` elements should contain the elements that are not equal to `val`. Order beyond `k` doesn't matter.

### 2. Clarification Questions

- **Input constraints?** Array length 0–100, values 0–50, val 0–100.
- **Edge cases?** Empty array; all elements equal val; no elements equal val.
- **Expected output?** Return integer `k` (new length). Array modified in-place.
- **Can input be modified?** Yes — in-place required.

### 3. Brute Force Approach

- **Idea:** Create a new array with only elements ≠ val, copy back.
- **Time:** O(n)
- **Space:** O(n)

### 4. Optimized Approach

- 💡 **Core Insight:** Use a **write pointer** (`k`). Scan through the array — whenever `nums[i] != val`, write it at position `k` and increment `k`. This is a **partition** of "keep" vs. "remove" elements, identical to the Move Zeroes pattern.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| New array | O(n) | O(n) | Extra space |
| Write pointer | O(n) | O(1) | In-place, optimal |
| Swap with end (order doesn't matter) | O(n) | O(1) | Fewer copies when val is rare |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- `k` is the write pointer — the next position to place a kept element.
- Scan every element: if it's not `val`, copy it to `nums[k]` and advance `k`.
- After the loop, `k` is the count of remaining elements.

```python
def removeElement(nums: list[int], val: int) -> int:
    k = 0  # Write pointer for kept elements

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k
```

**Alternative — swap with end (when removals are rare):**

```python
def removeElement(nums: list[int], val: int) -> int:
    k = len(nums)
    i = 0

    while i < k:
        if nums[i] == val:
            # Swap with last element and shrink
            nums[i] = nums[k - 1]
            k -= 1
            # Don't advance i — check the swapped element
        else:
            i += 1

    return k
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `nums = [3, 2, 2, 3]`, `val = 3`

| i | nums[i] | Action | k | Array |
|---|---------|--------|---|-------|
| 0 | 3 | skip | 0 | [3,2,2,3] |
| 1 | 2 | copy to k=0 | 1 | [2,2,2,3] |
| 2 | 2 | copy to k=1 | 2 | [2,2,2,3] |
| 3 | 3 | skip | 2 | [2,2,2,3] |

Return `k = 2`. First 2 elements: `[2, 2]`.

### Edge Case Testing

- **Empty input:** `nums = []` → loop doesn't run, return 0.
- **Single element:** `[3], val=3` → skip, return 0. `[3], val=2` → copy, return 1.
- **Typical case:** `[3,2,2,3], val=3` → `k=2`.
- **Extreme values:** All equal to val → return 0. None equal to val → return n.

### Complexity

- **Time:** O(n) — single pass.
- **Space:** O(1) — one pointer variable.

### Optimization Discussion

**Standard approach:** O(n) copies regardless. Best when val is common.

**Swap-with-end approach:** Number of copies equals number of elements to remove. Best when val is rare. But doesn't preserve relative order.

### Follow-up Variations

- **Remove Duplicates from Sorted Array (LC 26)** — same write-pointer pattern, condition changes to duplicate detection.
- **Move Zeroes (LC 283)** — partition non-zeroes to front, zeroes to back.
- **Remove Element with order preservation guaranteed** — use the standard approach.

### ⚠️ Common Traps

- **Returning the array instead of the count:** The function returns an integer `k`, not the array.
- **Forgetting the swap-with-end doesn't preserve order:** If follow-up asks about order, use the standard write-pointer approach.
- **Not handling empty array:** Check that the loop simply doesn't execute.
