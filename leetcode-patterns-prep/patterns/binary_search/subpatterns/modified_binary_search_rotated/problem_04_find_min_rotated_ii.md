# Find Minimum in Rotated Sorted Array II

**Difficulty:** Hard
**Pattern:** Binary Search
**Subpattern:** Modified Binary Search — Rotated Arrays
**Link:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a rotated sorted array that **may contain duplicates**, find the minimum element. This is the harder variant of LC 153 where duplicates introduce ambiguity.

### 2. Clarification Questions

- **Input constraints?** `1 <= n <= 5000`, values in `[-5000, 5000]`, **duplicates allowed**.
- **Edge cases?** All elements identical, min at rotation point surrounded by duplicates.
- **Expected output?** The minimum value.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** Linear scan to find the minimum.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** Same as LC 153, but when `nums[mid] == nums[hi]`, we **cannot determine** which half contains the min. Safe move: `hi -= 1` (we only lose a duplicate of mid, never the unique min).
- **Time:** O(log n) average, O(n) worst case
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Always linear |
| Optimized | O(log n) avg, O(n) worst | O(1) | Degrades with many duplicates |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Compare `nums[mid]` with `nums[hi]` as in LC 153.
- **New case:** When `nums[mid] == nums[hi]`, shrink `hi` by 1. This is safe because even if `nums[hi]` is the min, `nums[mid]` is an identical copy still in range.
- Loop until `lo == hi`.

```python
def findMin(nums):
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if nums[mid] > nums[hi]:
            # Min is in the right half (past the break point)
            lo = mid + 1
        elif nums[mid] < nums[hi]:
            # Min is in the left half (mid could be min)
            hi = mid
        else:
            # nums[mid] == nums[hi] — can't decide, shrink safely
            hi -= 1

    return nums[lo]
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums = [2, 2, 2, 0, 1]`

| Step | lo | hi | mid | nums[mid] vs nums[hi] | Action |
|------|----|----|-----|----------------------|--------|
| 1 | 0 | 4 | 2 | 2 > 1 | lo = 3 |
| 2 | 3 | 4 | 3 | 0 < 1 | hi = 3 |
| Done | lo == hi == 3 | | | | Return nums[3] = 0 |

`nums = [3, 3, 1, 3]`

| Step | lo | hi | mid | nums[mid] vs nums[hi] | Action |
|------|----|----|-----|----------------------|--------|
| 1 | 0 | 3 | 1 | 3 == 3 | hi = 2 |
| 2 | 0 | 2 | 1 | 3 > 1 | lo = 2 |
| Done | lo == hi == 2 | | | | Return nums[2] = 1 |

### Edge Case Testing

- **Empty input:** Constraint guarantees length >= 1.
- **Single element:** `[5]` -> return 5 immediately.
- **Typical case:** Demonstrated above.
- **Extreme values:** All identical `[3,3,3,3]` -> repeatedly `hi -= 1` until lo == hi. Returns 3. Takes O(n).

### Complexity

- **Time:** O(log n) average, **O(n) worst case** — when all elements are equal, we shrink by 1 each step.
- **Space:** O(1) — only pointers.

### Optimization Discussion

The O(n) worst case is **provably unavoidable**. Consider `[1,1,1,...,1,0,1,...,1,1]` — no algorithm can skip elements without risk of missing the single 0.

### Follow-up Variations

- What if we want the index of the minimum, not the value?
- Compare with LC 153 — what's the **exact** added complexity from duplicates?
- Can you prove that `hi -= 1` never discards the answer?

### Common Traps

- **Decrementing `lo` instead of `hi`:** Always shrink `hi`. We compare with `nums[hi]`, so removing a duplicate from the right end is safe.
- **Using `lo += 1` and `hi -= 1` together in the ambiguous case:** This can skip the min. Only shrink one side.
- **Assuming O(log n) in interviews:** Always mention the worst case and explain **why** it's unavoidable with duplicates.
