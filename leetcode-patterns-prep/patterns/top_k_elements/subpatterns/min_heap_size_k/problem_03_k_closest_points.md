# K Closest Points to Origin

**Difficulty:** Medium
**Pattern:** Top K Elements
**Subpattern:** Min Heap of Size K
**Link:** https://leetcode.com/problems/k-closest-points-to-origin/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of points on a 2D plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`. Distance is Euclidean, and the answer may be in any order.

### 2. Clarification Questions

- **Input constraints?** `1 <= k <= points.length <= 10^4`, coordinates in range `[-10^4, 10^4]`.
- **Edge cases?** Multiple points at the same distance; `k = n` (return all); point at origin.
- **Expected output?** A list of `k` coordinate pairs, any order.
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Compute the distance for every point, sort all points by distance, return the first `k`.
- **Time:** O(n log n)
- **Space:** O(n)

### 4. Optimized Approach

- 💡 **Core Insight:** Use a **max heap of size k** (simulated via negated distances in Python's min heap). The heap holds the k closest points seen so far. If a new point is closer than the farthest in our heap, swap it in. This is the "min heap of size k" pattern applied inversely — we keep the **k smallest** distances by evicting the **largest** among our k candidates.
- **Time:** O(n log k)
- **Space:** O(k)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort all | O(n log n) | O(n) | Simple, processes everything |
| Max Heap of size k | O(n log k) | O(k) | **Better when k << n** |
| Quickselect | O(n) avg | O(1) | Fastest average, O(n^2) worst |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Compute squared distance (avoid sqrt — it doesn't affect ordering).
- Use a max heap of size k by **negating** the distance (Python only has min heap).
- For each point, if heap has fewer than k elements or point is closer than the farthest in heap, update.

```python
import heapq

def kClosest(points, k):
    # Max heap of size k (negate distance for max-heap behavior)
    heap = []

    for x, y in points:
        dist = -(x * x + y * y)  # Negate for max heap
        if len(heap) < k:
            heapq.heappush(heap, (dist, x, y))
        elif dist > heap[0][0]:
            # This point is closer than the farthest in our top-k
            heapq.heapreplace(heap, (dist, x, y))

    return [[x, y] for _, x, y in heap]
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`points = [[1,3],[-2,2],[5,8],[0,1]], k = 2`

Squared distances: `[10, 8, 89, 1]`

1. `(1,3)` dist=10 → heap: `[(-10,1,3)]`
2. `(-2,2)` dist=8 → heap: `[(-10,1,3),(-8,-2,2)]` (size < k, push)
3. `(5,8)` dist=89 → `-89 < -10` → skip (farther than farthest)
4. `(0,1)` dist=1 → `-1 > -10` → replace → heap: `[(-8,-2,2),(-1,0,1)]`
5. Return `[[-2,2],[0,1]]` ✓

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `k = 1`, one push, return it.
- **Typical case:** Covered in dry run.
- **Extreme values:** Points at origin have distance 0 — always closest, always kept.

### Complexity

- **Time:** O(n log k) — each of n points may trigger an O(log k) heap operation.
- **Space:** O(k) — heap stores exactly k points.

### Optimization Discussion

- **Squared distance** avoids floating-point imprecision from `sqrt`. Since we only compare, monotonicity is preserved.
- **Quickselect** partitions around the kth distance in O(n) average, but worst-case O(n^2).
- **`heapq.nsmallest`:** `heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)` is a clean alternative.

### Follow-up Variations

- **K farthest points from origin** — use a min heap of size k directly (no negation needed).
- **Closest to an arbitrary point** — adjust distance formula to `(x - px)^2 + (y - py)^2`.
- **Streaming points** — the heap approach naturally extends to online data.

### ⚠️ Common Traps

- **Using `sqrt` unnecessarily.** Squared distances preserve order and avoid float issues.
- **Confusing min heap vs max heap direction.** We want the k **smallest** distances, so we use a **max** heap to evict the largest among candidates.
- **Forgetting to negate distances.** Python's `heapq` is a min heap; negate values to simulate a max heap.
