# Arranging Coins

**Difficulty:** Easy
**Pattern:** Binary Search
**Subpattern:** Boundary Binary Search
**Link:** https://leetcode.com/problems/arranging-coins/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given `n` coins, arrange them in a staircase shape where the k-th row has exactly `k` coins. Return the number of **complete rows** of the staircase. The last row may be incomplete.

### 2. Clarification Questions

- **Input constraints?** `1 <= n <= 2^31 - 1` (very large).
- **Edge cases?** `n = 1` (one complete row). `n = 0` is not in constraints. Perfect staircase where all rows are complete.
- **Expected output?** An integer — the number of complete rows.
- **Can input be modified?** N/A (single integer input).

### 3. Brute Force Approach

- **Idea:** Subtract 1, 2, 3, ... from n until we can't complete a row.
- **Time:** O(sqrt(n)) — the number of rows is proportional to sqrt(n).
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** k complete rows require `k * (k + 1) / 2` coins. Binary search for the **largest k** such that `k * (k + 1) / 2 <= n`. This is a boundary search on a monotonically increasing function.
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(sqrt(n)) | O(1) | Row-by-row subtraction |
| Optimized | O(log n) | O(1) | Binary search on row count |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Binary search over the number of complete rows `k` in range `[1, n]`.
- Compute `total = k * (k + 1) // 2` — the coins needed for k complete rows.
- If `total <= n`, record `k` as candidate and search right for larger k.
- If `total > n`, search left.

```python
def arrangeCoins(n):
    lo, hi = 1, n
    result = 0

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        total = mid * (mid + 1) // 2  # coins needed for mid complete rows

        if total <= n:
            result = mid  # mid rows can be completed, try more
            lo = mid + 1
        else:
            hi = mid - 1  # too many coins needed, try fewer rows

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `n = 8`

- `lo=1, hi=8` -> `mid=4`, `total=10 > 8` -> `hi=3`
- `lo=1, hi=3` -> `mid=2`, `total=3 <= 8` -> `result=2`, `lo=3`
- `lo=3, hi=3` -> `mid=3`, `total=6 <= 8` -> `result=3`, `lo=4`
- `lo=4, hi=3` -> exit. **Return 3**

**Verification:** Rows: 1 + 2 + 3 = 6 coins used, 2 remaining (incomplete 4th row).

### Edge Case Testing

- **Empty input:** Not possible (n >= 1).
- **Single element:** `n=1` -> `mid=1`, `total=1 <= 1`, `result=1`. Returns **1**.
- **Perfect staircase:** `n=6` -> finds `k=3` since `3*4/2 = 6`. Returns **3**.
- **Extreme values:** `n=2^31-1` -> binary search handles large values; integer arithmetic stays within 64-bit bounds.

### Complexity

- **Time:** O(log n) — binary search over range [1, n].
- **Space:** O(1) — constant extra space.

### Optimization Discussion

A **math-based O(1)** solution exists using the quadratic formula: `k = floor((-1 + sqrt(1 + 8n)) / 2)`. However, floating-point precision issues can arise with very large `n`. The binary search approach is safer and still very efficient.

### Follow-up Variations

- What if coins in each row can be **at most k** (not exactly k)?
- Reverse problem: given k rows, how many coins are needed?
- What if some rows require extra coins (e.g., row i needs `2i` coins)?

### Common Traps

- **Integer overflow** — `mid * (mid + 1)` can overflow 32-bit integers for large `n`. Python handles big integers natively, but in C++/Java, use `long`.
- **Setting `hi = n` instead of a tighter bound** — `hi = n` works but `hi = min(n, 2 * sqrt(n))` is tighter. In practice, `hi = n` is fine since log(n) iterations is fast.
- **Off-by-one with `<=` vs `<`** — the condition is `total <= n` (we want complete rows, so exactly `n` coins is valid).
