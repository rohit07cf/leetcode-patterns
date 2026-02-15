# Find Median from Data Stream

**Difficulty:** Hard
**Pattern:** Top K Elements
**Subpattern:** Max Heap for K Smallest
**Link:** https://leetcode.com/problems/find-median-from-data-stream/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Design a data structure that supports adding integers from a data stream and finding the median of all elements seen so far at any point.

### 2. Clarification Questions

- **Input constraints?** -10^5 <= num <= 10^5, at most 5 * 10^4 calls, `findMedian` only called when at least one element exists.
- **Edge cases?** Single element (median is itself), two elements (average), even vs odd count.
- **Expected output?** `addNum(num)` adds a number; `findMedian()` returns the median as a float.
- **Can input be modified?** N/A — streaming design.

### 3. Brute Force Approach

- **Idea:** Maintain a sorted list. On each insert, use binary search to find position and insert. Median is the middle element(s).
- **Time:** O(n) per insert (shifting), O(1) per findMedian.
- **Space:** O(n)

### 4. Optimized Approach

- 💡 **Core Insight:** Use **two heaps** — a **max heap** for the smaller half and a **min heap** for the larger half. The max heap's root is the largest of the small half; the min heap's root is the smallest of the large half. The median is derived from these two roots. Keep heaps balanced (sizes differ by at most 1).
- **Time:** O(log n) per addNum, O(1) per findMedian.
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time (add) | Time (median) | Space | Notes |
|----------|-----------|---------------|-------|-------|
| Sorted list + insert | O(n) | O(1) | O(n) | Shifting is expensive |
| Two heaps | O(log n) | O(1) | O(n) | Optimal for streaming |
| Self-balancing BST | O(log n) | O(log n) | O(n) | More complex to implement |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- `small` = max heap (stores the smaller half, negated for Python).
- `large` = min heap (stores the larger half).
- Always add to `small` first, then rebalance so that `small` has the same or one more element than `large`.
- Median: if odd total, top of `small`; if even, average of both tops.

```python
import heapq

class MedianFinder:
    def __init__(self):
        # Max heap for smaller half (negated values)
        self.small = []
        # Min heap for larger half
        self.large = []

    def addNum(self, num):
        # Always push to max heap (small) first
        heapq.heappush(self.small, -num)

        # Ensure max of small <= min of large
        if self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance sizes: small can have at most 1 more than large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            # Odd count — median is top of small (max heap)
            return -self.small[0]
        # Even count — average of both tops
        return (-self.small[0] + self.large[0]) / 2.0
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Add: 1, 2, 3

1. `addNum(1)`: small=[-1], large=[] → median = 1
2. `addNum(2)`: small=[-1], large=[2] (rebalanced) → median = (1+2)/2 = 1.5
3. `addNum(3)`: push -3 to small → small=[-3,-1], large=[2] → -small[0]=3 > large[0]=2, swap → small=[-2,-1], large=[3] → sizes ok → but small has 2, large has 1, that's fine → median = -small[0] = **2** ✓

### Edge Case Testing

- **Empty input:** `findMedian` not called when empty per constraints.
- **Single element:** Pushed to `small`, returned directly.
- **Typical case:** Alternating adds and finds — heaps stay balanced.
- **Extreme values:** -10^5 and 10^5 — no overflow in Python.

### Complexity

- **Time:** O(log n) per `addNum` (heap operations), O(1) per `findMedian`.
- **Space:** O(n) — all elements stored across two heaps.

### Optimization Discussion

- **Follow-up (LC prompt):** If all numbers are in [0, 100], use a counting array of size 101 and binary search for the median — O(1) add, O(100) find.
- If 99% of numbers are in [0, 100], handle outliers separately with a small sorted structure.

### Follow-up Variations

- **Sliding window median** (LC 480) — use two heaps with lazy deletion.
- Percentile queries (e.g., 90th percentile) — adjust heap size ratio.

### ⚠️ Common Traps

- **Forgetting to rebalance** — sizes can drift apart by more than 1 if you skip the balance step.
- **Negation errors** — Python's heapq is min-only; every push/pop to the max heap must negate.
- **Integer vs float division** — return a float for even-count medians (`/ 2.0` not `// 2`).
