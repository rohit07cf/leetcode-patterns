# Common Tree Interview Tricks — Your Secret Weapon Bag

## Baby Explanation (ELI10)

- Trees are the #1 topic at FAANG interviews. Most tree problems use the same handful of tricks.
- Once you learn these 8 tricks, you can solve about 90% of tree problems by recognizing which trick to apply.
- This file is your "trick bag" -- a collection of reusable techniques with mini examples.
- Read this before every mock interview. Each trick is a mini-tool you can pull out when needed.
- The tricks build on everything from the previous files (DFS, BFS, BST, LCA, Tree DP).
- When you are stuck on a tree problem, scroll through these tricks. One of them will fit.

---

## Pattern Recognition

**Use this file when:**
- You have identified it is a tree problem but do not know the approach
- You are stuck and need a technique to handle a tricky requirement
- You want to review all tree tricks before an interview

**Start with basics first:**
- Always try simple DFS/BFS before reaching for a trick
- Most tricks are just DFS with a small twist

---

## Trick 1: Use a Helper Function with Extra Parameters

**When to use:** You need to pass information DOWN the tree -- a running sum, a valid range, a depth counter, or a path.

The main function is simple. The helper carries extra state.

```python
# Example: Validate BST — pass valid range down
def isValidBST(root):
    def helper(node, low, high):
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        return (helper(node.left, low, node.val) and
                helper(node.right, node.val, high))

    return helper(root, float('-inf'), float('inf'))
```

```
        5          helper(5, -inf, inf)  -> valid
       / \
      3   7        helper(3, -inf, 5)   -> valid
     / \           helper(7, 5, inf)    -> valid
    1   4          helper(1, -inf, 3)   -> valid
                   helper(4, 3, 5)      -> valid

Each child gets a TIGHTER range from its parent.
```

### Another example: Path Sum (LeetCode 112)

```python
def hasPathSum(root, targetSum):
    def helper(node, remaining):
        if not node:
            return False
        remaining -= node.val
        if not node.left and not node.right:  # Leaf
            return remaining == 0
        return helper(node.left, remaining) or helper(node.right, remaining)

    return helper(root, targetSum)
```

```
        5          target = 22
       / \
      4   8        5 -> remaining = 17
     /   / \
    11  13  4      5->4->11->2 = 22, remaining = 0 at leaf 2!
   / \       \
  7   2       1
```

---

## Trick 2: Return Multiple Values from Recursion (Tuple)

**When to use:** You need to compute MULTIPLE things at each node simultaneously. Instead of running DFS twice, return a tuple.

```python
# Example: Check if balanced AND get height at the same time
def isBalanced(root):
    def dfs(node):
        # Returns (is_balanced, height)
        if not node:
            return (True, 0)

        left_bal, left_h = dfs(node.left)
        right_bal, right_h = dfs(node.right)

        balanced = left_bal and right_bal and abs(left_h - right_h) <= 1
        height = max(left_h, right_h) + 1

        return (balanced, height)

    return dfs(root)[0]
```

```
        1
       / \
      2   3        dfs(2) returns (True, 2)
     / \           dfs(3) returns (True, 1)
    4   5          dfs(1): balanced = True and True and |2-1|<=1 = True

Without tuple: you would need two separate DFS calls = O(n) + O(n).
With tuple: one DFS does both = O(n). Half the work!
```

### Another example: Min and Max of subtree

```python
def subtreeMinMax(root):
    def dfs(node):
        # Returns (min_val, max_val)
        if not node:
            return (float('inf'), float('-inf'))

        left_min, left_max = dfs(node.left)
        right_min, right_max = dfs(node.right)

        return (min(node.val, left_min, right_min),
                max(node.val, left_max, right_max))

    return dfs(root)
```

---

## Trick 3: Use Global / Nonlocal for Tracking Answers

**When to use:** The answer spans across subtrees and might not go through the root. You need to track the BEST answer seen at any node during DFS.

```python
# Example: Diameter of Binary Tree
def diameterOfBinaryTree(root):
    best = [0]  # Using list so inner function can modify it

    def dfs(node):
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        best[0] = max(best[0], left + right)  # Update global
        return max(left, right) + 1            # Return to parent

    dfs(root)
    return best[0]
```

**Why a list `[0]` instead of a plain `int`?**
Python closures can READ outer variables but cannot REASSIGN them without `nonlocal`. A list is mutable, so `best[0] = ...` works without `nonlocal`.

Alternative using `nonlocal`:
```python
def diameterOfBinaryTree(root):
    best = 0

    def dfs(node):
        nonlocal best          # <-- This makes it work
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        best = max(best, left + right)
        return max(left, right) + 1

    dfs(root)
    return best
```

```
        1
       /
      2            Diameter = 4 (path: 5->3->2->4->6)
     / \           This does NOT go through root!
    3   4          The global variable catches it at node 2.
   /     \
  5       6
```

