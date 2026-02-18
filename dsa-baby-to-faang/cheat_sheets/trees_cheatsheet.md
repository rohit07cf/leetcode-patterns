# Trees Cheat Sheet

> Read this 1 hour before your interview. You got this.

---

## TreeNode Class (Memorize This)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## ASCII Tree Diagram — Know Your Vocabulary

```
        1          <-- root (level 0)
       / \
      2   3        <-- level 1
     / \   \
    4   5   6      <-- level 2  (4, 5, 6 are leaves)

- Parent of 4 is 2.  Children of 2 are 4 and 5.
- Height of tree = 2 (edges from root to deepest leaf)
- Depth of node 5 = 2 (edges from root down to 5)
```

```
BST (Binary Search Tree) — left < node < right

        8
       / \
      3   10
     / \    \
    1   6    14
```

---

## Tree Recursion Checklist (Ask These EVERY Time)

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | What does my function return? | Defines the contract (int? bool? node?) |
| 2 | What is the base case? | Usually `if not node: return ...` |
| 3 | How do I combine left and right results? | This IS the logic of your solution |
| 4 | Do I pass info DOWN (preorder) or gather info UP (postorder)? | Decides traversal order |
| 5 | Do I need a global/nonlocal variable? | For tracking max, count, etc. |
| 6 | What is the time/space complexity? | Usually O(n) time, O(h) space |

---

## DFS Templates (Depth-First Search)

### Preorder: Root -> Left -> Right (process BEFORE going deeper)

```python
def preorder(node):
    if not node:
        return
    print(node.val)        # <-- process here
    preorder(node.left)
    preorder(node.right)
```

### Inorder: Left -> Root -> Right (gives sorted order in BST!)

```python
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val)        # <-- process here
    inorder(node.right)
```

### Postorder: Left -> Right -> Root (process AFTER children)

```python
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)        # <-- process here
```

---

## BFS Template (Level-Order Traversal)

```python
from collections import deque

def bfs(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        level_size = len(queue)          # nodes at this level
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

---

## When to Use DFS vs BFS

| Use DFS When... | Use BFS When... |
|-----------------|-----------------|
| Need to explore full paths (root to leaf) | Need level-by-level processing |
| Checking properties of entire tree | Finding shortest depth / closest node |
| Postorder gathering (subtree info) | Printing levels, zigzag, right view |
| Path sum problems | Minimum depth of tree |
| Backtracking on tree paths | Connecting nodes at same level |

**Rule of thumb:** If the problem says "level" or "depth" or "closest" -> BFS. Otherwise -> DFS.

---

## BST Search

```python
def search_bst(root, target):
    if not root:
        return None
    if target == root.val:
        return root
    elif target < root.val:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)
```

## BST Insert

```python
def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root
```

---

## Validate BST Template

```python
def is_valid_bst(node, lo=float('-inf'), hi=float('inf')):
    if not node:
        return True
    if node.val <= lo or node.val >= hi:
        return False
    return (is_valid_bst(node.left, lo, node.val) and
            is_valid_bst(node.right, node.val, hi))
```

Key idea: pass a valid range DOWN. Left child must be < current. Right child must be > current.

---

## Lowest Common Ancestor (LCA) Template

```python
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root          # p and q are on different sides
    return left or right     # both on one side
```

---

## Tree Diameter Template

```
Diameter = longest path between ANY two nodes (count edges).
The path may or may NOT go through the root.
```

```python
def diameter(root):
    ans = 0
    def height(node):
        nonlocal ans
        if not node:
            return 0
        left_h = height(node.left)
        right_h = height(node.right)
        ans = max(ans, left_h + right_h)   # update diameter
        return 1 + max(left_h, right_h)    # return height
    height(root)
    return ans
```

---

## Maximum Path Sum Template (Hard but Common)

```python
def max_path_sum(root):
    ans = float('-inf')
    def dfs(node):
        nonlocal ans
        if not node:
            return 0
        left = max(dfs(node.left), 0)      # ignore negative paths
        right = max(dfs(node.right), 0)
        ans = max(ans, left + node.val + right)  # path through node
        return node.val + max(left, right)        # best single branch
    dfs(root)
    return ans
```

---

## Quick Reference: Problem -> Pattern -> Template

| Problem | Pattern | Key Idea |
|---------|---------|----------|
| Max depth of tree | DFS postorder | `1 + max(left, right)` |
| Min depth of tree | BFS | First leaf you hit = answer |
| Level order traversal | BFS | Process queue level by level |
| Path sum (root to leaf) | DFS preorder | Pass remaining sum down |
| Invert binary tree | DFS postorder | Swap left and right children |
| Validate BST | DFS preorder | Pass valid range `(lo, hi)` |
| LCA | DFS postorder | Find p and q, bubble up |
| Diameter | DFS postorder | Track `left_h + right_h` at each node |
| Serialize / deserialize | BFS or preorder DFS | Use `None` markers for nulls |
| Right side view | BFS | Last node in each level |
| Symmetric tree | DFS | Compare `left.left` with `right.right` |
| Flatten to linked list | DFS postorder | Process right, then left, link |
| Count good nodes | DFS preorder | Pass max-so-far down |

---

## Common Mistakes to Avoid

1. Forgetting `if not node: return` base case
2. Confusing height (edges) vs depth (edges from root)
3. Not using `nonlocal` when updating a variable inside nested function
4. Thinking BST means balanced -- it does NOT
5. Returning `None` when you should return `0` (or vice versa)
6. Forgetting that inorder traversal of BST gives sorted order

---

## Complexity Quick Reference

| Operation | Time | Space |
|-----------|------|-------|
| DFS / BFS traversal | O(n) | O(h) DFS / O(w) BFS |
| BST search (balanced) | O(log n) | O(log n) |
| BST search (worst) | O(n) | O(n) |
| Build tree from arrays | O(n) | O(n) |

Where: n = number of nodes, h = height, w = max width

**You are ready. Trust your recursion. Trust your base case. Go crush it.**
