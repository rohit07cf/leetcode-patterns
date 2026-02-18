# Common Graph Tricks for Interviews

## Baby Explanation (ELI10)

- These are "secret moves" that experienced coders use to solve graph problems faster
- Each trick is a small twist on BFS/DFS that unlocks a new type of problem
- Think of them as power-ups: once you learn them, hard problems become easy
- Tricks 1, 2, 6, 7, and 8 are essential for FAANG interviews

---

## Trick 1: Build Adjacency List from Edge List

The FIRST thing you do in almost every graph problem.

```python
from collections import defaultdict

def build_graph(edges, directed=False, weighted=False):
    graph = defaultdict(list)
    for edge in edges:
        if weighted:
            u, v, w = edge
            graph[u].append((v, w))
            if not directed: graph[v].append((u, w))
        else:
            u, v = edge
            graph[u].append(v)
            if not directed: graph[v].append(u)
    return graph
```

```
[[0,1], [0,2], [1,3]]  ->  {0:[1,2], 1:[0,3], 2:[0], 3:[1]}
```

---

## Trick 2: Multi-Source BFS

Start BFS from MANY nodes at once. Like dropping multiple stones in a pond.

```
Rotting Oranges: 2=rotten, 1=fresh. Rotten spreads each minute.
  2 1 1       Start ALL rotten oranges in queue at once.
  1 1 0       BFS spreads from all simultaneously.
  0 1 1
```

```python
from collections import deque

def multi_source_bfs(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))      # ALL sources at once
            elif grid[r][c] == 1:
                fresh += 1

    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    max_time = 0
    while queue:
        r, c, time = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                max_time = time + 1
                queue.append((nr, nc, time + 1))
    return max_time if fresh == 0 else -1
```

---

## Trick 3: Bidirectional BFS

Search from BOTH start and end. Meet in the middle. Cuts search space!

```
Normal:  Start ---------> End     Area: O(b^d)
Bidir:   Start ---> <--- End      Area: O(2 * b^(d/2))
```

```python
def bidirectional_bfs(graph, start, end):
    if start == end: return 0
    front_s, front_e = {start}, {end}
    vis_s, vis_e = {start}, {end}
    level = 0
    while front_s and front_e:
        level += 1
        if len(front_s) > len(front_e):          # Expand smaller side
            front_s, front_e = front_e, front_s
            vis_s, vis_e = vis_e, vis_s
        nxt = set()
        for node in front_s:
            for nb in graph[node]:
                if nb in vis_e: return level      # Met!
                if nb not in vis_s:
                    vis_s.add(nb)
                    nxt.add(nb)
        front_s = nxt
    return -1
```

---

## Trick 4: 0-1 BFS (Deque Trick)

Weights are only 0 or 1? Use a deque. Weight-0 goes to FRONT, weight-1 to BACK.
Like Dijkstra but O(V+E) instead of O((V+E) log V).

```python
from collections import deque

def zero_one_bfs(graph, start, n):
    """graph[u] = [(v, weight)] where weight is 0 or 1."""
    dist = [float('inf')] * n
    dist[start] = 0
    dq = deque([start])
    while dq:
        node = dq.popleft()
        for nb, w in graph[node]:
            if dist[node] + w < dist[nb]:
                dist[nb] = dist[node] + w
                if w == 0: dq.appendleft(nb)      # Free -> front
                else:      dq.append(nb)           # Cost 1 -> back
    return dist
```

---

## Trick 5: Implicit Graphs (State = Node)

No explicit graph given. "Nodes" are states, compute neighbors on the fly.

```
Word Ladder: "hit" -> "hot" -> "dot" -> "dog" -> "cog"
  Each word = node. Neighbors = words differing by 1 letter.
  Shortest transformation = BFS!

Open the Lock: state = "0000", neighbors = turn any digit +/- 1.
```

```python
from collections import deque

def word_ladder(begin, end, word_list):
    words = set(word_list)
    if end not in words: return 0
    queue = deque([(begin, 1)])
    visited = {begin}
    while queue:
        word, steps = queue.popleft()
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                nxt = word[:i] + c + word[i+1:]
                if nxt == end: return steps + 1
                if nxt in words and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
    return 0
```

---

## Trick 6: Detect Cycle in Directed Graph (3 Colors)

WHITE=unvisited, GRAY=in current path, BLACK=done. Hit GRAY = CYCLE!

```
    A ---> B ---> C
           ^      |
           |      v
           +------D     B is GRAY when reached from D -> CYCLE!
```

```python
def has_cycle_directed(graph, n):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    def dfs(node):
        color[node] = GRAY
        for nb in graph[node]:
            if color[nb] == GRAY: return True        # Cycle!
            if color[nb] == WHITE and dfs(nb): return True
        color[node] = BLACK
        return False
    return any(color[i] == WHITE and dfs(i) for i in range(n))
```

---

## Trick 7: Detect Cycle in Undirected Graph

Cycle = visiting a node that is already visited AND is NOT our parent.

```
    A --- B       DFS: A->B->D->C->A
    |     |       At C, neighbor A is visited but A != parent (D).
    C --- D       Visited + not parent = CYCLE!
```

```python
def has_cycle_undirected(graph, n):
    visited = set()
    def dfs(node, parent):
        visited.add(node)
        for nb in graph[node]:
            if nb not in visited:
                if dfs(nb, node): return True
            elif nb != parent: return True       # Cycle!
        return False
    return any(i not in visited and dfs(i, -1) for i in range(n))
```

---

## Trick 8: Clone Graph Pattern

Deep copy a graph. Use hashmap {old_node: new_node} to avoid infinite loops.

```
Original:  1---2     Clone:  1'---2'
           |   |             |    |
           4---3             4'---3'
```

```python
def clone_graph(node):
    if not node: return None
    old_to_new = {}
    def dfs(node):
        if node in old_to_new: return old_to_new[node]
        clone = Node(node.val)
        old_to_new[node] = clone              # Register BEFORE recursing!
        for nb in node.neighbors:
            clone.neighbors.append(dfs(nb))
        return clone
    return dfs(node)
```

Register BEFORE recursing -- otherwise A clones B, B clones A, infinite loop!

---

## Top 5 Mistakes Beginners Make

1. **Using Trick 7 on directed graphs** -- parent check only works undirected; use 3-color
2. **Forgetting to register clone BEFORE recursing** (Trick 8) -- infinite loops
3. **Multi-source BFS: adding sources one at a time** -- must add ALL at once
4. **Implicit graphs: unclear state definition** -- ask "what is a node? what are neighbors?"
5. **0-1 BFS: using regular queue** instead of deque -- breaks correctness

## Complexity Summary

```
Trick 1 (Build graph):       O(E) time, O(V+E) space
Trick 2 (Multi-source BFS):  O(V+E) time, O(V) space
Trick 3 (Bidirectional BFS): O(b^(d/2)) time
Trick 4 (0-1 BFS):           O(V+E) time, O(V) space
Trick 5 (Implicit graph):    Depends on state space
Trick 6 (Cycle directed):    O(V+E) time, O(V) space
Trick 7 (Cycle undirected):  O(V+E) time, O(V) space
Trick 8 (Clone graph):       O(V+E) time, O(V) space
```

## What To Say In Interview (Talk Track)

> "I recognize this as a [multi-source BFS / implicit graph / cycle detection]
> problem. The key insight is [all sources start simultaneously / states are
> nodes / we track visited states with colors]. Let me code the standard
> template for this pattern."
