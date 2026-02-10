# Min-Heap of Size K (Most Common)

## What This Subpattern Means

- Maintain a **min-heap** that holds exactly **K elements** — the K largest seen so far.
- The root of the heap (the minimum among K) = the Kth largest overall.
- Think of it as: "a bag that only fits K items. When a new item comes, throw out the smallest to make room."

---

## The Trigger (How You Recognize It)

- "**Kth largest** element in an array"
- "**K closest** points to origin" (keep K smallest distances → min-heap on negated distances, or max-heap on distances of size K)
- "Kth largest in a **stream**" (maintain heap as new elements arrive)
- You want to find top K elements and K is much smaller than N

---

## Template

```python
import heapq

def kth_largest(nums, k):
    heap = []  # min-heap

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # remove smallest

    return heap[0]  # Kth largest
```

---

## Mistakes

- **Using max-heap for Kth largest.** That gives the overall maximum, not the Kth largest. Use min-heap of size K.
- **Not limiting heap size.** If you never pop, you're just building a sorted list of everything — defeats the purpose.
- **Forgetting that `heapq.heappop(heap)` returns the SMALLEST element** (it's a min-heap).
- **K closest points trap:** push `(distance, point)` tuples. Heap sorts by first element (distance).

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Kth Largest Element in an Array | Min-Heap of Size K | | |
| Kth Closest Point to Origin | Min-Heap of Size K | | |
| Kth Largest Element in a Stream | Min-Heap of Size K | | |

---

## TL;DR

- Min-heap of size K → root is the Kth largest
- Push new element, pop if size > K
- O(N log K) time, O(K) space
- Python heapq = min-heap by default (no negation needed for this variant)
