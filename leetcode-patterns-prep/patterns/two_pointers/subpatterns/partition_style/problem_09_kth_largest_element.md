# Kth Largest Element in an Array

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Partition Style
**Link:** https://leetcode.com/problems/kth-largest-element-in-an-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Find the **kth largest** element in an unsorted array. This is the element at index `n - k` if the array were sorted in ascending order. Solve **without fully sorting**.

### 2. Clarification Questions

- **Input constraints?** Array length 1–10⁵, values -10⁴ to 10⁴, 1 ≤ k ≤ n.
- **Edge cases?** k = 1 (max); k = n (min); duplicates; single element.
- **Expected output?** Return the kth largest integer.
- **Can input be modified?** Yes — in-place partition is expected.

### 3. Brute Force Approach

- **Idea:** Sort the array, return `nums[n - k]`.
- **Time:** O(n log n)
- **Space:** O(1) or O(n) depending on sort.

### 4. Optimized Approach

- 💡 **Core Insight:** Use **Quickselect** (Hoare's selection algorithm). Partition the array around a pivot — elements less than pivot go left, greater go right. If the pivot lands at index `n - k`, we're done. Otherwise, recurse into the relevant half. **Average case O(n)** using the partition subroutine.
- **Time:** O(n) average, O(n²) worst case.
- **Space:** O(1) iterative.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort | O(n log n) | O(1) | Simple, guaranteed |
| Min-heap of size k | O(n log k) | O(k) | Good when k << n |
| Quickselect | O(n) avg | O(1) | Fastest average case |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Lomuto partition:** Choose a pivot (last element). Walk through the array; elements ≤ pivot go to the left side. Return the final pivot position.
- **Quickselect:** Repeatedly partition, narrowing the search to the half containing index `n - k`.
- Randomize pivot choice to avoid O(n²) worst case.

```python
import random

def findKthLargest(nums: list[int], k: int) -> int:
    target_idx = len(nums) - k  # Index in sorted order

    def partition(left: int, right: int) -> int:
        """Lomuto partition: returns final pivot index."""
        # Randomize pivot to avoid worst case
        pivot_idx = random.randint(left, right)
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

        pivot = nums[right]
        store = left  # Write pointer for elements <= pivot

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1

        # Place pivot in its final position
        nums[store], nums[right] = nums[right], nums[store]
        return store

    left, right = 0, len(nums) - 1

    while left <= right:
        pivot_pos = partition(left, right)

        if pivot_pos == target_idx:
            return nums[pivot_pos]
        elif pivot_pos < target_idx:
            left = pivot_pos + 1  # Search right half
        else:
            right = pivot_pos - 1  # Search left half

    # Should never reach here given valid input
    return -1
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `nums = [3, 2, 1, 5, 6, 4]`, `k = 2` → target_idx = 4

**Iteration 1:** partition(0, 5), suppose pivot = 4 (after random swap to end).

Array partitioned: `[3, 2, 1, 4, 6, 5]` → pivot at index 3.

3 < 4 → search right: left = 4.

**Iteration 2:** partition(4, 5), suppose pivot = 5.

Array: `[3, 2, 1, 4, 5, 6]` → pivot at index 4.

4 == target_idx → return `nums[4]` = **5**.

### Edge Case Testing

- **Empty input:** Not possible (length ≥ 1, k ≥ 1).
- **Single element:** `[1], k=1` → target_idx=0, partition returns 0, return 1.
- **Typical case:** `[3,2,1,5,6,4], k=2` → 5.
- **Extreme values:** All duplicates `[3,3,3], k=2` → 3. k=n (minimum) works fine.

### Complexity

- **Time:** O(n) average — each partition halves the search space: n + n/2 + n/4 + ... = 2n. Worst case O(n²) if pivot is always min/max (mitigated by random pivot).
- **Space:** O(1) — iterative with in-place partitioning.

### Optimization Discussion

- **Random pivot** makes O(n²) extremely unlikely (probability decreases exponentially).
- **Median-of-medians** guarantees O(n) worst case but has a large constant factor — rarely used in practice.
- **Heap approach** (O(n log k)) is better when k is very small and you can't modify the input.

### Follow-up Variations

- **Kth Smallest Element** — change target_idx to `k - 1`.
- **Top K Frequent Elements (LC 347)** — quickselect on frequency counts.
- **Find Median from Data Stream (LC 295)** — two heaps.
- **Wiggle Sort II (LC 324)** — uses quickselect to find median.

### ⚠️ Common Traps

- **Confusing kth largest with kth smallest:** kth largest is at index `n - k` in sorted order, not `k - 1`.
- **Not randomizing pivot:** Without randomization, sorted/nearly-sorted input degrades to O(n²).
- **Off-by-one in Lomuto partition:** The `store` pointer must be initialized to `left`, not 0.
- **Advancing `mid` after swap with `right` in Lomuto:** In Lomuto, we iterate through `i` naturally — but remember the pivot swap at the end.
