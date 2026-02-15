# Count Negative Numbers in a Sorted Matrix

**Difficulty:** Easy
**Pattern:** Binary Search
**Subpattern:** Classic Binary Search
**Link:** https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an m x n matrix where each row and each column is sorted in **non-increasing** order, count the number of negative numbers in the matrix.

### 2. Clarification Questions

- **Input constraints?** m, n >= 1 (up to 100). Rows and columns sorted in non-increasing (descending) order.
- **Edge cases?** All positive, all negative, single element, no negatives at all.
- **Expected output?** Integer count of negative numbers.
- **Can input be modified?** Not needed — read-only.

### 3. Brute Force Approach

- **Idea:** Iterate through every cell, count negatives.
- **Time:** O(m * n)
- **Space:** O(1)

### 4. Optimized Approach

- 💡 **Core Insight:** Each row is sorted in non-increasing order. Binary search each row to find the **first negative number**. Everything from that index to the end is negative. Count = `cols - first_negative_index` per row.
- **Time:** O(m * log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(m * n) | O(1) | Check every cell |
| Binary Search per row | O(m * log n) | O(1) | Find first negative in each row |
| Staircase (optimal) | O(m + n) | O(1) | Exploit both row and column sorting |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

### Approach A: Binary Search per Row

- For each row, binary search for the first negative number.
- Since rows are sorted in **descending** order, negatives are on the **right** side.
- Find the leftmost negative: the first index where `row[mid] < 0`.

```python
def countNegatives(grid: list[list[int]]) -> int:
    count = 0
    cols = len(grid[0])

    for row in grid:
        # WHY: binary search for first negative in this descending-sorted row
        left, right = 0, cols

        while left < right:
            mid = left + (right - left) // 2

            if row[mid] < 0:
                right = mid  # WHY: mid is negative, but there may be an earlier one
            else:
                left = mid + 1  # WHY: mid is non-negative, first negative is to the right

        # WHY: left is index of first negative; everything from left to end is negative
        count += cols - left

    return count
```

### Approach B: Staircase (Bonus — O(m + n))

- Start from the **top-right** corner.
- If current cell is negative, the entire column below is also negative — add remaining rows, move left.
- If non-negative, move down.

```python
def countNegatives(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    count = 0
    r, c = 0, cols - 1  # WHY: start at top-right corner

    while r < rows and c >= 0:
        if grid[r][c] < 0:
            count += rows - r  # WHY: all cells below in this column are also negative
            c -= 1  # WHY: move left to find boundary
        else:
            r += 1  # WHY: move down to find negatives

    return count
```

---

## PHASE 3 — AFTER CODING

### Dry Run (Binary Search Approach)

**Input:**
```
grid = [[ 4,  3,  2, -1],
        [ 3,  2,  1, -1],
        [ 1,  1, -1, -2],
        [-1, -1, -2, -3]]
```

| Row | Binary Search | First Neg Index | Negatives |
|-----|---------------|-----------------|-----------|
| [4, 3, 2, -1] | left converges to 3 | 3 | 4 - 3 = 1 |
| [3, 2, 1, -1] | left converges to 3 | 3 | 4 - 3 = 1 |
| [1, 1, -1, -2] | left converges to 2 | 2 | 4 - 2 = 2 |
| [-1, -1, -2, -3] | left converges to 0 | 0 | 4 - 0 = 4 |

**Total:** 1 + 1 + 2 + 4 = **8**

### Edge Case Testing

- **Empty input:** Constraints guarantee m, n >= 1.
- **Single element:** `[[5]]` → 0 negatives. `[[-1]]` → 1 negative.
- **Typical case:** Mixed positives and negatives → binary search finds boundary per row.
- **Extreme values:** All positive → left = cols for each row, count = 0. All negative → left = 0 for each row, count = m * n.

### Complexity

**Binary Search Approach:**
- **Time:** O(m * log n) — binary search on each of m rows.
- **Space:** O(1) — constant extra space.

**Staircase Approach:**
- **Time:** O(m + n) — each step moves left or down, at most m + n steps.
- **Space:** O(1) — constant extra space.

### Optimization Discussion

The **staircase approach** is the true optimal at O(m + n). It exploits **both** row and column sorting simultaneously. In an interview, mention the binary search approach first, then upgrade to staircase as a follow-up optimization.

### Follow-up Variations

- What if we need the count of **positive** numbers instead? (Same logic, flip the condition.)
- **Search a 2D Matrix II (LC 240):** Same staircase technique for searching a value.
- What if only rows are sorted (not columns)? (Binary search per row is optimal.)

### Common Traps

- **Sorting direction:** Rows are sorted **descending**, not ascending. Negatives are on the **right**, not the left. Don't apply ascending binary search logic blindly.
- **Using `right = cols - 1` with `left <= right`:** Works but requires adjusting the count formula. Using `right = cols` with `left < right` is cleaner for boundary search.
- **Forgetting the column-sorted property:** The staircase approach only works because **both** rows and columns are sorted. If only rows were sorted, stick with binary search per row.
