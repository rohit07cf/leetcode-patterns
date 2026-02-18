# BFS -- Breadth-First Search

## Baby Explanation (ELI10)

- BFS is like dropping a stone in a pond -- **ripples spread outward layer by layer**
- First you visit all neighbors 1 step away, then 2 steps, then 3 steps...
- It uses a **queue** (first in, first out -- like a line at the grocery store)
- BFS naturally finds the **shortest path** in unweighted graphs (because it explores closest nodes first!)
- Think of it as: "Visit ALL friends first, THEN friends-of-friends, THEN friends-of-friends-of-friends"
- The **visited set** prevents infinite loops -- without it, A visits B, B visits A, A visits B... forever!

## Pattern Recognition

Use BFS when you see:
- "Shortest path" in an **unweighted** graph
- "Minimum number of steps/moves/hops"
- "Level by level" or "layer by layer" traversal
- "Nearest" or "closest" something
- "Spread" or "infection" problems (rotten oranges, fire spreading)

Avoid when:
- You need to explore ALL paths (use DFS/backtracking)
- Graph has weighted edges (use Dijkstra)
- You need to detect cycles in directed graphs (DFS with colors is cleaner)
- Memory is very tight (BFS can use more memory than DFS)

## Minimal Python Template

```python
from collections import deque

def bfs(graph, start):
    """BFS traversal from a starting node."""
    visited = set([start])       # Track what we have seen
    queue = deque([start])       # FIFO queue

    while queue:
        node = queue.popleft()   # Take from FRONT of queue
        # process(node)          # Do something with this node

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)      # Mark BEFORE adding to queue!
                queue.append(neighbor)     # Add to BACK of queue

    return visited
```

### BFS with Level Tracking (VERY common pattern!)

```python
from collections import deque

def bfs_levels(graph, start):
    """BFS that tracks distance / level from start."""
    visited = set([start])
    queue = deque([start])
    level = 0

    while queue:
        level_size = len(queue)           # How many nodes at THIS level?

        for _ in range(level_size):       # Process entire level
            node = queue.popleft()
            # process(node, level)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        level += 1                        # Move to next level

    return level  # total number of levels
```

### BFS Shortest Path (with parent tracking)

```python
from collections import deque

def bfs_shortest_path(graph, start, target):
    """Find shortest path from start to target."""
    visited = set([start])
    queue = deque([(start, [start])])     # Store (node, path_so_far)

    while queue:
        node, path = queue.popleft()

        if node == target:
            return path                   # Found it! Return the path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []  # No path found
```

## Step-by-Step Example (Tiny Input)

```
Graph:
    A --- B --- E
    |     |
    C --- D

Start: A,  Target: E

Queue state at each step:
---------------------------------------------------------
Step 0:  queue = [A]           visited = {A}
         Pop A. Neighbors: B, C

Step 1:  queue = [B, C]        visited = {A, B, C}
         Pop B. Neighbors: A(skip), D, E

Step 2:  queue = [C, D, E]     visited = {A, B, C, D, E}
         Pop C. Neighbors: A(skip), D(skip)

Step 3:  queue = [D, E]        visited = {A, B, C, D, E}
         Pop D. Neighbors: B(skip), C(skip)

Step 4:  queue = [E]           visited = {A, B, C, D, E}
         Pop E. TARGET FOUND!

Path: A -> B -> E  (length 2 -- shortest!)
---------------------------------------------------------

WHY this is shortest: BFS explored level by level.
  Level 0: A
  Level 1: B, C        (1 step from A)
  Level 2: D, E        (2 steps from A)

  E is found at level 2 = shortest distance is 2
```

```
Visual of BFS exploration (like ripples):

  Level 0      Level 1       Level 2
  .......      .......       .......
  ...A...  ->  .B.A.C.  ->  .B.A.C.
  .......      .......       .D...E.

  Ripple 1: Visit A
  Ripple 2: Visit B, C (neighbors of A)
  Ripple 3: Visit D, E (neighbors of B and C)
```

## Why the Visited Set is CRITICAL

```
WITHOUT visited set:

  A --- B
  |     |
  C --- D

  Queue: [A]
  Pop A, add B, C     -> Queue: [B, C]
  Pop B, add A, D     -> Queue: [C, A, D]     <-- A is back!
  Pop C, add A, D     -> Queue: [A, D, A, D]  <-- duplicates!
  Pop A, add B, C     -> Queue: [D, A, D, B, C]  <-- INFINITE LOOP!

  The program will run FOREVER and crash with out-of-memory.

WITH visited set:
  We skip nodes already in visited -> each node processed exactly once
  Time: O(V + E), not infinity!
```

## BFS vs DFS -- When to Use Which?

```
+-----------------------------+----------+---------+
| Situation                   |   BFS    |   DFS   |
+-----------------------------+----------+---------+
| Shortest path (unweighted)  |    Y     |    N    |
| Level-by-level traversal    |    Y     |    N    |
| Nearest/closest node        |    Y     |    N    |
| Explore all paths           |    N     |    Y    |
| Detect cycle (directed)     |  Meh     |    Y    |
| Topological sort            | Y(Kahn)  | Y(DFS)  |
| Less memory usage           |    N     |    Y    |
| Connected components        |    Y     |    Y    |
+-----------------------------+----------+---------+

Rule of thumb:
  "Shortest" or "minimum steps" -> BFS
  "All paths" or "any path"     -> DFS
  Everything else               -> either works
```

## Common Variations

1. **Multi-source BFS** -- start from multiple nodes at once (e.g., rotten oranges)
2. **0-1 BFS** -- edges have weight 0 or 1, use deque instead of queue
3. **Bidirectional BFS** -- search from both start and end, meet in middle
4. **BFS on grid** -- neighbors are up/down/left/right cells
5. **BFS with state** -- node = (position, some_state), not just position

## Top 5 Mistakes Beginners Make

1. **Adding to visited AFTER popping** instead of WHEN adding to queue
   - This causes duplicates in the queue and TLE (time limit exceeded)
   - ALWAYS mark visited when you ADD to queue, not when you POP
2. **Using a list instead of deque** -- `list.pop(0)` is O(n), `deque.popleft()` is O(1)
3. **Forgetting the visited set** -- infinite loops and crashes
4. **Not tracking levels** when the problem asks for shortest distance
5. **Using BFS on weighted graphs** -- BFS only gives shortest path for unweighted!

## Complexity (Time + Space)

```
Time:  O(V + E)
  - Each node is visited once: O(V)
  - Each edge is checked once: O(E)

Space: O(V)
  - Visited set: O(V)
  - Queue can hold up to O(V) nodes in worst case

V = number of vertices (nodes)
E = number of edges
```

## What To Say In Interview (Talk Track)

> "Since we need the shortest path in an unweighted graph, BFS is the right
> choice because it explores nodes level by level, guaranteeing the first time
> we reach the target is via the shortest path. I will use a queue and a visited
> set to avoid revisiting nodes. Time complexity is O(V + E) and space is O(V)."
