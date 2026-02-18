# Tree DP Introduction

## Baby Explanation (ELI10)

- Tree DP = computing answers by going from leaves UP to the root
- Think of it like a company: each employee reports a number to their boss
- The boss combines the numbers from their direct reports
- The CEO (root) has the final answer
- It's just DFS where you USE the values returned by children
- If you can do tree DFS, you can do tree DP — it's the same thing with a purpose

---

## Pattern Recognition

✅ Use this when you see:
- "Diameter of tree"
- "Maximum path sum"
- "Longest path"
- "Height" or "depth" problems
- Any problem where you need to combine info from subtrees
- "Rob houses arranged in a tree"

❌ Avoid when:
- You need level-by-level processing → use BFS
- The problem doesn't involve combining subtree results

---

## The Key Insight

Regular DFS: visit every node, do something.

Tree DP: at each node, **combine results from children** to compute something.

```
Regular DFS:    "Visit node, go left, go right"
Tree DP:        "Go left, go right, COMBINE results at current node"
```

This means tree DP is almost always **POSTORDER** — you process children first.

---

## The Universal Tree DP Template

```python
def solve(root):
    best = [0]  # global answer (use list so inner function can modify)

    def dfs(node):
        # Base case: empty node
        if not node:
            return 0

        # Step 1: Get answers from children (POSTORDER)
        left = dfs(node.left)
        right = dfs(node.right)

        # Step 2: Update global answer using BOTH subtrees
        # (this is the "path through current node" calculation)
        best[0] = max(best[0], left + right + node.val)

        # Step 3: Return info about THIS subtree to parent
        # (parent can only use ONE path — left OR right)
        return max(left, right) + node.val

    dfs(root)
    return best[0]
```

**The two key questions:**
1. What do I **update globally**? (uses both left and right)
2. What do I **return to parent**? (can only pick one direction)

---

## Classic Example: Diameter of Binary Tree

**Problem:** Find the longest path between any two nodes (in edges).

```
        1
       / \
      2   3
     / \
    4   5

Diameter = 3 (path: 4 → 2 → 1 → 3)
```

### Why This Is Tree DP

At each node, the longest path THROUGH that node = left_height + right_height.

The diameter is the maximum of all such paths.

### Step-by-Step Walkthrough

```
Start at node 1
  → Go left to node 2
    → Go left to node 4
      → Go left: None → return 0
      → Go right: None → return 0
      → Update best: max(0, 0+0) = 0
      → Return to parent: max(0, 0) + 1 = 1
    → Go right to node 5
      → Go left: None → return 0
      → Go right: None → return 0
      → Update best: max(0, 0+0) = 0
      → Return to parent: max(0, 0) + 1 = 1
    → Back at node 2:
      → left_height = 1, right_height = 1
      → Update best: max(0, 1+1) = 2
      → Return to parent: max(1, 1) + 1 = 2
  → Go right to node 3
    → Go left: None → return 0
    → Go right: None → return 0
    → Update best: max(2, 0+0) = 2
    → Return to parent: max(0, 0) + 1 = 1
  → Back at node 1:
    → left_height = 2, right_height = 1
    → Update best: max(2, 2+1) = 3  ← THIS IS THE DIAMETER
    → Return: max(2, 1) + 1 = 3

Answer: 3
```

### Code

```python
def diameter_of_binary_tree(root):
    best = [0]

    def height(node):
        if not node:
            return 0

        left_h = height(node.left)
        right_h = height(node.right)

        # Path through this node
        best[0] = max(best[0], left_h + right_h)

        # Return height of this subtree
        return max(left_h, right_h) + 1

    height(root)
    return best[0]
```

---

## Classic Example: Maximum Path Sum

**Problem:** Find the maximum sum path between any two nodes.

```
       -10
       / \
      9   20
         / \
        15   7

Max path = 15 + 20 + 7 = 42
```

### Code

```python
def max_path_sum(root):
    best = [float('-inf')]

    def dfs(node):
        if not node:
            return 0

        # Only take positive contributions
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))

        # Path through this node (uses both sides)
        best[0] = max(best[0], left + right + node.val)

        # Return best single path to parent
        return max(left, right) + node.val

    dfs(root)
    return best[0]
```

**Key trick:** `max(0, dfs(...))` — if a subtree sum is negative, don't include it!

---

## House Robber III (DP with Two States)

**Problem:** Rob houses on a tree. Can't rob two directly connected nodes.

```
        3
       / \
      2   3
       \   \
        3   1

Rob 3 + 3 + 1 = 7
```

### The DP Idea

At each node, two choices:
- **Rob this node:** can't rob children. Take node.val + grandchildren values.
- **Skip this node:** take the best from children (they can be robbed or not).

### Code

```python
def rob(root):
    def dfs(node):
        # Returns (rob_this_node, skip_this_node)
        if not node:
            return (0, 0)

        left = dfs(node.left)
        right = dfs(node.right)

        # Rob this node: can't rob children
        rob_it = node.val + left[1] + right[1]

        # Skip this node: take best of children
        skip_it = max(left) + max(right)

        return (rob_it, skip_it)

    return max(dfs(root))
```

**Key pattern:** Return a TUPLE of values (multiple states per node).

---

## The Two Flavors of Tree DP

| Flavor | What You Return | Global Variable? | Example |
|--------|----------------|-------------------|---------|
| Single value + global | One number (e.g., height) | Yes — tracks the real answer | Diameter, Max Path Sum |
| Tuple (no global) | Multiple values (e.g., rob/skip) | No — answer is at root | House Robber III |

---

## How Info Flows in Tree DP

```
        ROOT
       /    \
     LEFT   RIGHT
     / \     / \
    .   .   .   .

Info flows UP:
   Leaves compute simple values
   Parents combine children's values
   Root has the final answer

        ROOT  ← final answer here
       ↑    ↑
     LEFT   RIGHT
     ↑  ↑   ↑  ↑
    .   .   .   .   ← start from leaves
```

---

## Common Variations

1. **Diameter / longest path** — return height, track diameter globally
2. **Maximum path sum** — same pattern, with `max(0, child)` trick
3. **House Robber on tree** — return tuple (take, skip)
4. **Longest path with same value** — track matching values
5. **Count good nodes** — pass max-so-far down (preorder + postorder mix)

---

## Top 5 Mistakes Beginners Make

1. **Confusing what to return vs what to track globally** — return = info for parent, global = actual answer
2. **Forgetting the base case** — always handle `None` nodes
3. **Not considering negative values** — use `max(0, child)` when negatives can hurt
4. **Returning both subtrees to parent** — parent can only extend ONE path
5. **Using preorder when postorder is needed** — tree DP needs children's results first

---

## Complexity

- **Time:** O(n) — visit each node exactly once
- **Space:** O(h) — recursion stack, where h = height of tree
  - Balanced tree: O(log n)
  - Skewed tree: O(n)

---

## What To Say In Interview (Talk Track)

> "This is a tree DP problem. At each node, I need to combine results from left and right subtrees."
> "I'll use postorder DFS — process children first, then the current node."
> "I'll track the global answer separately because the path through a node uses both subtrees, but I can only return one direction to the parent."
> "Time is O(n), space is O(h) for the recursion stack."

---

## What's Next?

Go to: [08_common_tree_interview_tricks.md](08_common_tree_interview_tricks.md)
