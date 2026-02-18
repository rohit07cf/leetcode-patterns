# DFS -- Depth-First Search

## Baby Explanation (ELI10)

- DFS is like exploring a maze: **always go as deep as possible, then backtrack**
- Imagine you are in a maze and always turn left -- you go deep into one path until you hit a dead end, then come back and try the next path
- It uses a **stack** (last in, first out -- like a stack of plates)
- The recursive version uses the **call stack** automatically (Python does this for you!)
- DFS is great for: "Can I reach X from Y?", "Find all paths", "Detect cycles"
- Just like BFS, the **visited set** prevents infinite loops

## Pattern Recognition

Use DFS when you see:
- "Find if a path exists" (any path, not necessarily shortest)
- "Find ALL paths" or "count all paths"
- "Connected components" (how many groups?)
- "Detect a cycle" in a directed graph
- "Topological sort" (DFS-based approach)
- "Island" problems (flood fill)

Avoid when:
- "Shortest path" or "minimum steps" (use BFS)
- "Nearest" or "closest" (use BFS)
- "Level by level" traversal (use BFS)

## Minimal Python Template -- Recursive DFS

```python
def dfs(graph, node, visited):
    """DFS traversal using recursion."""
    visited.add(node)
    # process(node)              # Do something with this node

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Usage:
visited = set()
dfs(graph, start_node, visited)
```

### Recursive DFS -- Finding a Path

```python
def dfs_has_path(graph, node, target, visited):
    """Check if there is a path from node to target."""
    if node == target:
        return True

    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs_has_path(graph, neighbor, target, visited):
                return True           # Found it! Propagate True up

    return False                      # Tried all paths, no luck
```

## Minimal Python Template -- Iterative DFS (Using Stack)

```python
def dfs_iterative(graph, start):
    """DFS traversal using an explicit stack."""
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()            # Take from TOP of stack (LIFO)

        if node in visited:
            continue
        visited.add(node)
        # process(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    return visited
```

**KEY DIFFERENCE from BFS:**
```
BFS:  queue = deque()   -> queue.popleft()    (FIFO - first in, first out)
DFS:  stack = []        -> stack.pop()        (LIFO - last in, first out)

That is the ONLY difference in the iterative versions!
```

## Step-by-Step Example -- Recursive DFS

```
Graph:
    A --- B --- E
    |     |
    C --- D

DFS starting from A:
---------------------------------------------------------
Call dfs(A)
  visited = {A}
  Neighbor B: not visited -> call dfs(B)
    |
    +-> Call dfs(B)
        visited = {A, B}
        Neighbor A: skip (visited)
        Neighbor D: not visited -> call dfs(D)
          |
          +-> Call dfs(D)
              visited = {A, B, D}
              Neighbor B: skip (visited)
              Neighbor C: not visited -> call dfs(C)
                |
                +-> Call dfs(C)
                    visited = {A, B, D, C}
                    Neighbor A: skip (visited)
                    Neighbor D: skip (visited)
                    No more neighbors -> RETURN (backtrack)
                |
              Neighbor E: not visited -> call dfs(E)  [Oops, D-E? Let me fix]
              No more neighbors -> RETURN (backtrack)
          |
        Neighbor E: not visited -> call dfs(E)
          |
          +-> Call dfs(E)
              visited = {A, B, D, C, E}
              No unvisited neighbors -> RETURN
          |
        No more neighbors -> RETURN
    |
  Neighbor C: skip (visited)
  DONE!

DFS order: A -> B -> D -> C -> E
---------------------------------------------------------
```

```
Recursion stack visualization:

  Call stack grows DOWN:

  dfs(A)
    dfs(B)
      dfs(D)
        dfs(C)          <-- hit dead end, backtrack
      dfs(E)            <-- backtrack to B, try next neighbor
                         <-- backtrack to A, C already visited
  DONE

  Think of it as going DEEP first:
  A -> B -> D -> C (dead end!) -> back to D -> back to B -> E
```

## DFS for Counting Connected Components

```python
def count_components(n, edges):
    """Count connected components in undirected graph."""
    from collections import defaultdict

    # Build graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    count = 0

    for node in range(n):              # Try every node as a starting point
        if node not in visited:
            dfs(graph, node, visited)  # This marks the entire component
            count += 1                 # One more component found

    return count
```

```
Example:
  n = 5, edges = [[0,1], [1,2], [3,4]]

    0 --- 1 --- 2       3 --- 4

  Start at 0: DFS visits {0, 1, 2} -> count = 1
  Skip 1 (visited), skip 2 (visited)
  Start at 3: DFS visits {3, 4}    -> count = 2

  Answer: 2 components
```

## DFS vs BFS -- Side by Side

```
Same graph, different exploration order:

    A --- B --- E
    |     |
    C --- D

  BFS from A:  A, B, C, D, E    (layer by layer)
    Level 0: A
    Level 1: B, C
    Level 2: D, E

  DFS from A:  A, B, D, C, E    (deep first, then backtrack)
    Go deep: A -> B -> D -> C (dead end) -> back -> E
```

## Common Variations

1. **DFS with path tracking** -- keep a `path` list, add before recursing, remove after
2. **DFS with cycle detection** -- use 3 colors (white/gray/black) for directed graphs
3. **DFS for topological sort** -- add to result in post-order (after visiting all neighbors)
4. **DFS on grid** -- neighbors are 4 directions (up/down/left/right)
5. **DFS with memoization** -- cache results of subproblems (bridges to DP!)

## Top 5 Mistakes Beginners Make

1. **Forgetting the visited set** -- infinite recursion, stack overflow crash
2. **Python recursion limit** -- default is 1000! For big graphs, add:
   ```python
   import sys
   sys.setrecursionlimit(10000)
   ```
   Or use iterative DFS instead.
3. **Not backtracking properly** -- for "find ALL paths", you must REMOVE from visited after recursing:
   ```python
   visited.add(node)
   dfs(neighbor)
   visited.remove(node)    # BACKTRACK -- so other paths can use this node
   ```
4. **Confusing DFS traversal order** -- pre-order (process before recursing) vs post-order (process after recursing) matters for topo sort
5. **Using DFS for shortest path** -- DFS does NOT guarantee shortest path! Use BFS for that.

## Complexity (Time + Space)

```
Time:  O(V + E)
  - Each node visited once: O(V)
  - Each edge checked once: O(E)

Space: O(V)
  - Visited set: O(V)
  - Recursion stack (or explicit stack): O(V) in worst case
    (worst case = graph is a long chain: 1 -> 2 -> 3 -> ... -> n)

V = number of vertices (nodes)
E = number of edges
```

## What To Say In Interview (Talk Track)

> "I will use DFS to explore the graph. Starting from the given node, I will
> recursively visit all unvisited neighbors, marking each node as visited to
> avoid cycles. For this problem, DFS works well because we need to explore
> connectivity / find if a path exists / count components. Time is O(V + E)
> and space is O(V) for the visited set and recursion stack."
