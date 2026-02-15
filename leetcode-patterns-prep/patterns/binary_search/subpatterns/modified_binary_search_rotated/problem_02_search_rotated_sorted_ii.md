# Search in Rotated Sorted Array II

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Modified Binary Search — Rotated Arrays
**Link:** https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a rotated sorted array that **may contain duplicates**, determine if a target value exists. Return `True` or `False`.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 5000`, values in `[-10^4, 10^4]`, **duplicates allowed**.
- **Edge cases?** All elements identical, target at rotation point, no rotation.
- **Expected output?** Boolean — is target present?
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** Linear scan checking every element.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** Same logic as LC 33, but duplicates create an **ambiguous case** when `nums[lo] == nums[mid] == nums[hi]`. We can't determine which half is sorted, so we **shrink both ends by one** and retry.
- **Time:** O(log n) average, O(n) worst case (e.g., all duplicates)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Simple scan |
| Optimized | O(log n) avg, O(n) worst | O(1) | Binary search with duplicate handling |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Same framework as LC 33: determine which half is sorted, search accordingly.
- **Key addition:** When `nums[lo] == nums[mid] == nums[hi]`, we cannot decide which side is sorted. Shrink: `lo += 1`, `hi -= 1`.

```python
def search(nums, target):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if nums[mid] == target:
            return True

        # Ambiguous case — duplicates hide the sorted half
        if nums[lo] == nums[mid] == nums[hi]:
            lo += 1
            hi -= 1
            continue

        # Left half is sorted
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1

    return False
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums = [2, 5, 6, 0, 0, 1, 2]`, `target = 0`

| Step | lo | hi | mid | nums[mid] | Action |
|------|----|----|-----|-----------|--------|
| 1 | 0 | 6 | 3 | 0 | Found! Return True |

`nums = [1, 0, 1, 1, 1]`, `target = 0`

| Step | lo | hi | mid | nums[mid] | Action |
|------|----|----|-----|-----------|--------|
| 1 | 0 | 4 | 2 | 1 | nums[0]==nums[2]==nums[4]==1, shrink -> lo=1, hi=3 |
| 2 | 1 | 3 | 2 | 1 | Left sorted [0,1], 0 in [0,1)? yes -> hi=1 |
| 3 | 1 | 1 | 1 | 0 | Found! Return True |

### Edge Case Testing

- **Empty input:** Length >= 1 per constraints.
- **Single element:** `[1]`, target=1 -> True. Target=0 -> False.
- **Typical case:** Demonstrated above.
- **Extreme values:** All same `[2,2,2,2]`, target=3 -> shrinks to empty, returns False. Worst-case O(n).

### Complexity

- **Time:** O(log n) average, **O(n) worst case** — when all elements are identical and target is absent, we shrink one element at a time.
- **Space:** O(1) — only pointers.

### Optimization Discussion

The O(n) worst case is **unavoidable** with duplicates. Consider: `[1,1,1,1,1,1,2,1,1,1]` — no binary search can skip elements without potentially missing the 2.

### Follow-up Variations

- How does the worst case change if at most k duplicates are allowed?
- Can you preprocess to remove duplicates first? (Trades space for cleaner logic.)
- What if you need the index, not just existence?

### Common Traps

- **Forgetting the ambiguous case:** Without the `nums[lo] == nums[mid] == nums[hi]` check, the algorithm gives wrong results on inputs like `[1, 0, 1, 1, 1]`.
- **Only checking `nums[lo] == nums[mid]`:** You need the three-way equality. If only `nums[lo] == nums[mid]` but `nums[hi]` differs, you can still determine the sorted half.
- **Assuming O(log n) guaranteed:** Interviewers will ask about worst case — be ready to explain why O(n) is unavoidable.
