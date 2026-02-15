# Move Zeroes

**Difficulty:** Easy
**Pattern:** Sorting
**Subpattern:** Quick Sort / Partition
**Link:** https://leetcode.com/problems/move-zeroes/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums`, move all `0`s to the **end** while maintaining the **relative order** of non-zero elements. Must be done **in-place** without making a copy of the array.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 10^4`, `-2^31 <= nums[i] <= 2^31 - 1`
- **Edge cases?** No zeroes, all zeroes, single element, zeroes at start/end
- **Expected output?** In-place modification, no return needed
- **Can input be modified?** Yes, must modify in-place

### 3. Brute Force Approach

- **Idea:** Create a new array with non-zero elements first, then fill remaining with zeroes.
- **Time:** O(n)
- **Space:** O(n)

### 4. Optimized Approach

- **💡 Core Insight:** This is a **stable partition** — partition around the value 0, keeping non-zero elements in their original order. Use a "write pointer" (`insert_pos`) that tracks where the next non-zero should go. This mirrors the **Lomuto partition scheme** where elements are moved to the "less than pivot" side.

- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| New array | O(n) | O(n) | Violates in-place requirement |
| **Lomuto-style partition** | **O(n)** | **O(1)** | In-place, stable, minimal writes |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Maintain `insert_pos` — the index where the next non-zero element should be placed
- Scan through the array with `i`
- When `nums[i]` is non-zero, place it at `insert_pos` and increment
- After the scan, fill remaining positions with zeroes

```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_pos = 0  # Where the next non-zero should go

        # Pass 1: Move all non-zero elements to the front, preserving order
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # Pass 2: Fill the rest with zeroes
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
```

**Alternative: Single-pass swap approach**

```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_pos = 0  # Boundary of non-zero region

        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap non-zero to the front (only swap if positions differ)
                if i != insert_pos:
                    nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `[0, 1, 0, 3, 12]`

**Two-pass approach:**

| Step | i | insert_pos | Array | Action |
|------|---|------------|-------|--------|
| 0 | 0 | 0 | `[0,1,0,3,12]` | nums[0]=0, skip |
| 1 | 1 | 0 | `[0,1,0,3,12]` | nums[1]=1, place at 0 -> `[1,1,0,3,12]`, insert_pos=1 |
| 2 | 2 | 1 | `[1,1,0,3,12]` | nums[2]=0, skip |
| 3 | 3 | 1 | `[1,1,0,3,12]` | nums[3]=3, place at 1 -> `[1,3,0,3,12]`, insert_pos=2 |
| 4 | 4 | 2 | `[1,3,0,3,12]` | nums[4]=12, place at 2 -> `[1,3,12,3,12]`, insert_pos=3 |
| Fill | | 3 | `[1,3,12,0,0]` | Fill indices 3,4 with 0 |

Result: `[1, 3, 12, 0, 0]`

### Edge Case Testing

- **Empty input:** Constraint says `n >= 1`, not applicable
- **Single element:** `[0]` -> `[0]`, `[5]` -> `[5]` (insert_pos = 0 or 1, trivial)
- **Typical case:** `[0,1,0,3,12]` -> `[1,3,12,0,0]`
- **Extreme values:** No zeroes `[1,2,3]` -> unchanged; all zeroes `[0,0,0]` -> unchanged

### Complexity

- **Time:** O(n) — single pass through the array (or two passes for the fill version)
- **Space:** O(1) — only one extra variable `insert_pos`

### Optimization Discussion

- **Swap approach** is a true single-pass but performs more operations per element (swaps instead of assignments)
- **Two-pass approach** minimizes writes when there are few non-zero elements at the end
- The `if i != insert_pos` check in the swap approach avoids unnecessary self-swaps

### Follow-up Variations

- Move zeroes to the front instead of end (scan from right to left)
- Move a specific value to the end (change condition from `!= 0` to `!= val`)
- Remove Element (LeetCode 27) — same Lomuto pattern, return new length
- Remove Duplicates from Sorted Array (LeetCode 26) — same write-pointer idea

### Common Traps

- **Not preserving relative order** — using a two-pointer swap from both ends (like Sort Array By Parity) is **not stable** and would reorder non-zero elements
- **Forgetting to fill with zeroes** — the two-pass approach leaves old values behind indices `insert_pos` to `n-1`
- **Self-swap when `i == insert_pos`** — not a bug but wastes operations; the `if i != insert_pos` guard optimizes this
- **Confusing this with "partition"** — standard quick sort partition is unstable; this problem requires a **stable** partition
