# Shortest Paths -- BFS vs Dijkstra

## Baby Explanation (ELI10)

- Imagine finding the fastest route to school
- If every road takes the **same time** (unweighted), just count roads -- that is **BFS**
- If roads take **different times** (weighted), you need to be smarter -- that is **Dijkstra**
- Dijkstra = "always go to the cheapest unvisited place next" (like a greedy shopper)
- Dijkstra uses a **priority queue** (min-heap) -- it always picks the smallest cost first
- If some roads have **negative** tolls (they PAY you to drive!), you need **Bellman-Ford**

## Pattern Recognition

Use BFS when you see:
- "Shortest path" and all edges have the **same weight** (or weight = 1)
- "Minimum number of steps/moves"
- Grid problems where each move costs 1

Use Dijkstra when you see:
- "Shortest path" and edges have **different positive weights**
- "Minimum cost to reach"
- "Cheapest flight" / "network delay"
- Weighted graph, all weights >= 0

Avoid both when:
- Graph has **negative weight edges** -- use Bellman-Ford
- You need ALL pairs shortest path -- consider Floyd-Warshall

## The Golden Rule

```
+--------------------------------------+-------------------+
|  Edge weights                        |  Algorithm        |
+--------------------------------------+-------------------+
|  All equal (or unweighted)           |  BFS              |
|  Non-negative, different weights     |  Dijkstra         |
|  Negative weights possible           |  Bellman-Ford     |
|  All pairs shortest path             |  Floyd-Warshall   |
|  Weights are only 0 or 1             |  0-1 BFS (deque)  |
+--------------------------------------+-------------------+
```

## BFS for Shortest Path (Unweighted)

```python
from collections import deque

def bfs_shortest(graph, start, target):
    """Shortest path in unweighted graph. Returns distance."""
    visited = set([start])
    queue = deque([(start, 0)])         # (node, distance)

    while queue:
        node, dist = queue.popleft()

        if node == target:
            return dist

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1   # Not reachable
```

## Dijkstra's Algorithm -- Template

```python
import heapq
from collections import defaultdict

def dijkstra(graph, start, target):
    """
    Shortest path in weighted graph (non-negative weights).
    graph[u] = [(v, weight), ...]
    Returns shortest distance from start to target.
    """
    # dist[node] = shortest known distance from start
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0

    # Min-heap: (distance, node)
    heap = [(0, start)]

    while heap:
        d, node = heapq.heappop(heap)

        if node == target:
            return d                    # Found shortest path!

        if d > dist[node]:
            continue                    # Skip outdated entry

        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return -1   # Not reachable
```

### Dijkstra -- All Distances from Start

```python
def dijkstra_all(graph, start, n):
    """Return shortest distance from start to ALL other nodes."""
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, node = heapq.heappop(heap)

        if d > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return dist
```

## Step-by-Step Dijkstra Example

```
Weighted graph:
    A ---4--- B
    |         |
    2         1
    |         |
    C ---3--- D ---5--- E

graph = {
    'A': [('B',4), ('C',2)],
    'B': [('A',4), ('D',1)],
    'C': [('A',2), ('D',3)],
    'D': [('B',1), ('C',3), ('E',5)],
    'E': [('D',5)]
}

Find shortest path from A to E:

Heap: [(0, A)]        dist = {A:0}

Step 1: Pop (0, A)
  Neighbor B: 0+4=4 < inf -> dist[B]=4, push (4,B)
  Neighbor C: 0+2=2 < inf -> dist[C]=2, push (2,C)
  Heap: [(2,C), (4,B)]

Step 2: Pop (2, C)     <-- cheapest first!
  Neighbor A: 2+2=4 > 0 (dist[A]) -> skip
  Neighbor D: 2+3=5 < inf -> dist[D]=5, push (5,D)
  Heap: [(4,B), (5,D)]

Step 3: Pop (4, B)
  Neighbor A: 4+4=8 > 0 -> skip
  Neighbor D: 4+1=5 = 5 (dist[D]) -> not less, skip
  Heap: [(5,D)]

Step 4: Pop (5, D)
  Neighbor B: 5+1=6 > 4 -> skip
  Neighbor C: 5+3=8 > 2 -> skip
  Neighbor E: 5+5=10 < inf -> dist[E]=10, push (10,E)
  Heap: [(10,E)]

Step 5: Pop (10, E) -- TARGET!
  Answer: 10

Shortest path: A -2-> C -3-> D -5-> E = 10
  (NOT A -4-> B -1-> D -5-> E = 10... same cost, different path)

  A ---4--- B
  |         |
  2*        1
  |         |
  C ---3*-- D ---5*-- E

  Path: A -> C -> D -> E, cost = 2+3+5 = 10
```

## Bellman-Ford (Brief Mention)

```python
def bellman_ford(n, edges, start):
    """
    Handles NEGATIVE weights. Detects negative cycles.
    edges: [(u, v, weight), ...]
    """
    dist = [float('inf')] * n
    dist[start] = 0

    # Relax ALL edges, n-1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative cycles (one more round)
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None       # Negative cycle detected!

    return dist
```

```
Time: O(V * E) -- much slower than Dijkstra!
Use ONLY when you have negative weights.
```

## Decision Table -- Which Algorithm?

```
Q: Do all edges have the same weight (or no weights)?
  YES -> BFS  (simple, fast, O(V+E))
  NO  -> continue...

Q: Are all weights non-negative?
  YES -> Dijkstra  (O((V+E) log V) with heap)
  NO  -> continue...

Q: Do you need single-source shortest path?
  YES -> Bellman-Ford  (O(V*E), handles negative weights)
  NO  -> Floyd-Warshall  (O(V^3), all pairs)
```

## Common Variations

1. **Network Delay Time** -- Dijkstra to all nodes, return max distance
2. **Cheapest Flights Within K Stops** -- modified Dijkstra/Bellman-Ford with constraint
3. **Path With Minimum Effort** -- Dijkstra where edge weight = elevation difference
4. **Swim in Rising Water** -- Dijkstra on grid
5. **Shortest Path in Binary Matrix** -- BFS on grid (all weights = 1)

## Top 5 Mistakes Beginners Make

1. **Using BFS on weighted graphs** -- BFS does NOT consider weights!
2. **Forgetting `if d > dist[node]: continue`** in Dijkstra -- leads to processing stale entries and TLE
3. **Using Dijkstra with negative weights** -- Dijkstra does NOT work with negative weights
4. **Not building the graph correctly** -- for Dijkstra, store `(neighbor, weight)` tuples
5. **Forgetting that heapq is a MIN-heap** -- smallest element comes out first (which is what we want)

## Complexity (Time + Space)

```
BFS:
  Time:  O(V + E)
  Space: O(V)

Dijkstra (with binary heap):
  Time:  O((V + E) log V)
  Space: O(V + E)

Bellman-Ford:
  Time:  O(V * E)
  Space: O(V)

V = vertices, E = edges
```

## What To Say In Interview (Talk Track)

For BFS:
> "Since all edges have equal weight, BFS gives us the shortest path directly.
> Each level in BFS corresponds to one more step, and the first time we reach
> the target is the shortest path. Time is O(V + E)."

For Dijkstra:
> "Since the graph has non-negative weighted edges, I will use Dijkstra's
> algorithm with a min-heap. At each step I pop the node with the smallest
> known distance and relax its neighbors. The key insight is that once we pop
> a node, we have found its shortest distance. Time is O((V+E) log V)."
