# Merge Sorted Array

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Same Direction
**Link:** https://leetcode.com/problems/merge-sorted-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given two sorted arrays `nums1` (size `m + n`, with `m` real elements and `n` zeroes as placeholders) and `nums2` (size `n`), merge `nums2` into `nums1` in-place so the result is sorted.

### 2. Clarification Questions
- Input constraints? `nums1.length == m + n`, `nums2.length == n`, `0 <= m, n <= 200`
- Edge cases? One array empty, identical elements, one array all smaller
- Expected output? Modify `nums1` in-place, no return value
- Can input be modified? Yes, `nums1` is the target

### 3. Brute Force Approach
- **Idea:** Copy `nums2` into the tail of `nums1`, then sort.
- **Time:** O((m+n) log(m+n))
- **Space:** O(1) (in-place sort) or O(m+n) (sort implementation)

### 4. Optimized Approach
- **Core Insight:** Fill `nums1` from the **back**. Compare the largest unplaced elements from both arrays and place the bigger one at the current write position. This avoids overwriting elements in `nums1` that haven't been processed yet.
- **Time:** O(m + n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Copy + Sort | O((m+n)log(m+n)) | O(1) | Simple but inefficient |
| Merge from front | O(m+n) | O(m) | Need temp copy of nums1 |
| Merge from back | O(m+n) | O(1) | Optimal — no extra space |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Three pointers: `p1` at end of real elements in `nums1`, `p2` at end of `nums2`, `write` at end of `nums1`.
- Compare and place the **larger** element at `write`, decrement the corresponding pointer.
- If `p1` exhausts first, copy remaining `nums2` elements.

```python
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    p1 = m - 1       # last real element in nums1
    p2 = n - 1       # last element in nums2
    write = m + n - 1 # last position in nums1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            # nums1's element is larger — place it
            nums1[write] = nums1[p1]
            p1 -= 1
        else:
            nums1[write] = nums2[p2]
            p2 -= 1
        write -= 1

    # if nums2 has remaining elements, copy them
    # (if nums1 has remaining, they're already in place)
    while p2 >= 0:
        nums1[write] = nums2[p2]
        p2 -= 1
        write -= 1
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3`

| Step | p1 | p2 | write | Compare | Action | nums1 |
|------|----|----|-------|---------|--------|-------|
| 0 | 2 | 2 | 5 | 3 vs 6 | place 6 | [1,2,3,0,0,**6**] |
| 1 | 2 | 1 | 4 | 3 vs 5 | place 5 | [1,2,3,0,**5**,6] |
| 2 | 2 | 0 | 3 | 3 vs 2 | place 3 | [1,2,3,**3**,5,6] |
| 3 | 1 | 0 | 2 | 2 vs 2 | place 2 (nums1) | [1,2,**2**,3,5,6] |
| 4 | 0 | 0 | 1 | 1 vs 2 | place 2 (nums2) | [1,**2**,2,3,5,6] |

p2 exhausted. nums1 remainder already in place. Result: `[1, 2, 2, 3, 5, 6]`.

### Edge Case Testing
- **Empty input:** `m=0`: just copy nums2. `n=0`: nothing to do
- **Single element:** `nums1=[0], m=0, nums2=[1], n=1` -> `[1]`
- **Typical case:** Shown above
- **Extreme values:** All of nums2 smaller than nums1 -> nums2 gets placed first in the cleanup loop

### Complexity
- **Time:** O(m + n) — each element placed exactly once
- **Space:** O(1) — in-place merge using existing space in nums1

### Optimization Discussion
Already optimal. The key insight is merging **backwards** to avoid overwriting. A Pythonic shortcut (`nums1[:] = sorted(nums1[:m] + nums2)`) works but is O((m+n)log(m+n)) and uses O(m+n) space.

### Follow-up Variations
- **Merge Two Sorted Lists (LC 21)** — linked list version
- **Merge k Sorted Lists (LC 23)** — heap-based extension
- **Squares of a Sorted Array (LC 977)** — merge from both ends

### Common Traps
- Merging **forward** and overwriting elements in `nums1` that haven't been read yet
- Forgetting the cleanup loop for remaining `nums2` elements
- Not needing a cleanup for `nums1` (its elements are already in the correct positions)
