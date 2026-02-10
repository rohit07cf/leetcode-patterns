# Max-Heap for K Smallest (Inverted)

## What This Subpattern Means

- When you need the **K smallest** elements, use a **max-heap** of size K.
- In Python, simulate max-heap by **negating values** before pushing to heapq.
- The root (largest among K) = the Kth smallest overall. If a new element is smaller, it replaces the root.

---

## The Trigger (How You Recognize It)

- "Find **K closest** elements to a target" (sometimes solved with two pointers)
- "**Kth smallest** element in a sorted matrix"
- "**Top K frequent** elements" (can use heap on frequencies)
- You want the K smallest and need to evict the largest when the heap is full

---

## Template

```python
import heapq

def kth_smallest(nums, k):
    heap = []  # simulated max-heap (negate values)

    for num in nums:
        heapq.heappush(heap, -num)   # negate to simulate max-heap
        if len(heap) > k:
            heapq.heappop(heap)      # remove largest (not in bottom K)

    return -heap[0]  # negate back to get actual value
```

---

## Mistakes

- **Forgetting to negate BOTH when pushing AND when reading the result.** Push `-num`, read `-heap[0]`.
- **Using min-heap for K smallest.** That gives the overall minimum, not the Kth smallest. Use max-heap of size K.
- **Top K frequent trap:** you might want a min-heap of size K on frequencies (keep K highest frequencies) — think about whether you're finding K largest or K smallest frequencies.
- **Sorted matrix:** consider using a min-heap that processes rows/columns in order instead of the max-heap approach.

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Find K Closest Elements | Max-Heap for K Smallest | | |
| Kth Smallest Element in a Sorted Matrix | Max-Heap for K Smallest | | |
| Top K Frequent Elements | Max-Heap for K Smallest | | |

---

## TL;DR

- K smallest → max-heap of size K (negate values in Python)
- Root = Kth smallest (negated). Evict the largest to make room.
- Always negate on push AND when reading the result
- Some problems have alternative approaches (two pointers, bucket sort) — know when heap isn't the best choice
