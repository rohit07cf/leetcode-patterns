# Grid as Graph -- Islands and Flood Fill

## Baby Explanation (ELI10)

- A grid (like a chessboard) IS a graph in disguise!
- Each cell is a **node**, and neighbors are the cells **up, down, left, right**
- You do NOT need to build an adjacency list -- just check 4 directions
- "Number of Islands" = "How many groups of connected land cells?"
- **Flood fill** = start at one cell and "paint" all connected cells (like the paint bucket tool in MS Paint)
- The grid IS the graph. No conversion needed. Just treat it like one!

## The Grid-to-Graph Conversion Trick

```
Grid:                        Graph (implicit):
+---+---+---+                Each cell (r,c) has up to 4 neighbors:
| 0 | 1 | 2 |                  - UP:    (r-1, c)
+---+---+---+                  - DOWN:  (r+1, c)
| 3 | 4 | 5 |                  - LEFT:  (r, c-1)
+---+---+---+                  - RIGHT: (r, c+1)
| 6 | 7 | 8 |
+---+---+---+

Cell 4 neighbors: cell 1 (up), cell 7 (down), cell 3 (left), cell 5 (right)
Cell 0 neighbors: cell 1 (right), cell 3 (down)  -- only 2! (corners have fewer)

The DIRECTIONS array:
  directions = [(-1,0), (1,0), (0,-1), (0,1)]
                  up     down   left    right
```

## Pattern Recognition

Use grid-as-graph when you see:
- 2D matrix with "land" and "water" (1s and 0s)
- "Number of islands", "max area", "perimeter"
- "Shortest path in a maze/grid"
- "Flood fill" or "paint" adjacent cells
- "Rotting oranges" (multi-source BFS on grid)
- Any 2D grid where you explore connected regions

Avoid when:
- The grid represents a different structure (like a DP table)
- Connections are not just up/down/left/right (diagonal, knight moves, etc.)
  -- You CAN still use this approach, just change the directions array!

## Number of Islands -- The Classic Problem

```
Grid:
  1 1 0 0 0
  1 1 0 0 0
  0 0 1 0 0
  0 0 0 1 1

Land = 1, Water = 0

How many islands? 3

  [1 1] 0  0  0       Island 1: top-left block
  [1 1] 0  0  0
   0  0 [1] 0  0       Island 2: center cell
   0  0  0 [1 1]       Island 3: bottom-right block
```

### Solution: DFS Flood Fill

```python
def num_islands(grid):
    """Count number of islands using DFS flood fill."""
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        # Boundary check + water check + already visited check
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return

        grid[r][c] = '0'               # Mark as visited (sink the land)

        dfs(r - 1, c)                   # Up
        dfs(r + 1, c)                   # Down
        dfs(r, c - 1)                   # Left
        dfs(r, c + 1)                   # Right

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':       # Found unvisited land!
                dfs(r, c)               # Flood fill entire island
                count += 1             # One more island found

    return count
```

## Grid BFS Template

```python
from collections import deque

def grid_bfs(grid, start_r, start_c):
    """BFS on a grid from a starting cell."""
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]   # up, down, left, right

    visited = set()
    visited.add((start_r, start_c))
    queue = deque([(start_r, start_c, 0)])         # (row, col, distance)

    while queue:
        r, c, dist = queue.popleft()
        # process(r, c, dist)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Boundary check
            if 0 <= nr < rows and 0 <= nc < cols:
                # Valid cell check (not wall, not visited)
                if (nr, nc) not in visited and grid[nr][nc] != 0:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

    return visited
```

## Grid DFS Template

```python
def grid_dfs(grid, r, c, visited):
    """DFS on a grid from cell (r, c)."""
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    visited.add((r, c))
    # process(r, c)

    for dr, dc in directions:
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            if (nr, nc) not in visited and grid[nr][nc] == 1:
                grid_dfs(grid, nr, nc, visited)
```

