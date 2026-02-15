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

## Curated Problem Sets (10 per subpattern)

### Min Heap of Size K
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | Kth Largest Element (215) | Medium | `min_heap_size_k/problem_01_kth_largest_element.md` |
| 2 | Top K Frequent (347) | Medium | `min_heap_size_k/problem_02_top_k_frequent.md` |
| 3 | K Closest Points (973) | Medium | `min_heap_size_k/problem_03_k_closest_points.md` |
| 4 | Sort Chars By Frequency (451) | Medium | `min_heap_size_k/problem_04_sort_chars_by_frequency.md` |
| 5 | Kth Largest in Stream (703) | Easy | `min_heap_size_k/problem_05_kth_largest_stream.md` |
| 6 | Last Stone Weight (1046) | Easy | `min_heap_size_k/problem_06_last_stone_weight.md` |
| 7 | Find K Pairs Smallest Sums (373) | Medium | `min_heap_size_k/problem_07_find_k_pairs_smallest_sums.md` |
| 8 | Kth Smallest Sorted Matrix (378) | Medium | `min_heap_size_k/problem_08_kth_smallest_sorted_matrix.md` |
| 9 | Reorganize String (767) | Medium | `min_heap_size_k/problem_09_reorganize_string.md` |
| 10 | Task Scheduler (621) | Medium | `min_heap_size_k/problem_10_task_scheduler.md` |

### Max Heap for K Smallest
| # | Problem | Difficulty | File |
|---|---------|-----------|------|
| 1 | Kth Smallest in BST (230) | Medium | `max_heap_k_smallest/problem_01_kth_smallest_bst.md` |
| 2 | K-th Smallest Pair Distance (719) | Hard | `max_heap_k_smallest/problem_02_kth_smallest_pair_distance.md` |
| 3 | Find Median Data Stream (295) | Hard | `max_heap_k_smallest/problem_03_find_median_data_stream.md` |
| 4 | Merge k Sorted Lists (23) | Hard | `max_heap_k_smallest/problem_04_merge_k_sorted_lists.md` |
| 5 | Ugly Number II (264) | Medium | `max_heap_k_smallest/problem_05_ugly_number_ii.md` |
| 6 | Super Ugly Number (313) | Medium | `max_heap_k_smallest/problem_06_super_ugly_number.md` |
| 7 | Smallest Range Covering (632) | Hard | `max_heap_k_smallest/problem_07_smallest_range_covering.md` |
| 8 | K-th Smallest Prime Fraction (786) | Medium | `max_heap_k_smallest/problem_08_kth_smallest_prime_fraction.md` |
| 9 | Meeting Rooms II (253) | Medium | `max_heap_k_smallest/problem_09_meeting_rooms_ii.md` |
| 10 | Furthest Building (1642) | Medium | `max_heap_k_smallest/problem_10_furthest_building.md` |

---

## TL;DR

- Kth largest → min-heap of size K (root = answer)
- Kth smallest → max-heap of size K (negate values in Python)
- Always limit heap size to K — pop when it exceeds K
- O(N log K) beats O(N log N) when K is small
- Python heapq = min-heap. Negate values for max-heap.
