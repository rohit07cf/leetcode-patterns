# Sort Array By Parity

**Difficulty:** Easy
**Pattern:** Sorting
**Subpattern:** Quick Sort / Partition
**Link:** https://leetcode.com/problems/sort-array-by-parity/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums`, move all **even** integers to the beginning and all **odd** integers to the end. Return any array that satisfies this condition.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 5000`, `0 <= nums[i] <= 5000`
- **Edge cases?** All even, all odd, single element, alternating
- **Expected output?** Any valid arrangement with evens before odds
- **Can input be modified?** Yes, in-place is acceptable

### 3. Brute Force Approach

- **Idea:** Create two lists — one for evens, one for odds — then concatenate.
- **Time:** O(n)
- **Space:** O(n)

### 4. Optimized Approach

- **💡 Core Insight:** This is a **2-way partition** — the simplest form of the quick sort partition step. Use two pointers from opposite ends. Swap when `left` points to odd and `right` points to even. This is identical to partitioning around a "parity pivot."

- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Two lists + concat | O(n) | O(n) | Simple but extra space |
| **Two-pointer partition** | **O(n)** | **O(1)** | In-place, single pass |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Two pointers: `left` starts at 0, `right` starts at end
- `left` advances past even numbers (they're already correct)
- `right` retreats past odd numbers (they're already correct)
- When `left` is odd and `right` is even -> swap them

```python
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            # Advance left past evens (already in correct position)
            if nums[left] % 2 == 0:
                left += 1
            # Retreat right past odds (already in correct position)
            elif nums[right] % 2 == 1:
                right -= 1
            else:
                # left is odd, right is even — swap them
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `[3, 1, 2, 4]`

| Step | left | right | Array | Action |
|------|------|-------|-------|--------|
| 0 | 0 | 3 | `[3,1,2,4]` | nums[0]=3 odd, nums[3]=4 even -> swap |
| 1 | 1 | 2 | `[4,1,2,3]` | nums[1]=1 odd, nums[2]=2 even -> swap |
| 2 | 2 | 1 | `[4,2,1,3]` | left >= right, done |

Result: `[4, 2, 1, 3]` — all evens before odds.

### Edge Case Testing

- **Empty input:** Constraint says `n >= 1`, not applicable
- **Single element:** `left >= right` immediately -> return as-is
- **Typical case:** `[3,1,2,4]` -> `[4,2,1,3]`
- **Extreme values:** All even `[2,4,6]` -> left advances to end, no swaps; all odd `[1,3,5]` -> right retreats to start, no swaps

### Complexity

- **Time:** O(n) — each element examined at most once, pointers converge
- **Space:** O(1) — only two pointer variables, swaps in-place

### Optimization Discussion

- Already optimal: O(n) time and O(1) space
- This is the simplest application of the partition concept
- Could also use a single-pointer approach (like Lomuto partition) but two-pointer is more intuitive

### Follow-up Variations

- Sort Array By Parity II (even at even indices, odd at odd indices)
- Partition array by a predicate function (generalized version)
- Sort by divisibility by k (not just 2)
- Stable partition (maintain relative order within evens and odds) — requires O(n) space

### Common Traps

- **Using `% 2 == 1` for odd check on negative numbers** — in Python, `-3 % 2 == 1` so this works, but in other languages `-3 % 2 == -1`; use `% 2 != 0` for safety
- **Not advancing both pointers after swap** — after swapping, both elements are in their correct zones, so advance both
- **Off-by-one in loop condition** — use `left < right` (not `<=`); when they're equal, that element can go on either side
