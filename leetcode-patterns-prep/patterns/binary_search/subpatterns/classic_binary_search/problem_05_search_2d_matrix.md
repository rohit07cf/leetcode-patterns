# Search a 2D Matrix

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Classic Binary Search
**Link:** https://leetcode.com/problems/search-a-2d-matrix/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an m x n matrix where each row is sorted and the first element of each row is greater than the last element of the previous row, determine if a target value exists in the matrix.

### 2. Clarification Questions

- **Input constraints?** m, n >= 1. Rows sorted ascending. First element of row > last element of previous row.
- **Edge cases?** 1x1 matrix, target not present, target at corners.
- **Expected output?** Boolean — true if target exists, false otherwise.
- **Can input be modified?** Not needed — read-only search.

### 3. Brute Force Approach

- **Idea:** Scan every cell in the matrix.
- **Time:** O(m * n)
- **Space:** O(1)

### 4. Optimized Approach

- 💡 **Core Insight:** Because of the row-linking property, the entire matrix is effectively one **sorted 1D array**. Map a 1D index to 2D coordinates: `row = idx // n`, `col = idx % n`. Then run standard binary search.
- **Time:** O(log(m * n))
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(m * n) | O(1) | Full scan |
| Two Binary Searches | O(log m + log n) | O(1) | Search row, then column |
| Single Binary Search | O(log(m * n)) | O(1) | Treat as flattened sorted array |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Treat the 2D matrix as a virtual 1D sorted array of length `m * n`.
- Convert 1D index to 2D: `row = mid // cols`, `col = mid % cols`.
- Standard binary search on the virtual array.

```python
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = left + (right - left) // 2
        # WHY: convert 1D index to 2D coordinates
        value = matrix[mid // cols][mid % cols]

        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:**
```
matrix = [[1,  3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 60]]
target = 3
```
`rows = 3, cols = 4`, total = 12

| Step | left | right | mid | row, col | value | Action |
|------|------|-------|-----|----------|-------|--------|
| 1 | 0 | 11 | 5 | 1, 1 | 11 | 11 > 3 → right = 4 |
| 2 | 0 | 4 | 2 | 0, 2 | 5 | 5 > 3 → right = 1 |
| 3 | 0 | 1 | 0 | 0, 0 | 1 | 1 < 3 → left = 1 |
| 4 | 1 | 1 | 1 | 0, 1 | 3 | Found! Return True |

### Edge Case Testing

- **Empty input:** Constraints guarantee m, n >= 1.
- **Single element:** `[[5]]`, target=5 → True. Target=3 → False.
- **Typical case:** Target in middle of matrix → logarithmic convergence.
- **Extreme values:** Target < matrix[0][0] or > matrix[-1][-1] → loop exits quickly.

### Complexity

- **Time:** O(log(m * n)) — equivalent to O(log m + log n), single binary search on virtual array.
- **Space:** O(1) — no extra data structures.

### Optimization Discussion

**Alternative: Two binary searches.** First binary search to find the correct row (last row whose first element <= target), then binary search within that row. Same complexity, slightly more code.

### Follow-up Variations

- **Search a 2D Matrix II (LC 240):** Rows and columns sorted but no row-linking property. Requires staircase search O(m + n).
- What if the matrix is very large and stored on disk? (Minimize random accesses.)

### Common Traps

- **Wrong index conversion:** `row = mid // cols` and `col = mid % cols`. Using `rows` instead of `cols` is a common bug.
- **Confusing with LC 240:** This problem has the row-linking guarantee. LC 240 does not — different approach needed.
- **Off-by-one on `right`:** Should be `rows * cols - 1`, not `rows * cols`.
