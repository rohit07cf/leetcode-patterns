# DP on Trees

## Baby Explanation (ELI10)

- In normal DP, you fill a table left to right (like reading a book).
  In tree DP, you fill the answers bottom to top (from leaves up to the root).
- Imagine a family tree. You ask every child a question. Each parent combines
  the answers from their children to figure out their own answer.
- The leaves know their answer right away (base case). Every other node
  computes its answer from its children (transition). The root has the final answer.
- Tree DP uses DFS (depth-first search). You go all the way down, compute
  answers at the bottom, and carry them back up.

## Pattern Recognition

Use this when you see:
- A tree and "find the maximum/minimum path/sum"
- "Diameter of tree" or "longest path in tree"
- Selecting/not selecting nodes in a tree (like House Robber on a tree)
- Any problem where the answer at a node depends on its children's answers

Avoid when:
- The structure is a graph with cycles (tree DP needs no cycles)
- The data is linear (use regular 1D/2D DP)
- You need BFS-level traversal (tree DP is DFS-based)

## How Tree DP Works

```
  Regular DP:  Fill table left --> right
               dp[0] --> dp[1] --> dp[2] --> ... --> dp[n]

  Tree DP:     Fill tree bottom --> up (DFS post-order)

               Leaves compute first, parents combine.

                      root (compute LAST)
                     /    \
                   A        B
                  / \        \
                 C   D        E   <-- leaves compute FIRST
```

### The Tree DP Template

```python
def tree_dp(root):
    def dfs(node):
        if not node:
            return base_value          # base case (null node)

        left_val = dfs(node.left)      # solve left subtree first
        right_val = dfs(node.right)    # solve right subtree first

        # Combine children's answers for this node
        current_answer = combine(left_val, right_val, node.val)

        # Optionally update a global answer
        nonlocal best
        best = max(best, some_function(left_val, right_val, node.val))

        return current_answer          # pass info UP to parent

    best = initial_value
    dfs(root)
    return best
```

Key idea: DFS returns a value. The parent uses children's returned values.

---

## Problem 1: Diameter of Binary Tree (LeetCode 543)

**The question:** Find the length of the longest path between any two nodes.
The path does not need to pass through the root.

### Baby Explanation

Think of the tree as a system of roads. The diameter is the longest road
trip you can take, measured in number of edges. The road goes DOWN from
some node to a leaf on one side, back UP, and DOWN the other side.

### The Key Insight

At each node, the longest path THROUGH that node is:
left_height + right_height

But what we RETURN to the parent is:
1 + max(left_height, right_height)   (the tallest branch only)

```
  Why? A parent can only use ONE branch from a child, not both.
  The "go left AND right" path is only counted at the turning point.

         [A]
        /   \
      [B]   [C]        Path B-A-C uses both branches of A.
      /       \         But A's parent can only go through A-B OR A-C,
    [D]       [E]       not both.
```

### State, Transition, Base Case

```
  DFS returns: height of subtree rooted at this node
  At each node: diameter_through_here = left_height + right_height
  Update global: best = max(best, diameter_through_here)
  Return to parent: 1 + max(left_height, right_height)
  Base case: null node returns 0
```

### Step-by-Step Example

```
  Tree:
         1
        / \
       2   3
      / \
     4   5

  Standard: DFS returns height (number of edges to deepest leaf).

  dfs(null) = 0           (convention: null has height 0)

  dfs(4): L=0, R=0.  diameter_here = 0+0 = 0.  return max(0,0)+1 = 1
  dfs(5): L=0, R=0.  diameter_here = 0+0 = 0.  return max(0,0)+1 = 1
  dfs(2): L=1, R=1.  diameter_here = 1+1 = 2.  return max(1,1)+1 = 2
  dfs(3): L=0, R=0.  diameter_here = 0+0 = 0.  return max(0,0)+1 = 1
  dfs(1): L=2, R=1.  diameter_here = 2+1 = 3.  return max(2,1)+1 = 3

  Global best diameter = max(0, 0, 2, 0, 3) = 3
  Answer: 3  (path: 4 -> 2 -> 1 -> 3)
```

### Code

