# Sort Colors (Dutch National Flag)

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Partition Style
**Link:** https://leetcode.com/problems/sort-colors/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array with elements 0, 1, and 2 (representing red, white, blue), sort them **in-place** so all 0s come first, then 1s, then 2s — without using a library sort.

### 2. Clarification Questions

- **Input constraints?** Array of length 1–300, values only 0, 1, 2.
- **Edge cases?** All same color; only two colors present; single element.
- **Expected output?** Modify array in-place; no return value.
- **Can input be modified?** Yes — in-place is required.

### 3. Brute Force Approach

- **Idea:** Count occurrences of 0, 1, 2. Then overwrite the array with that many of each value (two-pass).
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- 💡 **Core Insight:** Use **three pointers** (Dutch National Flag by Dijkstra). Pointer `lo` tracks the boundary for 0s, `hi` tracks boundary for 2s, and `mid` scans through. Swap elements to their correct region in a single pass.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Counting sort (two-pass) | O(n) | O(1) | Simple but two passes |
| Dutch National Flag (one-pass) | O(n) | O(1) | Single pass, true partition style |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Maintain three pointers: `lo = 0`, `mid = 0`, `hi = n - 1`.
- `mid` scans left to right:
  - If `nums[mid] == 0`: swap with `lo`, advance both `lo` and `mid`.
  - If `nums[mid] == 1`: just advance `mid`.
  - If `nums[mid] == 2`: swap with `hi`, decrement `hi` (don't advance `mid` — the swapped value is unexamined).

```python
def sortColors(nums: list[int]) -> None:
    lo, mid, hi = 0, 0, len(nums) - 1

    while mid <= hi:
        if nums[mid] == 0:
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[hi] = nums[hi], nums[mid]
            hi -= 1
            # Don't advance mid — swapped element needs inspection
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `[2, 0, 2, 1, 1, 0]`

| Step | lo | mid | hi | Array | Action |
|------|----|-----|----|-------|--------|
| 1 | 0 | 0 | 5 | [2,0,2,1,1,0] | nums[mid]=2 → swap(mid,hi), hi-- |
| 2 | 0 | 0 | 4 | [0,0,2,1,1,2] | nums[mid]=0 → swap(lo,mid), lo++, mid++ |
| 3 | 1 | 1 | 4 | [0,0,2,1,1,2] | nums[mid]=0 → swap(lo,mid), lo++, mid++ |
| 4 | 2 | 2 | 4 | [0,0,2,1,1,2] | nums[mid]=2 → swap(mid,hi), hi-- |
| 5 | 2 | 2 | 3 | [0,0,1,1,2,2] | nums[mid]=1 → mid++ |
| 6 | 2 | 3 | 3 | [0,0,1,1,2,2] | nums[mid]=1 → mid++ |

mid > hi → stop. Result: `[0, 0, 1, 1, 2, 2]`

### Edge Case Testing

- **Empty input:** Length constraint is ≥ 1, but code handles it (loop doesn't execute).
- **Single element:** `[1]` → no swaps, returns `[1]`.
- **Typical case:** `[2,0,1]` → `[0,1,2]`.
- **Extreme values:** All same value `[0,0,0]` → no swaps needed.

### Complexity

- **Time:** O(n) — each element is visited at most twice (once by `mid`, at most one swap).
- **Space:** O(1) — only three pointer variables.

### Optimization Discussion

The one-pass Dutch National Flag is already optimal. The two-pass counting approach is simpler to code but interviewers specifically want the partition-based single-pass solution.

### Follow-up Variations

- **Sort with k distinct values** — generalize to k-way partition.
- **Partition around a pivot** — foundation of quicksort's partition step.
- **Sort Colors II (LintCode 143)** — sort array with k colors in-place.

### ⚠️ Common Traps

- **Advancing `mid` after swapping with `hi`:** The element swapped from `hi` hasn't been examined yet. You must **not** increment `mid` in the `== 2` case.
- **Off-by-one on termination:** The loop condition is `mid <= hi` (inclusive), not `mid < hi`.