## Step-by-Step Example -- BFS on Grid

```
Grid (1=path, 0=wall):
  1 1 0
  0 1 0
  0 1 1

Start: (0,0)  Target: (2,2)
Find shortest path.

BFS trace:
-------------------------------------------------------
Pop (0,0,d=0): right (0,1) valid  -> Queue: [(0,1,1)]
Pop (0,1,d=1): down  (1,1) valid  -> Queue: [(1,1,2)]
Pop (1,1,d=2): down  (2,1) valid  -> Queue: [(2,1,3)]
Pop (2,1,d=3): right (2,2) valid  -> TARGET FOUND! dist=4
-------------------------------------------------------

Path visualization:
  S * 0       S = Start, E = End, * = path
  0 * 0
  0 * E       Shortest path distance = 4
```

## Max Area of Island

```python
def max_area_of_island(grid):
    """Find the largest island by area."""
    rows, cols = len(grid), len(grid[0])
    max_area = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
            return 0

        grid[r][c] = 0                     # Mark visited
        area = 1                           # Count this cell

        area += dfs(r - 1, c)             # Add area from all 4 directions
        area += dfs(r + 1, c)
        area += dfs(r, c - 1)
        area += dfs(r, c + 1)

        return area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))

    return max_area
```

## Visited: Separate Set vs Modify Grid In-Place

```
Option 1: Modify grid in-place (saves space)
  grid[r][c] = 0     # "Sink" the land after visiting
  Pros: No extra space needed
  Cons: Destroys the original grid

Option 2: Separate visited set
  visited = set()
  visited.add((r, c))
  Pros: Preserves original grid
  Cons: O(R*C) extra space

In interviews:
  - Ask: "Can I modify the input grid?"
  - If yes: modify in-place (cleaner, less space)
  - If no: use a visited set
```

## Boundary Checking -- The Most Common Bug

```python
# The boundary check you will write 1000 times:
if 0 <= nr < rows and 0 <= nc < cols:
    # valid cell, safe to access grid[nr][nc]

# Alternatively, check FIRST in recursive DFS:
def dfs(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return    # Out of bounds!
    if grid[r][c] != 1:
        return    # Not land (or already visited)
    # ... process cell
```

## Common Variations

1. **Number of Islands** -- count connected components of 1s
2. **Max Area of Island** -- DFS returns area count
3. **Surrounded Regions** -- BFS/DFS from border O's, flip the rest
4. **Rotting Oranges** -- multi-source BFS from all rotten oranges at once
5. **Shortest Path in Binary Matrix** -- BFS with 8 directions
6. **Walls and Gates** -- multi-source BFS from all gates
7. **Pacific Atlantic Water Flow** -- BFS/DFS from both oceans inward

## Top 5 Mistakes Beginners Make

1. **Forgetting boundary checks** -- accessing `grid[-1][0]` crashes (or wraps in Python!)
2. **Not marking visited BEFORE recursing** -- causes infinite loops
3. **Using wrong directions** -- double-check: `(-1,0)` is UP (row decreases going up)
4. **Forgetting diagonal directions** when problem says 8-connected
5. **Modifying grid when you should not** -- always ask "Can I modify the input?"

## Complexity (Time + Space)

```
Time:  O(R * C)  -- each cell visited at most once
Space: O(R * C)  -- visited set + queue/recursion stack
       O(min(R,C)) for BFS queue if modifying grid in-place
```

## What To Say In Interview (Talk Track)

> "I will treat this grid as an implicit graph where each cell is a node and
> its 4 neighbors (up, down, left, right) are edges. I will iterate through
> every cell, and when I find an unvisited land cell, I will perform DFS/BFS
> to mark all connected land cells as visited. Each complete DFS/BFS discovers
> one island. I will modify the grid in-place to mark visited cells, avoiding
> extra space. Time is O(R*C) since each cell is visited at most once."
