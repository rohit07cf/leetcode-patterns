# Wiggle Sort II

**Difficulty:** Medium
**Pattern:** Sorting
**Subpattern:** Quick Sort / Partition
**Link:** https://leetcode.com/problems/wiggle-sort-ii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3] > nums[4] < ...`. This is a **strict** inequality — equal adjacent elements are not allowed.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 5 * 10^4`, `0 <= nums[i] <= 5000`
- **Edge cases?** Two elements, many duplicates, all distinct, odd/even length
- **Expected output?** In-place reordering satisfying the wiggle property
- **Can input be modified?** Yes, must reorder in-place

### 3. Brute Force Approach

- **Idea:** Sort the array, then interleave the smaller half and larger half into odd/even positions.
- **Time:** O(n log n)
- **Space:** O(n)

### 4. Optimized Approach

- **💡 Core Insight:** Find the **median** using quickselect in O(n), then use **3-way partitioning with index mapping** to place elements smaller than median at even indices (from the right) and larger at odd indices (from the left). The index mapping `(2*i + 1) % (n | 1)` distributes elements to prevent equal adjacent values.

- **Time:** O(n) average
- **Space:** O(n) for the practical solution (O(1) with virtual indexing, but very tricky)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort + interleave | O(n log n) | O(n) | Simple, reliable |
| Quickselect + 3-way | O(n) avg | O(n) | Optimal time |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Sort-based approach** (recommended for interviews — clean, easy to explain):
  1. Sort the array
  2. Split into two halves: small (first half) and large (second half)
  3. **Reverse both halves** — this prevents duplicates from being adjacent
  4. Interleave: place small values at even indices, large at odd indices

```python
class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        sorted_nums = sorted(nums)
        n = len(nums)

        # Split into small and large halves
        # For odd n: small gets one extra element
        mid = (n - 1) // 2
        small = sorted_nums[:mid + 1]
        large = sorted_nums[mid + 1:]

        # Reverse both halves — critical to separate duplicates near the median
        small.reverse()
        large.reverse()

        # Interleave: small at even indices, large at odd indices
        for i in range(len(small)):
            nums[2 * i] = small[i]
        for i in range(len(large)):
            nums[2 * i + 1] = large[i]
```

**Optimal O(n) with Quickselect (advanced):**

```python
import random

class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        n = len(nums)

        # Step 1: Find median using quickselect
        median = self._quickselect(nums[:], n // 2)

        # Step 2: Index mapping — maps virtual index to actual index
        # Places larger values at odd indices, smaller at even indices
        def mapped(i):
            return (2 * i + 1) % (n | 1)

        # Step 3: 3-way partition using mapped indices
        lt, i, gt = 0, 0, n - 1
        while i <= gt:
            if nums[mapped(i)] > median:
                nums[mapped(lt)], nums[mapped(i)] = nums[mapped(i)], nums[mapped(lt)]
                lt += 1
                i += 1
            elif nums[mapped(i)] < median:
                nums[mapped(i)], nums[mapped(gt)] = nums[mapped(gt)], nums[mapped(i)]
                gt -= 1
            else:
                i += 1

    def _quickselect(self, nums, k):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            pivot = nums[random.randint(lo, hi)]
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
            if lt <= k <= gt:
                return pivot
            elif k < lt:
                hi = lt - 1
            else:
                lo = gt + 1
        return -1
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `[1, 5, 1, 1, 6, 4]`

**Sort-based approach:**
1. Sorted: `[1, 1, 1, 4, 5, 6]`
2. mid = 2, small = `[1, 1, 1]`, large = `[4, 5, 6]`
3. Reversed: small = `[1, 1, 1]`, large = `[6, 5, 4]`
4. Interleave: `[1, 6, 1, 5, 1, 4]`
5. Check: `1 < 6 > 1 < 5 > 1 < 4` -> valid

### Edge Case Testing

- **Empty input:** Constraint says `n >= 1`, not applicable
- **Single element:** `[1]` -> no change needed, trivially valid
- **Typical case:** `[1,5,1,1,6,4]` -> `[1,6,1,5,1,4]`
- **Extreme values:** `[1,1,2,2]` -> `[1,2,1,2]` (reversing halves prevents `[1,1,2,2]` -> `[1,2,1,2]`)

### Complexity

- **Time:** O(n log n) for sort-based; O(n) average for quickselect-based
- **Space:** O(n) — need copy of array for interleaving

### Optimization Discussion

- The sort-based approach is **strongly recommended** for interviews — it's clean, correct, and easy to explain
- The O(n) virtual-index approach is a famous puzzle but extremely hard to get right under pressure
- The **key trick** of reversing halves prevents duplicates near the median from being adjacent

### Follow-up Variations

- Wiggle Sort I (non-strict: `<=` and `>=`) — much simpler, single pass with adjacent swaps
- Check if a wiggle sort arrangement exists
- Wiggle subsequence (DP problem, different category)

### Common Traps

- **Not reversing the halves** — `[4,5,5,6]` split into `[4,5]` and `[5,6]` gives `[4,5,5,6]` -> `5 == 5` violates strict inequality. Reversing gives `[5,4]` and `[6,5]` -> `[5,6,4,5]`
- **Wrong split point for odd-length arrays** — small half should get the extra element (ceil division)
- **Strict vs. non-strict inequality** — Wiggle Sort II requires `<` and `>`, not `<=` and `>=`
- **Virtual index mapping is error-prone** — `(2*i+1) % (n|1)` is a non-obvious formula; avoid in interviews unless asked
