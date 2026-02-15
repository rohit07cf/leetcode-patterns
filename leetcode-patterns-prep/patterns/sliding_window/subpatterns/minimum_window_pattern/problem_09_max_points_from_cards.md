# Maximum Points You Can Obtain from Cards

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Minimum Window Pattern
**Link:** https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an array `cardPoints` and integer `k`, you must take exactly `k` cards from either the beginning or end of the row. Return the maximum total points you can obtain.

### 2. Clarification Questions
- Input constraints? `1 <= cardPoints.length <= 10^5`, `1 <= cardPoints[i] <= 10^4`, `1 <= k <= cardPoints.length`.
- Edge cases? `k == n` (take all cards), `k == 1` (take max of first or last), all equal values.
- Expected output? An integer — maximum sum of k cards taken from edges.
- Can input be modified? Yes.

### 3. Brute Force Approach
- **Idea:** Try all combinations: take `i` from the left and `k - i` from the right for `i = 0..k`.
- **Time:** O(k) — actually this is already efficient with prefix sums!
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** Taking `k` cards from the edges is the same as **leaving a contiguous window of `n - k` cards in the middle**. To maximize edge sum, **minimize the sum of the middle window**. Use a fixed-size sliding window of length `n - k` to find the minimum subarray sum.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Prefix sums | O(k) | O(k) | Compute left/right prefix sums |
| Min window | O(n) | O(1) | Minimize middle, maximize edges |

Both are excellent. The sliding window approach generalizes better and uses constant space.

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Compute `total_sum` of all cards.
- Find the **minimum sum** of any contiguous subarray of length `n - k`.
- Answer: `total_sum - min_window_sum`.
- Special case: if `k == n`, return `total_sum`.

```python
def maxScore(cardPoints: list[int], k: int) -> int:
    n = len(cardPoints)
    window_size = n - k

    # if taking all cards, return total
    if window_size == 0:
        return sum(cardPoints)

    # compute sum of the first window
    window_sum = sum(cardPoints[:window_size])
    min_window_sum = window_sum

    # slide the window across the array
    for i in range(window_size, n):
        window_sum += cardPoints[i]             # add new right element
        window_sum -= cardPoints[i - window_size]  # remove old left element
        min_window_sum = min(min_window_sum, window_sum)

    return sum(cardPoints) - min_window_sum
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `cardPoints = [1,2,3,4,5,6,1]`, `k = 3`

`n = 7`, `window_size = 4`, `total = 22`

Initial window (indices 0-3): sum = 1+2+3+4 = 10

| i | add | remove | window_sum | min |
|---|-----|--------|------------|-----|
| 4 | 5 | 1 | 14 | 10 |
| 5 | 6 | 2 | 18 | 10 |
| 6 | 1 | 3 | 16 | 10 |

`min_window_sum = 10` (the window `[1,2,3,4]`)

**Answer:** `22 - 10 = 12`

This corresponds to taking cards `[6,5,1]`... wait: taking 1 from right + 2 from left? Actually: we leave `[1,2,3,4]` in the middle and take `[5,6,1]` from the edges? No — the middle window `[1,2,3,4]` is indices 0-3, so we take indices 4,5,6 = `[5,6,1]` = 12. That's taking 3 from the right.

**Output:** `12`

### Edge Case Testing
- **Empty input:** Not possible per constraints.
- **Single element:** `cardPoints = [5]`, `k = 1` → window_size=0, return 5.
- **Typical case:** Shown in dry run.
- **Extreme values:** `k == n` → take all cards, return total sum.

### Complexity
- **Time:** O(n) — one pass to compute initial window, one pass to slide.
- **Space:** O(1) — only tracking sums and pointers.

### Optimization Discussion
- **Prefix sum approach:** Compute prefix sums from left (`left[i]` = sum of first `i` cards) and right (`right[i]` = sum of last `i` cards). For each split `i` from left and `k-i` from right, check `left[i] + right[k-i]`. This is O(k) time, O(k) space.
- The minimum window approach is conceptually elegant — it converts a two-sided problem into a standard window problem.

### Follow-up Variations
- What if you can take cards from the middle too? (Different problem entirely.)
- Minimum points from k cards (maximize the middle window instead).
- What if some cards have negative values? (Still works — window sum can go negative.)

### Common Traps
- **Trying to simulate left/right choices** with recursion — leads to O(2^k) without memoization.
- **Forgetting `k == n` edge case** — window_size becomes 0, and the initial window sum computation would be empty.
- **Off-by-one in window sliding** — ensure exactly `n - k` elements in the window at all times.
