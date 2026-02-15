# Maximum Sum Subarray of Size K

**Difficulty:** Easy
**Pattern:** Sliding Window
**Subpattern:** Fixed Window
**Link:** https://leetcode.com/problems/maximum-sum-subarray-of-size-k/ (Premium / Classic)

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of integers and a number `k`, find the **maximum sum** of any contiguous subarray of size `k`.

### 2. Clarification Questions

- **Input constraints?** Array length >= k, k >= 1. Elements can be negative.
- **Edge cases?** Array of size exactly k (only one window). All negative numbers.
- **Expected output?** A single integer — the maximum sum.
- **Can input be modified?** Yes, but no modification needed.

### 3. Brute Force Approach

- **Idea:** For every index `i`, compute the sum of `arr[i..i+k-1]` using a nested loop.
- **Time:** O(n * k)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** When sliding the window one position right, **subtract the element leaving** and **add the element entering**. No need to recompute the entire sum.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n * k) | O(1) | Recomputes sum each time |
| Optimized | O(n) | O(1) | Slide: subtract left, add right |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Compute the sum of the first window of size `k`.
- Slide the window: subtract `arr[i - k]`, add `arr[i]`.
- Track the maximum sum seen.

```python
def max_sum_subarray_k(arr, k):
    n = len(arr)
    if n < k:
        return 0

    # Compute sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window across the array
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]  # add new element, remove old
        max_sum = max(max_sum, window_sum)

    return max_sum
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `arr = [2, 1, 5, 1, 3, 2], k = 3`

| Step | Window | Sum | Max |
|------|--------|-----|-----|
| Init | [2,1,5] | 8 | 8 |
| i=3 | [1,5,1] | 8-2+1=7 | 8 |
| i=4 | [5,1,3] | 7-1+3=9 | 9 |
| i=5 | [1,3,2] | 9-5+2=6 | 9 |

**Output:** `9`

### Edge Case Testing

- **Empty input:** `n < k` returns 0.
- **Single element:** `k = 1` returns max element.
- **Typical case:** Covered in dry run.
- **Extreme values:** All negative numbers — still works because we track max of all window sums.

### Complexity

- **Time:** O(n) — single pass through the array.
- **Space:** O(1) — only a few variables.

### Optimization Discussion

This is already optimal. Any algorithm must examine each element at least once, so O(n) is a lower bound.

### Follow-up Variations

- **Minimum sum** subarray of size k (same technique, track min).
- **Maximum product** subarray of size k (different — needs log trick or careful handling of negatives).
- Return the **starting index** of the max-sum subarray.

### Common Traps

- **Off-by-one in window boundaries.** The element leaving is at `i - k`, not `i - k + 1`.
- **Forgetting to initialize max with first window sum.** Initializing to 0 fails with all-negative arrays.
- **Not handling `n < k`.** Always validate input before processing.
