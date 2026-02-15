# Sort Array By Parity

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction
**Link:** https://leetcode.com/problems/sort-array-by-parity/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an integer array, rearrange it so that all **even** numbers come before all **odd** numbers. Any ordering within the even/odd groups is acceptable.

### 2. Clarification Questions
- Input constraints? Array length 1 to 5000. Values 0 to 5000.
- Edge cases? All even -> already valid. All odd -> already valid. Single element -> valid.
- Expected output? The rearranged array (any valid ordering accepted).
- Can input be modified? Yes — in-place modification is fine.

### 3. Brute Force Approach
- **Idea:** Create two lists (evens and odds), concatenate them.
- **Time:** O(n)
- **Space:** O(n) — extra arrays.

### 4. Optimized Approach
- 💡 **Core Insight:** Use opposite-direction two pointers like a **partition step** (similar to quicksort's partition). `left` finds the next odd number from the front, `right` finds the next even number from the back, then **swap** them into their correct halves.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Split + Concat | O(n) | O(n) | Simple, extra space |
| Two Pointers | O(n) | O(1) | In-place partition |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- `left` scans forward looking for odd numbers (misplaced in the even section).
- `right` scans backward looking for even numbers (misplaced in the odd section).
- When both find misplaced elements, swap them.

```python
def sortArrayByParity(nums: list[int]) -> list[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        # Advance left past correctly-placed even numbers
        while left < right and nums[left] % 2 == 0:
            left += 1
        # Advance right past correctly-placed odd numbers
        while left < right and nums[right] % 2 == 1:
            right -= 1

        if left < right:
            nums[left], nums[right] = nums[right], nums[left]  # swap misplaced pair
            left += 1
            right -= 1

    return nums
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `nums = [3, 1, 2, 4]`

| Step | left | right | Action | Array State |
|------|------|-------|--------|-------------|
| 1 | 0 | 3 | nums[0]=3 (odd), nums[3]=4 (even) -> swap | [4, 1, 2, 3] |
| 2 | 1 | 2 | nums[1]=1 (odd), nums[2]=2 (even) -> swap | [4, 2, 1, 3] |
| 3 | 2 | 1 | left >= right, stop | [4, 2, 1, 3] |

Result: `[4, 2, 1, 3]` (evens before odds)

### Edge Case Testing
- **Empty input:** Not possible per constraints (length >= 1).
- **Single element:** `[1]` -> `left == right`, no swap, returns `[1]`. Correct.
- **Typical case:** `[3,1,2,4]` -> `[4,2,1,3]`. Even before odd. Correct.
- **Extreme values:** All even `[2,4,6]` -> `left` advances past all, no swaps. All odd `[1,3,5]` -> `right` retreats past all, no swaps.

### Complexity
- **Time:** O(n) — each element visited at most once by each pointer.
- **Space:** O(1) — swaps are in place, only two pointer variables.

### Optimization Discussion
Already optimal. O(n) time is required since every element must be examined. O(1) space because we partition in place.

### Follow-up Variations
- **Sort Array By Parity II** (LeetCode 922): Even indices must hold even values, odd indices must hold odd values. Use two pointers — one on even indices, one on odd indices.
- **Move Zeroes** (LeetCode 283): Partition zeros to the end while maintaining relative order. Requires same-direction two pointers (order matters).
- **Dutch National Flag / Sort Colors** (LeetCode 75): Three-way partition using three pointers.

### ⚠️ Common Traps
- Forgetting the `left < right` guard in the inner `while` loops — pointers can cross.
- Checking `nums[left] % 2 == 1` for odd — works for positive numbers but be careful with negative numbers in other problems (Python's `%` handles it correctly, but some languages don't).
- Trying to maintain **relative order** — this problem doesn't require it, but if it did, opposite-direction swaps would break it (use same-direction partition instead).
