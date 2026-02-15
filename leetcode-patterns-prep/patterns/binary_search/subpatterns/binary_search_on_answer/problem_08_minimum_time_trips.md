# Minimum Time to Complete Trips

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Binary Search on Answer
**Link:** https://leetcode.com/problems/minimum-time-to-complete-trips/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array `time` where `time[i]` is the time for bus `i` to complete one trip, find the **minimum total time** needed so that all buses collectively complete at least `totalTrips` trips. Each bus runs independently and continuously.

### 2. Clarification Questions

- **Input constraints?** `1 <= time.length <= 10^5`, `1 <= time[i] <= 10^7`, `1 <= totalTrips <= 10^7`
- **Edge cases?** Single bus -> answer = `time[0] * totalTrips`. All buses same speed -> answer = `ceil(totalTrips / n) * time[0]`.
- **Expected output?** A single integer — minimum time.
- **Can input be modified?** Yes, but no need.

### 3. Brute Force Approach

- **Idea:** Simulate time second by second. At each second, count total trips completed by all buses. Stop when total >= `totalTrips`.
- **Time:** O(answer * n) — answer can be up to 10^14
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** If `t` time units is enough to complete `totalTrips`, then `t+1` is also enough. The number of trips completed is **monotonically non-decreasing** with time. Binary search on time.

- **Feasibility check:** At time `t`, bus `i` completes `t // time[i]` trips. Sum across all buses and check if >= `totalTrips`.

- **Time:** O(n * log(min(time) * totalTrips))
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(answer * n) | O(1) | answer can be 10^14, TLE |
| Optimized | O(n * log(min(time) * totalTrips)) | O(1) | ~47 iterations at most |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Binary search on time in `[1, min(time) * totalTrips]`
- Upper bound: the fastest bus alone completes all trips
- Feasibility: sum of `t // time[i]` across all buses

```python
from typing import List

def minimumTime(time: List[int], totalTrips: int) -> int:
    lo, hi = 1, min(time) * totalTrips    # fastest bus does all trips

    while lo < hi:
        mid = (lo + hi) // 2
        # Feasibility: total trips completed by all buses at time mid
        trips = sum(mid // t for t in time)

        if trips >= totalTrips:
            hi = mid        # enough trips — try less time
        else:
            lo = mid + 1    # not enough — need more time

    return lo
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `time = [1, 2, 3], totalTrips = 5`

`lo = 1, hi = 1 * 5 = 5`

| Time (mid) | Trips per bus | Total | Feasible? |
|------------|--------------|-------|-----------|
| mid=3 | [3, 1, 1] | 5 | Yes -> hi=3 |
| mid=2 | [2, 1, 0] | 3 | No -> lo=3 |
| lo=3, hi=3 -> return 3 |

**Output:** `3` (correct: bus 1 does 3 trips, bus 2 does 1, bus 3 does 1)

### Edge Case Testing

- **Empty input:** Constraints guarantee n >= 1.
- **Single element:** `time = [5], totalTrips = 3` -> answer = 15.
- **Typical case:** Shown above.
- **Extreme values:** `time = [10^7], totalTrips = 10^7` -> answer = 10^14. Binary search handles this in ~47 iterations.

### Complexity

- **Time:** O(n * log(min(time) * totalTrips)) — binary search over a large range, each check is O(n).
- **Space:** O(1) — no extra storage.

### Optimization Discussion

The upper bound `min(time) * totalTrips` is tight — it's the time for the fastest bus to do all trips alone. A looser bound like `max(time) * totalTrips` also works but increases iterations slightly.

**Early termination** in the feasibility check: once `trips >= totalTrips`, we can stop summing. This helps when there are many buses.

### Follow-up Variations

- What if buses have different capacities (passengers per trip)?
- What if buses need a cooldown period between trips?
- What if we want to minimize the number of buses needed to complete trips in time `T`? (Flip the binary search dimension.)

### Common Traps

- **Upper bound overflow.** `min(time) * totalTrips` can be up to 10^14. Use 64-bit integers in typed languages. Python handles big integers natively.
- **Using `max(time)` instead of `min(time)` for the upper bound.** Both work, but `min(time)` gives a tighter bound.
- **Not recognizing this as binary search on answer.** The "time" being searched is the answer, not an array index.
