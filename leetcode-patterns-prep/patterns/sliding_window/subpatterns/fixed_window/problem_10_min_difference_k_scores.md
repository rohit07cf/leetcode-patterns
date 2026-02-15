# Minimum Difference Between Highest and Lowest of K Scores

**Difficulty:** Easy
**Pattern:** Sliding Window
**Subpattern:** Fixed Window
**Link:** https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array `nums` of student scores and an integer `k`, pick any `k` scores from the array. Return the **minimum possible difference** between the highest and lowest of the chosen `k` scores.

### 2. Clarification Questions

- **Input constraints?** `1 <= k <= nums.length <= 1000`. `0 <= nums[i] <= 10^5`.
- **Edge cases?** `k = 1` (difference is always 0). `k = n` (must use all scores). All identical scores.
- **Expected output?** An integer — the minimum difference.
- **Can input be modified?** Yes — **sorting is the key step**.

### 3. Brute Force Approach

- **Idea:** Check all combinations of k elements using `C(n, k)`, find min(max - min) for each.
- **Time:** O(C(n, k) * k) — exponential for large n.
- **Space:** O(k)

### 4. Optimized Approach

- **Core Insight:** After **sorting** the array, the optimal k elements are always **consecutive** in the sorted order. Why? Any gap between chosen elements would widen the range unnecessarily. So the answer is `min(nums[i + k - 1] - nums[i])` over all valid i.

  This transforms the problem into a **fixed-size sliding window on a sorted array**.

- **Time:** O(n log n) — dominated by sorting.
- **Space:** O(1) — ignoring sort space.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (combinations) | O(C(n,k) * k) | O(k) | Infeasible |
| Sort + sliding window | O(n log n) | O(1) | Optimal |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort the array.
- Slide a window of size k: the difference is `nums[i + k - 1] - nums[i]`.
- Track the minimum difference.

```python
def minimumDifference(nums, k):
    if k == 1:
        return 0

    nums.sort()  # consecutive elements minimize the range
    min_diff = float('inf')

    # Slide window of size k over sorted array
    for i in range(len(nums) - k + 1):
        diff = nums[i + k - 1] - nums[i]  # max - min in this window
        min_diff = min(min_diff, diff)

    return min_diff
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [9, 4, 1, 7], k = 2`

**After sorting:** `[1, 4, 7, 9]`

| i | Window | Diff | Min Diff |
|---|--------|------|----------|
| 0 | [1, 4] | 3 | 3 |
| 1 | [4, 7] | 3 | 3 |
| 2 | [7, 9] | 2 | 2 |

**Output:** `2`

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `k = 1` returns 0 (early return).
- **Typical case:** Covered in dry run.
- **Extreme values:** All same values returns 0. `k = n` returns `nums[-1] - nums[0]` after sorting.

### Complexity

- **Time:** O(n log n) — sorting dominates. The sliding window pass is O(n).
- **Space:** O(1) — in-place sort (Python's Timsort uses O(n) auxiliary space internally, but no extra data structures).

### Optimization Discussion

The sorting step is the bottleneck. The sliding window itself is O(n). For this problem's constraints (n <= 1000), even O(n^2) would work, but the sort + window approach is cleaner and scalable.

**Why consecutive elements in sorted order?** Suppose you pick elements `a <= b <= ... <= c` where some sorted elements between a and c are skipped. Replacing a skipped element with the one that was skipped would keep max - min the same or reduce it. So the optimal set is always contiguous after sorting.

### Follow-up Variations

- **Maximum difference** of k scores (trivially: pick the k largest minus k smallest, but actually just `nums[-1] - nums[0]` if k >= 2).
- What if you must pick k scores from **different students** (each student has multiple scores)?
- **Minimum range covering elements from k lists** (LC 632 — much harder).

### Common Traps

- **Forgetting to sort.** The sliding window only works on sorted data. Without sorting, consecutive elements don't minimize the range.
- **Off-by-one in window boundary.** In a window starting at `i` with k elements, the last element is at `i + k - 1`, not `i + k`.
- **Not handling k = 1.** When k = 1, the difference is always 0. The loop still works (every window has size 1, diff = 0), but an early return is cleaner.
