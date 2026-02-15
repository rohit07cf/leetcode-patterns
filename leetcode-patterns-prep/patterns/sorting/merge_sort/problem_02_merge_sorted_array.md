# Merge Sorted Array

**Difficulty:** Easy
**Pattern:** Sorting
**Subpattern:** Merge Sort
**Link:** https://leetcode.com/problems/merge-sorted-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given two sorted integer arrays `nums1` and `nums2`, merge `nums2` into `nums1` as one sorted array **in-place**. `nums1` has enough space (size `m + n`) to hold the result, with the first `m` elements being valid and the last `n` positions being zeros as placeholders.

### 2. Clarification Questions

- **Input constraints?** `0 <= m, n <= 200`, `nums1.length == m + n`, `nums2.length == n`.
- **Edge cases?** `n == 0` (nothing to merge), `m == 0` (just copy nums2), one array fully smaller than the other.
- **Expected output?** `nums1` modified in-place to contain all `m + n` elements in sorted order.
- **Can input be modified?** Yes, `nums1` must be modified in-place.

### 3. Brute Force Approach

- **Idea:** Copy `nums2` into the empty slots of `nums1`, then sort the entire array.
- **Time:** O((m + n) log(m + n))
- **Space:** O(1) if using in-place sort

### 4. Optimized Approach

- **Core Insight:** Merge from the **back**. Start filling `nums1` from index `m + n - 1` using two pointers at the ends of both arrays. The largest unplaced element always goes to the rightmost unfilled position. This avoids overwriting valid elements in `nums1`.
- **Time:** O(m + n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (copy + sort) | O((m+n) log(m+n)) | O(1) | Simple but wasteful |
| Optimized (merge from back) | O(m + n) | O(1) | Exploits pre-sorted property |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use three pointers: `p1` at end of valid `nums1` (`m - 1`), `p2` at end of `nums2` (`n - 1`), `write` at end of `nums1` (`m + n - 1`).
- Compare from the back, place the larger element at `write`, decrement pointers.
- If `nums2` has remaining elements after `p1` is exhausted, copy them. If `nums1` has remaining, they're already in place.

```python
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1 = m - 1       # Pointer to last valid element in nums1
        p2 = n - 1       # Pointer to last element in nums2
        write = m + n - 1 # Pointer to last position in nums1

        # Merge from back: place the larger of the two at write position
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[write] = nums1[p1]
                p1 -= 1
            else:
                nums1[write] = nums2[p2]
                p2 -= 1
            write -= 1

        # If nums2 has remaining elements, copy them
        # (no need to handle remaining nums1 — already in place)
        while p2 >= 0:
            nums1[write] = nums2[p2]
            p2 -= 1
            write -= 1
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums1 = [1, 2, 3, 0, 0, 0]`, `m = 3`, `nums2 = [2, 5, 6]`, `n = 3`

| Step | p1 | p2 | write | Action | nums1 |
|------|----|----|-------|--------|-------|
| 1 | 2 | 2 | 5 | 3 < 6, place 6 | [1,2,3,0,0,**6**] |
| 2 | 2 | 1 | 4 | 3 < 5, place 5 | [1,2,3,0,**5**,6] |
| 3 | 2 | 0 | 3 | 3 > 2, place 3 | [1,2,**3**,**3**,5,6] |
| 4 | 1 | 0 | 2 | 2 == 2, place nums2's 2 | [1,2,**2**,3,5,6] |
| 5 | 1 | — | — | p2 exhausted, done | [1,2,2,3,5,6] |

### Edge Case Testing

- **Empty input:** `m = 0` -> just copy `nums2` into `nums1`. The while loop with `p1` never runs, second loop copies all.
- **Single element:** `nums1 = [1, 0], m = 1, nums2 = [2], n = 1` -> `[1, 2]`.
- **Typical case:** As shown in dry run.
- **Extreme values:** `nums2` all smaller -> they fill the front of `nums1` correctly.

### Complexity

- **Time:** O(m + n) — each element is placed exactly once.
- **Space:** O(1) — in-place, no extra arrays.

### Optimization Discussion

- This is already optimal. The key insight that makes O(1) space possible is merging **backwards** so we never overwrite unprocessed elements.
- A forward merge would require O(m) extra space to save `nums1`'s elements.

### Follow-up Variations

- Merge two sorted linked lists (LC 21).
- Merge k sorted arrays (LC 23).
- Find the median of two sorted arrays (LC 4).

### Common Traps

- **Merging forward instead of backward** overwrites valid elements in `nums1` before they're processed.
- **Forgetting the remaining `nums2` copy** after the main loop. If all of `nums1`'s elements are larger, `nums2` elements still need placement.
- **Off-by-one errors** with pointer initialization. `p1 = m - 1`, not `m`. When `m = 0`, `p1 = -1` and the first loop never executes.
