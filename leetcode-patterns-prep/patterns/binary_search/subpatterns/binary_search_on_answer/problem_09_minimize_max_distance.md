# Minimize Max Distance to Gas Station

**Difficulty:** Hard
**Pattern:** Binary Search
**Subpattern:** Binary Search on Answer
**Link:** https://leetcode.com/problems/minimize-max-distance-to-gas-station/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given `stations` (sorted positions of gas stations on a number line) and an integer `k` (number of new stations to add), **minimize the maximum distance** between any two adjacent stations after optimally placing the `k` new stations.

### 2. Clarification Questions

- **Input constraints?** `10 <= stations.length <= 2000`, `0 <= stations[i] <= 10^8`, `1 <= k <= 10^6`. Stations are sorted and unique.
- **Edge cases?** `k` very large -> max distance approaches 0. `k = 0` -> answer is the current max gap.
- **Expected output?** A floating-point number — the minimized max distance (within 10^-6 precision).
- **Can input be modified?** Yes, but no need.

### 3. Brute Force Approach

- **Idea:** Greedily place one station at a time into the largest gap, splitting it in half. Use a max-heap to track gaps.
- **Time:** O(k * log(n))
- **Space:** O(n)

### 4. Optimized Approach

- **Core Insight:** Binary search on the answer (the max distance `d`). For a given `d`, greedily compute how many stations are needed: each gap of size `g` needs `ceil(g / d) - 1` new stations. If total needed <= `k`, `d` is feasible.

- **Note:** This is a **floating-point binary search** — we iterate until precision is sufficient (typically ~100 iterations or until `hi - lo < 10^-6`).

- **Time:** O(n * log(max_gap / epsilon))
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Greedy + Heap | O(k * log(n)) | O(n) | k can be 10^6, slower |
| Binary Search | O(n * log(max_gap / eps)) | O(1) | ~50 iterations, clean |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Compute gaps between consecutive stations
- Binary search on max distance `d` in `[0, max_gap]`
- Feasibility: for each gap, compute stations needed = `ceil(gap / d) - 1`
- Use ~100 iterations for floating-point precision (or while `hi - lo > 1e-6`)

```python
import math
from typing import List

def minmaxGasDist(stations: List[int], k: int) -> float:
    # Compute gaps between consecutive stations
    gaps = [stations[i + 1] - stations[i] for i in range(len(stations) - 1)]

    lo, hi = 0.0, max(gaps)

    # Float binary search: ~100 iterations guarantees precision < 10^-6
    for _ in range(100):
        mid = (lo + hi) / 2.0
        # Feasibility: how many new stations needed to make all gaps <= mid?
        stations_needed = sum(math.ceil(g / mid) - 1 for g in gaps if g > mid)

        if stations_needed <= k:
            hi = mid        # feasible — try smaller max distance
        else:
            lo = mid        # need more stations — allow larger distance

    return lo
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 9`

All gaps = 1.0, `max_gap = 1.0`, `lo = 0, hi = 1.0`

| Max dist (mid) | Stations needed per gap | Total | Feasible? |
|-----------------|------------------------|-------|-----------|
| mid=0.5 | ceil(1/0.5)-1 = 1 each | 9 | Yes -> hi=0.5 |
| mid=0.25 | ceil(1/0.25)-1 = 3 each | 27 | No -> lo=0.25 |
| ... converges to 0.5 |

**Output:** `0.5` (correct: place one station in each gap)

### Edge Case Testing

- **Empty input:** Constraints guarantee n >= 10.
- **Single gap:** `stations = [0, 10], k = 4` -> gap=10, need 10/(4+1)=2.0.
- **Typical case:** Shown above.
- **Extreme values:** Very large `k` -> answer approaches 0. `k = 0` -> answer is max existing gap.

### Complexity

- **Time:** O(n * log(max_gap / epsilon)) — with 100 fixed iterations and O(n) feasibility check.
- **Space:** O(n) — for storing gaps (can be O(1) by computing on the fly).

### Optimization Discussion

**Fixed iterations vs. epsilon check:** Using `for _ in range(100)` is more robust than `while hi - lo > 1e-6` because it avoids floating-point edge cases where convergence stalls. After 100 iterations, precision is `max_gap / 2^100`, far beyond what's needed.

**Alternative:** The greedy heap approach works too but is slower when `k` is large.

### Follow-up Variations

- What if stations have different costs to build at different locations?
- What if we want to minimize the average distance instead of the maximum?
- What if the road is circular (wrap-around)?

### Common Traps

- **This is floating-point binary search.** Don't use `lo < hi` with integer adjustments. Use a fixed number of iterations or an epsilon check.
- **`ceil(g / mid) - 1` not `ceil(g / mid)`.** We need the number of **new** stations, not the number of segments. Splitting a gap into `s` segments requires `s - 1` new stations.
- **Division by zero.** When `mid` approaches 0, `ceil(g / mid)` explodes. The `if g > mid` guard or starting `lo > 0` prevents this.
- **Gaps of size 0.** If two stations are at the same position, the gap is 0 and needs 0 new stations. The `if g > mid` guard handles this.
