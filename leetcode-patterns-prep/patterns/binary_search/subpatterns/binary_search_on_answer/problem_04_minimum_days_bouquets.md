# Minimum Number of Days to Make m Bouquets

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Binary Search on Answer
**Link:** https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given `bloomDay[i]` (the day flower `i` blooms), find the **minimum number of days** to make `m` bouquets, where each bouquet requires `k` **adjacent** bloomed flowers. Return `-1` if impossible.

### 2. Clarification Questions

- **Input constraints?** `1 <= bloomDay.length <= 10^5`, `1 <= bloomDay[i] <= 10^9`, `1 <= m, k <= 10^6`
- **Edge cases?** If `m * k > n`, impossible — return `-1`. If all flowers bloom on day 1, answer is 1.
- **Expected output?** A single integer (minimum days) or `-1`.
- **Can input be modified?** Yes, but no need.

### 3. Brute Force Approach

- **Idea:** Try every possible day from 1 to `max(bloomDay)`. For each day, count how many bouquets can be made from adjacent bloomed flowers.
- **Time:** O(max(bloomDay) * n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** If we can make `m` bouquets by day `d`, we can also make them by day `d+1` (more flowers bloomed). The answer is **monotonic** over days — binary search on the day.

- **Feasibility check:** On a given day, scan left-to-right counting consecutive bloomed flowers. Every time we reach `k` consecutive, that's one bouquet. Check if total bouquets >= `m`.

- **Time:** O(n * log(max(bloomDay)))
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(max(bloomDay) * n) | O(1) | TLE with bloomDay up to 10^9 |
| Optimized | O(n * log(max(bloomDay))) | O(1) | ~30 iterations of binary search |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Early return `-1` if `m * k > n` (not enough flowers)
- Binary search on day in `[1, max(bloomDay)]`
- Feasibility: count consecutive bloomed flowers, tally bouquets

```python
from typing import List

def minDays(bloomDay: List[int], m: int, k: int) -> int:
    n = len(bloomDay)
    # Impossible if we need more flowers than exist
    if m * k > n:
        return -1

    lo, hi = 1, max(bloomDay)

    while lo < hi:
        mid = (lo + hi) // 2
        # Feasibility: can we make m bouquets by day mid?
        bouquets = 0
        consecutive = 0

        for bloom in bloomDay:
            if bloom <= mid:
                consecutive += 1
                if consecutive == k:    # enough for one bouquet
                    bouquets += 1
                    consecutive = 0     # reset for next bouquet
            else:
                consecutive = 0         # chain broken

        if bouquets >= m:
            hi = mid        # feasible — try fewer days
        else:
            lo = mid + 1    # not enough bouquets — need more days

    return lo
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `bloomDay = [1,10,3,10,2], m = 3, k = 1`

`m * k = 3 <= 5 = n`, so possible. `lo = 1, hi = 10`

| Day (mid) | Bloomed? | Bouquets | Feasible? |
|-----------|----------|----------|-----------|
| mid=5 | [Y,N,Y,N,Y] | 3 | Yes -> hi=5 |
| mid=3 | [Y,N,Y,N,Y] | 3 | Yes -> hi=3 |
| mid=2 | [Y,N,N,N,Y] | 2 | No -> lo=3 |
| lo=3, hi=3 -> return 3 |

**Output:** `3` (correct)

### Edge Case Testing

- **Empty input:** Constraints guarantee n >= 1.
- **Single element:** `bloomDay = [5], m = 1, k = 1` -> returns 5.
- **Typical case:** Shown above.
- **Extreme values:** `m * k > n` -> returns -1 immediately. All same bloom day -> that day is the answer.

### Complexity

- **Time:** O(n * log(max(bloomDay))) — binary search over days, each feasibility check is O(n).
- **Space:** O(1) — only counters.

### Optimization Discussion

The early `-1` check `m * k > n` is crucial — it avoids binary search on impossible inputs and prevents integer overflow in languages where `m * k` might overflow (use `m > n / k` as a safe alternative).

### Follow-up Variations

- What if bouquets don't need adjacent flowers? (Sort bloom days, pick every k-th.)
- What if each bouquet can use flowers from different groups with a distance constraint?

### Common Traps

- **Forgetting the impossibility check.** If `m * k > n`, no amount of waiting helps.
- **Not resetting `consecutive` to 0 after forming a bouquet.** The same flowers cannot be reused.
- **Adjacency requirement.** Flowers must be consecutive in the array — cannot skip unbloomed flowers.
- **Integer overflow.** `m * k` can overflow 32-bit integers. Use `long` or check `m > n // k` instead.
