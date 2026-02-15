# Wiggle Sort

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Partition Style
**Link:** https://leetcode.com/problems/wiggle-sort/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Rearrange an array such that `nums[0] <= nums[1] >= nums[2] <= nums[3] >= nums[4] ...`. In other words, elements at **odd indices** are local peaks and elements at **even indices** are local valleys.

### 2. Clarification Questions

- **Input constraints?** Array length 0–5×10⁴, values 0–10⁴.
- **Edge cases?** Empty array; single element; two elements; already wiggle-sorted.
- **Expected output?** Modify array in-place; no return value.
- **Can input be modified?** Yes — in-place required.

### 3. Brute Force Approach

- **Idea:** Sort the array, then swap adjacent pairs starting from index 1: swap(1,2), swap(3,4), etc.
- **Time:** O(n log n)
- **Space:** O(1) or O(n) depending on sort.

### 4. Optimized Approach

- 💡 **Core Insight:** Scan left to right. At each index, check if the wiggle property is violated with its neighbor. If at an **even index** and `nums[i] > nums[i+1]`, swap. If at an **odd index** and `nums[i] < nums[i+1]`, swap. A **local greedy fix** works because fixing one pair never breaks the previous pair.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort + swap pairs | O(n log n) | O(1) | Simple but sorting overhead |
| Greedy single pass | O(n) | O(1) | Optimal, elegant |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- At even indices: element should be ≤ next → if it's greater, swap.
- At odd indices: element should be ≥ next → if it's smaller, swap.
- This is a partition-style rearrangement: each element gets placed in its correct "role" (peak or valley).

```python
def wiggleSort(nums: list[int]) -> None:
    for i in range(len(nums) - 1):
        if i % 2 == 0:
            # Even index: should be a valley (nums[i] <= nums[i+1])
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        else:
            # Odd index: should be a peak (nums[i] >= nums[i+1])
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
```

**Even more concise:**

```python
def wiggleSort(nums: list[int]) -> None:
    for i in range(len(nums) - 1):
        # Swap if the wiggle property is violated
        if (i % 2 == 0 and nums[i] > nums[i + 1]) or \
           (i % 2 == 1 and nums[i] < nums[i + 1]):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `[3, 5, 2, 1, 6, 4]`

| i | Condition | Action | Array |
|---|-----------|--------|-------|
| 0 (even) | 3 > 5? No | skip | [3,5,2,1,6,4] |
| 1 (odd) | 5 < 2? No | skip | [3,5,2,1,6,4] |
| 2 (even) | 2 > 1? Yes | swap | [3,5,1,2,6,4] |
| 3 (odd) | 2 < 6? Yes | swap | [3,5,1,6,2,4] |
| 4 (even) | 2 > 4? No | skip | [3,5,1,6,2,4] |

Result: `[3, 5, 1, 6, 2, 4]` — satisfies `3≤5≥1≤6≥2≤4`.

### Why Greedy Works

When we fix position `i`, can it break position `i-1`?

- If `i` is even and we swap `nums[i]` with `nums[i+1]` (making `nums[i]` smaller), position `i-1` (odd) needed `nums[i-1] >= nums[i]`. Making `nums[i]` smaller only helps.
- Symmetric argument for odd indices.

### Edge Case Testing

- **Empty input:** Loop doesn't execute; array stays empty.
- **Single element:** `[5]` → no pairs to check.
- **Typical case:** `[3,5,2,1,6,4]` → `[3,5,1,6,2,4]`.
- **Extreme values:** Already wiggle-sorted → no swaps; sorted ascending → alternating swaps.

### Complexity

- **Time:** O(n) — single pass with at most n-1 comparisons.
- **Space:** O(1) — only loop variable.

### Optimization Discussion

This is already optimal. The greedy approach is simpler and faster than sorting. Note this produces **one valid** wiggle arrangement — there may be multiple.

### Follow-up Variations

- **Wiggle Sort II (LC 324)** — strict inequality `nums[0] < nums[1] > nums[2]`. Much harder; requires median-finding.
- **Check if array is wiggle-sorted** — just verify the alternating condition.
- **Wiggle Subsequence (LC 376)** — find longest wiggle subsequence.

### ⚠️ Common Traps

- **Confusing Wiggle Sort I (≤, ≥) with Wiggle Sort II (<, >):** The greedy single-pass approach does **not** work for strict inequality.
- **Thinking greedy breaks earlier fixes:** It doesn't — swapping to satisfy the current pair can only help (not hurt) the previous pair.
