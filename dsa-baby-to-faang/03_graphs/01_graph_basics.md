# Graph Basics -- What Are Graphs?

## Baby Explanation (ELI10)

- A **graph** is like a social network: people are **nodes**, friendships are **edges**
- If Alice is friends with Bob, there is an edge connecting them
- Some friendships are one-way (I follow a celebrity, they don't follow me back) -- that's a **directed** graph
- Some roads have tolls (cost money) -- that's a **weighted** graph
- Graphs are EVERYWHERE in interviews: maps, networks, relationships, dependencies
- If you can say "X is connected to Y", you probably have a graph

## Directed vs Undirected

```
  UNDIRECTED (two-way street)       DIRECTED (one-way street)

    A --- B                           A ---> B
    |     |                           |      |
    |     |                           v      v
    C --- D                           C ---> D

  A-B means A can reach B             A->B means A can reach B
  AND B can reach A                   but B CANNOT reach A (unless B->A exists)
```

## Weighted vs Unweighted

```
  UNWEIGHTED                        WEIGHTED
  (all edges cost the same)         (edges have different costs)

    A --- B                           A --5-- B
    |     |                           |       |
    |     |                           3       2
    |     |                           |       |
    C --- D                           C --1-- D

  Going A->B costs 1 (same as any)  Going A->B costs 5, C->D costs 1
```

## Adjacency List -- THE Way to Store Graphs in Interviews

Think of it as: for each person, keep a list of their friends.

```python
# Building an adjacency list from scratch
graph = {
    'A': ['B', 'C'],      # A is friends with B and C
    'B': ['A', 'D'],      # B is friends with A and D
    'C': ['A', 'D'],      # C is friends with A and D
    'D': ['B', 'C'],      # D is friends with B and C
}
```

### Building from an Edge List (VERY common in interviews!)

```python
from collections import defaultdict

# Edges given as pairs: [node1, node2]
edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['C', 'D']]

# UNDIRECTED graph -- add both directions
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

# DIRECTED graph -- add only one direction
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)       # only u -> v, NOT v -> u
```

## Adjacency Matrix (Brief Mention)

```
     A  B  C  D
A  [ 0  1  1  0 ]      1 = edge exists
B  [ 1  0  0  1 ]      0 = no edge
C  [ 1  0  0  1 ]
D  [ 0  1  1  0 ]

- Uses O(V^2) space -- wasteful for sparse graphs
- Good for quick "is there an edge between X and Y?" lookups
- In interviews, almost ALWAYS use adjacency list instead
```

## Connected Components

```
  A --- B       E --- F       H
  |     |       |
  C --- D       G

  Component 1: {A, B, C, D}    (all connected to each other)
  Component 2: {E, F, G}       (all connected to each other)
  Component 3: {H}             (alone, no friends)

  3 connected components total
```

A connected component = a group of nodes where you can reach any node
from any other node in that group by following edges.

## Degree of a Node

```
  Degree = number of edges connected to a node
           = number of friends

    A --- B --- C
    |           |
    D           E

  degree(A) = 2  (connected to B and D)
  degree(B) = 3  (connected to A, C, and... wait let me count the edges)
  degree(B) = 2  (connected to A and C)
  degree(C) = 2  (connected to B and E)
  degree(D) = 1  (connected to A only)
  degree(E) = 1  (connected to C only)

  For DIRECTED graphs:
    in-degree  = number of edges pointing INTO the node
    out-degree = number of edges pointing OUT of the node
```

## Pattern Recognition

Use graphs when you see:
- "connected", "neighbors", "adjacent", "reachable"
- Relationships between items (friends, courses, dependencies)
- Grid problems (each cell is a node!)
- "Find if there is a path from X to Y"
- "Find the shortest path"
- "Count the number of groups/components"

Avoid when:
- Data is purely sequential (use arrays/linked lists)
- Data is hierarchical with one parent per node (use trees)

## Minimal Python Template -- Build a Graph

```python
from collections import defaultdict

def build_graph(edges, directed=False):
    """Build adjacency list from edge list."""
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph
```

## Step-by-Step Example (Tiny Input)

```
Input edges: [[0,1], [0,2], [1,3], [2,3]]
Build undirected graph:

Step 1: Edge [0,1] -> graph[0].append(1), graph[1].append(0)
Step 2: Edge [0,2] -> graph[0].append(2), graph[2].append(0)
Step 3: Edge [1,3] -> graph[1].append(3), graph[3].append(1)
Step 4: Edge [2,3] -> graph[2].append(3), graph[3].append(2)

Result:
  graph = {
      0: [1, 2],
      1: [0, 3],
      2: [0, 3],
      3: [1, 2]
  }

Visual:
    0 --- 1
    |     |
    2 --- 3
```

## Common Variations
- Weighted graph: store `(neighbor, weight)` tuples instead of just neighbor
- Graph with node values: separate dictionary for values
- Implicit graph: no edge list given, you compute neighbors on the fly (grids!)

## Top 5 Mistakes Beginners Make

1. **Forgetting to add BOTH directions** for undirected graphs
2. **Not using defaultdict** and getting KeyError on missing nodes
3. **Confusing directed vs undirected** -- read the problem carefully!
4. **Forgetting isolated nodes** -- nodes with no edges still exist
5. **Using adjacency matrix** when adjacency list is simpler and faster

## Complexity (Time + Space)

| Operation            | Adjacency List | Adjacency Matrix |
|----------------------|----------------|------------------|
| Space                | O(V + E)       | O(V^2)           |
| Add edge             | O(1)           | O(1)             |
| Check if edge exists | O(degree)      | O(1)             |
| Get all neighbors    | O(degree)      | O(V)             |
| Build from edge list | O(E)           | O(V^2)           |

V = number of vertices (nodes), E = number of edges

## What To Say In Interview (Talk Track)

> "I will represent this as a graph using an adjacency list, since we need
> to efficiently traverse neighbors. Let me build the graph from the given
> edges first. Since this is undirected, I will add edges in both directions.
> The space for the adjacency list is O(V + E)."