---

## Trick 4: Convert Tree Problem to a Known Pattern

Many tree problems are disguised versions of simpler patterns. Learn to recognize the conversion.

| If the problem says... | Convert to... |
|------------------------|---------------|
| "Kth smallest in BST" | Inorder traversal (gives sorted order!) |
| "Level averages" | BFS level by level, compute avg per level |
| "Serialize/deserialize tree" | Preorder with None markers |
| "Right side view" | BFS, take last node of each level |
| "Flatten to linked list" | Preorder traversal, rewire pointers |
| "Path sum to target" | DFS with running total parameter |
| "Sum of all left leaves" | DFS, check if child is a left leaf |
| "Invert binary tree" | Postorder DFS, swap left and right |

### Example: Invert Binary Tree (LeetCode 226)

This is just "swap every node's children." Postorder DFS.

```python
def invertTree(root):
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
```

```
Before:         After:
    4               4
   / \             / \
  2   7           7   2
 / \ / \         / \ / \
1  3 6  9       9  6 3  1
```

---

## Trick 5: BFS for Level-Related Problems

**When to use:** The problem mentions "level", "depth", "layer", "floor", "row", or "minimum distance."

All these problems use the SAME BFS template with small tweaks.

```python
from collections import deque

def bfsTemplate(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)  # KEY: snapshot before the loop
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
```

### Quick variations:

```python
# Right side view: take last element of each level
right_view = [level[-1] for level in bfsTemplate(root)]

# Level averages: compute mean of each level
averages = [sum(level) / len(level) for level in bfsTemplate(root)]

# Zigzag: reverse every other level
for i, level in enumerate(result):
    if i % 2 == 1:
        level.reverse()
```

```
        3          Level 0: [3]
       / \
      9   20       Level 1: [9, 20]
         / \
        15   7     Level 2: [15, 7]

Right view: [3, 20, 7]
Averages: [3.0, 14.5, 11.0]
Zigzag: [[3], [20, 9], [15, 7]]
```

---

## Trick 6: Serialize and Deserialize Trees (LeetCode 297)

**When to use:** Convert a tree to a string and reconstruct it back. This tests your understanding of traversals deeply.

The approach: Preorder DFS with "N" markers for None nodes.

```python
class Codec:
    def serialize(self, root):
        result = []

        def dfs(node):
            if not node:
                result.append("N")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        values = iter(data.split(","))

        def dfs():
            val = next(values)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
```

```
Tree:       1           Serialized: "1,2,N,N,3,4,N,N,5,N,N"
           / \
          2   3         Trace serialize:
             / \          visit 1 -> "1"
            4   5         visit 2 -> "2"
                          left of 2 is None -> "N"
                          right of 2 is None -> "N"
                          visit 3 -> "3"
                          visit 4 -> "4"
                          ...and so on

Deserialize reads the SAME order back and rebuilds the tree.
```

**Why preorder?** Because the first value tells you the root, then you can recursively build left and right. The None markers tell you when a subtree ends.

---

## Trick 7: Build Tree from Traversals (LeetCode 105)

**When to use:** Given preorder + inorder (or postorder + inorder), reconstruct the unique tree.

**Key insights:**
- Preorder's FIRST element = the root
- Inorder tells you what is LEFT vs RIGHT of that root
- Postorder's LAST element = the root

```python
def buildTree(preorder, inorder):
    if not inorder:
        return None

    root_val = preorder.pop(0)
    root = TreeNode(root_val)

    mid = inorder.index(root_val)   # Find root in inorder

    root.left = buildTree(preorder, inorder[:mid])      # Left part
    root.right = buildTree(preorder, inorder[mid + 1:])  # Right part

    return root
```

### Step-by-step example:
```
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]

Step 1: root = 3 (first in preorder)
        Find 3 in inorder at index 1
        Left inorder: [9]        Right inorder: [15, 20, 7]

Step 2: root.left -> root = 9 (next in preorder)
        Find 9 in inorder at index 0
        Left: []  Right: []  -> leaf node

Step 3: root.right -> root = 20 (next in preorder)
        Find 20 in inorder: [15, 20, 7] at index 1
        Left: [15]  Right: [7]

Result:
        3
       / \
      9   20
         / \
        15   7
```

**Optimization:** Use a hash map for O(1) lookup in inorder:
```python
def buildTree(preorder, inorder):
    idx_map = {val: i for i, val in enumerate(inorder)}
    pre_iter = iter(preorder)

    def build(left, right):
        if left > right:
            return None
        root_val = next(pre_iter)
        root = TreeNode(root_val)
        mid = idx_map[root_val]
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root

    return build(0, len(inorder) - 1)
```
This runs in O(n) instead of O(n^2).

---

## Trick 8: Subtree Problems

**When to use:** Check if one tree is a subtree of another, or find identical subtrees.

