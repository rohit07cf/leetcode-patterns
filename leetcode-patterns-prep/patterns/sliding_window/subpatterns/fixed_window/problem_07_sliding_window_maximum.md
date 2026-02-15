# Sliding Window Maximum

**Difficulty:** Hard
**Pattern:** Sliding Window
**Subpattern:** Fixed Window
**Link:** https://leetcode.com/problems/sliding-window-maximum/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums` and a window size `k`, return the **maximum element** in each sliding window of size `k` as it moves from left to right.

### 2. Clarification Questions

- **Input constraints?** `1 <= k <= nums.length <= 10^5`. Elements in range `[-10^4, 10^4]`.
- **Edge cases?** `k = 1` (each element is its own max). `k = n` (single window). Descending/ascending arrays. All identical elements.
- **Expected output?** List of integers of length `n - k + 1`.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** For each window position, scan all k elements to find the maximum.
- **Time:** O(n * k)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** Use a **monotonic decreasing deque**. The deque stores **indices** of elements in decreasing order of value. The front always holds the index of the current window's maximum. When sliding:
  1. Remove indices that fall outside the window.
  2. Remove indices from the back whose values are less than the new element (they can never be the max).
  3. Add the new index.

- **Time:** O(n)
- **Space:** O(k)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n * k) | O(1) | Too slow for 10^5 |
| Max Heap | O(n log k) | O(k) | Lazy deletion adds complexity |
| **Monotonic Deque** | **O(n)** | **O(k)** | **Optimal — each element enters/exits deque once** |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Maintain a deque of **indices** in decreasing order of their values.
- For each new element:
  1. **Evict expired** — remove front if its index is outside the window.
  2. **Maintain monotonicity** — pop from back while `nums[back] <= nums[i]`.
  3. **Append** new index to back.
  4. **Record max** — `nums[deque[0]]` is the window max.

```python
from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()  # stores indices, values are in decreasing order
    result = []

    for i in range(len(nums)):
        # Remove indices outside the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements from back — they'll never be the max
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        # Window is fully formed starting at index k-1
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3`

| i | nums[i] | Deque (indices) | Deque (values) | Result |
|---|---------|-----------------|----------------|--------|
| 0 | 1 | [0] | [1] | — |
| 1 | 3 | [1] | [3] | — |
| 2 | -1 | [1, 2] | [3, -1] | **3** |
| 3 | -3 | [1, 2, 3] | [3, -1, -3] | **3** |
| 4 | 5 | [4] | [5] | **5** |
| 5 | 3 | [4, 5] | [5, 3] | **5** |
| 6 | 6 | [6] | [6] | **6** |
| 7 | 7 | [7] | [7] | **7** |

**Output:** `[3, 3, 5, 5, 6, 7]`

**Key moment at i=4:** nums[4]=5 is larger than all deque elements. All popped, deque becomes [4].

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `k = 1` — each element is appended directly. Deque always has one element.
- **Typical case:** Covered in dry run.
- **Extreme values:** Sorted ascending — deque always has 1 element (all previous popped). Sorted descending — deque grows to size k (no popping from back).

### Complexity

- **Time:** O(n) — each element is pushed and popped from the deque **at most once**. Amortized O(1) per element.
- **Space:** O(k) — deque holds at most k indices.

### Optimization Discussion

**Why not a heap?** A max-heap gives O(n log k), which is worse. Also, the heap has **stale elements** (indices outside the window) that need lazy deletion, adding complexity.

**Why monotonic deque works:** Elements smaller than the new element can **never** be the maximum of any future window containing the new element. So removing them is safe and keeps the deque monotonically decreasing.

### Follow-up Variations

- **Sliding Window Minimum** — same logic, but maintain increasing deque.
- **Sliding Window Median** (LC 480) — much harder, requires two heaps or sorted container.
- **Maximum of subarrays of all sizes** — run this for each k from 1 to n.
- **Shortest subarray with sum >= target** — variable window, different technique.

### Common Traps

- **Storing values instead of indices.** You need indices to check if the front element is still inside the window.
- **Using `<` instead of `<=` when popping.** Using strict `<` leaves duplicates in the deque. Use `<=` to keep only the rightmost occurrence (or `<` if you want leftmost — but `<=` is simpler).
- **Forgetting to check `dq[0] < i - k + 1`.** Without this, expired elements stay at the front and produce wrong answers.
- **Off-by-one on when to start recording.** The first full window ends at index `k - 1`, not `k`.
