# Tree Basics — Your First Step Into Trees

## Baby Explanation (ELI10)

- A **tree** is like a family tree: one person at the top (grandparent), and below them are their children, and below them are THEIR children, and so on.
- Every tree has ONE starting point at the top called the **root** (like the oldest grandparent).
- Data flows DOWNWARD. A parent can have children, but a child has exactly ONE parent.
- The bottom-most people (who have no children) are called **leaves** — like leaves at the tips of a real tree.
- Trees show up in EVERYTHING: file folders on your computer, HTML on websites, company org charts, and of course... coding interviews.
- If you understand recursion, you understand trees. Every subtree is just a smaller tree!

---

## Every Tree Term You Need — With Pictures

### Root
The very top node. The starting point. Every tree has exactly one.
```
        1        <-- This is the root
       / \
      2   3
```

### Node
Any single "box" in the tree. Each node holds a value.
```
        1        <-- node
       / \
      2   3      <-- node, node
     / \
    4   5        <-- node, node
```
This tree has 5 nodes total.

### Leaf
A node with NO children. It's at the very bottom — a dead end.
```
        1
       / \
      2   3      <-- 3 is a leaf (no children)
     / \
    4   5        <-- 4 and 5 are leaves
```
Leaves here: 3, 4, 5

### Parent and Child
A node directly above another is the **parent**. The node below is the **child**.
```
        1          1 is parent of 2 and 3
       / \
      2   3        2 is parent of 4 and 5
     / \
    4   5          4 and 5 are children of 2
```

### Sibling
Nodes that share the same parent — like real siblings!
```
        1
       / \
      2   3      <-- 2 and 3 are siblings (both children of 1)
     / \
    4   5        <-- 4 and 5 are siblings (both children of 2)
```

### Depth (of a node)
How many steps DOWN from the root to reach this node. Root is depth 0.
```
        1          depth 0
       / \
      2   3        depth 1
     / \
    4   5          depth 2
```

### Height (of a tree)
The longest path from the root DOWN to any leaf. This tree has height 2.
```
        1          height of tree = 2
       / \         (longest path: 1 -> 2 -> 4)
      2   3
     / \
    4   5
```

### Edge
The line connecting a parent to a child. A tree with N nodes has N-1 edges.
```
        1
       / \       <-- these lines are edges
      2   3
     / \
    4   5
```
5 nodes, 4 edges.

---

## Binary Tree vs N-ary Tree

### Binary Tree (the star of interviews)
Each node has AT MOST 2 children: a left child and a right child.
```
        1
       / \
      2   3        <-- each node has 0, 1, or 2 children
     / \
    4   5
```

### N-ary Tree
Each node can have ANY number of children.
```
          1
        / | \
       2  3  4       <-- node 1 has 3 children
      /|     |
     5 6     7       <-- node 2 has 2 children, node 4 has 1
```
Most interview problems use binary trees, but a few use N-ary trees.

---

## How Trees Are Built in Python

This is the TreeNode class you will use in almost every tree problem.
**Memorize this. Write it with your eyes closed.**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

That's it. Three things: a value, a left child, a right child.

### Building a tree by hand

```
        1
       / \
      2   3
     / \
    4   5
```

```python
#  Build it bottom-up (leaves first)
node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3)
root  = TreeNode(1, node2, node3)
```

Or build it in one line (nested):
```python
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
```

### How LeetCode gives you trees
LeetCode represents trees as arrays: `[1, 2, 3, 4, 5]`
```
Index:    0  1  2  3  4
Value:   [1, 2, 3, 4, 5]

        1           index 0
       / \
      2   3         index 1, 2
     / \
    4   5           index 3, 4

For node at index i:
  Left child  = index 2*i + 1
  Right child = index 2*i + 2
  Parent      = index (i-1) // 2
```

---

## Why Trees Matter in Interviews

1. **They test recursion** — the #1 skill interviewers want to see.
2. **They appear EVERYWHERE** — at least 20-30% of interview questions involve trees.
3. **They build toward graphs** — trees are just simple graphs, so mastering trees makes graphs easier.
4. **They test multiple skills at once** — DFS, BFS, recursion, dynamic programming.

---

## The Golden Rule: Trees = Recursion

Every tree problem follows this thinking pattern:

```
To solve a problem for a tree rooted at node:
  1. What is the answer if node is None? (BASE CASE)
  2. Assume my function magically works for node.left and node.right
  3. How do I combine those answers to get the answer for node?
```

### Example: Count all nodes in a tree

```python
def count_nodes(root):
    if root is None:       # Base case: empty tree has 0 nodes
        return 0
    left = count_nodes(root.left)    # Trust recursion for left
    right = count_nodes(root.right)  # Trust recursion for right
    return left + right + 1          # Combine: left + right + me
```

Trace it on this tree:
```
        1
       / \
      2   3

count_nodes(1):
    count_nodes(2):
        count_nodes(None) -> 0      (left of 2)
        count_nodes(None) -> 0      (right of 2)
        return 0 + 0 + 1 = 1
    count_nodes(3):
        count_nodes(None) -> 0      (left of 3)
        count_nodes(None) -> 0      (right of 3)
        return 0 + 0 + 1 = 1
    return 1 + 1 + 1 = 3            CORRECT! 3 nodes total.
```

---

## Types of Binary Trees (Know These Names)

### Full Binary Tree
Every node has 0 or 2 children (never just 1).
```
        1
       / \
      2   3
     / \
    4   5
```

### Complete Binary Tree
All levels are fully filled EXCEPT possibly the last, which fills left to right.
```
        1
       / \
      2   3
     / \  /
    4  5  6
```

### Perfect Binary Tree
All levels are completely filled. Every leaf is at the same depth.
```
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

### Balanced Binary Tree
The height of left and right subtrees differ by at most 1 for EVERY node.
```
    BALANCED:           NOT BALANCED:
        1                   1
       / \                 /
      2   3               2
     /                   /
    4                   3
```

---

## Quick Reference

| Term | Meaning |
|------|---------|
| Root | Top node, no parent |
| Leaf | Bottom node, no children |
| Depth | Distance from root (root = 0) |
| Height | Longest path from root to leaf |
| Edge | Connection between parent and child |
| Subtree | Any node + all its descendants |
| Binary | At most 2 children per node |

---

## What To Say In Interview

> "Before I start coding, let me clarify — this is a binary tree, not a BST, correct?
> My approach will be recursive. The base case is when the node is None.
> For each node, I will process the left subtree, the right subtree,
> and then combine the results."

This shows the interviewer you think clearly and understand tree structure.

---

## Complexity Basics for Trees

- **Visiting every node once** = O(n) time, where n is the number of nodes.
- **Recursion uses the call stack** = O(h) space, where h is the height of the tree.
  - Best case (balanced): h = log(n)
  - Worst case (skewed): h = n (tree is basically a linked list)

```
BALANCED (h = log n):       SKEWED (h = n):
        1                   1
       / \                   \
      2   3                   2
     / \ / \                   \
    4  5 6  7                   3
                                 \
                                  4
```

Trees are your best friend in interviews. Master them, and you master recursion itself.
