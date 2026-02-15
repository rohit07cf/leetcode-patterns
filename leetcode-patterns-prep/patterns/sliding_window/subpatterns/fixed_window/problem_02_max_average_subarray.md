# Maximum Average Subarray I

**Difficulty:** Easy
**Pattern:** Sliding Window
**Subpattern:** Fixed Window
**Link:** https://leetcode.com/problems/maximum-average-subarray-i/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums` and an integer `k`, find the **contiguous subarray of length `k`** that has the maximum average value. Return the maximum average.

### 2. Clarification Questions

- **Input constraints?** `1 <= k <= nums.length <= 10^5`. Elements in range `[-10^4, 10^4]`.
- **Edge cases?** Array of exactly size k. All identical elements. Mix of positive and negative.
- **Expected output?** A float — the maximum average.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** Compute the average of every subarray of size k using nested loops.
- **Time:** O(n * k)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** Track the **running sum** of the window. The maximum average equals **max_sum / k**. We only need to find the max sum — division by k is done once at the end.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n * k) | O(1) | Recomputes sum each window |
| Optimized | O(n) | O(1) | Slide window, divide once |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Compute the sum of the first k elements.
- Slide the window, updating sum by adding the new element and removing the old.
- Track max sum, then convert to average at the end.

```python
def findMaxAverage(nums, k):
    # Sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide: subtract leftmost, add new rightmost
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    # Divide once at the end to avoid repeated float division
    return max_sum / k
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [1, 12, -5, -6, 50, 3], k = 4`

| Step | Window | Sum | Max Sum |
|------|--------|-----|---------|
| Init | [1,12,-5,-6] | 2 | 2 |
| i=4 | [12,-5,-6,50] | 2-1+50=51 | 51 |
| i=5 | [-5,-6,50,3] | 51-12+3=42 | 51 |

**Output:** `51 / 4 = 12.75`

### Edge Case Testing

- **Empty input:** Constraints guarantee `k >= 1` and `len >= k`, so not possible.
- **Single element:** `k = 1` returns max element as float.
- **Typical case:** Covered in dry run.
- **Extreme values:** All `-10^4` — returns `-10^4.0`. Handles negatives correctly.

### Complexity

- **Time:** O(n) — one pass through the array.
- **Space:** O(1) — constant extra memory.

### Optimization Discussion

Already optimal. The key optimization over brute force is avoiding recomputation — each element is added and removed from the window exactly once.

### Follow-up Variations

- **Maximum Average Subarray II** (LC 644, Hard): Find max average for subarrays of length >= k. Requires binary search + prefix sums.
- Return the **starting index** instead of the average.
- Handle **streaming data** where elements arrive one at a time.

### Common Traps

- **Using float division inside the loop.** Unnecessary overhead. Compare sums, divide once.
- **Integer overflow in other languages.** In Python this isn't an issue, but in Java/C++ watch for `int` overflow with large arrays.
- **Returning int instead of float.** The problem expects a float result.
