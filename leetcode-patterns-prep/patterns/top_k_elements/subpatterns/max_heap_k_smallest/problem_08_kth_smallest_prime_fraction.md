# K-th Smallest Prime Fraction

**Difficulty:** Medium
**Pattern:** Top K Elements
**Subpattern:** Max Heap for K Smallest
**Link:** https://leetcode.com/problems/k-th-smallest-prime-fraction/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a sorted array `arr` of 1 and prime numbers, consider all fractions `arr[i] / arr[j]` where `i < j`. Return the kth smallest fraction as `[arr[i], arr[j]]`.

### 2. Clarification Questions

- **Input constraints?** 2 <= n <= 1000, 1 <= arr[i] <= 3 * 10^4, arr[0] = 1, arr is sorted and contains only 1 and primes.
- **Edge cases?** k = 1 (smallest fraction), k = n*(n-1)/2 (largest fraction < 1), n = 2.
- **Expected output?** A list `[arr[i], arr[j]]` representing numerator and denominator.
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Generate all O(n^2) fractions, sort them, return the kth.
- **Time:** O(n^2 log n)
- **Space:** O(n^2)

### 4. Optimized Approach

- 💡 **Core Insight:** Think of the fractions as k sorted lists. For a fixed denominator `arr[j]`, the fractions `arr[0]/arr[j], arr[1]/arr[j], ...` are already sorted (numerator increases). Use a **min heap of size n** to do a k-way merge across these "columns." Start with the smallest fraction from each denominator column and pop k times.
- **Time:** O(k log n)
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Generate all + sort | O(n^2 log n) | O(n^2) | Simple but slow |
| Min heap k-way merge | O(k log n) | O(n) | Efficient, heap-based |
| Binary search on value | O(n log(max_val)) | O(1) | Also optimal |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- For each denominator `arr[j]` (j from 1 to n-1), the smallest fraction is `arr[0] / arr[j]`.
- Seed heap with these n-1 fractions.
- Pop k-1 times, each time pushing the next fraction from that denominator's column.
- The kth pop is the answer.

```python
import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        # Heap: (fraction_value, numerator_index, denominator_index)
        # Start with smallest fraction for each denominator
        heap = [(arr[0] / arr[j], 0, j) for j in range(1, n)]
        heapq.heapify(heap)

        for _ in range(k):
            frac, i, j = heapq.heappop(heap)
            # Push next fraction from same denominator column
            if i + 1 < j:  # Numerator index must stay < denominator index
                heapq.heappush(heap, (arr[i + 1] / arr[j], i + 1, j))

        return [arr[i], arr[j]]
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`arr = [1, 2, 3, 5]`, k = 3

All fractions sorted: 1/5=0.2, 1/3=0.33, 2/5=0.4, 1/2=0.5, 3/5=0.6, 2/3=0.67

- Heap init: [(1/5,0,3), (1/3,0,2), (1/2,0,1)]
- Pop 1 (1/5, 0, 3): push (2/5, 1, 3) → heap: [(1/3,0,2), (1/2,0,1), (2/5,1,3)]
- Pop 2 (1/3, 0, 2): push (2/3, 1, 2) → heap: [(2/5,1,3), (1/2,0,1), (2/3,1,2)]
- Pop 3 (2/5, 1, 3): → answer = **[2, 5]** ✓

### Edge Case Testing

- **Empty input:** Not possible (n >= 2).
- **Single element:** n = 2 → one fraction: arr[0]/arr[1], k must be 1.
- **Typical case:** Mixed primes, pop k times — works as shown.
- **Extreme values:** Large n = 1000, k = n*(n-1)/2 → worst case O(n^2 log n) pops, but usually k is much smaller.

### Complexity

- **Time:** O(k log n) — k pops from a heap of size at most n.
- **Space:** O(n) — heap stores at most n-1 entries.

### Optimization Discussion

**Binary search on fraction value:** Binary search on a value `mid` in [0, 1]. For each `mid`, count how many fractions are <= `mid` using a two-pointer technique on the sorted array. This achieves O(n log(1/epsilon)) but requires careful handling to identify the exact fraction.

### Follow-up Variations

- **Kth Smallest Pair Distance (LC 719)** — binary search on distance instead of fraction.
- **Find K Pairs with Smallest Sums (LC 373)** — same k-way merge pattern with two sorted arrays.

### ⚠️ Common Traps

- **Floating point comparison** — using float division in heap is acceptable here since we return indices, not the float value. But be aware of precision issues in other contexts.
- **Index constraint i < j** — numerator index must be strictly less than denominator index; don't push invalid pairs.
- **Off-by-one in k** — pop exactly k times; the last popped pair is the answer.
