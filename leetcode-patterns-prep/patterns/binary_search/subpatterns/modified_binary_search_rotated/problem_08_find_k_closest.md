# Find K Closest Elements

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Modified Binary Search — Rotated Arrays
**Link:** https://leetcode.com/problems/find-k-closest-elements/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a sorted array and two integers `k` and `x`, find the `k` closest elements to `x`. Return them in **sorted order**. If two elements are equally close, prefer the smaller one.

### 2. Clarification Questions

- **Input constraints?** `1 <= k <= arr.length <= 10^4`, values in `[-10^4, 10^4]`.
- **Edge cases?** `x` smaller than all elements, `x` larger than all, `x` in the array, `k == n`.
- **Expected output?** List of k integers in sorted (ascending) order.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** Sort by distance to `x`, take the first `k`, then sort by value.
- **Time:** O(n log n)
- **Space:** O(n)

### 4. Optimized Approach

- **Core Insight:** The answer is a **contiguous window** of size `k` in the sorted array. Binary search for the **left boundary** of this window. For each candidate left boundary `mid`, compare `x - arr[mid]` vs `arr[mid + k] - x` to decide whether to shift the window right.
- **Time:** O(log(n - k) + k)
- **Space:** O(1) (excluding output)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n log n) | O(n) | Sort by distance |
| Two Pointer | O(n) | O(1) | Shrink from both ends |
| Binary Search | O(log(n-k) + k) | O(1) | Best — search for window start |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Binary search for `lo` = left boundary of the k-element window.
- Search range: `[0, n - k]` (window can start from 0 to n-k).
- At each `mid`, compare distance from `x` to `arr[mid]` vs `arr[mid + k]`:
  - If `x - arr[mid] > arr[mid + k] - x`: window is too far left, move right.
  - Otherwise: window might be correct or too far right, move left.

```python
def findClosestElements(arr, k, x):
    lo, hi = 0, len(arr) - k

    while lo < hi:
        mid = lo + (hi - lo) // 2

        # Compare left edge distance vs right-of-window distance
        if x - arr[mid] > arr[mid + k] - x:
            # Left element is farther — shift window right
            lo = mid + 1
        else:
            # Right-of-window element is farther (or equal) — keep/shift left
            hi = mid

    return arr[lo:lo + k]
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`arr = [1, 2, 3, 4, 5]`, `k = 4`, `x = 3`

n=5, search range [0, 1].

| Step | lo | hi | mid | x - arr[mid] | arr[mid+k] - x | Action |
|------|----|----|-----|-------------|----------------|--------|
| 1 | 0 | 1 | 0 | 3-1=2 | 5-3=2 | 2 > 2? No -> hi=0 |
| Done | lo==hi==0 | | | | | Return arr[0:4] = [1,2,3,4] |

This is correct — when distances are equal, we prefer the smaller element (left window).

### Edge Case Testing

- **Empty input:** Constraint guarantees `k >= 1` and `arr.length >= 1`.
- **Single element:** `arr = [5]`, k=1 -> lo=hi=0, return `[5]`.
- **Typical case:** Shown above.
- **Extreme values:** `x` smaller than all elements -> window stays at index 0. `x` larger than all -> window moves to `n - k`.

### Complexity

- **Time:** O(log(n - k) + k) — binary search over `n - k` candidates, then slicing k elements.
- **Space:** O(1) — excluding the output list of size k.

### Optimization Discussion

The binary search approach is optimal. The two-pointer approach (shrink from both ends) is O(n) and simpler to code but slower. The key insight that makes binary search work is that the result must be a **contiguous subarray**.

### Follow-up Variations

- What if the array is **not sorted**? Must use a heap for O(n log k).
- What if we need the k closest but **not** in sorted order? Same algorithm, just skip final sort.
- Streaming version: elements arrive one at a time, maintain k closest to x.

### Common Traps

- **Using `abs(x - arr[mid]) > abs(x - arr[mid + k])` instead:** The non-abs version `x - arr[mid] > arr[mid + k] - x` handles the tie-breaking rule (prefer smaller element) correctly. With `abs()` you'd need extra logic.
- **Search range `[0, n-1]` instead of `[0, n-k]`:** The window has size k, so the rightmost valid start is `n - k`.
- **Off-by-one: comparing `arr[mid + k - 1]` instead of `arr[mid + k]`:** We compare the element just **outside** the right edge of the window, not the last element inside it. This determines whether to shift.
