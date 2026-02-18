# Topological Sort

## Baby Explanation (ELI10)

- Imagine getting dressed in the morning: you MUST put on underwear BEFORE pants, socks BEFORE shoes
- Topo sort = putting tasks in an order so that **every prerequisite comes before the task that needs it**
- It only works on **DAGs** (Directed Acyclic Graphs) -- no cycles allowed!
  - Why? If A requires B, and B requires A, you can NEVER start -- that is a cycle
- If there IS a cycle, topo sort fails -- and that is how we **detect cycles**!
- Think: course prerequisites, build dependencies, recipe steps

## Pattern Recognition

Use topo sort when you see:
- "Prerequisites", "dependencies", "ordering"
- "Course schedule" -- classic interview problem
- "Build order" or "compilation order"
- "Can you finish all tasks?" (cycle detection!)
- Directed graph + need to find a valid ordering

Avoid when:
- Graph is undirected (topo sort is for directed graphs only)
- You need shortest path (use BFS/Dijkstra)
- No ordering/dependency relationship exists

## What is a DAG?

```
  DAG (Directed Acyclic Graph)         NOT a DAG (has a cycle)

    A ---> B ---> D                      A ---> B
    |             ^                      ^      |
    v             |                      |      v
    C ------->----+                      D <--- C

  A comes first, then B and C,          A->B->C->D->A  = CYCLE!
  then D. Valid ordering: A, B, C, D    No valid ordering exists.
  or A, C, B, D
```

## Approach 1: BFS (Kahn's Algorithm) -- RECOMMENDED for interviews

The idea: Start with nodes that have NO prerequisites (in-degree = 0).
Process them, remove their edges, and new nodes become "free" (in-degree drops to 0).

```python
from collections import deque, defaultdict

def topo_sort_bfs(num_nodes, edges):
    """
    Kahn's Algorithm (BFS-based topological sort).
    edges: list of [prerequisite, task] pairs
    Returns: ordered list, or empty list if cycle exists
    """
    # Step 1: Build graph and count in-degrees
    graph = defaultdict(list)
    in_degree = [0] * num_nodes

    for pre, task in edges:
        graph[pre].append(task)
        in_degree[task] += 1

    # Step 2: Start with all nodes that have in-degree 0
    queue = deque()
    for node in range(num_nodes):
        if in_degree[node] == 0:
            queue.append(node)

    # Step 3: Process queue
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1           # "Remove" the edge
            if in_degree[neighbor] == 0:       # No more prerequisites!
                queue.append(neighbor)

    # Step 4: Check for cycle
    if len(order) == num_nodes:
        return order          # Valid ordering found
    else:
        return []             # CYCLE detected! Not all nodes were processed
```

## Approach 2: DFS-based Topo Sort

The idea: Do DFS, and add a node to the result AFTER visiting all its neighbors (post-order).
Then reverse the result.

```python
def topo_sort_dfs(num_nodes, edges):
    """
    DFS-based topological sort.
    Returns: ordered list, or empty list if cycle exists
    """
    from collections import defaultdict

    graph = defaultdict(list)
    for pre, task in edges:
        graph[pre].append(task)

    # 0 = unvisited, 1 = in current path, 2 = done
    state = [0] * num_nodes
    order = []
    has_cycle = False

    def dfs(node):
        nonlocal has_cycle
        if has_cycle:
            return

        state[node] = 1                    # Mark: currently visiting

        for neighbor in graph[node]:
            if state[neighbor] == 1:       # Back edge = CYCLE!
                has_cycle = True
                return
            if state[neighbor] == 0:       # Unvisited
                dfs(neighbor)

        state[node] = 2                    # Mark: done
        order.append(node)                 # Post-order: add AFTER children

    for node in range(num_nodes):
        if state[node] == 0:
            dfs(node)

    if has_cycle:
        return []

    return order[::-1]                     # Reverse post-order!
```

## Step-by-Step Example -- Kahn's Algorithm

