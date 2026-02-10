# Top K Elements

> **Top K = "keep only the best K in a small bag."** You have a stream of N items but you only care about the top K. A heap lets you maintain those K items efficiently without sorting everything.

---

## When to Use

- The problem asks for the **Kth largest** or **Kth smallest** element
- You need the **top K** frequent / closest / largest / smallest elements
- You're processing a **stream** and need to maintain a running "top K"
- Sorting the entire input would work but is overkill (you only need K elements)
- The problem says "find K elements" where K << N

---

## How to Spot It Fast

- "**Kth largest** element" → min-heap of size K
- "**Kth smallest** element" → max-heap of size K (negate values in Python)
- "**Top K frequent** elements" → heap or bucket sort
- "**K closest** points to origin" → max-heap of size K (keep closest, evict farthest)
- "**K closest** elements to target" → heap or two pointers
- The constraint says K is much smaller than N

---

## Core Idea

- **For Kth largest: use a MIN-heap of size K**
  - The heap holds the K largest elements seen so far
  - The ROOT (minimum of the heap) is the Kth largest
  - When a new element comes in: if it's bigger than the root, pop root, push new element
  - Why min-heap? Because you want to evict the SMALLEST of the K largest → that's the root of a min-heap

```
Finding 3rd largest in [3, 1, 5, 12, 2, 11]

Heap (size 3):    [5, 11, 12]   (min-heap: root = 5)
                   ↑
                   3rd largest!

New element 2: 2 < 5 → ignore (not in top 3)
New element 13: 13 > 5 → pop 5, push 13 → [11, 12, 13], new 3rd largest = 11
```

---

## Template (Python)

```python
import heapq

def kth_largest(nums, k):
    """Find Kth largest using min-heap of size k."""
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)    # remove smallest (not in top K)

    return heap[0]  # root = Kth largest


def top_k_frequent(nums, k):
    """Find K most frequent elements."""
    from collections import Counter

    count = Counter(nums)
    # Use a min-heap of size k on frequencies
    return heapq.nlargest(k, count.keys(), key=count.get)
```

---

## Common Pitfalls

1. **Using a MAX-heap for Kth largest.** That gives you the 1st largest, not the Kth. Use a MIN-heap of size K.
2. **Python's heapq is a MIN-heap only.** For max-heap behavior, negate the values: `heapq.heappush(heap, -val)`.
3. **Forgetting to limit heap size to K.** If you push everything without popping, you're just sorting. Pop when `len(heap) > k`.
4. **Off-by-one with heap size.** After processing, `heap[0]` (the root) is the Kth largest.
5. **Using sorted() instead of a heap.** Sorting is O(N log N). A heap of size K is O(N log K) — faster when K << N.
6. **Not considering bucket sort for "top K frequent."** If value range is bounded, bucket sort can be O(N) — faster than heap.
7. **K closest points: comparing distances wrong.** Use squared distance (avoid sqrt for performance and precision).
8. **Popping from an empty heap.** Always check heap size before popping.
9. **Confusing Kth largest with Kth smallest.** Kth largest uses min-heap. Kth smallest uses max-heap. Draw it on paper if confused.
10. **Not knowing `heapq.nlargest(k, iterable)` and `heapq.nsmallest(k, iterable)` exist.** These are convenient but still O(N log K).

---

## Practice Problems (from Excel)

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Kth Largest Element in an Array | Min-Heap of Size K | | |
| Kth Closest Point to Origin | Min-Heap of Size K | | |
| Kth Largest Element in a Stream | Min-Heap of Size K | | |
| Find K Closest Elements | Max-Heap for K Smallest | | |
| Kth Smallest Element in a Sorted Matrix | Max-Heap for K Smallest | | |
| Top K Frequent Elements | Max-Heap for K Smallest | | |

---

## TL;DR

- Kth largest → min-heap of size K (root = answer)
- Kth smallest → max-heap of size K (negate values in Python)
- Always limit heap size to K — pop when it exceeds K
- O(N log K) beats O(N log N) when K is small
- Python heapq = min-heap. Negate values for max-heap.
