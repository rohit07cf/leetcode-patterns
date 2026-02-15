# Find Peak Element

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Modified Binary Search — Rotated Arrays
**Link:** https://leetcode.com/problems/find-peak-element/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array where `nums[-1] = nums[n] = -infinity`, find **any** index `i` such that `nums[i] > nums[i-1]` and `nums[i] > nums[i+1]`. Multiple peaks may exist — return any one.

### 2. Clarification Questions

- **Input constraints?** `1 <= n <= 1000`, values in `[-2^31, 2^31 - 1]`, **no two adjacent elements are equal**.
- **Edge cases?** Single element (always a peak), strictly increasing, strictly decreasing.
- **Expected output?** Index of **any** peak element.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** Scan left to right, return first element greater than its neighbor on both sides.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** If `nums[mid] < nums[mid + 1]`, a peak **must exist** to the right (the slope is going up, and the boundary is -infinity). Similarly, if `nums[mid] < nums[mid - 1]`, a peak exists to the left. This gives us a binary search on the "slope."
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Linear scan |
| Optimized | O(log n) | O(1) | Binary search on slope direction |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use `lo < hi` loop so we converge to a single index.
- If `nums[mid] < nums[mid + 1]`, the peak is to the right -> `lo = mid + 1`.
- Otherwise, mid itself might be the peak -> `hi = mid`.
- When `lo == hi`, we've found a peak.

```python
def findPeakElement(nums):
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if nums[mid] < nums[mid + 1]:
            # Slope going up — peak must be to the right
            lo = mid + 1
        else:
            # Slope going down — peak is at mid or to the left
            hi = mid

    return lo  # lo == hi, this is a peak
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums = [1, 2, 3, 1]`

| Step | lo | hi | mid | nums[mid] vs nums[mid+1] | Action |
|------|----|----|-----|-------------------------|--------|
| 1 | 0 | 3 | 1 | 2 < 3 | lo = 2 |
| 2 | 2 | 3 | 2 | 3 > 1 | hi = 2 |
| Done | lo == hi == 2 | | | | Return 2 (nums[2] = 3) |

### Edge Case Testing

- **Empty input:** Constraint guarantees length >= 1.
- **Single element:** `[5]` -> lo=hi=0 immediately, return 0. Correct — single element is always a peak.
- **Typical case:** Shown above.
- **Extreme values:** Strictly increasing `[1,2,3,4,5]` -> keeps going right, returns index 4 (last element). Valid because `nums[5] = -inf`.

### Complexity

- **Time:** O(log n) — halving each iteration.
- **Space:** O(1) — two pointers.

### Optimization Discussion

Already optimal. The problem only requires finding **any** peak, which is what makes O(log n) possible. Finding **all** peaks would require O(n).

### Follow-up Variations

- Find peak in a **2D matrix** (LC 1901 — Find a Peak Element II).
- What if adjacent elements can be equal? The guarantee of no adjacent duplicates is critical for binary search to work here.
- Find the **global maximum** — requires O(n), binary search only finds a local peak.

### Common Traps

- **Accessing `nums[mid + 1]` out of bounds:** Safe here because `lo < hi` means `mid < hi`, so `mid + 1 <= hi` and is valid.
- **Thinking this only works for unimodal arrays:** The array can have multiple peaks. Binary search finds **one** of them because we always move toward the uphill direction.
- **Confusing with rotated array search:** This is about slope direction, not sorted halves. The key property is `nums[-1] = nums[n] = -infinity`, guaranteeing a peak exists.
