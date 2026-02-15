# Kth Largest Element in an Array

**Difficulty:** Medium
**Pattern:** Top K Elements
**Subpattern:** Min Heap of Size K
**Link:** https://leetcode.com/problems/kth-largest-element-in-an-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums` and an integer `k`, return the **kth largest** element in the array. This is the kth largest in sorted order, not the kth distinct element.

### 2. Clarification Questions

- **Input constraints?** `1 <= k <= nums.length <= 10^5`, elements in range `[-10^4, 10^4]`.
- **Edge cases?** Array with all identical elements; `k = 1` (max); `k = len(nums)` (min).
- **Expected output?** A single integer — the kth largest value.
- **Can input be modified?** Yes, in-place modification is acceptable.

### 3. Brute Force Approach

- **Idea:** Sort the entire array in descending order and return the element at index `k - 1`.
- **Time:** O(n log n)
- **Space:** O(1) if sorting in-place

### 4. Optimized Approach

- 💡 **Core Insight:** Maintain a **min heap of size k**. The heap's root is always the kth largest element seen so far. Any element smaller than the root can't be in the top k, so we discard it.
- **Time:** O(n log k)
- **Space:** O(k)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (sort) | O(n log n) | O(1) | Simple but processes all elements fully |
| Min Heap of size k | O(n log k) | O(k) | **Optimal when k << n** |
| Quickselect | O(n) avg | O(1) | Fastest average but O(n^2) worst case |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Build a min heap from the first `k` elements.
- For each remaining element, if it's larger than the heap root, replace the root and heapify.
- The root of the heap at the end is the kth largest.

```python
import heapq

def findKthLargest(nums, k):
    # Min heap keeps the k largest elements seen so far
    heap = nums[:k]
    heapq.heapify(heap)  # O(k) to build initial heap

    for num in nums[k:]:
        if num > heap[0]:
            # Replace root (smallest of top-k) with larger candidate
            heapq.heapreplace(heap, num)

    # Root of min heap = kth largest overall
    return heap[0]
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums = [3, 2, 1, 5, 6, 4], k = 2`

1. Initial heap from first 2: `[2, 3]` (min heap)
2. Process `1`: `1 < 2` — skip
3. Process `5`: `5 > 2` — replace → `[3, 5]`
4. Process `6`: `6 > 3` — replace → `[5, 6]`
5. Process `4`: `4 < 5` — skip
6. Return `heap[0] = 5` ✓ (2nd largest is 5)

### Edge Case Testing

- **Empty input:** Not possible per constraints (`k >= 1`, `len >= 1`).
- **Single element:** `k = 1`, heap = `[element]`, return it directly.
- **Typical case:** Covered in dry run above.
- **Extreme values:** All same values → heap stays constant, returns that value.

### Complexity

- **Time:** O(n log k) — each of the n elements may trigger a heap operation costing O(log k).
- **Space:** O(k) — heap stores exactly k elements.

### Optimization Discussion

- **Quickselect** gives O(n) average time but O(n^2) worst case. The heap approach is more predictable.
- **`heapq.nlargest(k, nums)`** is a clean one-liner that internally uses a similar min-heap strategy.
- For streaming data, the heap approach naturally extends — Quickselect does not.

### Follow-up Variations

- What if the array is a **stream**? → See Problem 5 (Kth Largest in a Stream).
- What if you need the **kth smallest**? → Use a max heap of size k (negate values in Python).
- Can you solve it in O(n) guaranteed? → Median-of-medians Quickselect.

### ⚠️ Common Traps

- **Using a max heap instead of min heap.** A max heap would require storing all n elements. The min heap of size k keeps only the top-k, with the root being the answer.
- **Off-by-one with k.** The kth largest is `heap[0]`, not `heap[k-1]`.
- **Forgetting `heapreplace` vs `heappush`/`heappop`.** `heapreplace` is a single O(log k) operation; doing push then pop is two operations (though `heappushpop` also works).
