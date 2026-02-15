# Capacity To Ship Packages Within D Days

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Binary Search on Answer
**Link:** https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array `weights` representing packages that must be shipped **in order**, find the **minimum ship capacity** such that all packages can be shipped within `days` days. Each day the ship loads consecutive packages until the next one would exceed capacity.

### 2. Clarification Questions

- **Input constraints?** `1 <= days <= weights.length <= 5 * 10^4`, `1 <= weights[i] <= 500`
- **Edge cases?** `days == len(weights)` means one package per day, so capacity = `max(weights)`. `days == 1` means capacity = `sum(weights)`.
- **Expected output?** A single integer — the minimum ship capacity.
- **Can input be modified?** Yes, but no need.

### 3. Brute Force Approach

- **Idea:** Try every capacity from `max(weights)` to `sum(weights)`. For each, simulate shipping. Return the first that fits within `days`.
- **Time:** O(n * sum(weights))
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** If capacity `c` can ship everything in `days` days, then `c+1` can too. The answer space `[max(weights), sum(weights)]` is **monotonic** — binary search for the minimum valid capacity.

- **Feasibility check:** Greedily pack consecutive packages onto the current day. When adding the next package would exceed capacity, start a new day. Count total days needed.

- **Time:** O(n * log(sum(weights)))
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n * sum(weights)) | O(1) | TLE for large sums |
| Optimized | O(n * log(sum(weights))) | O(1) | ~25 binary search iterations |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Binary search on capacity in `[max(weights), sum(weights)]`
- Greedy feasibility check: pack packages left-to-right, count days used
- If days used <= `days`, capacity is sufficient — search left

```python
from typing import List

def shipWithinDays(weights: List[int], days: int) -> int:
    lo, hi = max(weights), sum(weights)

    while lo < hi:
        mid = (lo + hi) // 2
        # Feasibility: can we ship with capacity mid in <= days?
        days_needed = 1
        current_load = 0

        for w in weights:
            if current_load + w > mid:
                days_needed += 1   # start a new day
                current_load = 0
            current_load += w

        if days_needed <= days:
            hi = mid        # feasible — try smaller capacity
        else:
            lo = mid + 1    # not enough — need larger capacity

    return lo
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `weights = [1,2,3,4,5,6,7,8,9,10], days = 5`

`lo = 10, hi = 55`

| Capacity (mid) | Day loads | Days | Feasible? |
|----------------|-----------|------|-----------|
| mid=32 | [1..9],[10] | 2 | Yes -> hi=32 |
| mid=21 | [1..6],[7..10] | 2 | Yes -> hi=21 |
| mid=15 | [1..5],[6,7],[8],[9],[10] | 5 | Yes -> hi=15 |
| mid=12 | [1..4],[5,6],[7],[8],[9],[10] | 6 | No -> lo=13 |
| mid=14 | [1..4],[5,6],[7],[8],[9],[10] | 6 | No -> lo=15 |
| lo=15, hi=15 -> return 15 |

**Output:** `15` (correct)

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `weights = [10], days = 1` -> capacity = 10.
- **Typical case:** Shown in dry run above.
- **Extreme values:** All weights = 500, n = 50000, days = 1 -> capacity = 25,000,000. Binary search handles in ~25 steps.

### Complexity

- **Time:** O(n * log(sum(weights))) — binary search over the capacity range, each check is O(n).
- **Space:** O(1) — only tracking current load and day count.

### Optimization Discussion

The search range `[max(weights), sum(weights)]` is tight. `max(weights)` is the hard lower bound (every package must fit), and `sum(weights)` is when everything ships in 1 day.

### Follow-up Variations

- What if packages can be reordered? (Sort descending, then bin-pack — becomes a different problem.)
- What if there are multiple ships? (Partition into `k * days` segments.)

### Common Traps

- **Lower bound must be `max(weights)`, not 1.** A capacity smaller than the heaviest package can never ship it.
- **Order matters.** Packages must be shipped in order — you cannot rearrange them.
- **Off-by-one on day counting.** Start `days_needed = 1` (the first day is always used), then increment when starting a new day.
