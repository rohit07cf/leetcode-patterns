# Segregate Even and Odd Numbers

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Partition Style
**Link:** https://www.geeksforgeeks.org/segregate-even-and-odd-numbers/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of integers, rearrange it so that all **even** numbers appear before all **odd** numbers. The relative order within even and odd groups does **not** need to be preserved.

### 2. Clarification Questions

- **Input constraints?** Typical: array length 1–10⁵, values can be any integers (positive, negative, zero).
- **Edge cases?** All even; all odd; single element; negative numbers (even/odd determined by `% 2`); zero is even.
- **Expected output?** Modify array in-place (or return rearranged array).
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Create two lists (evens and odds), concatenate.
- **Time:** O(n)
- **Space:** O(n)

### 4. Optimized Approach

- 💡 **Core Insight:** Classic **Hoare-style two-pointer partition**. `lo` starts at the beginning, `hi` at the end. Move `lo` right past evens, move `hi` left past odds, then swap the misplaced pair. This is the simplest partition problem — a direct warm-up for Dutch National Flag.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Two lists + concat | O(n) | O(n) | Simple, extra space |
| Two-pointer partition | O(n) | O(1) | In-place, optimal |
| Stable partition (preserve order) | O(n) | O(n) | Needed if order matters |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Two pointers approach from both ends.
- `lo` advances while pointing at even numbers (correctly placed).
- `hi` retreats while pointing at odd numbers (correctly placed).
- When both stop — `lo` at an odd, `hi` at an even — swap them.

```python
def segregate_even_odd(nums: list[int]) -> list[int]:
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        # Skip correctly placed evens on the left
        while lo < hi and nums[lo] % 2 == 0:
            lo += 1
        # Skip correctly placed odds on the right
        while lo < hi and nums[hi] % 2 == 1:
            hi -= 1
        # Swap misplaced pair
        if lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1

    return nums
```

**Variant preserving relative order (stable partition):**

```python
def segregate_even_odd_stable(nums: list[int]) -> list[int]:
    """Preserves relative order using write-pointer technique."""
    result = [0] * len(nums)
    write = 0

    # First pass: place evens
    for num in nums:
        if num % 2 == 0:
            result[write] = num
            write += 1

    # Second pass: place odds
    for num in nums:
        if num % 2 == 1:
            result[write] = num
            write += 1

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `[12, 34, 45, 9, 8, 90, 3]`

| Step | lo | hi | Action | Array |
|------|----|----|--------|-------|
| 1 | 0 | 6 | 12 even → lo=1 | [12,34,45,9,8,90,3] |
| 2 | 1 | 6 | 34 even → lo=2 | [12,34,45,9,8,90,3] |
| 3 | 2 | 6 | 45 odd, stop lo | [12,34,45,9,8,90,3] |
| 4 | 2 | 6 | 3 odd → hi=5 | [12,34,45,9,8,90,3] |
| 5 | 2 | 5 | 90 even, stop hi | [12,34,45,9,8,90,3] |
| 6 | 2 | 5 | swap(2,5), lo=3, hi=4 | [12,34,90,9,8,45,3] |
| 7 | 3 | 4 | 9 odd, stop lo | [12,34,90,9,8,45,3] |
| 8 | 3 | 4 | 8 even, stop hi | [12,34,90,9,8,45,3] |
| 9 | 3 | 4 | swap(3,4), lo=4, hi=3 | [12,34,90,8,9,45,3] |

lo > hi → stop. Result: `[12, 34, 90, 8, 9, 45, 3]` — evens before odds.

### Edge Case Testing

- **Empty input:** `lo > hi` initially if somehow length 0; loop doesn't execute.
- **Single element:** `[5]` → `lo == hi`, loop doesn't execute.
- **Typical case:** `[12,34,45,9,8,90,3]` → evens first, odds last.
- **Extreme values:** All even `[2,4,6]` → `lo` advances past all, no swaps. All odd `[1,3,5]` → `hi` retreats past all, no swaps.

### Complexity

- **Time:** O(n) — each element visited at most once by either pointer.
- **Space:** O(1) — two pointer variables only.

### Optimization Discussion

The Hoare-style partition is optimal for the unstable version. If relative order must be preserved, O(n) extra space is needed (or O(n²) with in-place shifting). This problem is the simplest possible partition and is the ideal **first problem** to practice before Sort Colors.

### Follow-up Variations

- **Preserve relative order** — use stable partition (two-pass or extra array).
- **Sort Array By Parity (LC 905)** — same problem on LeetCode.
- **Three-way partition** — extend to even / divisible-by-3-but-not-2 / odd.
- **Negative before positive** — same structure, different predicate.

### ⚠️ Common Traps

- **Negative number modulo in Python:** In Python, `-3 % 2 == 1` (not -1 like in C/Java). This is actually helpful — Python's modulo always returns non-negative for positive divisors. But in other languages, use `abs(num) % 2` or bitwise `num & 1`.
- **Missing `lo < hi` guard in inner while loops:** Without bounds checking, pointers can cross and cause index errors.
- **Confusing stable vs. unstable partition:** The two-pointer swap approach does **not** preserve relative order. State this explicitly in an interview.
