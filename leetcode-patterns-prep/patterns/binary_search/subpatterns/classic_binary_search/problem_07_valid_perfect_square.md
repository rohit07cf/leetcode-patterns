# Valid Perfect Square

**Difficulty:** Easy
**Pattern:** Binary Search
**Subpattern:** Classic Binary Search
**Link:** https://leetcode.com/problems/valid-perfect-square/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a positive integer `num`, return `true` if it is a perfect square (i.e., there exists an integer `k` such that `k * k == num`), without using any built-in sqrt function.

### 2. Clarification Questions

- **Input constraints?** 1 <= num <= 2^31 - 1.
- **Edge cases?** num = 1 (perfect square), large numbers, num = 2 (not perfect square).
- **Expected output?** Boolean.
- **Can input be modified?** Single integer input.

### 3. Brute Force Approach

- **Idea:** Check k = 1, 2, 3, ... until `k * k >= num`.
- **Time:** O(sqrt(num))
- **Space:** O(1)

### 4. Optimized Approach

- 💡 **Core Insight:** Binary search on the range [1, num]. For each `mid`, compare `mid * mid` with `num`. If equal, it is a perfect square. If `mid * mid < num`, search right. If `mid * mid > num`, search left. This is an **exact-match binary search** on the answer space.
- **Time:** O(log num)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(sqrt(num)) | O(1) | Linear increment |
| Binary Search | O(log num) | O(1) | Search on answer space |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Binary search on [1, num].
- Compare `mid * mid` to `num`.
- Return true on exact match, false when search space exhausted.

```python
def isPerfectSquare(num: int) -> bool:
    left, right = 1, num

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid  # WHY: compute once to avoid redundant calculation

        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1

    return False  # WHY: no integer k found where k*k == num
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `num = 16`

| Step | left | right | mid | mid*mid | Action |
|------|------|-------|-----|---------|--------|
| 1 | 1 | 16 | 8 | 64 | 64 > 16 → right = 7 |
| 2 | 1 | 7 | 4 | 16 | 16 == 16 → Return True |

**Input:** `num = 14`

| Step | left | right | mid | mid*mid | Action |
|------|------|-------|-----|---------|--------|
| 1 | 1 | 14 | 7 | 49 | 49 > 14 → right = 6 |
| 2 | 1 | 6 | 3 | 9 | 9 < 14 → left = 4 |
| 3 | 4 | 6 | 5 | 25 | 25 > 14 → right = 4 |
| 4 | 4 | 4 | 4 | 16 | 16 > 14 → right = 3 |
| 5 | left > right | — | — | — | Return False |

### Edge Case Testing

- **Empty input:** Not applicable — num >= 1.
- **Single element:** num = 1 → mid = 1, 1*1 = 1 → True.
- **Typical case:** num = 16 → True. num = 14 → False.
- **Extreme values:** num = 2^31 - 1 → Python handles big int multiplication. In Java/C++, use `long` for `mid * mid`.

### Complexity

- **Time:** O(log num) — binary search over [1, num].
- **Space:** O(1) — constant extra space.

### Optimization Discussion

- **Math trick:** A perfect square is a sum of consecutive odd numbers: 1, 1+3, 1+3+5, ... Subtract 1, 3, 5, 7, ... from num. If you reach 0, it's a perfect square. O(sqrt(n)) time.
- **Newton's method:** Iteratively refine guess. O(log n) with faster convergence.

### Follow-up Variations

- **Sqrt(x) (LC 69):** Return the floor of the square root instead of boolean.
- Sum of two perfect squares? (LC 633)

### Common Traps

- **Integer overflow:** `mid * mid` overflows in typed languages. Use `long` in Java or compare `mid` to `num / mid` instead.
- **Starting left at 0:** If num = 0 were valid and left starts at 0, `mid = 0` causes issues with division-based overflow checks. Since num >= 1, start at 1.
- **Confusing with Sqrt(x):** This needs an **exact** match, not a floor. Different return type and logic.
