# Count of Range Sum

**Difficulty:** Hard
**Pattern:** Sorting
**Subpattern:** Merge Sort
**Link:** https://leetcode.com/problems/count-of-range-sum/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums` and two integers `lower` and `upper`, return the number of range sums `sum(nums[i..j])` that lie within `[lower, upper]` inclusive, where `i <= j`.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 10^5`, `-2^31 <= nums[i] <= 2^31 - 1`, `-10^5 <= lower <= upper <= 10^5`.
- **Edge cases?** Single element, all zeros, all sums out of range, negative numbers.
- **Expected output?** A single integer count.
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Compute prefix sums, then check all pairs `(i, j)` to see if `prefix[j+1] - prefix[i]` falls in `[lower, upper]`.
- **Time:** O(n^2)
- **Space:** O(n) for prefix array

### 4. Optimized Approach

- **Core Insight:** A range sum `sum(i..j) = prefix[j+1] - prefix[i]`. We need to count pairs where `lower <= prefix[j] - prefix[i] <= upper` with `i < j`. During merge sort on the prefix array, for each element in the left half, use two pointers on the right half to find the range `[prefix_left + lower, prefix_left + upper]`. Both halves being sorted makes this a linear scan.
- **Time:** O(n log n)
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(n) | TLE for n = 10^5 |
| Merge Sort | O(n log n) | O(n) | Counting during merge, elegant |
| BIT / Segment Tree | O(n log n) | O(n) | Coordinate compression needed |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Build prefix sum array of length `n + 1` (with `prefix[0] = 0`).
- During merge sort, **before merging**, count valid pairs: for each `prefix[i]` in the left half, find how many `prefix[j]` in the right half satisfy `lower <= prefix[j] - prefix[i] <= upper`, i.e., `prefix[i] + lower <= prefix[j] <= prefix[i] + upper`.
- Use two pointers `lo_ptr` and `hi_ptr` on the sorted right half to find this window.

```python
class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        # Build prefix sums: prefix[j] - prefix[i] = sum(nums[i..j-1])
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        return self._merge_sort(prefix, 0, len(prefix) - 1, lower, upper)

    def _merge_sort(self, arr: list[int], lo: int, hi: int,
                    lower: int, upper: int) -> int:
        if lo >= hi:
            return 0

        mid = (lo + hi) // 2
        count = 0
        count += self._merge_sort(arr, lo, mid, lower, upper)
        count += self._merge_sort(arr, mid + 1, hi, lower, upper)

        # Count cross-half pairs before merging
        # For each left element, find right elements in [left + lower, left + upper]
        j_lo = mid + 1  # First right index where arr[j] >= arr[i] + lower
        j_hi = mid + 1  # First right index where arr[j] > arr[i] + upper

        for i in range(lo, mid + 1):
            while j_lo <= hi and arr[j_lo] < arr[i] + lower:
                j_lo += 1
            while j_hi <= hi and arr[j_hi] <= arr[i] + upper:
                j_hi += 1
            # Valid range: [j_lo, j_hi)
            count += (j_hi - j_lo)

        # Standard merge
        self._merge(arr, lo, mid, hi)
        return count

    def _merge(self, arr: list[int], lo: int, mid: int, hi: int) -> None:
        temp = []
        i, j = lo, mid + 1

        while i <= mid and j <= hi:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= hi:
            temp.append(arr[j])
            j += 1

        arr[lo:hi + 1] = temp
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [-2, 5, -1]`, `lower = -2`, `upper = 2`

Prefix: `[0, -2, 3, 2]`

We need pairs `(i, j)` where `i < j` and `-2 <= prefix[j] - prefix[i] <= 2`.

Valid range sums:
- `sum(0,0) = -2` (in range)
- `sum(2,2) = -1` (in range)
- `sum(0,2) = 2` (in range)

**Count = 3**

Merge sort traces through prefix `[0, -2, 3, 2]`, counting at each merge level where `j_lo` and `j_hi` narrow the valid window efficiently.

### Edge Case Testing

- **Empty input:** Not possible (length >= 1).
- **Single element:** `nums = [0]`, `lower = 0`, `upper = 0` -> prefix = `[0, 0]`, one valid pair -> 1.
- **Typical case:** `[-2, 5, -1]` -> 3.
- **Extreme values:** Large negative/positive values. Python handles big integers, but in C++/Java, use `long` for prefix sums.

### Complexity

- **Time:** O(n log n) — `j_lo` and `j_hi` pointers only move forward for increasing `i`, making the counting step O(n) per level. log n levels total.
- **Space:** O(n) — prefix array and temporary merge array.

### Optimization Discussion

- The two-pointer counting trick works because **both halves are sorted** after recursive calls. As `arr[i]` increases (left half sorted), the window `[arr[i] + lower, arr[i] + upper]` shifts right, so `j_lo` and `j_hi` never move backward.
- Alternative: BIT with coordinate compression on prefix sums, but merge sort is cleaner for this problem.

### Follow-up Variations

- Count of Smaller Numbers After Self (LC 315).
- Reverse Pairs (LC 493).
- Subarray Sum Equals K (LC 560) — simpler hash map version.

### Common Traps

- **Prefix sum off-by-one.** The prefix array must have length `n + 1` with `prefix[0] = 0`. Forgetting the leading zero means missing range sums that start at index 0.
- **Overflow in non-Python languages.** Prefix sums of 10^5 elements with values up to 2^31 can overflow 32-bit integers. Use 64-bit.
- **Pointer reset confusion.** The `j_lo` and `j_hi` pointers should NOT reset for each `i`. They persist across iterations because the left half is sorted, making the valid window shift monotonically.
