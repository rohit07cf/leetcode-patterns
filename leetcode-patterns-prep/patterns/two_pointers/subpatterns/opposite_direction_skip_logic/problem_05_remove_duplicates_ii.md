# Remove Duplicates from Sorted Array II

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction — Skip Logic
**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a sorted integer array `nums`, remove duplicates **in-place** such that each element appears **at most twice**. Return the new length `k`, with the first `k` elements of `nums` holding the result.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 3 * 10^4`, `-10^4 <= nums[i] <= 10^4`, array is sorted in non-decreasing order
- **Edge cases?** All identical, all unique, exactly two of each, single element
- **Expected output?** Integer `k` — the length of the valid portion; first `k` elements modified in-place
- **Can input be modified?** Yes — required to modify in-place

### 3. Brute Force Approach

- **Idea:** Use extra array, copy elements allowing at most two of each. Then copy back.
- **Time:** O(n)
- **Space:** O(n)

### 4. Optimized Approach

- **💡 Core Insight:** Use a **write pointer** (`w`) and a **read pointer** (`r`). The skip logic: for each element the read pointer sees, compare it to `nums[w - 2]` (two positions back in the write area). If they're the same, this would be a third duplicate — **skip it**. Otherwise, write it and advance `w`. This generalizes to "at most K" by comparing with `nums[w - K]`.

- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Extra Array | O(n) | O(n) | Simple but uses space |
| Two Pointers | O(n) | O(1) | In-place with skip logic |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Write pointer `w` tracks where the next valid element goes.
- Read pointer `r` scans every element.
- **Skip condition:** if `w >= 2` and `nums[r] == nums[w - 2]`, this is a 3rd+ duplicate — skip.
- Otherwise, copy `nums[r]` to `nums[w]` and advance `w`.
- First two elements are always kept (can't exceed limit with fewer than 3).

```python
def removeDuplicates(nums: list[int]) -> int:
    if len(nums) <= 2:
        return len(nums)

    w = 2  # First two elements always valid

    for r in range(2, len(nums)):
        # Skip if this would be a 3rd consecutive duplicate
        if nums[r] != nums[w - 2]:
            nums[w] = nums[r]
            w += 1

    return w
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [1, 1, 1, 2, 2, 3]`

| r | nums[r] | nums[w-2] | skip? | action | w | nums state |
|---|---------|-----------|-------|--------|---|------------|
| 2 | 1 | 1 | yes | skip | 2 | [1,1,1,2,2,3] |
| 3 | 2 | 1 | no | write | 3 | [1,1,2,2,2,3] |
| 4 | 2 | 1 | no | write | 4 | [1,1,2,2,2,3] |
| 5 | 3 | 2 | no | write | 5 | [1,1,2,2,3,3] |

**Output:** `k = 5`, `nums[:5] = [1, 1, 2, 2, 3]` ✓

### Edge Case Testing

- **Empty input:** Constraints guarantee `n >= 1`.
- **Single element:** `[1]` → returns 1 immediately.
- **Typical case:** Works as shown.
- **Extreme values:** All identical `[2,2,2,2,2]` → keeps first two → `k = 2`.

### Complexity

- **Time:** O(n) — single pass through the array
- **Space:** O(1) — in-place modification, only pointer variables

### Optimization Discussion

This is already optimal. The elegant part is the **generalization**: to allow at most `K` duplicates, simply change `w = 2` to `w = K` and `nums[w - 2]` to `nums[w - K]`. Same code works for Remove Duplicates I (K=1).

```python
# Generalized version — allow at most K duplicates
def removeDuplicatesK(nums, K):
    w = min(K, len(nums))
    for r in range(w, len(nums)):
        if nums[r] != nums[w - K]:
            nums[w] = nums[r]
            w += 1
    return w
```

### Follow-up Variations

- **Remove Duplicates from Sorted Array (LC 26):** Same idea with K=1.
- **Remove Element (LC 27):** Skip a specific value instead of duplicates.
- **Move Zeroes (LC 283):** Write pointer for non-zeros, fill remainder with zeros.

### ⚠️ Common Traps

- **Comparing with `nums[r-1]` instead of `nums[w-2]`** — you must compare against the *write* region, not the read region, because the read region may contain already-skipped duplicates.
- **Starting `w` at 0** — the first two elements are always valid; start at `w = 2`.
- **Off-by-one in the lookback** — `w - 2` not `w - 1`; we allow *two* copies, so we check two positions back.
