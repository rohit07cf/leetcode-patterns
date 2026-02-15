# Top K Frequent Elements

**Difficulty:** Medium
**Pattern:** Top K Elements
**Subpattern:** Min Heap of Size K
**Link:** https://leetcode.com/problems/top-k-frequent-elements/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. The answer may be returned in any order.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 10^5`, `1 <= k <= number of unique elements`.
- **Edge cases?** All elements the same (`k = 1`); every element unique (`k = n`).
- **Expected output?** A list of `k` integers (order doesn't matter).
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Count frequencies with a hash map, sort by frequency descending, return the first `k` elements.
- **Time:** O(n + u log u) where u = number of unique elements
- **Space:** O(u)

### 4. Optimized Approach

- 💡 **Core Insight:** After counting frequencies, maintain a **min heap of size k** keyed by frequency. The heap always holds the k most frequent elements. Any element with frequency ≤ the heap root can't be in the top k.
- **Time:** O(n + u log k)
- **Space:** O(u + k)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort by frequency | O(n + u log u) | O(u) | Simple, sorts all unique elements |
| Min Heap of size k | O(n + u log k) | O(u + k) | **Better when k << u** |
| Bucket Sort | O(n) | O(n) | Optimal but uses more space |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Count element frequencies using a hash map.
- Push `(frequency, element)` tuples onto a min heap of size k.
- When heap exceeds size k, pop the smallest frequency — it's not in the top k.

```python
import heapq
from collections import Counter

def topKFrequent(nums, k):
    freq = Counter(nums)

    # Min heap of size k, keyed by frequency
    heap = []
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            # Evict the least frequent among our candidates
            heapq.heappop(heap)

    # Extract elements from heap (order doesn't matter)
    return [num for count, num in heap]
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums = [1, 1, 1, 2, 2, 3], k = 2`

Frequencies: `{1: 3, 2: 2, 3: 1}`

1. Push `(3, 1)` → heap: `[(3, 1)]`
2. Push `(2, 2)` → heap: `[(2, 2), (3, 1)]`
3. Push `(1, 3)` → heap: `[(1, 3), (3, 1), (2, 2)]` → size > 2, pop `(1, 3)`
4. Heap: `[(2, 2), (3, 1)]`
5. Return `[2, 1]` ✓

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `nums = [5], k = 1` → freq `{5: 1}` → return `[5]`.
- **Typical case:** Covered in dry run.
- **Extreme values:** All elements identical → freq has one entry → heap has one entry → return it.

### Complexity

- **Time:** O(n + u log k) — O(n) to count, O(u log k) for heap operations over u unique elements.
- **Space:** O(u + k) — hash map stores u entries, heap stores k entries.

### Optimization Discussion

- **Bucket sort approach:** Create buckets indexed by frequency (max freq = n). Walk buckets from highest to lowest, collect k elements. O(n) time but O(n) space for the bucket array.
- **`heapq.nlargest`:** `heapq.nlargest(k, freq.keys(), key=freq.get)` is a clean one-liner.
- For very large datasets where k is small, the heap approach shines.

### Follow-up Variations

- **Top K frequent words** (LeetCode 692) — same approach but break ties alphabetically (requires custom comparison).
- **K least frequent elements** — use a max heap of size k instead.
- **Streaming frequency** — combine with a hash map and heap, update on each new element.

### ⚠️ Common Traps

- **Heap keyed by element value instead of frequency.** The heap must compare by frequency so we evict the least frequent candidate.
- **Returning frequencies instead of elements.** Extract the second field from each heap tuple.
- **Assuming output must be sorted.** The problem says "in any order," so no sorting of results needed.
