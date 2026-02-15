# Sort Array By Parity

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Partition Style
**Link:** https://leetcode.com/problems/sort-array-by-parity/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array, rearrange it so that all **even** numbers come before all **odd** numbers. Any ordering within the even/odd groups is acceptable.

### 2. Clarification Questions

- **Input constraints?** Array length 1–5000, values 0–5000.
- **Edge cases?** All even; all odd; single element; zero is even.
- **Expected output?** Return the rearranged array (or modify in-place).
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Create two separate lists for evens and odds, then concatenate them.
- **Time:** O(n)
- **Space:** O(n)

### 4. Optimized Approach

- 💡 **Core Insight:** Classic **two-pointer partition**. Use `lo` at the start and `hi` at the end. Move `lo` right past evens, move `hi` left past odds, then swap when both are misplaced. This is identical to Lomuto/Hoare-style partitioning around "even vs. odd."
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Two lists + concat | O(n) | O(n) | Simple, extra space |
| Two-pointer swap | O(n) | O(1) | In-place, optimal |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- `lo` starts at index 0, `hi` at end.
- `lo` advances while pointing at even numbers (correctly placed).
- `hi` retreats while pointing at odd numbers (correctly placed).
- When both stop, swap — an odd at `lo` with an even at `hi`.

```python
def sortArrayByParity(nums: list[int]) -> list[int]:
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        # Advance lo past evens
        while lo < hi and nums[lo] % 2 == 0:
            lo += 1
        # Retreat hi past odds
        while lo < hi and nums[hi] % 2 == 1:
            hi -= 1
        # Swap misplaced pair
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo += 1
        hi -= 1

    return nums
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `[3, 1, 2, 4]`

| Step | lo | hi | Action | Array |
|------|----|----|--------|-------|
| 1 | 0 | 3 | lo→3(odd), hi→4(even), swap | [4,1,2,3] |
| 2 | 1 | 2 | lo→1(odd), hi→2(even), swap | [4,2,1,3] |
| 3 | 2 | 1 | lo > hi, stop | [4,2,1,3] |

Result: `[4, 2, 1, 3]` — all evens before odds.

### Edge Case Testing

- **Empty input:** Not possible per constraints (length ≥ 1).
- **Single element:** `[1]` → `[1]`, no swap.
- **Typical case:** `[3,1,2,4]` → `[4,2,1,3]`.
- **Extreme values:** All even `[2,4,6]` → no swaps; all odd `[1,3,5]` → no effective swaps.

### Complexity

- **Time:** O(n) — each element visited at most once by either pointer.
- **Space:** O(1) — two pointers, in-place swaps.

### Optimization Discussion

Already optimal. The two-pointer approach is a direct application of Hoare's partition scheme. You can also use a single-pointer scan (like Move Zeroes) if you want to preserve relative order within the even group.

### Follow-up Variations

- **Preserve relative order** — use the stable partition (insert_pos technique from Move Zeroes).
- **Sort Array By Parity II (LC 922)** — evens at even indices, odds at odd indices.
- **Three-way partition** — e.g., divisible by 3, remainder 1, remainder 2.

### ⚠️ Common Traps

- **Forgetting `lo < hi` guard in inner loops:** Without it, pointers can cross and cause out-of-bounds access.
- **Not handling the `lo == hi` case:** If the middle element is the stopping point, the extra swap is harmless but be mindful in explanations.
