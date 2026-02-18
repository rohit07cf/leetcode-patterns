# Common Tree Interview Tricks

## Baby Explanation (ELI10)

- Trees are the #1 topic at FAANG interviews
- Most tree problems use the same handful of tricks
- Once you learn these tricks, you can solve 90% of tree problems
- This file is your "trick bag" — a collection of reusable techniques
- Read this before every tree problem
- Each trick = a mini-tool you can pull out when needed

---

## Pattern Recognition

✅ Use this when you see:
- Any tree problem where you're stuck
- You've identified it's a tree problem but don't know the approach
- You need a specific technique to handle a tricky requirement

❌ Avoid when:
- The problem isn't about trees
- You haven't tried basic DFS/BFS first

---

## Trick 1: Use a Helper Function with Extra Parameters

**When:** You need to pass extra info DOWN the tree (like a running sum, a valid range, or a path).

```python
# Example: Validate BST — pass valid range down
def is_valid_bst(root):
    def helper(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (helper(node.left, min_val, node.val) and
                helper(node.right, node.val, max_val))

    return helper(root, float('-inf'), float('inf'))
```

```
        5          valid range: (-inf, inf)
       / \
      3   7        3's range: (-inf, 5), 7's range: (5, inf)
     / \
    1   4          1's range: (-inf, 3), 4's range: (3, 5)
```

---

## Trick 2: Return Multiple Values (Tuple)

**When:** You need to compute multiple things at each node.

```python
# Example: Check if balanced AND get height at the same time
def is_balanced(root):
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

---

## Trick 3: Use Global / Nonlocal for Tracking

**When:** You need to track an answer that spans across subtrees.

```python
# Example: Diameter of Binary Tree
def diameter(root):
    best = [0]  # using list to allow mutation in nested function

    def dfs(node):
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        best[0] = max(best[0], left + right)  # update global
        return max(left, right) + 1            # return to parent

    dfs(root)
    return best[0]
```

**Why list instead of `int`?** Python closures can read outer variables but can't reassign them (without `nonlocal`). A list is mutable, so `best[0] = ...` works.

Alternative with nonlocal:
```python
def diameter(root):
    best = 0
    def dfs(node):
        nonlocal best
        # ... same logic
    dfs(root)
    return best
```

---

## Trick 4: Convert Tree Problem to Known Pattern

| If the problem says... | Convert to... |
|------------------------|---------------|
| "Kth smallest in BST" | Inorder traversal (sorted!) |
| "Level averages" | BFS level by level |
| "Serialize tree" | Preorder with None markers |
| "Right side view" | BFS, take last of each level |
| "Flatten to linked list" | Preorder traversal |
| "Path sum" | DFS with running total |

---

## Trick 5: BFS for Level-Related Problems

**When:** The problem mentions "level", "depth", "layer", "floor", or "row".

```python
from collections import deque

def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)  # KEY: snapshot the level size
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

```
        3          Level 0: [3]
       / \
      9   20       Level 1: [9, 20]
         / \
        15   7     Level 2: [15, 7]
```

**Variations:**
- Right side view → take `level[-1]`
- Zigzag → reverse every other level
- Max width → track indices

---

## Trick 6: Serialize / Deserialize Trees

**When:** You need to convert a tree to a string and back.

```python
# Serialize: Preorder with "None" markers
def serialize(root):
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

# Deserialize: Read values in same preorder
def deserialize(data):
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
          2   3
             / \
            4   5
```

---

## Trick 7: Build Tree from Traversals

**When:** Given two traversals, reconstruct the tree.

**Key insight:**
- Preorder: first element is always the ROOT
- Inorder: root splits array into LEFT and RIGHT subtrees

```python
def build_tree(preorder, inorder):
    if not inorder:
        return None

    root_val = preorder.pop(0)
    root = TreeNode(root_val)

    mid = inorder.index(root_val)

    root.left = build_tree(preorder, inorder[:mid])
    root.right = build_tree(preorder, inorder[mid + 1:])

    return root
```

```
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]

Root = 3 (first in preorder)
Inorder: [9] | 3 | [15, 20, 7]
          ↑ left      ↑ right

        3
       / \
      9   20
         / \
        15   7
```

---

## Trick 8: Subtree Problems

**When:** Check if one tree is a subtree of another.

```python
def is_subtree(root, sub_root):
    if not root:
        return False

    if is_same_tree(root, sub_root):
        return True

    return (is_subtree(root.left, sub_root) or
            is_subtree(root.right, sub_root))

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and
            is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))
```

```
Tree:           3       Subtree:    4
               / \                 / \
              4   5               1   2
             / \
            1   2

is_subtree(tree, subtree) → True
```

---

## Quick Reference: Which Trick for Which Problem?

| Problem Type | Trick to Use |
|-------------|-------------|
| Validate BST | Trick 1 (helper with range) |
| Is Balanced + Height | Trick 2 (return tuple) |
| Diameter / Max Path Sum | Trick 3 (global variable) |
| Kth Smallest in BST | Trick 4 (inorder = sorted) |
| Level Order / Right View | Trick 5 (BFS) |
| Serialize Tree | Trick 6 (preorder + None markers) |
| Build from Traversals | Trick 7 (preorder root + inorder split) |
| Is Subtree | Trick 8 (recursive comparison) |

---

## Top 5 Mistakes Beginners Make

1. **Not identifying if it's preorder or postorder** — top-down info = preorder, bottom-up combining = postorder
2. **Forgetting None base case** — every tree recursion needs `if not node`
3. **Using BFS when DFS is simpler** — most tree problems are easier with DFS
4. **Not drawing the tree** — always draw a small tree before coding
5. **Trying to track too many things** — start simple, add complexity only if needed

---

## Complexity

- Most tree tricks: **O(n) time, O(h) space**
- Subtree check: **O(m * n)** worst case (m and n are sizes of two trees)
- Build from traversals: **O(n^2)** naive, **O(n)** with hash map for index lookup

---

## What To Say In Interview (Talk Track)

> "I'll use a recursive DFS approach. Let me think about whether I need preorder or postorder..."
> "I need to pass extra information down the tree, so I'll use a helper function with additional parameters."
> "I'll track the global answer separately since the optimal path might span both subtrees."
> "Let me draw a small tree to trace through my solution."

---

## You've Completed the Trees Section!

Go to: [../03_graphs/01_graph_basics.md](../03_graphs/01_graph_basics.md)
