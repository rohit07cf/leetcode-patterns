# Sqrt(x)

**Difficulty:** Easy
**Pattern:** Binary Search
**Subpattern:** Classic Binary Search
**Link:** https://leetcode.com/problems/sqrtx/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a non-negative integer `x`, return the **integer part** of the square root of `x` (i.e., the largest integer `k` such that `k * k <= x`).

### 2. Clarification Questions

- **Input constraints?** 0 <= x <= 2^31 - 1.
- **Edge cases?** x = 0, x = 1, perfect squares, very large x.
- **Expected output?** Non-negative integer (floor of sqrt).
- **Can input be modified?** Single integer input — no modification needed.

### 3. Brute Force Approach

- **Idea:** Try k = 0, 1, 2, ... until `k * k > x`. Return `k - 1`.
- **Time:** O(sqrt(x))
- **Space:** O(1)

### 4. Optimized Approach

- 💡 **Core Insight:** We're searching for the **largest** `k` where `k * k <= x`. The values `k * k` are monotonically increasing, so this is a binary search on the answer space [0, x]. Find the **right boundary** — the last `k` satisfying the condition.
- **Time:** O(log x)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(sqrt(x)) | O(1) | Linear increment |
| Binary Search | O(log x) | O(1) | Search on answer space |
| Newton's Method | O(log x) | O(1) | Faster constant factor but trickier |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Binary search on range [0, x].
- If `mid * mid <= x`, `mid` is a candidate — save it and search right for a larger one.
- If `mid * mid > x`, search left.

```python
def mySqrt(x: int) -> int:
    if x < 2:
        return x  # WHY: sqrt(0) = 0, sqrt(1) = 1

    left, right = 0, x
    result = 0

    while left <= right:
        mid = left + (right - left) // 2

        if mid * mid <= x:
            result = mid  # WHY: mid is a valid candidate, but there may be a larger one
            left = mid + 1
        else:
            right = mid - 1  # WHY: mid is too large

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `x = 8`

| Step | left | right | mid | mid*mid | Action |
|------|------|-------|-----|---------|--------|
| 1 | 0 | 8 | 4 | 16 | 16 > 8 → right = 3 |
| 2 | 0 | 3 | 1 | 1 | 1 <= 8 → result = 1, left = 2 |
| 3 | 2 | 3 | 2 | 4 | 4 <= 8 → result = 2, left = 3 |
| 4 | 3 | 3 | 3 | 9 | 9 > 8 → right = 2 |
| 5 | left > right | — | — | — | Return result = 2 |

**Answer:** 2 (since 2^2 = 4 <= 8 < 9 = 3^2)

### Edge Case Testing

- **Empty input:** Not applicable.
- **Single element:** x = 0 → returns 0. x = 1 → returns 1.
- **Typical case:** x = 8 → returns 2.
- **Extreme values:** x = 2^31 - 1 → mid * mid could overflow in typed languages. Python handles big integers natively.

### Complexity

- **Time:** O(log x) — binary search over [0, x].
- **Space:** O(1) — constant extra space.

### Optimization Discussion

- **Tighter bounds:** We could use `right = x // 2` for x >= 4, since sqrt(x) <= x/2. Minor improvement.
- **Newton's method:** `k = (k + x/k) / 2` converges quadratically. Faster in practice, but binary search is more intuitive in interviews.

### Follow-up Variations

- **Valid Perfect Square (LC 367):** Return boolean instead of floor value.
- What if you need the result to a given decimal precision?

### Common Traps

- **Integer overflow:** In Java/C++, `mid * mid` can overflow. Use `mid <= x / mid` instead (but watch for division by zero when mid = 0).
- **Forgetting x = 0 and x = 1:** These are base cases where the answer is `x` itself.
- **Not tracking `result`:** Without storing the last valid `mid`, you lose the answer when the loop exits.
