# Grumpy Bookstore Owner

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Fixed Window
**Link:** https://leetcode.com/problems/grumpy-bookstore-owner/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

A bookstore owner has `customers[i]` customers at minute `i`. They are grumpy (`grumpy[i] = 1`) or not (`grumpy[i] = 0`) at each minute. When grumpy, customers are unsatisfied. The owner can use a **secret technique** for `minutes` consecutive minutes to suppress grumpiness. Find the **maximum number of satisfied customers**.

### 2. Clarification Questions

- **Input constraints?** `1 <= minutes <= customers.length <= 2 * 10^4`. `grumpy[i]` is 0 or 1.
- **Edge cases?** Owner is never grumpy (technique doesn't help). Owner is always grumpy. `minutes` equals array length.
- **Expected output?** An integer — maximum satisfied customers.
- **Can input be modified?** Yes, but cleaner not to.

### 3. Brute Force Approach

- **Idea:** Try every possible window of size `minutes` for the technique. For each, compute total satisfied customers.
- **Time:** O(n * minutes)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** Separate the problem into two parts:
  1. **Baseline:** Sum of `customers[i]` where `grumpy[i] == 0` (always satisfied, regardless of technique).
  2. **Bonus:** The technique "saves" `customers[i]` where `grumpy[i] == 1` within the window. Slide a window of size `minutes` to **maximize the bonus** (extra customers saved).

  **Answer = baseline + max_bonus.**

- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n * minutes) | O(1) | Recomputes each window |
| Optimized | O(n) | O(1) | Separate baseline from bonus |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Compute `baseline` — customers already satisfied (non-grumpy minutes).
- Compute `bonus` for the first window — sum of `customers[i]` where `grumpy[i] == 1`.
- Slide the window: adjust bonus based on entering/leaving grumpy minutes.
- Answer is `baseline + max_bonus`.

```python
def maxSatisfied(customers, grumpy, minutes):
    n = len(customers)

    # Baseline: customers satisfied without technique
    baseline = sum(c for c, g in zip(customers, grumpy) if g == 0)

    # Bonus: extra customers saved by technique in first window
    bonus = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
    max_bonus = bonus

    # Slide the window to find the best position for the technique
    for i in range(minutes, n):
        # Add entering grumpy customers
        if grumpy[i] == 1:
            bonus += customers[i]
        # Remove leaving grumpy customers
        if grumpy[i - minutes] == 1:
            bonus -= customers[i - minutes]

        max_bonus = max(max_bonus, bonus)

    return baseline + max_bonus
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3`

**Baseline** (non-grumpy): customers[0]=1 + customers[2]=1 + customers[4]=1 + customers[6]=7 = **10**

| Window | Grumpy customers saved | Bonus | Max Bonus |
|--------|------------------------|-------|-----------|
| [0,1,2] | customers[1]=0 | 0 | 0 |
| [1,2,3] | customers[1]=0 + customers[3]=2 | 2 | 2 |
| [2,3,4] | customers[3]=2 | 2 | 2 |
| [3,4,5] | customers[3]=2 + customers[5]=1 | 3 | 3 |
| [4,5,6] | customers[5]=1 | 1 | 3 |
| [5,6,7] | customers[5]=1 + customers[7]=5 | 6 | 6 |

**Output:** `10 + 6 = 16`

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `minutes = 1` — technique covers one minute.
- **Typical case:** Covered in dry run.
- **Extreme values:** All grumpy — baseline is 0, bonus is max window sum. Never grumpy — baseline is total, bonus is 0.

### Complexity

- **Time:** O(n) — one pass for baseline, one pass for sliding window.
- **Space:** O(1) — constant extra variables.

### Optimization Discussion

The key insight that separates this from a harder problem is the **decomposition**: non-grumpy customers are always counted, and the technique only affects grumpy minutes. This transforms it into a simple "max sum of a subarray of size k" over the grumpy-filtered values.

### Follow-up Variations

- What if the technique can be used **twice** (non-overlapping windows)?
- What if the technique **reduces** grumpiness by 50% instead of eliminating it?
- What if the window size is **variable** (use at most `minutes` total, not necessarily consecutive)?

### Common Traps

- **Counting non-grumpy customers in the bonus.** The technique doesn't affect already-satisfied customers. Only grumpy minutes contribute to the bonus.
- **Modifying the input arrays.** Some solutions flip `grumpy[i]` to 0 — this works but is less clean.
- **Double-counting.** If you add all customers in the window and subtract baseline, you might accidentally double-count. The decomposition approach avoids this cleanly.
