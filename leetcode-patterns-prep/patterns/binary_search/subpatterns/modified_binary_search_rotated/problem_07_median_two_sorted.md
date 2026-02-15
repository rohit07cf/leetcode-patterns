# Median of Two Sorted Arrays

**Difficulty:** Hard
**Pattern:** Binary Search
**Subpattern:** Modified Binary Search — Rotated Arrays
**Link:** https://leetcode.com/problems/median-of-two-sorted-arrays/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given two sorted arrays `nums1` and `nums2`, find the **median** of the combined sorted array in O(log(m+n)) time. Do not actually merge them.

### 2. Clarification Questions

- **Input constraints?** `0 <= m, n <= 1000`, `1 <= m + n <= 2000`, values in `[-10^6, 10^6]`.
- **Edge cases?** One array empty, arrays of different lengths, odd vs even total length.
- **Expected output?** Float — median value.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** Merge both arrays and find the middle element(s).
- **Time:** O(m + n)
- **Space:** O(m + n)

### 4. Optimized Approach

- **Core Insight:** Binary search on the **partition** of the smaller array. We need to split both arrays such that all elements on the left side <= all elements on the right side, with equal counts on each side. Binary search the cut position in the smaller array; the cut in the larger array is determined by `half - cut1`.
- **Time:** O(log(min(m, n)))
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(m + n) | O(m + n) | Merge and index |
| Optimized | O(log(min(m, n))) | O(1) | Binary search on partition |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Always binary search on the **smaller** array for efficiency.
- For a partition `i` in nums1, the corresponding partition in nums2 is `j = half - i`.
- **Valid partition:** `nums1[i-1] <= nums2[j]` AND `nums2[j-1] <= nums1[i]`.
- Use `-inf` and `+inf` sentinels for boundary cases.

```python
def findMedianSortedArrays(nums1, nums2):
    # Always binary search on the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    half = (m + n + 1) // 2  # left partition size

    lo, hi = 0, m  # binary search on nums1's partition point

    while lo <= hi:
        i = lo + (hi - lo) // 2  # nums1 contributes i elements to left
        j = half - i              # nums2 contributes j elements to left

        # Sentinel values for edge partitions
        left1 = nums1[i - 1] if i > 0 else float('-inf')
        right1 = nums1[i] if i < m else float('inf')
        left2 = nums2[j - 1] if j > 0 else float('-inf')
        right2 = nums2[j] if j < n else float('inf')

        if left1 <= right2 and left2 <= right1:
            # Valid partition found
            if (m + n) % 2 == 1:
                return max(left1, left2)  # odd: median is max of left
            else:
                return (max(left1, left2) + min(right1, right2)) / 2.0
        elif left1 > right2:
            # Too many from nums1 on the left
            hi = i - 1
        else:
            # Too few from nums1 on the left
            lo = i + 1
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums1 = [1, 3]`, `nums2 = [2]`

m=2, n=1, half=2. Binary search on nums1 (already smaller would be nums2, let's swap): Actually m=2 > n=1, so swap: nums1=[2], nums2=[1,3], m=1, n=2, half=2.

| Step | lo | hi | i | j | left1 | right1 | left2 | right2 | Valid? |
|------|----|----|---|---|-------|--------|-------|--------|--------|
| 1 | 0 | 1 | 0 | 2 | -inf | 2 | 3 | inf | -inf<=inf, 3>2? No -> lo=1 |
| 2 | 1 | 1 | 1 | 1 | 2 | inf | 1 | 3 | 2<=3, 1<=inf? Yes! |

Odd total (3): return max(2, 1) = **2.0**. Correct.

### Edge Case Testing

- **Empty input:** One array empty -> all elements come from the other, `i=0` always, partition trivially valid.
- **Single element:** `[1]`, `[2]` -> half=1, quickly finds partition, returns 1.5.
- **Typical case:** Shown above.
- **Extreme values:** Arrays don't overlap `[1,2]`, `[3,4]` -> partition at boundary, sentinels handle it.

### Complexity

- **Time:** O(log(min(m, n))) — binary search only on the smaller array.
- **Space:** O(1) — constant extra space.

### Optimization Discussion

This is the **theoretically optimal** approach. The key insight is that finding the median is equivalent to finding the correct partition — a binary search problem on the smaller array.

### Follow-up Variations

- Find the **k-th smallest** element in two sorted arrays.
- Extend to **k sorted arrays** — use a different approach (heap or divide-and-conquer).
- What if arrays are stored on different machines (distributed median)?

### Common Traps

- **Not searching on the smaller array:** Searching on the larger array can lead to invalid `j` values (negative index).
- **Off-by-one in `half` calculation:** Use `(m + n + 1) // 2` to handle both odd and even correctly. This biases the left partition to have the extra element when total is odd.
- **Forgetting sentinel values:** When `i=0` or `j=0` (empty left partition in one array), you must use `-inf`. Similarly, `+inf` for empty right partitions.
- **Integer division for even case:** Return `/ 2.0` not `// 2` for float precision.
