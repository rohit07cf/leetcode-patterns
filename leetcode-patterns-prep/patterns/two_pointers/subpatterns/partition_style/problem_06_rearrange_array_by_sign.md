# Rearrange Array Elements by Sign

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Partition Style
**Link:** https://leetcode.com/problems/rearrange-array-elements-by-sign/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array with **equal** numbers of positive and negative integers, rearrange so that every **consecutive pair** has alternating signs. Start with a positive number. Preserve the **relative order** within positives and within negatives.

### 2. Clarification Questions

- **Input constraints?** Length 2–2×10⁵ (always even). Exactly half positive, half negative. No zeroes.
- **Edge cases?** Length 2 (one positive, one negative); all positives grouped together.
- **Expected output?** Return a new array with alternating signs starting positive.
- **Can input be modified?** Yes, but a new array is typically returned.

### 3. Brute Force Approach

- **Idea:** Separate into positive and negative lists, then interleave them.
- **Time:** O(n)
- **Space:** O(n)

### 4. Optimized Approach

- 💡 **Core Insight:** Use **two write pointers** — `pos_idx = 0` for positive positions (0, 2, 4, ...) and `neg_idx = 1` for negative positions (1, 3, 5, ...). Scan the original array and place each element at the appropriate write pointer, then advance that pointer by 2. This fills the result array in a single pass.
- **Time:** O(n)
- **Space:** O(n) — result array required (can't maintain order in-place easily).

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Separate + interleave | O(n) | O(n) | Two passes, clear logic |
| Two write pointers | O(n) | O(n) | Single pass over input |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Create a result array of size n.
- `pos_idx` starts at 0, `neg_idx` starts at 1 — these track the next available even/odd index.
- Scan each element: if positive, place at `pos_idx` and advance by 2. If negative, place at `neg_idx` and advance by 2.

```python
def rearrangeArray(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    pos_idx = 0  # Next even index for positives
    neg_idx = 1  # Next odd index for negatives

    for num in nums:
        if num > 0:
            result[pos_idx] = num
            pos_idx += 2
        else:
            result[neg_idx] = num
            neg_idx += 2

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `[3, 1, -2, -5, 2, -4]`

| num | Action | pos_idx | neg_idx | result |
|-----|--------|---------|---------|--------|
| 3 | positive → idx 0 | 2 | 1 | [3,0,0,0,0,0] |
| 1 | positive → idx 2 | 4 | 1 | [3,0,1,0,0,0] |
| -2 | negative → idx 1 | 4 | 3 | [3,-2,1,0,0,0] |
| -5 | negative → idx 3 | 4 | 5 | [3,-2,1,-5,0,0] |
| 2 | positive → idx 4 | 6 | 5 | [3,-2,1,-5,2,0] |
| -4 | negative → idx 5 | 6 | 7 | [3,-2,1,-5,2,-4] |

Result: `[3, -2, 1, -5, 2, -4]`

### Edge Case Testing

- **Empty input:** Not possible (length ≥ 2).
- **Single element:** Not possible (always even length ≥ 2 with equal pos/neg).
- **Typical case:** `[3,1,-2,-5,2,-4]` → `[3,-2,1,-5,2,-4]`.
- **Extreme values:** Already alternating `[1,-1,2,-2]` → `[1,-1,2,-2]` (no change).

### Complexity

- **Time:** O(n) — single pass through the array.
- **Space:** O(n) — result array. In-place with order preservation is not straightforward.

### Optimization Discussion

O(n) space seems unavoidable if relative order must be preserved. An in-place solution would require complex rotations (O(n²) time) to maintain order. The two-pointer fill is the standard interview answer.

### Follow-up Variations

- **Unequal positives/negatives** — place extras at the end.
- **In-place with O(1) space** — sacrifice order preservation or accept O(n²).
- **Wiggle Sort (LC 280)** — alternating greater/lesser instead of sign.

### ⚠️ Common Traps

- **Trying to solve in-place while preserving order:** This is extremely difficult without O(n) space or O(n²) time. Accept O(n) space.
- **Zeroes in input:** The problem guarantees no zeroes, but if asked as a follow-up, clarify whether zero is positive or negative.
