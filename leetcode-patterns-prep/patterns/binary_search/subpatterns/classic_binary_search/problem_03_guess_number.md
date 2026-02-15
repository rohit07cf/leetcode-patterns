# Guess Number Higher or Lower

**Difficulty:** Easy
**Pattern:** Binary Search
**Subpattern:** Classic Binary Search
**Link:** https://leetcode.com/problems/guess-number-higher-or-lower/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

A number is picked from 1 to n. You have an API `guess(num)` that returns `-1` (pick is lower), `1` (pick is higher), or `0` (correct). Find the picked number with minimum calls.

### 2. Clarification Questions

- **Input constraints?** 1 <= n <= 2^31 - 1. The picked number is in [1, n].
- **Edge cases?** n = 1 (only one choice), picked number at boundaries (1 or n).
- **Expected output?** The picked number (integer).
- **Can input be modified?** No input array — just a number range.

### 3. Brute Force Approach

- **Idea:** Try every number from 1 to n, calling `guess()` each time.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- 💡 **Core Insight:** The number range [1, n] is inherently **sorted**. Binary search on the range, using the `guess()` API as the comparator instead of array access.
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Linear scan through all numbers |
| Optimized | O(log n) | O(1) | Binary search on [1, n] |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Binary search over the range [1, n] instead of an array.
- Use the `guess()` API return value to decide direction.
- Return when `guess()` returns 0.

```python
# The guess API is already defined for you.
# def guess(num: int) -> int:
#   returns -1 if pick < num, 1 if pick > num, 0 if pick == num

def guessNumber(n: int) -> int:
    left, right = 1, n

    while left <= right:
        mid = left + (right - left) // 2  # WHY: avoid overflow in other languages
        result = guess(mid)

        if result == 0:
            return mid  # WHY: found the picked number
        elif result == -1:
            right = mid - 1  # WHY: pick is lower than mid
        else:
            left = mid + 1  # WHY: pick is higher than mid

    return -1  # WHY: should never reach here given valid input
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `n = 10`, pick = `6`

| Step | left | right | mid | guess(mid) | Action |
|------|------|-------|-----|------------|--------|
| 1 | 1 | 10 | 5 | 1 | pick > 5 → left = 6 |
| 2 | 6 | 10 | 8 | -1 | pick < 8 → right = 7 |
| 3 | 6 | 7 | 6 | 0 | Found! Return 6 |

### Edge Case Testing

- **Empty input:** Not applicable — n >= 1.
- **Single element:** n = 1 → mid = 1, guess returns 0, return 1.
- **Typical case:** Pick in middle of range → ~log(n) steps.
- **Extreme values:** n = 2^31 - 1 → overflow-safe mid calculation is critical (in Java/C++).

### Complexity

- **Time:** O(log n) — halving the range each iteration.
- **Space:** O(1) — only a few variables.

### Optimization Discussion

Already optimal. This is a direct application of binary search on a conceptual sorted range rather than an explicit array.

### Follow-up Variations

- **Guess Number Higher or Lower II (LC 375):** Minimize the cost of guessing (dynamic programming).
- What if the API has a cost per call and you want to minimize total cost?

### Common Traps

- **Misreading the API:** The return values can be confusing. `-1` means the pick is **lower** than your guess (not that you should go lower). Read the problem statement carefully.
- **Integer overflow:** `(left + right) / 2` overflows for large n in Java/C++. Use `left + (right - left) / 2`.
- **Off-by-one on range:** Range starts at **1**, not 0.