```python
def diameterOfBinaryTree(root):
    best = 0

    def dfs(node):
        nonlocal best
        if not node:
            return 0

        left_h = dfs(node.left)
        right_h = dfs(node.right)

        best = max(best, left_h + right_h)   # path THROUGH this node

        return max(left_h, right_h) + 1      # height for parent

    dfs(root)
    return best
```

**Time:** O(n) | **Space:** O(h) where h = height of tree

---

## Problem 2: House Robber III (LeetCode 337)

**The question:** Houses are arranged in a binary tree. A robber cannot
rob two directly-connected houses. Find the maximum amount.

### Baby Explanation

Same as House Robber, but instead of houses in a line, they are in a tree.
If you rob a parent, you cannot rob its children (they are neighbors!).

### State: Each Node Returns TWO Values

```
  For each node, DFS returns a pair:
    (rob_this_node, skip_this_node)

  If I ROB this node:
    I CANNOT rob my children. I take my value + skip-values of children.
    rob = node.val + left_skip + right_skip

  If I SKIP this node:
    I CAN rob or skip each child (pick the best for each).
    skip = max(left_rob, left_skip) + max(right_rob, right_skip)
```

### Step-by-Step Example

```
  Tree:
         3
        / \
       2   3
        \   \
         3   1

  dfs(null) = (0, 0)

  dfs(left 3):  no children.
    rob = 3 + 0 + 0 = 3
    skip = 0 + 0 = 0
    return (3, 0)

  dfs(2): left=null(0,0), right=(3,0)
    rob = 2 + 0 + 0 = 2       (rob 2, must skip child 3)
    skip = max(0,0) + max(3,0) = 0 + 3 = 3  (skip 2, rob child 3)
    return (2, 3)

  dfs(1): no children.
    rob = 1, skip = 0
    return (1, 0)

  dfs(right 3): left=null(0,0), right=(1,0)
    rob = 3 + 0 + 0 = 3
    skip = 0 + max(1,0) = 1
    return (3, 1)

  dfs(root 3): left=(2,3), right=(3,1)
    rob = 3 + 3 + 1 = 7       (rob root, skip both children)
    skip = max(2,3) + max(3,1) = 3 + 3 = 6
    return (7, 6)

  Answer: max(7, 6) = 7  (rob root 3 + grandchild 3 + grandchild 1)
```

### Code

```python
def rob(root):
    def dfs(node):
        if not node:
            return (0, 0)      # (rob, skip)

        left = dfs(node.left)
        right = dfs(node.right)

        rob_this = node.val + left[1] + right[1]
        skip_this = max(left) + max(right)

        return (rob_this, skip_this)

    return max(dfs(root))
```

**Time:** O(n) | **Space:** O(h)

---

## Common Variations

| Problem                     | What DFS Returns               | Global Update          |
|-----------------------------|--------------------------------|------------------------|
| Diameter of Binary Tree     | height (int)                   | max(left_h + right_h) |
| House Robber III            | (rob, skip) tuple              | max at root            |
| Max Path Sum                | max single-branch sum          | max(l + r + node.val)  |
| Longest Path (same value)   | length of matching chain       | max(l + r)             |
| Binary Tree Cameras         | (covered, camera, not_covered) | min cameras at root    |

## Top 5 Mistakes Beginners Make

1. **Returning the wrong thing.** DFS must return what the PARENT needs, not the answer.
2. **Forgetting to handle null nodes.** Always have `if not node: return base_value`.
3. **Confusing "path through node" with "path to leaf."** The diameter goes THROUGH a node using both children, but we return only one branch to the parent.
4. **Not using nonlocal for global variable.** In Python, you need `nonlocal best` inside a nested function.
5. **Trying to do it iteratively first.** Start with recursive DFS. It is natural for trees.

## Complexity (Time + Space)

- Time: O(n) -- visit every node once
- Space: O(h) -- recursion stack depth, where h = height
  - Balanced tree: O(log n)
  - Skewed tree: O(n)

## What To Say In Interview (Talk Track)

> "This is a tree DP problem. I will use DFS where each call returns
> [what it returns] to its parent. At each node, I combine the values
> from my left and right children. The base case is a null node which
> returns [base value]. I also maintain a global variable to track
> [the answer], which I update at each node. Time is O(n) since I
> visit each node once. Space is O(h) for the recursion stack."
