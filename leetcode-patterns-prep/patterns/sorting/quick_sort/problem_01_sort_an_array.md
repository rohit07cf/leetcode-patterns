# Sort an Array

**Difficulty:** Medium
**Pattern:** Sorting
**Subpattern:** Quick Sort / Partition
**Link:** https://leetcode.com/problems/sort-an-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of integers `nums`, sort the array in ascending order and return it. You must solve it **without using built-in sort functions** with O(n log n) average time complexity.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 5 * 10^4`, `-5 * 10^4 <= nums[i] <= 5 * 10^4`
- **Edge cases?** Already sorted, reverse sorted, all duplicates, single element
- **Expected output?** The same array sorted in non-decreasing order
- **Can input be modified?** Yes, in-place sorting is acceptable

### 3. Brute Force Approach

- **Idea:** Selection sort — repeatedly find the minimum and place it at the front.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach

- **💡 Core Insight:** Quick sort uses a **pivot** to partition the array into elements less than, equal to, and greater than the pivot, then recursively sorts the sub-arrays. **Randomized pivot selection** avoids worst-case O(n^2) on sorted inputs. **3-way partition** handles duplicates efficiently.

- **Time:** O(n log n) average
- **Space:** O(log n) — recursion stack

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Selection Sort | O(n^2) | O(1) | Too slow for n = 50k |
| Merge Sort | O(n log n) | O(n) | Guaranteed but uses extra space |
| Quick Sort (randomized) | O(n log n) avg | O(log n) | In-place, cache-friendly |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Pick a **random pivot** to avoid worst-case on sorted/nearly-sorted inputs
- Use **3-way partitioning** (Dutch National Flag) to handle duplicates — elements equal to pivot don't recurse
- Recurse on the "less than" and "greater than" partitions only

```python
import random

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self._quicksort(nums, 0, len(nums) - 1)
        return nums

    def _quicksort(self, nums, lo, hi):
        if lo >= hi:
            return

        # Randomized pivot avoids O(n^2) on sorted input
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
                gt -= 1  # Don't advance i — swapped element needs checking
            else:
                i += 1  # nums[i] == pivot, just advance

        # Recurse on partitions that exclude the equal-to-pivot region
        self._quicksort(nums, lo, lt - 1)
        self._quicksort(nums, gt + 1, hi)
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Input: `[5, 2, 3, 1]`

1. Random pivot = `3`, partition: `[2, 1] [3] [5]`
2. Recurse left `[2, 1]` -> pivot `1`, partition: `[] [1] [2]` -> `[1, 2]`
3. Right `[5]` -> base case
4. Result: `[1, 2, 3, 5]`

### Edge Case Testing

- **Empty input:** Constraint says `n >= 1`, not applicable
- **Single element:** `lo >= hi`, returns immediately -> `[x]`
- **Typical case:** `[5,2,3,1]` -> `[1,2,3,5]`
- **Extreme values:** All duplicates `[2,2,2]` -> 3-way partition handles it in O(n), no unnecessary recursion

### Complexity

- **Time:** O(n log n) average — each partition splits roughly in half with random pivot; O(n^2) worst case is astronomically unlikely with randomization
- **Space:** O(log n) — recursion depth is O(log n) on average

### Optimization Discussion

- **3-way partition** is critical for LeetCode test cases with many duplicates — without it, arrays like `[2,2,2,...,2]` degrade to O(n^2)
- **Introsort** (switch to heapsort after recursion depth exceeds 2*log n) guarantees O(n log n) worst case
- Merge sort guarantees O(n log n) but uses O(n) space

### Follow-up Variations

- Sort in descending order (flip comparison)
- Sort a linked list (merge sort preferred — no random access)
- External sort for data that doesn't fit in memory

### Common Traps

- **Not randomizing pivot** — LeetCode has adversarial test cases that cause TLE with fixed pivot (first/last element)
- **2-way partition with many duplicates** — causes O(n^2) because equal elements all go to one side
- **Forgetting `gt -= 1` without advancing `i`** — the swapped element from the right hasn't been inspected yet
