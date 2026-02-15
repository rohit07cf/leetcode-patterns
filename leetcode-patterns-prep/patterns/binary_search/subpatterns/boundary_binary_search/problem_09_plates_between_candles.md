# Plates Between Candles

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Boundary Binary Search
**Link:** https://leetcode.com/problems/plates-between-candles/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a string `s` consisting of `'*'` (plates) and `'|'` (candles), and a list of queries `[left, right]`, for each query return the number of **plates between candles** within the substring `s[left..right]`. A plate is "between candles" if there exists at least one candle to its left and one to its right within the query range.

### 2. Clarification Questions

- **Input constraints?** `3 <= s.length <= 10^5`. `1 <= queries.length <= 10^5`. Characters are only `'*'` or `'|'`.
- **Edge cases?** No candles in range. No plates between candles. Query range has only one candle. Entire range is plates or candles.
- **Expected output?** A list of integers, one per query.
- **Can input be modified?** Yes, but no need.

### 3. Brute Force Approach

- **Idea:** For each query, scan the substring to find the first and last candle, then count plates between them.
- **Time:** O(q * n) where q = number of queries
- **Space:** O(1) per query

### 4. Optimized Approach

- **Core Insight:** Precompute:
  1. A **prefix sum** of plates at each position.
  2. A sorted list of **candle positions**.
  For each query `[left, right]`, use **boundary binary search** to find the **first candle >= left** and the **last candle <= right**. The plates between them = `prefix[last_candle] - prefix[first_candle]`.
- **Time:** O(n + q * log n)
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(q * n) | O(1) | Linear scan per query |
| Optimized | O(n + q log n) | O(n) | Prefix sum + binary search |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Precompute** prefix sum of plates and collect candle indices.
- For each query `[left, right]`:
  - **Binary search** for the **first candle at or after `left`** (lower bound).
  - **Binary search** for the **last candle at or before `right`** (upper bound - 1).
  - If valid (first_candle <= last_candle), count = `prefix[last_candle] - prefix[first_candle]`.

```python
import bisect

def platesBetweenCandles(s, queries):
    n = len(s)

    # Prefix sum of plates
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + (1 if s[i] == '*' else 0)

    # Collect all candle positions
    candles = [i for i in range(n) if s[i] == '|']

    result = []
    for left, right in queries:
        # First candle >= left (leftmost boundary)
        lo = bisect.bisect_left(candles, left)
        # Last candle <= right (rightmost boundary)
        hi = bisect.bisect_right(candles, right) - 1

        if lo <= hi and lo < len(candles):
            first_candle = candles[lo]
            last_candle = candles[hi]
            # Plates between these two candles
            result.append(prefix[last_candle] - prefix[first_candle])
        else:
            result.append(0)  # no valid candle pair in range

    return result
```

**Manual binary search version (interview-ready):**

```python
def platesBetweenCandles(s, queries):
    n = len(s)

    # Prefix sum of plates
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + (1 if s[i] == '*' else 0)

    # Collect candle positions
    candles = [i for i in range(n) if s[i] == '|']

    def first_candle_at_or_after(pos):
        """Find leftmost candle index >= pos."""
        lo, hi = 0, len(candles) - 1
        result = len(candles)  # sentinel: not found
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if candles[mid] >= pos:
                result = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return result

    def last_candle_at_or_before(pos):
        """Find rightmost candle index <= pos."""
        lo, hi = 0, len(candles) - 1
        result = -1  # sentinel: not found
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if candles[mid] <= pos:
                result = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return result

    result = []
    for left, right in queries:
        lo_idx = first_candle_at_or_after(left)
        hi_idx = last_candle_at_or_before(right)

        if lo_idx <= hi_idx and lo_idx < len(candles):
            fc = candles[lo_idx]
            lc = candles[hi_idx]
            result.append(prefix[lc] - prefix[fc])
        else:
            result.append(0)

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `s = "**|**|***|"`, `queries = [[2, 5], [5, 9]]`

**Candles:** indices `[2, 5, 9]`

**Prefix (plates):** `[0, 1, 2, 2, 3, 4, 4, 5, 6, 7, 7]`

**Query [2, 5]:**
- First candle >= 2: `candles[0] = 2` (lo_idx = 0)
- Last candle <= 5: `candles[1] = 5` (hi_idx = 1)
- Plates = `prefix[5] - prefix[2]` = `4 - 2` = **2**

**Query [5, 9]:**
- First candle >= 5: `candles[1] = 5` (lo_idx = 1)
- Last candle <= 9: `candles[2] = 9` (hi_idx = 2)
- Plates = `prefix[9] - prefix[5]` = `7 - 4` = **3**

**Output:** `[2, 3]`

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **No candles in range:** `s = "***"`, query `[0,2]` -> `candles` is empty or no candle in range. Returns 0.
- **Single candle in range:** lo_idx > hi_idx, returns 0.
- **Typical case:** Mix of plates and candles, verified above.
- **Extreme values:** 10^5 length string with 10^5 queries — O(n + q log n) handles efficiently.

### Complexity

- **Time:** O(n + q * log c) where c = number of candles — prefix sum is O(n), each query does two binary searches on candles array.
- **Space:** O(n) — prefix sum and candles arrays.

### Optimization Discussion

An **O(n + q)** approach exists using precomputed arrays `next_candle_left[i]` and `next_candle_right[i]` for each index. This avoids binary search entirely but uses O(n) extra space for these arrays. The binary search approach is cleaner and demonstrates the pattern.

### Follow-up Variations

- Count plates between the **k-th and (k+1)-th** candles.
- Support **dynamic updates** (adding/removing candles) — use a balanced BST or BIT.
- Extend to 2D: count elements between boundaries in a grid.

### Common Traps

- **Off-by-one with prefix sum** — using `prefix[last_candle] - prefix[first_candle]` correctly excludes plates at or before the first candle. Be careful with 0-indexed vs 1-indexed prefix arrays.
- **Not checking `lo_idx <= hi_idx`** — if the first candle is after the last candle (or either doesn't exist in range), there are no valid plates.
- **Using candle array indices vs string indices** — `lo_idx`/`hi_idx` are indices into the `candles` array; `candles[lo_idx]` gives the actual string position.
