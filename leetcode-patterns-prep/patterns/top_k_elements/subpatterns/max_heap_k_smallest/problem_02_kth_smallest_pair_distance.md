# Find K-th Smallest Pair Distance

**Difficulty:** Hard
**Pattern:** Top K Elements
**Subpattern:** Max Heap for K Smallest
**Link:** https://leetcode.com/problems/find-k-th-smallest-pair-distance/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums` and an integer `k`, return the kth smallest **distance** among all pairs `(nums[i], nums[j])` where `i < j`. The distance is `|nums[i] - nums[j]|`.

### 2. Clarification Questions

- **Input constraints?** 2 <= n <= 10^4, 0 <= nums[i] <= 10^6, 1 <= k <= n*(n-1)/2.
- **Edge cases?** All elements identical (all distances = 0), k = 1 (smallest distance), two elements.
- **Expected output?** A single integer — the kth smallest pair distance.
- **Can input be modified?** Yes, sorting is allowed.

### 3. Brute Force Approach

- **Idea:** Compute all O(n^2) pair distances, sort them, return the kth.
- **Time:** O(n^2 log n)
- **Space:** O(n^2)

### 4. Optimized Approach

- 💡 **Core Insight:** **Binary search on the answer.** Sort the array. For a candidate distance `mid`, count how many pairs have distance <= `mid` using a two-pointer sliding window. If count >= k, search lower; otherwise search higher. This avoids materializing all pairs.
- **Time:** O(n log n + n log W) where W = max(nums) - min(nums)
- **Space:** O(1) extra (beyond sorting)

**Max heap alternative** (demonstrates subpattern): Use a max heap of size k to track the k smallest distances — but this is O(n^2 log k) which is too slow for n = 10^4. The binary search approach is the interview-expected solution.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2 log n) | O(n^2) | TLE for large n |
| Max Heap size k | O(n^2 log k) | O(k) | Subpattern demo, still O(n^2) |
| Binary Search + Two Pointer | O(n log n + n log W) | O(1) | Optimal, interview standard |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort the array so that pair distances between adjacent elements are ordered.
- Binary search on the distance value `mid` in range `[0, max - min]`.
- For each `mid`, count pairs with distance <= `mid` using a sliding window.
- Narrow the search until we find the exact kth smallest distance.

```python
class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        n = len(nums)

        def count_pairs_within(dist):
            """Count pairs with distance <= dist using two pointers."""
            count = 0
            left = 0
            for right in range(n):
                # Shrink window until distance fits
                while nums[right] - nums[left] > dist:
                    left += 1
                # All pairs (left..right-1, right) have distance <= dist
                count += right - left
            return count

        lo, hi = 0, nums[-1] - nums[0]

        while lo < hi:
            mid = (lo + hi) // 2
            if count_pairs_within(mid) >= k:
                hi = mid  # Answer could be mid or smaller
            else:
                lo = mid + 1  # Need a larger distance

        return lo
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums = [1, 3, 1]`, k = 1

- Sorted: `[1, 1, 3]`
- All distances: |1-1|=0, |1-3|=2, |1-3|=2 → sorted: [0, 2, 2]
- Binary search: lo=0, hi=2
  - mid=1: count_pairs_within(1) → pairs: (1,1)=0 → count=1 → 1 >= 1 → hi=1
  - mid=0: count_pairs_within(0) → pairs: (1,1)=0 → count=1 → 1 >= 1 → hi=0
- lo == hi == 0 → return **0** ✓

### Edge Case Testing

- **Empty input:** Not possible per constraints (n >= 2).
- **Single element:** Not possible (n >= 2).
- **Typical case:** Mixed values, binary search converges in O(log W) steps.
- **Extreme values:** All elements the same → all distances = 0, answer is 0.

### Complexity

- **Time:** O(n log n + n log W) — sorting + binary search with O(n) counting per step.
- **Space:** O(1) — in-place sort (or O(n) depending on sort implementation).

### Optimization Discussion

A bucket sort approach is also possible when W is small: create W+1 buckets, count pairs in each bucket, and find the kth. This gives O(n + W) time.

### Follow-up Variations

- Find the kth **largest** pair distance → binary search from the other end.
- Find all pairs with distance exactly equal to k → two-pointer after sorting.

### ⚠️ Common Traps

- **Off-by-one in binary search** — using `lo <= hi` with wrong update logic leads to infinite loops. Use the `lo < hi` pattern with `hi = mid`.
- **Forgetting to sort** — the two-pointer counting only works on a sorted array.
- **Double counting** — each pair (i, j) with i < j should be counted once, not twice.
