# Peak Index in a Mountain Array

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Classic Binary Search
**Link:** https://leetcode.com/problems/peak-index-in-a-mountain-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a mountain array (values strictly increase then strictly decrease), find the index of the peak element. The peak is guaranteed to exist and is unique.

### 2. Clarification Questions

- **Input constraints?** Length >= 3. Guaranteed mountain shape: `arr[0] < arr[1] < ... < arr[peak] > ... > arr[n-1]`.
- **Edge cases?** Peak at index 1 (minimum left side), peak at index n-2 (minimum right side).
- **Expected output?** Integer — the peak index.
- **Can input be modified?** Not needed — read-only.

### 3. Brute Force Approach

- **Idea:** Linear scan — find the first index where `arr[i] > arr[i + 1]`.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- 💡 **Core Insight:** The mountain array has two halves: **ascending** (left of peak) and **descending** (right of peak). If `arr[mid] < arr[mid + 1]`, we're on the ascending side — peak is to the right. If `arr[mid] > arr[mid + 1]`, we're on the descending side — peak is at `mid` or to the left.
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Linear scan for first descent |
| Optimized | O(log n) | O(1) | Binary search on slope direction |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use `left < right` — converge to the peak.
- Compare `arr[mid]` with `arr[mid + 1]` to determine which slope we're on.
- Peak is where ascending ends and descending begins.

```python
def peakIndexInMountainArray(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1  # WHY: still ascending, peak is to the right
        else:
            right = mid  # WHY: descending or at peak, peak is at mid or left

    return left  # WHY: left == right, converged to the peak
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `arr = [0, 2, 5, 8, 6, 3, 1]`

Peak is at index 3 (value 8).

| Step | left | right | mid | arr[mid] vs arr[mid+1] | Action |
|------|------|-------|-----|------------------------|--------|
| 1 | 0 | 6 | 3 | 8 > 6 | right = 3 |
| 2 | 0 | 3 | 1 | 2 < 5 | left = 2 |
| 3 | 2 | 3 | 2 | 5 < 8 | left = 3 |
| 4 | left == right = 3 | — | — | — | Return 3 |

### Edge Case Testing

- **Empty input:** Not applicable — length >= 3.
- **Single element:** Not applicable — mountain requires at least 3 elements.
- **Typical case:** Peak in the middle → logarithmic convergence.
- **Extreme values:** Peak at index 1 → `arr = [1, 5, 3]`, returns 1. Peak at n-2 → `arr = [1, 3, 5, 2]`, returns 2.

### Complexity

- **Time:** O(log n) — binary search halving each iteration.
- **Space:** O(1) — only pointers.

### Optimization Discussion

This is identical to Find Peak Element (LC 162) in technique. The mountain guarantee simplifies reasoning (exactly one peak) but the code is the same.

### Follow-up Variations

- **Find in Mountain Array (LC 1095):** Find a target in a mountain array — binary search for peak, then binary search each half.
- **Minimum Number of Removals to Make Mountain Array (LC 1671):** DP problem using LIS.
- **Find Peak Element (LC 162):** Generalized version without mountain guarantee.

### Common Traps

- **Accessing `arr[mid + 1]` out of bounds:** Using `left < right` ensures `mid < right <= len(arr) - 1`, so `mid + 1` is always valid.
- **Using `left <= right` with `right = mid`:** Infinite loop when `left == right`.
- **Returning `mid` instead of `left`:** After the loop, `mid` holds a stale value. `left` (which equals `right`) is the answer.
- **Not recognizing this is the same as LC 162:** In interviews, connecting problems shows pattern recognition.
