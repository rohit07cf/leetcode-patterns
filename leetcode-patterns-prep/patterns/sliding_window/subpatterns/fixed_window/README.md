# Fixed-Size Sliding Window

## What This Subpattern Means

- The window size **k is given** — it doesn't change.
- You slide a window of exactly k elements across the array, computing something at each position.
- Think of it as: "looking through a window of fixed width, and the train moves one seat at a time."

---

## The Trigger (How You Recognize It)

- "Maximum/average sum of subarray of size **k**"
- "First negative number in every window of size **k**"
- The problem literally says "window of size k" or "contiguous subarray of length k"

---

## Template

```python
def fixed_window(arr, k):
    # Build the first window
    window_sum = sum(arr[:k])
    best = window_sum

    for right in range(k, len(arr)):
        window_sum += arr[right]         # new element enters
        window_sum -= arr[right - k]     # old element leaves
        best = max(best, window_sum)

    return best
```

```
Array: [2, 1, 5, 1, 3, 2]   k = 3

Window 1: [2, 1, 5]       sum = 8
Window 2:    [1, 5, 1]     sum = 7  (added 1, removed 2)
Window 3:       [5, 1, 3]  sum = 9  (added 3, removed 1)  ← best
Window 4:          [1, 3, 2] sum = 6 (added 2, removed 5)
```

---

## Mistakes

- **Recomputing the sum from scratch each time** — that's O(N*k). Instead, add the new element and subtract the old one: O(1) per slide.
- **Off-by-one: the element leaving is `arr[right - k]`**, not `arr[right - k + 1]` or `arr[left]`.
- **Forgetting to handle `len(arr) < k`** — check this edge case.
- **Starting the loop at index 0 instead of k** — the first window is already computed before the loop.

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Max Sum Subarray of Size K | Fixed Window | DONE | |
| Average of Subarrays | Fixed Window | DONE | |
| First Negative Number in Window | Fixed Window | DONE | |

---

## TL;DR

- Build first window, then slide: add right, remove left
- O(N) total, O(1) per slide
- The leaving element is `arr[right - k]`
- Always check edge case: `len(arr) < k`
