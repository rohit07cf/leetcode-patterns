# Search in a Sorted Array of Unknown Size

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Modified Binary Search — Rotated Arrays
**Link:** https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a sorted array accessed through an `ArrayReader` interface (returns `2^31 - 1` for out-of-bounds indices), find the index of a target value. You **cannot** query the length of the array directly.

### 2. Clarification Questions

- **Input constraints?** Array length up to `10^4`, values in `[-9999, 9999]`, all unique, sorted ascending.
- **Edge cases?** Target at index 0, target beyond current search bounds, target not present.
- **Expected output?** Index of target, or -1.
- **Can input be modified?** No — read-only via `ArrayReader.get(index)`.

### 3. Brute Force Approach

- **Idea:** Linear scan from index 0 until we find the target or hit out-of-bounds.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** Two phases: (1) **Exponential expansion** to find a range `[lo, hi]` that contains the target, then (2) **standard binary search** within that range. Double the bound each step until `reader.get(hi) >= target`.
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Linear scan |
| Optimized | O(log n) | O(1) | Exponential search + binary search |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Phase 1 — Find bounds:** Start with `hi = 1`. While `reader.get(hi) < target`, double `hi` and set `lo = hi // 2`.
- **Phase 2 — Binary search:** Standard binary search in `[lo, hi]`, treating out-of-bounds values (`2^31 - 1`) as "too large."

```python
def search(reader, target):
    # Phase 1: Exponential search to find bounds
    lo, hi = 0, 1
    while reader.get(hi) < target:
        lo = hi
        hi *= 2  # double the range each time

    # Phase 2: Standard binary search within [lo, hi]
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        val = reader.get(mid)

        if val == target:
            return mid
        elif val < target:
            lo = mid + 1
        else:
            # val > target (includes out-of-bounds sentinel)
            hi = mid - 1

    return -1
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Array = `[1, 3, 5, 7, 9, 11]`, target = 9

**Phase 1 — Find bounds:**

| Step | lo | hi | reader.get(hi) | Action |
|------|----|----|----------------|--------|
| 1 | 0 | 1 | 3 < 9 | lo=1, hi=2 |
| 2 | 1 | 2 | 5 < 9 | lo=2, hi=4 |
| 3 | 2 | 4 | 9 >= 9 | Stop. Search [2, 4] |

**Phase 2 — Binary search in [2, 4]:**

| Step | lo | hi | mid | val | Action |
|------|----|----|-----|-----|--------|
| 1 | 2 | 4 | 3 | 7 < 9 | lo = 4 |
| 2 | 4 | 4 | 4 | 9 == 9 | Found! Return 4 |

### Edge Case Testing

- **Empty input:** Problem guarantees at least one element.
- **Single element:** `[5]`, target=5 -> hi stays 1, binary search finds index 0.
- **Typical case:** Shown above.
- **Extreme values:** Target at last position — exponential search overshoots, binary search narrows back. Out-of-bounds reads return `2^31 - 1` which is always > target, so `hi` shrinks correctly.

### Complexity

- **Time:** O(log n) — exponential search takes O(log n) doublings to find bounds, binary search takes O(log n) within those bounds.
- **Space:** O(1) — only pointers.

### Optimization Discussion

Exponential search is optimal for unknown-size arrays. It finds the right range in O(log T) where T is the target's position, then binary search takes O(log T). Total: O(log T), which is O(log n) in the worst case.

### Follow-up Variations

- What if the array is **not sorted** but you still can't query the size? (Must linear scan.)
- Combine with rotated array — unknown size AND rotated?
- What if `ArrayReader.get()` calls are expensive (network I/O)? Minimize total calls.

### Common Traps

- **Starting `hi` at 0:** Start at 1, otherwise `hi *= 2` stays at 0 forever.
- **Forgetting the out-of-bounds sentinel:** `reader.get(out_of_bounds)` returns `2^31 - 1`. This is > any valid value, so binary search naturally treats it as "too large" and moves `hi` left.
- **Not setting `lo = hi` before doubling:** If you always keep `lo = 0`, the binary search range is too wide — O(n) instead of O(log n).
