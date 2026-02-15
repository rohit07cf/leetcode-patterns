# Move Zeroes

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Same Direction
**Link:** https://leetcode.com/problems/move-zeroes/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an integer array `nums`, move all `0`s to the end while maintaining the relative order of the non-zero elements. Must be done **in-place** without making a copy of the array.

### 2. Clarification Questions
- Input constraints? `1 <= nums.length <= 10^4`, `-2^31 <= nums[i] <= 2^31 - 1`
- Edge cases? All zeroes, no zeroes, single element
- Expected output? Modify array in-place, return nothing
- Can input be modified? Yes, that's the requirement

### 3. Brute Force Approach
- **Idea:** Create a new array, copy non-zero elements first, then fill remaining with zeroes.
- **Time:** O(n)
- **Space:** O(n) — extra array

### 4. Optimized Approach
- **Core Insight:** Use a **slow pointer** (`write`) to track where the next non-zero should go, and a **fast pointer** (`read`) to scan through the array. Every non-zero element gets placed at `write`, then increment `write`. After the pass, fill remaining positions with 0.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(n) | Simple but uses extra space |
| Optimized (overwrite + fill) | O(n) | O(1) | Two passes, minimal writes |
| Optimized (swap) | O(n) | O(1) | Single-pass swap variant |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use `write` pointer to track insertion position for non-zero values.
- Scan with `read` pointer; when a non-zero is found, swap with `write` position.
- Both pointers move in the **same direction** (left to right).

```python
def moveZeroes(nums: list[int]) -> None:
    write = 0  # position to place next non-zero

    for read in range(len(nums)):
        if nums[read] != 0:
            # swap keeps non-zero elements in relative order
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `[0, 1, 0, 3, 12]`

| Step | read | nums[read] | write | Action | Array |
|------|------|-----------|-------|--------|-------|
| 0 | 0 | 0 | 0 | skip | [0,1,0,3,12] |
| 1 | 1 | 1 | 0 | swap(0,1) | [1,0,0,3,12] |
| 2 | 2 | 0 | 1 | skip | [1,0,0,3,12] |
| 3 | 3 | 3 | 1 | swap(1,3) | [1,3,0,0,12] |
| 4 | 4 | 12 | 1 | swap(2,4) | [1,3,12,0,0] |

Output: `[1, 3, 12, 0, 0]`

### Edge Case Testing
- **Empty input:** Length >= 1 per constraints, not applicable
- **Single element:** `[0]` -> `[0]`, `[5]` -> `[5]` — write stays at 0 or advances to 1, correct
- **Typical case:** `[0,1,0,3,12]` -> `[1,3,12,0,0]`
- **Extreme values:** All zeroes `[0,0,0]` -> `[0,0,0]`, no zeroes `[1,2,3]` -> `[1,2,3]`

### Complexity
- **Time:** O(n) — single pass through the array
- **Space:** O(1) — in-place swaps, no extra storage

### Optimization Discussion
The swap approach is already optimal. An alternative two-pass approach (copy non-zeroes, then fill zeroes) also runs in O(n)/O(1) but may perform more writes when there are few zeroes. The swap variant minimizes total writes.

### Follow-up Variations
- **Move all instances of a specific value** to the end (generalized version)
- **Minimize total number of operations** (writes)
- **Sort Colors (LC 75)** — extends the idea to three categories

### Common Traps
- Forgetting to maintain **relative order** of non-zero elements (can't just swap with the end)
- Using `nums[write] = nums[read]` without clearing old positions — need to either swap or do a fill pass
- Off-by-one on the `write` pointer after the loop when doing the fill approach
