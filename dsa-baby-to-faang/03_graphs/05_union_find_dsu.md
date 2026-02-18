# Union Find (Disjoint Set Union)

## Baby Explanation (ELI10)

- Imagine a school where kids form **friend groups** -- if Alice is friends with Bob, and Bob is friends with Carol, then Alice, Bob, and Carol are ALL in the same group
- Union Find keeps track of these groups efficiently
- Each group has a **leader** (representative) -- think of it as the "group captain"
- **Find** = "Who is the leader of my group?" (follow the chain to the top)
- **Union** = "Merge two groups into one" (one leader becomes subordinate to the other)
- Two special tricks make it SUPER fast: **path compression** and **union by rank**

## Pattern Recognition

Use Union Find when you see:
- "Are X and Y in the same group/component?"
- "Merge groups" or "connect nodes"
- "Count the number of groups/components"
- "Earliest time when all nodes are connected"
- Redundant connection / extra edge detection
- Problems where you add edges one by one

Avoid when:
- You need shortest path (use BFS/Dijkstra)
- You need to traverse/explore the graph (use BFS/DFS)
- You need to REMOVE connections (Union Find cannot un-union)
- The graph is directed (Union Find is for undirected connections)

## Minimal Python Template

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))    # Each node is its own leader
        self.rank = [0] * n             # Height of each tree
        self.components = n             # Number of groups

    def find(self, x):
        """Find the leader of x's group (with path compression)."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # PATH COMPRESSION
        return self.parent[x]

    def union(self, x, y):
        """Merge the groups of x and y. Returns False if already same group."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False                # Already in the same group

        # UNION BY RANK: attach shorter tree under taller tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.components -= 1            # One fewer group
        return True

    def connected(self, x, y):
        """Check if x and y are in the same group."""
        return self.find(x) == self.find(y)
```

## Path Compression -- The Magic Trick

```
WITHOUT path compression:
  find(4) follows: 4 -> 3 -> 2 -> 1 -> 0     (slow! 4 hops)

      0
      |
      1
      |
      2
      |
      3
      |
      4

WITH path compression:
  After find(4), everyone points directly to the root:

      0
    / | \ \
   1  2  3  4                                  (fast! 1 hop each)

  Next time find(4) is called: 4 -> 0          (just 1 hop!)

How it works:
  self.parent[x] = self.find(self.parent[x])
  This recursively makes every node on the path point to the root.
```

## Union by Rank -- Keep Trees Short

```
WITHOUT union by rank (can become a long chain):
  union(0,1), union(1,2), union(2,3), union(3,4)

      0
      |
      1          Long chain! find() is slow.
      |
      2
      |
      3
      |
      4

WITH union by rank (always attach shorter to taller):
  The shorter tree goes UNDER the taller tree.

      0
    / | \
   1  2   3       Short and flat! find() is fast.
          |
          4
```

## Step-by-Step Example

```
5 people: 0, 1, 2, 3, 4
Connections: (0,1), (2,3), (1,2), (3,4)

Initial state:
  parent = [0, 1, 2, 3, 4]     Everyone is their own leader
  Groups: {0} {1} {2} {3} {4}  5 groups

Step 1: union(0, 1)
  find(0)=0, find(1)=1, different groups -> merge
  parent = [0, 0, 2, 3, 4]     1's leader is now 0
  Groups: {0,1} {2} {3} {4}    4 groups

      0    2    3    4
      |
      1

Step 2: union(2, 3)
  find(2)=2, find(3)=3, different groups -> merge
  parent = [0, 0, 2, 2, 4]     3's leader is now 2
  Groups: {0,1} {2,3} {4}      3 groups

      0    2    4
      |    |
      1    3

Step 3: union(1, 2)
  find(1) -> parent[1]=0 -> find(0)=0, so root=0
  find(2) = 2
  Different groups -> merge. rank[0]=1, rank[2]=1 -> tie, 2 goes under 0
  parent = [0, 0, 0, 2, 4]     2's leader is now 0
  Groups: {0,1,2,3} {4}        2 groups

      0         4
     / \
    1   2
        |
        3

Step 4: union(3, 4)
  find(3) -> parent[3]=2 -> parent[2]=0 -> 0  (path compression: 3->0)
  find(4) = 4
  Different groups -> merge
  parent = [0, 0, 0, 0, 0]     After path compression, all point to 0!
  Groups: {0,1,2,3,4}          1 group

        0
      / | \ \
     1  2  3  4
```

## When to Use Union Find vs BFS/DFS

```
+-------------------------------+-------------+----------+
| Situation                     | Union Find  | BFS/DFS  |
+-------------------------------+-------------+----------+
| "Are X,Y connected?"         |     Y       |    Y     |
| Add edges one at a time      |     Y       |  Meh     |
| Count components              |     Y       |    Y     |
| Find shortest path           |     N       |    Y     |
| Traverse / explore graph     |     N       |    Y     |
| Detect redundant connection  |     Y       |  Hard    |
| Dynamic connectivity         |     Y       |    N     |
| Need to remove edges         |     N       |    N     |
+-------------------------------+-------------+----------+

Rule of thumb:
  - Building up connections over time? -> Union Find
  - Traversing or exploring? -> BFS/DFS
  - Need both? -> Build graph AND Union Find
```

## Connected Components with Union Find

```python
def count_components(n, edges):
    """Count connected components using Union Find."""
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.components
```

That is it! Three lines. Union Find makes this trivially easy.

## Common Variations

1. **Number of Connected Components** -- just return `uf.components`
2. **Redundant Connection** -- the union that returns False = the redundant edge
3. **Accounts Merge** -- union accounts with same email
4. **Earliest Time All Connected** -- process edges in time order, stop when components = 1
5. **Satisfiability of Equations** -- "a == b" means union(a, b)

## Top 5 Mistakes Beginners Make

1. **Forgetting path compression** -- without it, find() can be O(n) instead of nearly O(1)
2. **Forgetting union by rank** -- without it, trees can become long chains
3. **Comparing nodes instead of roots** -- always call `find()` before comparing!
   ```python
   # WRONG:
   if parent[x] == parent[y]     # parent might not be the root!
   # RIGHT:
   if find(x) == find(y)         # always find the root first
   ```
4. **Off-by-one in initialization** -- make sure n matches the number of nodes
5. **Using Union Find for directed graphs** -- it only works for undirected connections

## Complexity (Time + Space)

```
With path compression AND union by rank:

  find():     O(alpha(n)) -- nearly O(1)
  union():    O(alpha(n)) -- nearly O(1)
  connected(): O(alpha(n)) -- nearly O(1)

  alpha(n) = inverse Ackermann function
  For ALL practical purposes, alpha(n) <= 4
  So just say "nearly O(1)" or "amortized O(1)"

Space: O(n) for parent and rank arrays

For m operations on n elements:
  Time:  O(m * alpha(n)) which is basically O(m)
  Space: O(n)
```

## What To Say In Interview (Talk Track)

> "I will use a Union Find (Disjoint Set Union) data structure to track
> connected components. I will implement both path compression and union
> by rank for nearly O(1) amortized operations. Each union merges two
> components, and I track the total count. Space is O(n) for the parent
> and rank arrays."
