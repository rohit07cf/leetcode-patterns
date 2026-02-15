# Kth Smallest Element in a Sorted Matrix

**Difficulty:** Medium
**Pattern:** Top K Elements
**Subpattern:** Min Heap of Size K
**Link:** https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an `n x n` matrix where each row and each column is sorted in ascending order, return the **kth smallest** element in the matrix.

### 2. Clarification Questions

- **Input constraints?** `n` up to 300, `1 <= k <= n^2`, values in range `[-10^9, 10^9]`.
- **Edge cases?** `k = 1` (top-left element); `k = n^2` (bottom-right element); `n = 1` (single element).
- **Expected output?** A single integer — the kth smallest value.
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Flatten the matrix into a list, sort it, return the element at index `k - 1`.
- **Time:** O(n^2 log n)
- **Space:** O(n^2)

### 4. Optimized Approach

- 💡 **Core Insight:** Treat each row as a sorted list. Use a **min heap** to perform a **k-way merge**. Start with the first element of each row. Pop the smallest, then push the next element from that same row. After k pops, we have the kth smallest.
- **Time:** O(k log n)
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Flatten + sort | O(n^2 log n) | O(n^2) | Ignores sorted structure |
| Min Heap (k-way merge) | O(k log n) | O(n) | **Leverages row-sorted property** |
| Binary Search | O(n log(max-min)) | O(1) | Best space, good for large k |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Seed the min heap with the first element from each row: `(value, row, col)`.
- Pop k times. Each pop gives the next smallest element.
- After popping `(val, r, c)`, push `(matrix[r][c+1], r, c+1)` if `c+1 < n`.

```python
import heapq

def kthSmallest(matrix, k):
    n = len(matrix)

    # Seed heap with first element of each row
    heap = [(matrix[r][0], r, 0) for r in range(min(n, k))]
    heapq.heapify(heap)

    # Pop k times to find kth smallest
    for _ in range(k):
        val, r, c = heapq.heappop(heap)

        if c + 1 < n:
            # Push next element from the same row
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

    return val
```

---

## PHASE 3 — AFTER CODING

### Dry Run

```
matrix = [[1,  5,  9],
          [10, 11, 13],
          [12, 13, 15]], k = 5
```

1. Heap seed: `[(1,0,0), (10,1,0), (12,2,0)]`
2. Pop `(1,0,0)` → push `(5,0,1)` → heap: `[(5,0,1),(10,1,0),(12,2,0)]`
3. Pop `(5,0,1)` → push `(9,0,2)` → heap: `[(9,0,2),(10,1,0),(12,2,0)]`
4. Pop `(9,0,2)` → col 3 out of bounds, no push → heap: `[(10,1,0),(12,2,0)]`
5. Pop `(10,1,0)` → push `(11,1,1)` → heap: `[(11,1,1),(12,2,0)]`
6. Pop `(11,1,1)` → **5th pop** → return `11` ✓

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `matrix = [[5]], k = 1` → seed `(5,0,0)`, pop once → return `5`.
- **Typical case:** Covered in dry run.
- **Extreme values:** `k = n^2` → pop all elements, return bottom-right corner value.

### Complexity

- **Time:** O(k log n) — k heap pops, each O(log n) since heap holds at most n entries.
- **Space:** O(n) — heap holds one element per row (at most n).

### Optimization Discussion

- **Binary Search approach:** Binary search on the value range `[matrix[0][0], matrix[n-1][n-1]]`. For each mid, count elements ≤ mid using the staircase property. O(n log(max-min)) time, O(1) space.
- **When k is close to n^2**, the binary search approach is better since it doesn't depend on k.
- **When k is small**, the heap approach is faster since O(k log n) < O(n log(max-min)).

### Follow-up Variations

- **Kth largest in a sorted matrix** — start from bottom-right, or use `k' = n^2 - k + 1` for the kth smallest.
- **Sorted matrix search** (LeetCode 240) — related staircase traversal technique.
- **K Pairs with Smallest Sums** (LeetCode 373) — similar k-way merge idea.

### ⚠️ Common Traps

- **Seeding the heap with all n^2 elements.** Only seed with the first column (one per row). The rest are discovered lazily.
- **Forgetting bounds check on `c + 1 < n`.** Pushing out-of-bounds indices crashes.
- **Using a max heap of size k.** While it works, a min heap with k-way merge is more natural here and leverages the sorted row structure.
