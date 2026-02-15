# K Closest Points to Origin

**Difficulty:** Medium
**Pattern:** Sorting
**Subpattern:** Quick Sort / Partition
**Link:** https://leetcode.com/problems/k-closest-points-to-origin/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of `points` where `points[i] = [x, y]` represents a point on the XY-plane, return the `k` closest points to the origin `(0, 0)`. Distance is Euclidean. The answer may be in **any order** and is guaranteed to be unique (no ties at the kth boundary).

### 2. Clarification Questions

- **Input constraints?** `1 <= k <= points.length <= 10^4`, `-10^4 <= x, y <= 10^4`
- **Edge cases?** k = n (return all), k = 1 (closest single point), points at same distance
- **Expected output?** List of k points (any order)
- **Can input be modified?** Yes

### 3. Brute Force Approach

- **Idea:** Compute distance for each point, sort by distance, return first k.
- **Time:** O(n log n)
- **Space:** O(n)

### 4. Optimized Approach

- **💡 Core Insight:** Use **quickselect** to partition points by distance so that the k closest end up on one side — **no need to fully sort**. Compare squared distances to avoid floating point (sqrt is monotonic, so ranking is preserved).

- **Time:** O(n) average
- **Space:** O(1) extra (modifies input array)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort all points | O(n log n) | O(n) | Simple |
| Max-heap of size k | O(n log k) | O(k) | Good for streaming |
| **Quickselect** | **O(n) avg** | **O(1)** | Optimal for this problem |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Define a distance function using **squared distance** (avoid sqrt)
- Apply quickselect to partially sort so the k closest are at indices `[0:k]`
- Use 3-way partition with randomized pivot for robustness

```python
import random

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def dist(point):
            # Squared distance — no sqrt needed for comparison
            return point[0] ** 2 + point[1] ** 2

        # Quickselect: put k closest at indices [0:k]
        lo, hi = 0, len(points) - 1
        while lo <= hi:
            pivot_idx = random.randint(lo, hi)
            pivot_dist = dist(points[pivot_idx])

            # 3-way partition by distance
            lt, i, gt = lo, lo, hi
            while i <= gt:
                d = dist(points[i])
                if d < pivot_dist:
                    points[lt], points[i] = points[i], points[lt]
                    lt += 1
                    i += 1
                elif d > pivot_dist:
                    points[i], points[gt] = points[gt], points[i]
                    gt -= 1
                else:
                    i += 1

            # Check if k falls within or before the equal zone
            if k <= lt:
                # All k closest are strictly less than pivot
                hi = lt - 1
            elif k <= gt + 1:
                # k-th boundary is within the equal zone — done
                break
            else:
                # Need more points from the right
                lo = gt + 1

        return points[:k]
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `points = [[3,3],[5,-1],[-2,4]]`, `k = 2`

1. Distances: `[18, 26, 20]`
2. Suppose pivot = point `[-2,4]` (dist=20)
3. Partition: `[3,3]` (18 < 20) | `[-2,4]` (20 == 20) | `[5,-1]` (26 > 20)
4. lt=1, gt=1, k=2 -> `k <= gt + 1` (2 <= 2) -> break
5. Return `points[:2] = [[3,3], [-2,4]]`

### Edge Case Testing

- **Empty input:** Constraint says `n >= 1`, not applicable
- **Single element:** `k=1`, one point -> return it directly
- **Typical case:** `[[1,3],[-2,2]]`, k=1 -> `[[-2,2]]` (dist 8 vs 10)
- **Extreme values:** k = n -> return all points (quickselect exits immediately)

### Complexity

- **Time:** O(n) average — quickselect processes shrinking partitions, geometric series
- **Space:** O(1) extra — partitions the input array in-place

### Optimization Discussion

- **Squared distance comparison** avoids floating-point errors and sqrt overhead
- For **streaming** input (points arriving one at a time), use a **max-heap of size k**
- If k is very close to n, sorting may actually be simpler

### Follow-up Variations

- K farthest points from origin (quickselect with reversed comparison)
- Closest points to an arbitrary point `(a, b)` — adjust distance function
- K closest with a distance threshold (filter first, then select)
- Find the kth closest distance value (quickselect on distances, return the value)

### Common Traps

- **Using sqrt for distance** — unnecessary and introduces floating-point imprecision; squared distance preserves order
- **Wrong quickselect boundary check** — `k` is a count (1-indexed), but array indices are 0-indexed; target index is `k-1` but we want `points[:k]`
- **Not handling the "equal zone" correctly** — if multiple points have the same distance as the pivot, they all belong together
- **Forgetting randomized pivot** — deterministic pivot can degrade to O(n^2) on adversarial inputs
