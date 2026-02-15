# Move Zeroes

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Partition Style
**Link:** https://leetcode.com/problems/move-zeroes/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Move all zeroes in an array to the end while maintaining the relative order of non-zero elements. Must be done **in-place** without making a copy.

### 2. Clarification Questions

- **Input constraints?** Array length 1–10⁴, values are arbitrary integers.
- **Edge cases?** No zeroes; all zeroes; single element.
- **Expected output?** Modify array in-place; no return value.
- **Can input be modified?** Yes — in-place is required.

### 3. Brute Force Approach

- **Idea:** Create a new array. Copy all non-zero elements first, then fill the rest with zeroes.
- **Time:** O(n)
- **Space:** O(n)

### 4. Optimized Approach

- 💡 **Core Insight:** Use a **write pointer** (`insert_pos`) that tracks where the next non-zero should go. Scan with a read pointer — every non-zero gets written at `insert_pos`, then fill the rest with zeroes. This is a **partition** of non-zero vs. zero elements.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Extra array | O(n) | O(n) | Simple but uses extra space |
| Two-pointer (overwrite + fill) | O(n) | O(1) | Two passes but in-place |
| Two-pointer (swap) | O(n) | O(1) | Single pass, preserves order |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- `insert_pos` marks where the next non-zero should be placed.
- Scan left to right. When a non-zero is found, swap it with position `insert_pos` and advance `insert_pos`.
- This naturally pushes zeroes to the right while preserving order.

```python
def moveZeroes(nums: list[int]) -> None:
    insert_pos = 0  # Where the next non-zero should go

    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap non-zero to its correct position
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `[0, 1, 0, 3, 12]`

| i | insert_pos | Action | Array |
|---|------------|--------|-------|
| 0 | 0 | nums[0]=0, skip | [0,1,0,3,12] |
| 1 | 0 | nums[1]=1, swap(0,1), insert_pos=1 | [1,0,0,3,12] |
| 2 | 1 | nums[2]=0, skip | [1,0,0,3,12] |
| 3 | 1 | nums[3]=3, swap(1,3), insert_pos=2 | [1,3,0,0,12] |
| 4 | 2 | nums[4]=12, swap(2,4), insert_pos=3 | [1,3,12,0,0] |

Result: `[1, 3, 12, 0, 0]`

### Edge Case Testing

- **Empty input:** Length ≥ 1 per constraints; single element handled trivially.
- **Single element:** `[0]` → `[0]`, `[5]` → `[5]`.
- **Typical case:** `[0,1,0,3,12]` → `[1,3,12,0,0]`.
- **Extreme values:** All zeroes `[0,0,0]` → `[0,0,0]`; no zeroes `[1,2,3]` → `[1,2,3]` (swap with self).

### Complexity

- **Time:** O(n) — single pass through the array.
- **Space:** O(1) — two pointers only.

### Optimization Discussion

The swap approach is optimal. An alternative two-pass method (copy non-zeroes, then fill zeroes) avoids swaps but writes more. The swap version minimizes total write operations when there are few zeroes.

### Follow-up Variations

- **Move all instances of a value to end** — generalize to any target value.
- **Minimize total operations** — if few non-zeroes, iterate from right.
- **Remove Element (LC 27)** — same pattern but remove instead of move.

### ⚠️ Common Traps

- **Forgetting to preserve relative order:** A simple swap of first-zero-with-last-nonzero breaks order. The partition pointer approach maintains stability.
- **Self-swap overhead:** When `insert_pos == i`, the swap is redundant but harmless. Some interviewers may ask you to add a guard `if i != insert_pos`.
