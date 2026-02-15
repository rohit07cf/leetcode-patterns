# Sort Colors

**Difficulty:** Medium
**Pattern:** Sorting
**Subpattern:** Merge Sort
**Link:** https://leetcode.com/problems/sort-colors/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array `nums` with `n` objects colored red (0), white (1), or blue (2), sort them **in-place** so that objects of the same color are adjacent, in the order red, white, blue. You must solve this without using the library sort function.

### 2. Clarification Questions

- **Input constraints?** `1 <= n <= 300`, `nums[i]` is `0`, `1`, or `2`.
- **Edge cases?** All same color, only two colors present, single element.
- **Expected output?** Array sorted in-place, no return value.
- **Can input be modified?** Yes, must be in-place.

### 3. Brute Force Approach

- **Idea:** **Two-pass counting sort.** Count occurrences of 0, 1, 2 in the first pass. Overwrite the array with the correct counts in the second pass.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** **Dutch National Flag algorithm** (one pass). Use three pointers: `lo` (boundary for 0s), `mid` (current element), `hi` (boundary for 2s). Scan with `mid`: swap 0s to the front, swap 2s to the back, leave 1s in the middle. This is a **three-way partition** — the partitioning step that merge sort's merge complements.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (counting sort) | O(n) | O(1) | Two passes, simple |
| Dutch National Flag | O(n) | O(1) | One pass, interview favorite |
| Merge Sort | O(n log n) | O(n) | Overkill, but shows merge sort knowledge |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Three pointers:** `lo = 0` (next position for 0), `mid = 0` (current scanner), `hi = n - 1` (next position for 2).
- **Invariant:** `[0, lo)` are all 0s, `[lo, mid)` are all 1s, `(hi, n-1]` are all 2s.
- Process `nums[mid]`:
  - If **0**: swap with `lo`, advance both `lo` and `mid`.
  - If **1**: just advance `mid`.
  - If **2**: swap with `hi`, decrement `hi` (don't advance `mid` — swapped element needs inspection).

```python
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        lo, mid, hi = 0, 0, len(nums) - 1

        while mid <= hi:
            if nums[mid] == 0:
                # Swap 0 to the front
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 stays in the middle, just advance
                mid += 1
            else:  # nums[mid] == 2
                # Swap 2 to the back — don't advance mid (new element needs check)
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [2, 0, 2, 1, 1, 0]`

| Step | lo | mid | hi | nums | Action |
|------|----|----|-----|------|--------|
| 1 | 0 | 0 | 5 | [2,0,2,1,1,0] | nums[0]=2, swap with hi -> [0,0,2,1,1,2], hi=4 |
| 2 | 0 | 0 | 4 | [0,0,2,1,1,2] | nums[0]=0, swap with lo -> no change, lo=1, mid=1 |
| 3 | 1 | 1 | 4 | [0,0,2,1,1,2] | nums[1]=0, swap with lo -> no change, lo=2, mid=2 |
| 4 | 2 | 2 | 4 | [0,0,2,1,1,2] | nums[2]=2, swap with hi -> [0,0,1,1,2,2], hi=3 |
| 5 | 2 | 2 | 3 | [0,0,1,1,2,2] | nums[2]=1, mid=3 |
| 6 | 2 | 3 | 3 | [0,0,1,1,2,2] | nums[3]=1, mid=4 |
| 7 | — | 4 | 3 | — | mid > hi, stop |

**Output:** `[0, 0, 1, 1, 2, 2]`

### Edge Case Testing

- **Empty input:** Not possible (length >= 1).
- **Single element:** `[1]` -> `[1]`, loop runs once and advances `mid` past `hi`.
- **Typical case:** `[2, 0, 2, 1, 1, 0]` -> `[0, 0, 1, 1, 2, 2]`.
- **Extreme values:** All same `[1, 1, 1]` -> no swaps, `mid` advances through all. Two colors `[2, 0, 2, 0]` -> `[0, 0, 2, 2]`.

### Complexity

- **Time:** O(n) — single pass, each element processed at most twice (once by `mid`, once when swapped).
- **Space:** O(1) — in-place, only three pointer variables.

### Optimization Discussion

- **Why not merge sort?** Merge sort would work (O(n log n), O(n) space) but is overkill for three values. The Dutch National Flag is the canonical O(n) one-pass solution.
- **Connection to merge sort:** This problem illustrates **partitioning**, the complement of merging. Merge sort splits arbitrarily and merges intelligently; quicksort (and this problem) partitions intelligently. Understanding both is essential.
- **Counting sort** is the two-pass alternative — count 0s, 1s, 2s, then overwrite. Simpler but the one-pass Dutch Flag algorithm is what interviewers expect.

### Follow-up Variations

- Sort an Array (LC 912) — full sorting required.
- Move Zeroes (LC 283) — partition zeros to the end.
- Wiggle Sort II (LC 324) — uses Dutch National Flag as a subroutine.
- Sort Array By Parity (LC 905) — two-way partition.

### Common Traps

- **Advancing `mid` after swapping with `hi`.** The element swapped from `hi` to `mid` hasn't been inspected yet. It could be 0, 1, or 2. You must NOT advance `mid` in this case.
- **Advancing `mid` after swapping with `lo` is safe** because `lo <= mid`, so the swapped element is either a 1 (already inspected) or the same element (when `lo == mid`).
- **Using `mid < hi` instead of `mid <= hi`.** When `mid == hi`, the element at that position still needs to be classified. Use `<=`.
