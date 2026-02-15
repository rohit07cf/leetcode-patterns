# Count Negative Numbers in a Sorted Matrix

**Difficulty:** Easy
**Pattern:** Binary Search
**Subpattern:** Boundary Binary Search
**Link:** https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an `m x n` matrix where each row and each column is sorted in **non-increasing order**, count the number of **negative** numbers in the matrix.

### 2. Clarification Questions

- **Input constraints?** `1 <= m, n <= 100`. `-100 <= grid[i][j] <= 100`. Rows and columns sorted in non-increasing (descending) order.
- **Edge cases?** All positive. All negative. Single cell. Matrix of zeros.
- **Expected output?** A single integer — the count of negative numbers.
- **Can input be modified?** Yes, but no need.

### 3. Brute Force Approach

- **Idea:** Iterate through every cell and count negatives.
- **Time:** O(m * n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** Each row is sorted in non-increasing order. Use **boundary binary search** on each row to find the **first negative number**. All elements from that index onward are negative. Count = `n - boundary_index` per row.
- **Time:** O(m * log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(m * n) | O(1) | Check every cell |
| Binary Search | O(m * log n) | O(1) | Binary search each row |
| Staircase | O(m + n) | O(1) | Start from top-right corner |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- For each row, binary search for the **leftmost index** where the value is negative (< 0).
- Since rows are in **non-increasing** order, negatives are on the **right side**.
- Count negatives in that row as `n - first_negative_index`.

```python
def countNegatives(grid):
    count = 0
    n = len(grid[0])

    for row in grid:
        # Binary search for first negative in this row (non-increasing order)
        lo, hi = 0, n - 1
        boundary = n  # default: no negatives in this row

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if row[mid] < 0:
                boundary = mid  # candidate, keep searching left
                hi = mid - 1
            else:
                lo = mid + 1  # row[mid] >= 0, search right

        count += n - boundary

    return count
```

**Bonus — O(m + n) staircase approach:**

```python
def countNegatives(grid):
    m, n = len(grid), len(grid[0])
    count = 0
    col = n - 1  # start from top-right corner

    for row in range(m):
        # Move left while current cell is negative
        while col >= 0 and grid[row][col] < 0:
            col -= 1
        # All cells to the right of col are negative
        count += n - (col + 1)

    return count
```

---

## PHASE 3 — AFTER CODING

### Dry Run (Binary Search Approach)

**Input:**
```
grid = [[4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3]]
```

- **Row 0:** `[4,3,2,-1]` -> boundary at index 3 -> negatives = 4 - 3 = 1
- **Row 1:** `[3,2,1,-1]` -> boundary at index 3 -> negatives = 4 - 3 = 1
- **Row 2:** `[1,1,-1,-2]` -> boundary at index 2 -> negatives = 4 - 2 = 2
- **Row 3:** `[-1,-1,-2,-3]` -> boundary at index 0 -> negatives = 4 - 0 = 4

**Total: 1 + 1 + 2 + 4 = 8**

### Edge Case Testing

- **Empty input:** Not possible (m, n >= 1).
- **Single element:** `[[5]]` -> boundary = 1, count = 0. `[[-5]]` -> boundary = 0, count = 1.
- **All positive:** Every row has boundary = n, total count = 0.
- **All negative:** Every row has boundary = 0, total count = m * n.

### Complexity

- **Time:** O(m * log n) — binary search per row. Staircase approach is O(m + n).
- **Space:** O(1) — constant extra space.

### Optimization Discussion

The **staircase approach** (O(m + n)) exploits both row and column sorting. Start at the top-right corner. If the cell is negative, count negatives in that column and move left. If non-negative, move down. This is optimal but the binary search approach better demonstrates the boundary binary search pattern.

### Follow-up Variations

- Count **positive** numbers instead (mirror the boundary).
- Find the **row with the most negatives**.
- What if the matrix is sorted in **non-decreasing** order instead?
- Count elements in a specific range [a, b] using two boundary searches.

### Common Traps

- **Sorting direction confusion** — rows are in **non-increasing** order (descending), so negatives are on the right. Don't assume ascending order.
- **Off-by-one with boundary** — setting `boundary = n` (not `n-1`) as default handles the case where no negatives exist in a row.
- **Forgetting to exploit column sorting** — for the optimal O(m + n) staircase approach, the column ordering means the boundary only moves left as you go down rows.
