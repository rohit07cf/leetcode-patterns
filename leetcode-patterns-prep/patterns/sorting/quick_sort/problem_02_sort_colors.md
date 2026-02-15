# Sort Colors

**Difficulty:** Medium
**Pattern:** Sorting
**Subpattern:** Quick Sort / Partition
**Link:** https://leetcode.com/problems/sort-colors/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array `nums` with values `0`, `1`, and `2` (representing red, white, blue), sort them **in-place** so that all 0s come first, then 1s, then 2s. You must solve this without using the library sort function.

### 2. Clarification Questions

- **Input constraints?** `1 <= n <= 300`, values are only `0`, `1`, or `2`
- **Edge cases?** All same color, only two colors present, single element
- **Expected output?** In-place sorted array, no return value needed
- **Can input be modified?** Yes, must modify in-place

### 3. Brute Force Approach

- **Idea:** Two-pass counting sort — count 0s, 1s, 2s, then overwrite the array.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- **💡 Core Insight:** The **Dutch National Flag algorithm** (invented by Dijkstra) is a **3-way partition** that solves this in a **single pass**. Maintain three pointers: `lo` (boundary for 0s), `mid` (current scanner), and `hi` (boundary for 2s). This is the partition step of quick sort with pivot = 1.

- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Counting sort (2-pass) | O(n) | O(1) | Simple but two passes |
| Dutch National Flag | O(n) | O(1) | **Single pass**, true in-place |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use three pointers: `lo` tracks where next 0 goes, `hi` tracks where next 2 goes, `mid` scans
- When `mid` sees 0: swap with `lo`, advance both (swapped value is already processed)
- When `mid` sees 2: swap with `hi`, shrink `hi` (swapped value is unknown, don't advance `mid`)
- When `mid` sees 1: just advance `mid`

```python
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        lo, mid, hi = 0, 0, len(nums) - 1

        while mid <= hi:
            if nums[mid] == 0:
                # Swap 0 to the front
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1  # Safe: swapped value from lo is 0 or 1 (already seen)
            elif nums[mid] == 2:
                # Swap 2 to the back
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1  # Don't advance mid — swapped value is unexamined
            else:
                mid += 1  # 1 is already in the right zone
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `[2, 0, 2, 1, 1, 0]`

| Step | lo | mid | hi | Array | Action |
|------|----|-----|----|-------|--------|
| 0 | 0 | 0 | 5 | `[2,0,2,1,1,0]` | nums[0]=2, swap with hi |
| 1 | 0 | 0 | 4 | `[0,0,2,1,1,2]` | nums[0]=0, swap with lo |
| 2 | 1 | 1 | 4 | `[0,0,2,1,1,2]` | nums[1]=0, swap with lo |
| 3 | 2 | 2 | 4 | `[0,0,2,1,1,2]` | nums[2]=2, swap with hi |
| 4 | 2 | 2 | 3 | `[0,0,1,1,2,2]` | nums[2]=1, advance mid |
| 5 | 2 | 3 | 3 | `[0,0,1,1,2,2]` | nums[3]=1, advance mid |
| 6 | mid > hi, done | | | `[0,0,1,1,2,2]` | |

### Edge Case Testing

- **Empty input:** Constraint says `n >= 1`, not applicable
- **Single element:** `mid > hi` immediately or one iteration -> no swap needed
- **Typical case:** `[2,0,1]` -> `[0,1,2]`
- **Extreme values:** All same `[1,1,1]` -> mid advances through, no swaps

### Complexity

- **Time:** O(n) — each element is visited at most twice (once by `mid`, once if swapped)
- **Space:** O(1) — only three pointer variables

### Optimization Discussion

- This is already optimal — O(n) time, O(1) space, single pass
- The counting sort approach is simpler to code but requires two passes
- This algorithm generalizes to any 3-way partition problem

### Follow-up Variations

- Sort with k colors (k-way partition, requires multiple passes or different approach)
- Partition around a pivot value (same algorithm, just change the "1" to the pivot)
- Sort an array of 0s and 1s only (simpler 2-pointer partition)

### Common Traps

- **Advancing `mid` after swapping with `hi`** — the element swapped from `hi` hasn't been inspected yet; you must check it before moving on
- **Off-by-one on `hi`** — `hi` should start at `len(nums) - 1`, and loop condition is `mid <= hi` (not `<`)
- **Thinking `lo` swap needs re-inspection** — when `mid` swaps with `lo`, the swapped value is always 0 or 1 (already processed), so advancing `mid` is safe
