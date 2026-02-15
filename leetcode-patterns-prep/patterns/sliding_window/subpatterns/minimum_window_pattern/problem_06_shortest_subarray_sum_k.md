# Shortest Subarray with Sum at Least K

**Difficulty:** Hard
**Pattern:** Sliding Window
**Subpattern:** Minimum Window Pattern
**Link:** https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an integer array `nums` (which may contain **negative numbers**) and an integer `k`, find the length of the shortest non-empty subarray with a sum of at least `k`. Return `-1` if no such subarray exists.

### 2. Clarification Questions
- Input constraints? `1 <= nums.length <= 10^5`, `-10^5 <= nums[i] <= 10^5`, `1 <= k <= 10^9`.
- Edge cases? All negative numbers (return -1), single element >= k, negative numbers disrupt monotonicity.
- Expected output? An integer (shortest length), or -1.
- Can input be modified? Yes.

### 3. Brute Force Approach
- **Idea:** Check all subarrays using prefix sums. For each pair `(i, j)`, check if `prefix[j] - prefix[i] >= k`.
- **Time:** O(n^2)
- **Space:** O(n) for prefix sums.

### 4. Optimized Approach
- **Core Insight:** Build prefix sums. We need the smallest `j - i` where `prefix[j] - prefix[i] >= k` and `i < j`. Use a **monotonic deque** of prefix sum indices. The deque maintains increasing prefix sums — if a later prefix is smaller, earlier larger ones are useless (a smaller prefix always gives a larger difference). For each `j`, pop from the front while `prefix[j] - prefix[front] >= k`.
- **Time:** O(n)
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(n) | Check all pairs |
| Monotonic Deque | O(n) | O(n) | Optimal for negative numbers |

**Why not standard sliding window?** Negative numbers mean the running sum isn't monotonic — shrinking the window can **decrease** the sum. The deque handles this.

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Compute prefix sums where `prefix[j]` = sum of `nums[0..j-1]`.
- Maintain a deque of indices into `prefix`, kept in **increasing order** of prefix values.
- For each `j`, pop from **front** if `prefix[j] - prefix[deque[0]] >= k` (valid subarray, try shorter).
- Pop from **back** if `prefix[j] <= prefix[deque[-1]]` (current prefix is smaller, so deque[-1] is never useful).

```python
from collections import deque

def shortestSubarray(nums: list[int], k: int) -> int:
    n = len(nums)

    # build prefix sums: prefix[i] = sum(nums[0..i-1])
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    best = float('inf')
    dq = deque()  # stores indices into prefix, monotonically increasing values

    for j in range(n + 1):
        # if prefix[j] - prefix[front] >= k, we found a valid subarray
        while dq and prefix[j] - prefix[dq[0]] >= k:
            best = min(best, j - dq.popleft())

        # maintain monotonic property: remove larger prefixes from back
        while dq and prefix[j] <= prefix[dq[-1]]:
            dq.pop()

        dq.append(j)

    return best if best != float('inf') else -1
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `nums = [2, -1, 2]`, `k = 3`

Prefix: `[0, 2, 1, 3]`

| j | prefix[j] | Front pop? | Back pop? | dq | best |
|---|-----------|------------|-----------|-----|------|
| 0 | 0 | — | — | [0] | inf |
| 1 | 2 | 2-0=2 < 3 | 2>0, no pop | [0,1] | inf |
| 2 | 1 | 1-0=1 < 3 | 1<=2, pop 1 | [0,2] | inf |
| 3 | 3 | 3-0=3 >= 3 → pop 0, best=3 | 3-1=2 < 3 | [2,3] | 3 |

**Output:** `3`

### Edge Case Testing
- **Empty input:** Not possible per constraints.
- **Single element:** `nums = [5]`, `k = 5` → prefix = [0,5], j=1: 5-0=5 >= 5, best=1.
- **Typical case:** Shown in dry run.
- **Extreme values:** All negative → no subarray sums to k → returns -1.

### Complexity
- **Time:** O(n) — each index is pushed and popped from the deque at most once.
- **Space:** O(n) — prefix array and deque each hold at most n+1 elements.

### Optimization Discussion
- The monotonic deque is crucial because negative numbers prevent the standard two-pointer shrinking technique.
- If all numbers were **non-negative**, a simple sliding window (expand right, shrink left) would suffice in O(n).

### Follow-up Variations
- What if all numbers are non-negative? (Simpler sliding window.)
- Shortest subarray with sum **exactly** k.
- Shortest subarray with sum at least k in a **circular** array.

### Common Traps
- **Using standard sliding window with negatives** — the sum isn't monotonic, so shrinking can decrease the sum. This fails.
- **Forgetting to pop from both ends of the deque** — front pops find valid answers, back pops maintain monotonicity. Both are essential.
- **Off-by-one with prefix sums** — `prefix` has length `n+1`, and index 0 represents the empty prefix (sum = 0).
