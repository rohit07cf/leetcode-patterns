# Single Element in a Sorted Array

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Boundary Binary Search
**Link:** https://leetcode.com/problems/single-element-in-a-sorted-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a sorted array where every element appears exactly twice except for one element that appears once, find and return the single element. Must run in **O(log n)** time and **O(1)** space.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 10^5`. Array length is always odd. Array is sorted.
- **Edge cases?** Single element array. Single element at the start, middle, or end.
- **Expected output?** The integer that appears only once.
- **Can input be modified?** Yes, but no need.

### 3. Brute Force Approach

- **Idea:** XOR all elements — pairs cancel out, leaving the single element. Or linear scan checking pairs.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** Before the single element, pairs start at **even indices** (i.e., `nums[0]==nums[1]`, `nums[2]==nums[3]`). After the single element, pairs start at **odd indices**. Binary search for the **boundary** where this pairing pattern breaks.
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (XOR) | O(n) | O(1) | Ignores sorted property |
| Optimized | O(log n) | O(1) | Boundary binary search on pair pattern |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Only search on **even indices** — the single element must be at an even index.
- If `nums[mid] == nums[mid + 1]`, the single element is to the **right** (pairs are still intact).
- If `nums[mid] != nums[mid + 1]`, the single element is at `mid` or to the **left**.

```python
def singleNonDuplicate(nums):
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2
        # Ensure mid is even so we can check pairs starting at even index
        if mid % 2 == 1:
            mid -= 1

        if nums[mid] == nums[mid + 1]:
            lo = mid + 2  # pair is intact, single element is to the right
        else:
            hi = mid  # pair is broken, single element is at mid or left

    return nums[lo]
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]`

- `lo=0, hi=8` -> `mid=4` (even) -> `nums[4]=3 == nums[5]=4`? No -> `hi=4`
- `lo=0, hi=4` -> `mid=2` (even) -> `nums[2]=2 == nums[3]=3`? No -> `hi=2`
- `lo=0, hi=2` -> `mid=1` (odd, adjust to 0) -> `nums[0]=1 == nums[1]=1`? Yes -> `lo=2`
- `lo=2, hi=2` -> exit. Return `nums[2]` = **2**

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `nums=[5]` -> `lo=0, hi=0`, loop doesn't execute, returns `nums[0]=5`.
- **Single at start:** `nums=[1,2,2]` -> `mid=0`, `nums[0]!=nums[1]`, `hi=0`, returns `1`.
- **Single at end:** `nums=[1,1,2]` -> `mid=0`, `nums[0]==nums[1]`, `lo=2`, returns `2`.

### Complexity

- **Time:** O(log n) — binary search halves the search space each iteration.
- **Space:** O(1) — only pointers.

### Optimization Discussion

Already optimal. The key insight that makes this O(log n) instead of O(n) is recognizing the **structural invariant** of pair alignment before and after the single element.

### Follow-up Variations

- What if the array is **not sorted**? Must use XOR in O(n).
- What if **two** elements appear once? Use XOR + bit manipulation to separate them.
- What if elements appear **three times** except one? Use bit counting.

### Common Traps

- **Not forcing `mid` to an even index** — checking pairs starting at odd indices breaks the logic since pairs naturally start at even indices before the anomaly.
- **Using `lo <= hi` instead of `lo < hi`** — this is a convergence-style binary search where `lo == hi` is the answer.
- **Forgetting `mid + 1` could be out of bounds** — the `lo < hi` condition guarantees `mid < hi`, so `mid + 1 <= hi` is always valid.
