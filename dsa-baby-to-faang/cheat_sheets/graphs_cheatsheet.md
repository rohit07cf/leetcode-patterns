# Graphs Cheat Sheet

> Everything you need for graph problems in one place. Read this, then go win.

---

## The Grid Directions Helper (Copy-Paste This First)

```python
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]   # right, left, down, up

# For 8 directions (diagonals too):
dirs8 = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
```

---

## Build Adjacency List (Step 1 of Almost Every Graph Problem)

```python
from collections import defaultdict

# From edge list: [[0,1], [1,2], [0,2]]
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)       # remove this line for directed graph

# From adjacency matrix:
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            graph[i].append(j)
```

---

## BFS Template (Graphs)

```python
# Use when: shortest path (unweighted), level-by-level traversal
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### BFS Shortest Path (Unweighted)

```python
def shortest_path(graph, start, end):
    queue = deque([(start, 0)])      # (node, distance)
    visited = {start}
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append((nei, dist + 1))
    return -1                         # not reachable
```

---

## DFS Template (Recursive)

```python
# Use when: explore all paths, connected components, cycle detection
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

## DFS Template (Iterative — uses a stack)

```python
def dfs_iterative(graph, start):
    stack = [start]
    visited = {start}
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
```

---

## Grid BFS Template (Islands, Shortest Path in Matrix)

```python
from collections import deque

def grid_bfs(grid, start_r, start_c):
    rows, cols = len(grid), len(grid[0])
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    queue = deque([(start_r, start_c, 0)])     # row, col, distance
    visited = {(start_r, start_c)}
    while queue:
        r, c, dist = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols
                and (nr, nc) not in visited
                and grid[nr][nc] != 0):         # 0 = wall
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
```

## Grid DFS Template (Flood Fill, Island Counting)

```python
def grid_dfs(grid, r, c, visited):
    rows, cols = len(grid), len(grid[0])
    if (r < 0 or r >= rows or c < 0 or c >= cols
        or (r, c) in visited or grid[r][c] == 0):
        return
    visited.add((r, c))
    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        grid_dfs(grid, r + dr, c + dc, visited)
```

---

## Number of Islands Pattern

```python
def num_islands(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1" and (r, c) not in visited:
                grid_dfs(grid, r, c, visited)   # or BFS
                count += 1
    return count
```

---

## Topological Sort (Kahn's Algorithm — BFS-based)

```python
# Use when: ordering with prerequisites, course schedule, build order
from collections import deque, defaultdict

def topo_sort(num_nodes, edges):
    graph = defaultdict(list)
    in_degree = [0] * num_nodes
    for u, v in edges:              # u must come before v
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)

    return order if len(order) == num_nodes else []  # empty = cycle!
```

---

## Union Find (Disjoint Set Union)

```python
# Use when: connected components, "are X and Y connected?", grouping
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False                   # already connected
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px               # union by rank
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True
```

---

## Dijkstra's Algorithm (Shortest Path — Weighted Graphs)

```python
# Use when: shortest path with NON-NEGATIVE weights
import heapq
from collections import defaultdict

def dijkstra(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]                   # (distance, node)
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue                      # skip outdated entry
        for v, w in graph[u]:             # neighbor, weight
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist
```

---

## Cycle Detection

### Undirected Graph (DFS)

```python
def has_cycle_undirected(graph, n):
    visited = set()
    def dfs(node, parent):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei, node):
                    return True
            elif nei != parent:
                return True               # back edge = cycle
        return False
    for i in range(n):
        if i not in visited:
            if dfs(i, -1):
                return True
    return False
```

### Directed Graph (DFS with 3 colors)

```python
def has_cycle_directed(graph, n):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    def dfs(node):
        color[node] = GRAY                # in progress
        for nei in graph[node]:
            if color[nei] == GRAY:
                return True               # back edge = cycle
            if color[nei] == WHITE and dfs(nei):
                return True
        color[node] = BLACK                # done
        return False
    return any(color[i] == WHITE and dfs(i) for i in range(n))
```

---

## When to Use What — Decision Table

| Situation | Algorithm | Why |
|-----------|-----------|-----|
| Shortest path, unweighted | **BFS** | BFS guarantees shortest in unweighted |
| Shortest path, weighted (no negatives) | **Dijkstra** | Greedy with min-heap |
| Shortest path, negative weights | **Bellman-Ford** | Handles negatives |
| Detect cycle (undirected) | **DFS** or **Union Find** | Track parent or check connected |
| Detect cycle (directed) | **DFS (3 colors)** | Gray node revisited = cycle |
| Connected components | **BFS/DFS** or **Union Find** | Count separate explorations |
| Ordering with dependencies | **Topological Sort** | Kahn's BFS or DFS |
| "Is there a path?" | **BFS** or **DFS** | Either works |
| Minimum spanning tree | **Kruskal's** (Union Find) | Sort edges + union |
| Grid traversal | **Grid BFS/DFS** | Treat cells as nodes |
| Bipartite check | **BFS (2-coloring)** | Alternate colors, check conflict |

---

## Quick Reference: Problem -> Pattern

| Problem | Pattern |
|---------|---------|
| Number of islands | Grid DFS / BFS / Union Find |
| Clone graph | BFS + hashmap |
| Course schedule | Topological Sort |
| Course schedule II | Topological Sort (return order) |
| Shortest path in grid | Grid BFS |
| Network delay time | Dijkstra |
| Redundant connection | Union Find |
| Accounts merge | Union Find |
| Word ladder | BFS (each word = node) |
| Surrounded regions | DFS from border |
| Pacific Atlantic water flow | DFS from both oceans |
| Graph valid tree | Union Find (n-1 edges + no cycle) |
| Alien dictionary | Topological Sort |

---

## Common Mistakes to Avoid

1. Forgetting to mark visited BEFORE adding to queue (causes duplicates in BFS)
2. Using BFS for weighted shortest path (use Dijkstra instead!)
3. Not handling disconnected components (always loop over all nodes)
4. Grid problems: forgetting bounds check `0 <= nr < rows`
5. Directed vs undirected: forgetting to add both directions for undirected
6. Topological sort: not checking `len(order) == num_nodes` for cycle detection

---

## Complexity Reference

| Algorithm | Time | Space |
|-----------|------|-------|
| BFS / DFS | O(V + E) | O(V) |
| Topological Sort | O(V + E) | O(V + E) |
| Dijkstra (min-heap) | O((V + E) log V) | O(V) |
| Union Find (optimized) | O(alpha(n)) per op | O(V) |
| Grid BFS/DFS | O(rows * cols) | O(rows * cols) |

**Graphs are just trees with extra edges. You already know trees. You got this.**