Two helper functions: `isSubtree` checks every node, `isSameTree` checks if two trees match.

```python
def isSubtree(root, subRoot):
    if not root:
        return False

    if isSameTree(root, subRoot):
        return True

    return (isSubtree(root.left, subRoot) or
            isSubtree(root.right, subRoot))

def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and
            isSameTree(p.left, q.left) and
            isSameTree(p.right, q.right))
```

```
Main tree:       3       Subtree:    4
                / \                 / \
               4   5               1   2
              / \
             1   2

isSubtree checks:
  isSameTree(3, 4)? No (3 != 4)
  isSubtree(4, target)?
    isSameTree(4, 4)? -> 4==4, check children
      isSameTree(1, 1)? -> Yes
      isSameTree(2, 2)? -> Yes
    -> True!

Answer: True, the subtree exists starting at node 4.
```

**Complexity:** O(m * n) in the worst case, where m and n are the sizes of the two trees. For each of the n nodes in the main tree, we might compare all m nodes of the subtree.

---

## Quick Reference: Which Trick for Which Problem?

| Problem Type | Trick # | Technique |
|-------------|---------|-----------|
| Validate BST | 1 | Helper with range parameters |
| Path Sum | 1 | Helper with running total |
| Is Balanced + Height | 2 | Return tuple (balanced, height) |
| Diameter / Max Path Sum | 3 | Global variable + return to parent |
| Kth Smallest in BST | 4 | Convert to inorder traversal |
| Invert Binary Tree | 4 | Convert to swap children |
| Level Order / Right View | 5 | BFS with level size snapshot |
| Serialize / Deserialize | 6 | Preorder with None markers |
| Build from Traversals | 7 | Preorder root + inorder split |
| Is Subtree | 8 | Recursive isSameTree at each node |

---

## Bonus Trick: The "Boundary Walk" for Complex Problems

Some problems need you to track the boundary (leftmost/rightmost) nodes:

```
        1
       / \
      2   3
     / \   \
    4   5   6
       / \
      7   8

Left boundary: 1, 2, 4
Right boundary: 1, 3, 6
Leaves: 4, 7, 8, 6
Boundary traversal: 1, 2, 4, 7, 8, 6, 3
```

---

## Bonus Trick: Use a Dummy/Sentinel Node

When you need to handle edge cases (empty tree, single node), sometimes a sentinel simplifies the code:

```python
# Example: Flatten binary tree to linked list
def flatten(root):
    dummy = TreeNode(0)
    prev = [dummy]

    def dfs(node):
        if not node:
            return
        prev[0].right = node
        prev[0].left = None
        prev[0] = node
        # Save right because we will overwrite it
        right = node.right
        dfs(node.left)
        dfs(right)

    dfs(root)
```

---

## Top 5 Mistakes Beginners Make

1. **Not identifying whether to use preorder or postorder** -- Top-down info passing = preorder. Bottom-up computation = postorder. Choose wrong and your code will not work.
2. **Forgetting the None base case** -- Every tree recursion needs `if not node: return ...` at the start. Missing this causes crashes.
3. **Using BFS when DFS is simpler** -- Most tree problems are easier with DFS. Only reach for BFS when the problem is about levels.
4. **Not drawing the tree first** -- Always draw a small tree (5-7 nodes) and trace through your solution by hand before coding.
5. **Trying to track too many things** -- Start with the simplest approach. Add complexity (tuples, globals) only if needed.

---

## Complexity Summary

| Trick | Time | Space |
|-------|------|-------|
| Helper with params | O(n) | O(h) |
| Return tuple | O(n) | O(h) |
| Global tracking | O(n) | O(h) |
| BFS level tricks | O(n) | O(w) |
| Serialize/Deserialize | O(n) | O(n) |
| Build from traversals | O(n) with hashmap | O(n) |
| Subtree check | O(m * n) worst | O(h) |

Where n = number of nodes, h = height, w = max width.

---

## What To Say In Interview

> "I will use a recursive DFS approach. Let me think about whether I need
> preorder or postorder. Since I need to pass range information down,
> I will use a helper function with additional parameters."

> "I need to compute two things at each node simultaneously, so I will
> return a tuple from my recursive function to avoid traversing the tree twice."

> "I will track the global answer separately using a list since the
> optimal path might span both subtrees at some internal node."

> "Let me draw a small tree and trace through my solution to verify
> it handles the edge cases."

---

## You Have Completed the Trees Section!

You now have all the tools you need for tree problems in FAANG interviews:
1. Tree basics and terminology
2. DFS template (preorder, inorder, postorder)
3. BFS template (level-order)
4. BST patterns (search, insert, delete, validate)
5. All four traversals (recursive + iterative)
6. Lowest Common Ancestor
7. Tree DP (diameter, max path sum, house robber)
8. Eight reusable interview tricks

Practice 20-30 tree problems on LeetCode, and trees will become your strongest topic.
