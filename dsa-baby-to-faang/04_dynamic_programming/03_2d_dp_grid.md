# 2D Dynamic Programming: Grids and Strings

## Baby Explanation (ELI10)

- 2D DP means your answer depends on TWO things that change (like row AND column).
- Instead of a single row of boxes, you fill an entire grid -- like a spreadsheet.
- Each cell dp[i][j] is computed from its neighbors (usually above and left).
- Imagine you are on a checkerboard. At each square, you look at where you came
  from (above or left) and pick the best path so far.
- Grid DP is just 1D DP with an extra dimension. If you understood 1D, you can
  do 2D. Breathe. You got this.

## Pattern Recognition

Use this when you see:
- A 2D grid and "find the minimum/maximum path"
- "How many ways to go from top-left to bottom-right?"
- Two strings and "edit distance" / "longest common" / "matching"
- Any problem where you need to track two indices

Avoid when:
- Only one variable changes (use 1D DP)
- The grid has obstacles that block everything (might need BFS instead)
- You need the actual path, not just the count/cost (need backtracking on top)

## 2D Grid DP Template

```python
def solve(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]

    dp[0][0] = grid[0][0]                   # base case: top-left corner

    # Fill first row (can only come from the left)
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Fill first column (can only come from above)
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Fill the rest
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = combine(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[rows - 1][cols - 1]
```

---

## Problem 1: Unique Paths (LeetCode 62)

**The question:** A robot starts at the top-left corner of an m x n grid.
It can only move right or down. How many unique paths to the bottom-right?

### State, Transition, Base Case

```
  State:      dp[i][j] = number of ways to reach cell (i, j)
  Transition: dp[i][j] = dp[i-1][j] + dp[i][j-1]
              (ways from above + ways from left)
  Base case:  dp[0][j] = 1  (only one way across top row: go right)
              dp[i][0] = 1  (only one way down first column: go down)
```

### Step-by-Step Example

- Input: m = 3, n = 4 (3 rows, 4 columns)

```
  Initialize first row and first column to 1:

       col0  col1  col2  col3
  row0 [ 1 ] [ 1 ] [ 1 ] [ 1 ]
  row1 [ 1 ] [   ] [   ] [   ]
  row2 [ 1 ] [   ] [   ] [   ]

  Fill cell by cell (top + left):

  dp[1][1] = dp[0][1] + dp[1][0] = 1 + 1 = 2
  dp[1][2] = dp[0][2] + dp[1][1] = 1 + 2 = 3
  dp[1][3] = dp[0][3] + dp[1][2] = 1 + 3 = 4
  dp[2][1] = dp[1][1] + dp[2][0] = 2 + 1 = 3
  dp[2][2] = dp[1][2] + dp[2][1] = 3 + 3 = 6
  dp[2][3] = dp[1][3] + dp[2][2] = 4 + 6 = 10

       col0  col1  col2  col3
  row0 [ 1 ] [ 1 ] [ 1 ] [ 1 ]
  row1 [ 1 ] [ 2 ] [ 3 ] [ 4 ]
  row2 [ 1 ] [ 3 ] [ 6 ] [10 ]
```

- Output: 10

### Code

```python
def uniquePaths(m, n):
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]
```

**Time:** O(m * n) | **Space:** O(m * n)

---

## Problem 2: Minimum Path Sum (LeetCode 64)

**The question:** Given an m x n grid filled with non-negative numbers,
find a path from top-left to bottom-right which minimizes the sum.
You can only move right or down.

### State, Transition, Base Case

```
  State:      dp[i][j] = minimum cost to reach cell (i, j)
  Transition: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
  Base case:  dp[0][0] = grid[0][0]
              First row: dp[0][j] = dp[0][j-1] + grid[0][j]
              First col: dp[i][0] = dp[i-1][0] + grid[i][0]
```

### Step-by-Step Example

- Input: grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

```
  Original grid:         Fill dp table:
  [1] [3] [1]
  [1] [5] [1]            Base: dp[0][0] = 1
  [4] [2] [1]

  First row: 1 -> 1+3=4 -> 4+1=5
  First col: 1 -> 1+1=2 -> 2+4=6

       col0  col1  col2
  row0 [ 1 ] [ 4 ] [ 5 ]
  row1 [ 2 ] [   ] [   ]
  row2 [ 6 ] [   ] [   ]

  dp[1][1] = min(4, 2) + 5 = 2 + 5 = 7
  dp[1][2] = min(5, 7) + 1 = 5 + 1 = 6
  dp[2][1] = min(7, 6) + 2 = 6 + 2 = 8
  dp[2][2] = min(6, 8) + 1 = 6 + 1 = 7

       col0  col1  col2
  row0 [ 1 ] [ 4 ] [ 5 ]
  row1 [ 2 ] [ 7 ] [ 6 ]
  row2 [ 6 ] [ 8 ] [ 7 ]
```