```
Problem: 4 courses, prerequisites:
  To take course 1, you need course 0  -> edge [0, 1]
  To take course 2, you need course 0  -> edge [0, 2]
  To take course 3, you need course 1  -> edge [1, 3]
  To take course 3, you need course 2  -> edge [2, 3]

DAG:
    0 ---> 1
    |      |
    v      v
    2 ---> 3

In-degrees: [0:0, 1:1, 2:1, 3:2]

Step 1: in_degree[0] = 0 -> queue = [0]

Step 2: Pop 0, order = [0]
        Neighbors: 1, 2
        in_degree[1] = 1-1 = 0 -> add to queue
        in_degree[2] = 1-1 = 0 -> add to queue
        queue = [1, 2]

Step 3: Pop 1, order = [0, 1]
        Neighbors: 3
        in_degree[3] = 2-1 = 1 (not 0 yet)
        queue = [2]

Step 4: Pop 2, order = [0, 1, 2]
        Neighbors: 3
        in_degree[3] = 1-1 = 0 -> add to queue
        queue = [3]

Step 5: Pop 3, order = [0, 1, 2, 3]
        No neighbors.
        queue = []

len(order) = 4 = num_nodes -> NO CYCLE
Answer: [0, 1, 2, 3]

Valid orderings: [0, 1, 2, 3] or [0, 2, 1, 3] (both work!)
```

## Cycle Detection Using Topo Sort

```
If len(order) < num_nodes, there is a CYCLE.

Why? Nodes in a cycle never reach in-degree 0.

Example with cycle:
    0 ---> 1
    ^      |
    |      v
    3 <--- 2

In-degrees: [0:1, 1:1, 2:1, 3:1]    <-- ALL are >= 1!
Queue starts empty!
order = []
len(order) = 0 < 4 = num_nodes -> CYCLE DETECTED
```

## Getting Dressed -- The Classic Analogy

```
Items and dependencies:
  underwear -> pants
  pants -> belt
  pants -> shoes
  socks -> shoes
  shirt -> belt
  shirt -> tie
  tie -> jacket
  belt -> jacket

DAG:
  underwear -> pants -> belt -> jacket
                 |        ^       ^
                 v        |       |
               shoes    shirt -> tie
                 ^
                 |
               socks

One valid order:
  underwear, socks, shirt, pants, tie, belt, shoes, jacket

Another valid order:
  socks, underwear, shirt, pants, shoes, tie, belt, jacket

Both are correct! Topo sort is NOT unique.
```

## Common Variations

1. **Course Schedule I** -- "Can you finish all courses?" (cycle detection)
2. **Course Schedule II** -- "In what order?" (actual topo sort)
3. **Parallel courses** -- "Minimum semesters?" (topo sort with level tracking)
4. **Alien dictionary** -- Build a graph from ordering rules, then topo sort
5. **Build order** -- Same idea with software dependencies

## Top 5 Mistakes Beginners Make

1. **Forgetting to check for cycles** -- if `len(order) != num_nodes`, there is a cycle
2. **Using topo sort on undirected graphs** -- it is only for DIRECTED graphs
3. **Getting edge direction wrong** -- `[A, B]` means A must come before B
4. **Forgetting the reverse in DFS approach** -- DFS gives reverse topo order
5. **Not initializing in-degree for ALL nodes** -- nodes with no incoming edges should have in-degree 0

## Complexity (Time + Space)

```
Both approaches (BFS and DFS):

Time:  O(V + E)
  - Build graph: O(E)
  - Process each node once: O(V)
  - Process each edge once: O(E)

Space: O(V + E)
  - Graph storage: O(V + E)
  - In-degree array (BFS): O(V)
  - State array (DFS): O(V)
  - Queue/Stack: O(V)

V = number of nodes, E = number of edges
```

## What To Say In Interview (Talk Track)

> "This is a dependency ordering problem, which is a classic topological sort.
> I will use Kahn's algorithm (BFS approach) because it naturally detects cycles:
> I compute in-degrees, start with nodes that have in-degree 0, and process them
> level by level. If I cannot process all nodes, there is a cycle. Time and space
> are both O(V + E)."
