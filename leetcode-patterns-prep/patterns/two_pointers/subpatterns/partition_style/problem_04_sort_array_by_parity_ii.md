# Sort Array By Parity II

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Partition Style
**Link:** https://leetcode.com/problems/sort-array-by-parity-ii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array where half the elements are even and half are odd, rearrange it so that `nums[i]` is even when `i` is even, and `nums[i]` is odd when `i` is odd.

### 2. Clarification Questions

- **Input constraints?** Array length 2–2×10⁴ (always even). Exactly half even, half odd.
- **Edge cases?** Length 2; already sorted; completely interleaved wrong.
- **Expected output?** Return any valid arrangement satisfying the parity constraint.
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Separate into even and odd lists, then interleave them into a new array.
- **Time:** O(n)
- **Space:** O(n)

### 4. Optimized Approach

- 💡 **Core Insight:** Use **two independent pointers** — one scanning even indices (`i = 0, 2, 4, ...`) and one scanning odd indices (`j = 1, 3, 5, ...`). When `i` finds an odd number at an even index, and `j` finds an even number at an odd index, **swap them**. Both violations are fixed simultaneously.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Separate + interleave | O(n) | O(n) | Extra space for two lists |
| Two-pointer (even/odd index) | O(n) | O(1) | In-place, single pass |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Pointer `i` walks even indices looking for misplaced odd numbers.
- Pointer `j` walks odd indices looking for misplaced even numbers.
- When both find violations, swap — this fixes both positions at once.

```python
def sortArrayByParityII(nums: list[int]) -> list[int]:
    n = len(nums)
    i, j = 0, 1  # i scans even indices, j scans odd indices

    while i < n and j < n:
        # Find misplaced odd at an even index
        while i < n and nums[i] % 2 == 0:
            i += 2
        # Find misplaced even at an odd index
        while j < n and nums[j] % 2 == 1:
            j += 2
        # If both found violations, swap to fix both
        if i < n and j < n:
            nums[i], nums[j] = nums[j], nums[i]
            i += 2
            j += 2

    return nums
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `[4, 2, 5, 7]`

| Step | i | j | Action | Array |
|------|---|---|--------|-------|
| 1 | 0 | 1 | nums[0]=4 (even at even, ok) → i=2 | [4,2,5,7] |
| 2 | 2 | 1 | nums[2]=5 (odd at even, bad!) stop i | [4,2,5,7] |
| 3 | 2 | 1 | nums[1]=2 (even at odd, bad!) stop j | [4,2,5,7] |
| 4 | 2 | 1 | swap(2,1) → i=4, j=3 | [4,5,2,7] |

i ≥ n → stop. Result: `[4, 5, 2, 7]` — parity constraint satisfied.

### Edge Case Testing

- **Empty input:** Not possible (length ≥ 2).
- **Single element:** Not possible (length always even and ≥ 2).
- **Typical case:** `[4,2,5,7]` → `[4,5,2,7]`.
- **Extreme values:** Already valid `[2,1,4,3]` → no swaps needed.

### Complexity

- **Time:** O(n) — each pointer traverses at most n/2 elements.
- **Space:** O(1) — two index variables.

### Optimization Discussion

This is already optimal. The key insight is that every misplaced element at an even index is paired with a misplaced element at an odd index (since counts are balanced), so a single swap fixes two violations.

### Follow-up Variations

- **Sort Array By Parity (LC 905)** — simpler; just evens before odds.
- **Rearrange with specific ordering within groups** — maintain relative order while satisfying parity.
- **Generalize to k groups** — place elements by `val % k` at index `i % k`.

### ⚠️ Common Traps

- **Incrementing by 1 instead of 2:** Each pointer only visits indices of one parity. Always step by 2.
- **Forgetting bounds check after inner loops:** Both `i < n` and `j < n` must be checked before swapping.