- Output: 7 (path: 1 -> 3 -> 1 -> 1 -> 1)

### Code

```python
def minPathSum(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]

    dp[0][0] = grid[0][0]

    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[rows - 1][cols - 1]
```

**Time:** O(m * n) | **Space:** O(m * n)

---

## Problem 3: Edit Distance -- Brief Intro (LeetCode 72)

**The question:** Given two strings, find the minimum number of operations
(insert, delete, replace) to convert one string to the other.

### State, Transition, Base Case

```
  State:      dp[i][j] = min operations to convert word1[0..i-1] to word2[0..j-1]
  Transition: if word1[i-1] == word2[j-1]:
                  dp[i][j] = dp[i-1][j-1]         (chars match, no cost)
              else:
                  dp[i][j] = 1 + min(
                      dp[i-1][j],                  (delete from word1)
                      dp[i][j-1],                  (insert into word1)
                      dp[i-1][j-1]                 (replace)
                  )
  Base case:  dp[i][0] = i  (delete all chars from word1)
              dp[0][j] = j  (insert all chars of word2)
```

### Tiny Example: "cat" -> "cut"

```
         ""   c    u    t
    ""  [ 0] [ 1] [ 2] [ 3]
    c   [ 1] [ 0] [ 1] [ 2]
    a   [ 2] [ 1] [ 1] [ 2]
    t   [ 3] [ 2] [ 2] [ 1]
```

Answer: 1 (replace 'a' with 'u')

---

## Space Optimization: The Rolling Array Trick

You usually fill row by row, and each row only depends on the row above.
So you only need TWO rows instead of the full grid!

```
  Before (full grid):    After (two rows only):
  [row 0]                prev = [row 0]
  [row 1]                curr = [row 1]
  [row 2]                --> swap: prev = curr, compute new curr
  [row 3]

  Space: O(m * n)  -->   Space: O(n)    (just one row!)
```

```python
def minPathSum_optimized(grid):
    rows, cols = len(grid), len(grid[0])
    prev = [0] * cols

    prev[0] = grid[0][0]
    for j in range(1, cols):
        prev[j] = prev[j - 1] + grid[0][j]

    for i in range(1, rows):
        curr = [0] * cols
        curr[0] = prev[0] + grid[i][0]
        for j in range(1, cols):
            curr[j] = min(prev[j], curr[j - 1]) + grid[i][j]
        prev = curr

    return prev[cols - 1]
```

## The Fill Direction Cheat Sheet

```
  Problem                  Fill order
  ------------------------------------------
  Unique Paths             top-left --> bottom-right
  Minimum Path Sum         top-left --> bottom-right
  Edit Distance            top-left --> bottom-right
  Longest Palindrome Sub.  bottom-left --> top-right (or by length)
```

## Common Variations

| Problem              | dp[i][j] means                          | Transition                        |
|----------------------|-----------------------------------------|-----------------------------------|
| Unique Paths         | ways to reach (i,j)                     | top + left                        |
| Min Path Sum         | min cost to reach (i,j)                 | min(top, left) + grid[i][j]       |
| Edit Distance        | min ops for word1[:i] to word2[:j]      | match/insert/delete/replace       |
| Longest Common Subseq| LCS of first i and first j chars        | match: diag+1, else max(top,left) |

## Top 5 Mistakes Beginners Make

1. **Forgetting to fill first row and first column separately.** They are edge cases!
2. **Index confusion.** dp might be (m+1) x (n+1) for string problems.
3. **Wrong fill direction.** Always fill so dependencies are already computed.
4. **Not seeing the space optimization.** Mention the rolling array trick to impress.
5. **Confusing grid value vs dp value.** grid[i][j] is input, dp[i][j] is your answer.

## Complexity (Time + Space)

- All grid problems: O(m * n) time
- Space: O(m * n) full table, O(n) with rolling array optimization

## What To Say In Interview (Talk Track)

> "This is a 2D DP problem. My state dp[i][j] represents [meaning].
> At each cell, I can arrive from [above/left/diagonal], so
> the transition is dp[i][j] = [formula].
> Base cases: first row is [X], first column is [Y].
> I will fill top-left to bottom-right. Let me trace a 3x3 example.
> For space optimization, I can use a rolling array to reduce O(m*n) to O(n)."
