# Special Array With X Elements Greater Than or Equal X

**Difficulty:** Easy
**Pattern:** Binary Search
**Subpattern:** Boundary Binary Search
**Link:** https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of non-negative integers `nums`, find a value `x` such that there are **exactly x** elements in the array that are **greater than or equal to x**. Return `x` if it exists, or `-1` otherwise. If it exists, `x` is unique.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 100`. `0 <= nums[i] <= 1000`.
- **Edge cases?** All zeros. All elements are the same. Single element array.
- **Expected output?** Integer `x` or `-1`.
- **Can input be modified?** Yes — sorting is helpful.

### 3. Brute Force Approach

- **Idea:** For each candidate `x` from 0 to n, count how many elements are >= x. If count equals x, return x.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** Sort the array. For a candidate `x`, the count of elements >= x is `n - bisect_left(nums, x)`. Binary search for `x` in `[1, n]` where `n - (first index >= x) == x`. After sorting, use **boundary binary search** on the sorted array to count elements efficiently.
- **Time:** O(n log n)
- **Space:** O(1) if in-place sort

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Check each x, count each time |
| Optimized | O(n log n) | O(1) | Sort + binary search on x |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort the array.
- Binary search for `x` in range `[1, n]`.
- For each candidate `x`, use binary search (or direct index math on sorted array) to find how many elements are >= x.
- The count of elements >= x in a sorted array starting at index `idx` is `n - idx`.

```python
def specialArray(nums):
    nums.sort()
    n = len(nums)

    # Binary search for x in [1, n]
    for x in range(1, n + 1):
        # Find leftmost index where nums[idx] >= x using binary search
        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= x:
                hi = mid  # search left for the boundary
            else:
                lo = mid + 1
        # lo is the first index where nums[lo] >= x
        count = n - lo
        if count == x:
            return x

    return -1
```

**Cleaner alternative — pure binary search on x:**

```python
def specialArray(nums):
    nums.sort()
    n = len(nums)

    lo, hi = 1, n
    while lo <= hi:
        x = lo + (hi - lo) // 2

        # Count elements >= x using boundary binary search
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= x:
                right = mid
            else:
                left = mid + 1
        count = n - left

        if count == x:
            return x
        elif count > x:
            lo = x + 1  # too many elements >= x, increase x
        else:
            hi = x - 1  # too few elements >= x, decrease x

    return -1
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [3, 5]`, sorted: `[3, 5]`, `n = 2`

**Binary search on x:** `lo=1, hi=2`
- `x=1`: boundary search for >= 1 -> `left=0`, count = 2. `2 > 1` -> `lo=2`
- `x=2`: boundary search for >= 2 -> `left=0`, count = 2. `2 == 2` -> **return 2**

**Verification:** Elements >= 2: `[3, 5]` — exactly 2 elements.

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `nums=[1]` -> x=1, count of elements >= 1 is 1. Returns **1**. `nums=[0]` -> x=1, count of elements >= 1 is 0. Returns **-1**.
- **All zeros:** `nums=[0,0,0]` -> no x in [1,3] satisfies the condition. Returns **-1**.
- **All same:** `nums=[3,3,3]` -> x=3, count of elements >= 3 is 3. Returns **3**.

### Complexity

- **Time:** O(n log n) — sorting dominates. Binary search on x is O(log n), each with an inner O(log n) search.
- **Space:** O(1) — in-place sort, constant extra space.

### Optimization Discussion

A counting sort approach can achieve O(n) by counting frequencies and computing suffix sums. For each x from n down to 1, check if the suffix sum equals x. However, for the given constraints (n <= 100), the difference is negligible.

### Follow-up Variations

- What if the array can have negative numbers?
- Find all values of x that satisfy a relaxed condition (at least x elements >= x).
- Similar concept: **H-Index** (LC 274/275) — find the maximum h where at least h papers have >= h citations.

### Common Traps

- **Forgetting that x must be in [1, n]** — x = 0 is invalid since you can't have exactly 0 elements >= 0 (all elements are >= 0). x > n is impossible since there are only n elements.
- **Not handling the monotonicity correctly** — as x increases, count of elements >= x decreases. This monotonic relationship enables binary search on x.
- **Confusing with H-Index** — H-Index finds the **maximum** h, while this problem finds the **exact** x where count == x.
