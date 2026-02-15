# Merge Sorted Array

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Merge Style
**Link:** https://leetcode.com/problems/merge-sorted-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given two sorted arrays `nums1` (length m+n with trailing zeros) and `nums2` (length n), merge `nums2` into `nums1` **in-place** so the result is sorted.

### 2. Clarification Questions
- Input constraints? `nums1.length == m + n`, `nums2.length == n`, `0 <= m, n <= 200`
- Edge cases? One or both arrays empty; all elements of `nums2` smaller/larger than `nums1`
- Expected output? Modified `nums1` in-place, no return value
- Can input be modified? Yes — `nums1` is the destination

### 3. Brute Force Approach
- **Idea:** Copy `nums2` into the tail of `nums1`, then sort the entire array.
- **Time:** O((m+n) log(m+n))
- **Space:** O(1) extra (in-place sort)

### 4. Optimized Approach
- **Core Insight:** Merge **from the back**. The largest unused element goes into the last unfilled position. This avoids overwriting elements we still need.
- **Time:** O(m + n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O((m+n) log(m+n)) | O(1) | Simple but ignores sorted property |
| Optimized | O(m + n) | O(1) | Merge from right, no extra space |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Start three pointers: `p1` at end of valid `nums1`, `p2` at end of `nums2`, `write` at last index of `nums1`.
- Compare from the back, place the larger element at `write`, decrement pointers.
- If `nums2` has leftovers, copy them in. (`nums1` leftovers are already in place.)

```python
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    p1 = m - 1          # last valid element in nums1
    p2 = n - 1          # last element in nums2
    write = m + n - 1   # last position in nums1

    # Merge from the back — largest goes to the end
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[write] = nums1[p1]
            p1 -= 1
        else:
            nums1[write] = nums2[p2]
            p2 -= 1
        write -= 1

    # If nums2 has remaining elements, copy them
    # (nums1 leftovers are already in correct position)
    while p2 >= 0:
        nums1[write] = nums2[p2]
        p2 -= 1
        write -= 1
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums1 = [1,2,3,0,0,0]`, `m=3`, `nums2 = [2,5,6]`, `n=3`

| Step | p1 | p2 | write | Action | nums1 |
|------|----|----|-------|--------|-------|
| 1 | 2 | 2 | 5 | 6 > 3 → place 6 | [1,2,3,0,0,**6**] |
| 2 | 2 | 1 | 4 | 5 > 3 → place 5 | [1,2,3,0,**5**,6] |
| 3 | 2 | 0 | 3 | 3 >= 2 → place 3 | [1,2,3,**3**,5,6] |
| 4 | 1 | 0 | 2 | 2 >= 2 → place 2 | [1,2,**2**,3,5,6] |
| 5 | 0 | 0 | 1 | 2 > 1 → place 2 | [1,**2**,2,3,5,6] |
| 6 | 0 | — | 0 | p2 done | [1,2,2,3,5,6] |

### Edge Case Testing
- **Empty input:** `m=0` → just copy `nums2` into `nums1`; works via the second while loop
- **Single element:** `m=1, n=0` → nothing to merge, array unchanged
- **Typical case:** Mixed values as shown above
- **Extreme values:** All `nums2` values smaller → fills from position 0; all larger → fills from the end

### Complexity
- **Time:** O(m + n) — each element visited exactly once
- **Space:** O(1) — in-place, no extra arrays

### Optimization Discussion

Already optimal. The key trick is **reverse traversal** so we never overwrite unprocessed elements.

### Follow-up Variations
- What if `nums1` doesn't have extra space? → Need O(n) auxiliary array
- Merge two sorted linked lists (LeetCode 21)
- Merge k sorted arrays (LeetCode 23)

### Common Traps
- Merging front-to-back overwrites elements still needed in `nums1`
- Forgetting the cleanup loop for remaining `nums2` elements
- Off-by-one errors on pointer initialization (`m-1`, not `m`)
