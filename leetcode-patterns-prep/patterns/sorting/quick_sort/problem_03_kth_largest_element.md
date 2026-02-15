# Kth Largest Element in an Array

**Difficulty:** Medium
**Pattern:** Sorting
**Subpattern:** Quick Sort / Partition
**Link:** https://leetcode.com/problems/kth-largest-element-in-an-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums` and an integer `k`, return the **kth largest** element. This is the kth largest in **sorted order**, not the kth distinct element. You must solve it in O(n) average time.

### 2. Clarification Questions

- **Input constraints?** `1 <= k <= nums.length <= 10^5`, `-10^4 <= nums[i] <= 10^4`
- **Edge cases?** k=1 (max), k=n (min), all duplicates, single element
- **Expected output?** A single integer — the kth largest value
- **Can input be modified?** Yes, in-place modification is fine

### 3. Brute Force Approach

- **Idea:** Sort the array in descending order, return the element at index `k-1`.
- **Time:** O(n log n)
- **Space:** O(n) or O(log n) depending on sort

### 4. Optimized Approach

- **💡 Core Insight:** **Quickselect** — use the partition step of quick sort but only recurse into the half that contains the target index. The kth largest is at index `n - k` in a sorted array. After partitioning, if the pivot lands at `n - k`, we're done. Otherwise recurse into the relevant side only.

- **Time:** O(n) average
- **Space:** O(1) iterative

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Full sort | O(n log n) | O(log n) | Simple but overkill |
| Min-heap of size k | O(n log k) | O(k) | Good when k << n |
| **Quickselect** | **O(n) avg** | **O(1)** | Optimal average case |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Convert "kth largest" to target index: `target = len(nums) - k`
- Partition around a random pivot using Lomuto or 3-way scheme
- If pivot lands at target -> return it
- Otherwise narrow the search to the side containing target
- **Randomized pivot** is critical to avoid O(n^2) worst case

```python
import random

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        target = len(nums) - k  # kth largest = index (n-k) in sorted order

        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            # Randomized pivot to avoid worst-case
            pivot_idx = random.randint(lo, hi)
            pivot = nums[pivot_idx]

            # 3-way partition: [< pivot | == pivot | > pivot]
            lt, i, gt = lo, lo, hi
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            # Target is in the "equal" zone — we found it
            if lt <= target <= gt:
                return pivot

            # Narrow search to the side containing target
            if target < lt:
                hi = lt - 1
            else:
                lo = gt + 1

        return -1  # Should never reach here with valid input
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `nums = [3,2,1,5,6,4]`, `k = 2`

- `target = 6 - 2 = 4` (index 4 in sorted `[1,2,3,4,5,6]` is `5`)
- Suppose pivot = `4`, partition: `[3,2,1] [4] [5,6]`, lt=3, gt=3
- target=4 > gt=3, so `lo = 4`, search `[5,6]`
- Suppose pivot = `5`, partition: `[] [5] [6]`, lt=4, gt=4
- target=4, lt=4 <= 4 <= gt=4 -> return `5`

### Edge Case Testing

- **Empty input:** Constraint says `n >= 1`, not applicable
- **Single element:** `k=1`, target=0, pivot at index 0 -> return it
- **Typical case:** `[3,2,3,1,2,4,5,5,6]`, k=4 -> returns `4`
- **Extreme values:** All duplicates `[1,1,1]`, k=2 -> target=1, equal zone spans all -> return `1`

### Complexity

- **Time:** O(n) average — each iteration processes a shrinking partition; geometric series sums to O(n). Worst case O(n^2) but extremely unlikely with randomization.
- **Space:** O(1) — iterative implementation, only pointer variables

### Optimization Discussion

- **Median of medians** guarantees O(n) worst case but has a large constant factor — rarely used in practice
- **Heap approach** O(n log k) is better when k is very small and you can't modify the input
- **Introselect** (switch to median-of-medians after too many bad pivots) gives guaranteed O(n)

### Follow-up Variations

- Find kth smallest (use target = `k - 1` instead)
- Find median of an array (k = n/2)
- Find top-k elements (quickselect + partition gives all elements >= kth)
- Kth largest in a stream (use a min-heap of size k)

### Common Traps

- **Confusing "kth largest" with index** — kth largest is at index `n - k`, not `k - 1`
- **Not using randomized pivot** — LeetCode has adversarial inputs that cause TLE with deterministic pivot
- **Using 2-way partition with duplicates** — arrays like `[1,1,1,...,1]` cause O(n^2); 3-way partition collapses all equal elements in one step
- **Recursive quickselect blowing the stack** — iterative version is safer for large inputs
