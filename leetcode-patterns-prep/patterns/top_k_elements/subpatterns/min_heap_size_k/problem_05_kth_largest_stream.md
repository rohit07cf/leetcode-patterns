# Kth Largest Element in a Stream

**Difficulty:** Easy
**Pattern:** Top K Elements
**Subpattern:** Min Heap of Size K
**Link:** https://leetcode.com/problems/kth-largest-element-in-a-stream/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Design a class that finds the **kth largest** element in a stream. For each new element added via `add(val)`, return the current kth largest element across all values seen so far.

### 2. Clarification Questions

- **Input constraints?** `1 <= k <= 10^4`, initial array can have `0` to `10^4` elements, up to `10^4` calls to `add`.
- **Edge cases?** Initial array has fewer than k elements (kth largest undefined until enough elements arrive); duplicate values.
- **Expected output?** `add()` returns an integer — the kth largest after insertion.
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Store all elements in a sorted list. On each `add`, insert in sorted position, return element at index `len - k`.
- **Time:** O(n) per `add` (insertion into sorted list)
- **Space:** O(n)

### 4. Optimized Approach

- 💡 **Core Insight:** This is the **textbook use case** for a min heap of size k. The heap always holds the k largest elements seen so far, and the root is the kth largest. On each `add`, push the new value; if heap exceeds size k, pop the smallest.
- **Time:** O(log k) per `add`
- **Space:** O(k)

### 5. Trade-off Comparison

| Approach | Time (per add) | Space | Notes |
|----------|----------------|-------|-------|
| Sorted list | O(n) | O(n) | Linear scan + shift on insert |
| Min Heap of size k | O(log k) | O(k) | **Optimal for streaming** |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Initialize a min heap from the input array, trim to size k.
- On `add`, push the new value. If heap exceeds size k, pop the root.
- Return the root — it's the kth largest.

```python
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums[:]
        heapq.heapify(self.heap)

        # Trim heap down to size k (only keep the k largest)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            # Evict smallest — it can't be in the top k
            heapq.heappop(self.heap)

        # Root is the kth largest
        return self.heap[0]
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`k = 3, nums = [4, 5, 8, 2]`

1. Heapify: `[2, 4, 8, 5]` → trim to size 3 → pop `2` → `[4, 5, 8]`
2. `add(3)`: push 3 → `[3, 4, 8, 5]` → size 4 > 3, pop 3 → `[4, 5, 8]` → return `4`
3. `add(5)`: push 5 → `[4, 5, 8, 5]` → pop 4 → `[5, 5, 8]` → return `5`
4. `add(10)`: push 10 → `[5, 5, 10, 8]` → pop 5 → `[5, 8, 10]` → return `5`
5. `add(9)`: push 9 → `[5, 8, 10, 9]` → pop 5 → `[8, 9, 10]` → return `8`

### Edge Case Testing

- **Empty input:** `nums = []`, heap starts empty. First k calls to `add` grow the heap. Once size reaches k, root is valid.
- **Single element:** `k = 1, nums = [5]` → heap `[5]`, root is always the max.
- **Typical case:** Covered in dry run.
- **Extreme values:** Very large or very negative values are handled naturally by the heap.

### Complexity

- **Time:** O(n log k) for initialization (heapify + trim), O(log k) per `add` call.
- **Space:** O(k) — heap never exceeds size k.

### Optimization Discussion

- **Why not `heapreplace`?** We can't always replace — if `val < heap[0]` and heap is full, we push and pop, which is effectively a no-op on the heap's content. `heappushpop` handles this in one call but still correct either way.
- **Alternative:** Could use `heappushpop` when heap is already at size k for a slight speedup.

### Follow-up Variations

- **Kth smallest in a stream** — use a max heap of size k (negate values in Python).
- **Median in a stream** (LeetCode 295) — use two heaps (max heap + min heap).
- **Top K elements in a stream** — return all k elements from the heap, not just the root.

### ⚠️ Common Traps

- **Not trimming the initial heap to size k.** If the initial array has more than k elements, you must pop extras during initialization.
- **Returning `heap[-1]` instead of `heap[0]`.** The root of a min heap is at index 0.
- **Forgetting that fewer than k elements may exist early on.** The problem guarantees valid calls, but in a real interview, clarify this.
