# Diet Plan Performance

**Difficulty:** Easy
**Pattern:** Sliding Window
**Subpattern:** Fixed Window
**Link:** https://leetcode.com/problems/diet-plan-performance/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

A dieter consumes `calories[i]` on day `i`. For every **consecutive sequence of `k` days**, if the total calories are:
- **< lower:** lose 1 point
- **> upper:** gain 1 point
- **Otherwise:** no change

Return the total points after processing all windows.

### 2. Clarification Questions

- **Input constraints?** `1 <= k <= calories.length <= 10^5`. `0 <= calories[i] <= 20000`. `0 <= lower <= upper`.
- **Edge cases?** All windows exactly equal to lower or upper. k equals array length (single window).
- **Expected output?** An integer — total points (can be negative).
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** For each window of k days, sum the calories and compare to thresholds.
- **Time:** O(n * k)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** Classic fixed sliding window for sum. Maintain a running sum, slide by subtracting the leaving element and adding the entering element. Compare each window sum to `lower` and `upper`.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n * k) | O(1) | Recomputes sum |
| Optimized | O(n) | O(1) | Running sum with threshold checks |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Compute sum of the first k-day window.
- Check against thresholds and update points.
- Slide the window across the rest of the array, updating sum and points.

```python
def dietPlanPerformance(calories, k, lower, upper):
    points = 0
    window_sum = sum(calories[:k])

    # Check first window
    if window_sum < lower:
        points -= 1
    elif window_sum > upper:
        points += 1

    # Slide the window
    for i in range(k, len(calories)):
        window_sum += calories[i] - calories[i - k]

        if window_sum < lower:
            points -= 1
        elif window_sum > upper:
            points += 1

    return points
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `calories = [1, 2, 3, 4, 5], k = 1, lower = 3, upper = 3`

Each window has 1 element:

| Day | Calories | Sum | Points Change | Total |
|-----|----------|-----|---------------|-------|
| 0 | 1 | 1 | < 3: -1 | -1 |
| 1 | 2 | 2 | < 3: -1 | -2 |
| 2 | 3 | 3 | in range: 0 | -2 |
| 3 | 4 | 4 | > 3: +1 | -1 |
| 4 | 5 | 5 | > 3: +1 | 0 |

**Output:** `0`

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `k = 1` works — each element is its own window.
- **Typical case:** Covered in dry run.
- **Extreme values:** All calories = 0 and lower = 0 — every window sum equals lower, which is NOT strictly less than lower, so no points lost.

### Complexity

- **Time:** O(n) — one pass through the array.
- **Space:** O(1) — constant extra memory.

### Optimization Discussion

This is the simplest application of fixed sliding window. The only nuance is the **three-way comparison** (below lower, above upper, or in between).

### Follow-up Variations

- What if thresholds change per window (different lower/upper for each day range)?
- What if the dieter can **skip** up to m days? (Becomes a variable-size window problem.)
- Count the **number of windows** in each category instead of points.

### Common Traps

- **Using `<=` instead of `<` for lower threshold.** The problem says **strictly less than** lower and **strictly greater than** upper. Read carefully.
- **Forgetting to check the first window.** The first window must be evaluated before the sliding loop starts.
- **Off-by-one errors.** With k=1, there are n windows. With k=n, there is 1 window. Verify your loop range covers all cases.
