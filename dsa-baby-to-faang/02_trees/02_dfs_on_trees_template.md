# DFS on Trees — The Most Important Tree Technique

## Baby Explanation (ELI10)

- **DFS** stands for Depth-First Search. Imagine you are exploring a cave. You go as DEEP as you can into one tunnel before coming back and trying another tunnel.
- In a tree, DFS means: go all the way down one branch, then come back and go down the next branch.
- DFS is just recursion! When you call a function on `root.left` and `root.right`, you are doing DFS.
- There are 3 flavors of DFS, based on WHEN you process the current node:
  - **Preorder**: Process me FIRST, then my children (top-down)
  - **Inorder**: Process left child, then ME, then right child (left-root-right)
  - **Postorder**: Process my children FIRST, then me (bottom-up)
- **Postorder is the MOST COMMON in interviews** because most problems need bottom-up computation.

---

## Pattern Recognition

**Use DFS when you see:**
- "Find the height / depth / diameter of a tree"
- "Check if a tree has some property" (balanced, symmetric, same)
- "Find a path from root to leaf"
- "Compute something for every subtree"
- Any problem where you need to go deep before wide

**Avoid DFS when:**
- The problem asks for "level by level" processing (use BFS)
- The problem asks for "shortest path" in an unweighted structure (use BFS)
- You need to process nodes floor by floor

---

## The Three DFS Orders — Explained With Pictures

### Our example tree:
```
        1
       / \
      2   3
     / \
    4   5
```

### Preorder: Root, Left, Right (top-down)
**"Visit me, then my left child, then my right child."**

```
Visit order:  1 -> 2 -> 4 -> 5 -> 3

        1  (1st)
       / \
      2   3  (2nd)  (5th)
     / \
    4   5  (3rd)  (4th)
```

```python
def preorder(root):
    if not root:
        return
    print(root.val)          # Process FIRST
    preorder(root.left)      # Then left
    preorder(root.right)     # Then right
```

**When to use preorder:** When you need to pass information DOWN from parent to child.
Example: "Given a tree, assign each node its depth."

### Inorder: Left, Root, Right
**"Visit my left child, then me, then my right child."**

```
Visit order:  4 -> 2 -> 5 -> 1 -> 3

        1  (4th)
       / \
      2   3  (2nd)  (5th)
     / \
    4   5  (1st)  (3rd)
```

```python
def inorder(root):
    if not root:
        return
    inorder(root.left)       # Left first
    print(root.val)          # Process MIDDLE
    inorder(root.right)      # Then right
```

**When to use inorder:** Mainly for Binary Search Trees. Inorder traversal of a BST gives you sorted order!

### Postorder: Left, Right, Root (bottom-up)
**"Visit my children first, then me."**

```
Visit order:  4 -> 5 -> 2 -> 3 -> 1

        1  (5th)
       / \
      2   3  (3rd)  (4th)
     / \
    4   5  (1st)  (2nd)
```

```python
def postorder(root):
    if not root:
        return
    postorder(root.left)     # Left first
    postorder(root.right)    # Then right
    print(root.val)          # Process LAST
```

**When to use postorder:** When you need information from children BEFORE you can compute the answer for the parent. THIS IS THE MOST COMMON PATTERN.
Example: "Find the height of a tree" (you need to know the height of children first).

---

## The Universal DFS Template

**Memorize this. It solves 80% of tree problems.**

```python
def dfs(node):
    # Base case: empty tree
    if not node:
        return BASE_VALUE    # e.g., 0, True, None, []

    # Recurse on children (trust that these work!)
    left_result = dfs(node.left)
    right_result = dfs(node.right)

    # Combine results (THIS is where the magic happens)
    answer = COMBINE(left_result, right_result, node.val)

    return answer
```

### How to convert ANY tree problem to DFS:

**Step 1:** Ask: "What does my function return for a SINGLE node?"
**Step 2:** Ask: "What is the answer for an empty tree (None)?"
**Step 3:** Ask: "If I magically know the answer for left and right subtrees, how do I get the answer for the whole tree?"

---

## Example 1: Find the Height of a Tree

```
        1
       / \
      2   3
     / \
    4   5
```

**Step 1:** My function returns the height of the subtree rooted at this node.
**Step 2:** Height of None = 0 (or -1, depending on definition. We'll use 0.)
**Step 3:** Height = 1 + max(height of left, height of right)

```python
def height(root):
    if not root:
        return 0
    left_h = height(root.left)
    right_h = height(root.right)
    return 1 + max(left_h, right_h)
```

### Tracing the recursion (follow carefully!):
```
height(1):
    height(2):
        height(4):
            height(None) -> 0
            height(None) -> 0
            return 1 + max(0, 0) = 1
        height(5):
            height(None) -> 0
            height(None) -> 0
            return 1 + max(0, 0) = 1
        return 1 + max(1, 1) = 2
    height(3):
        height(None) -> 0
        height(None) -> 0
        return 1 + max(0, 0) = 1
    return 1 + max(2, 1) = 3

Answer: 3 (if counting nodes) or 2 (if counting edges)
```

---

## Example 2: Maximum Depth (LeetCode 104)

This is the same as height! One of the most common beginner problems.

```python
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

---

## Example 3: Check if a Tree is Symmetric (LeetCode 101)

```
Symmetric:            NOT Symmetric:
        1                   1
       / \                 / \
      2   2               2   2
     / \ / \             / \   \
    3  4 4  3           3   4   3
```

**Key insight:** Two trees are mirrors if:
- Their roots are equal
- Left's left mirrors Right's right
- Left's right mirrors Right's left

```python
def isSymmetric(root):
    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                isMirror(left.left, right.right) and
                isMirror(left.right, right.left))

    return isMirror(root.left, root.right) if root else True
```

---

## Visualizing the Call Stack

When DFS runs, each recursive call goes onto the call stack. Here is what happens with our tree:

```
        1
       / \
      2   3

Call stack grows DOWN:

 dfs(1)          <-- starts here
   dfs(2)        <-- goes left first
     dfs(4)      <-- goes left again (deepest!)
       dfs(None) <-- base case, returns
     dfs(5)      <-- back to 4's right
       dfs(None) <-- base case, returns
   dfs(3)        <-- all of 2 is done, now right of 1
     dfs(None)   <-- base case
     dfs(None)   <-- base case
 DONE            <-- back at root, combine everything
```

The stack at the DEEPEST point (when visiting node 4):
```
| dfs(4)  |  <-- top of stack (currently running)
| dfs(2)  |
| dfs(1)  |  <-- bottom of stack (waiting for everything)
+---------+
```
Stack height = depth of the node = O(h) space.

---

## Preorder DFS with Top-Down Info Passing

Sometimes you need to pass information DOWN from parent to child.

### Example: Find all root-to-leaf paths

```
        1
       / \
      2   3
     / \
    4   5

Paths: [1,2,4], [1,2,5], [1,3]
```

```python
def binaryTreePaths(root):
    result = []

    def dfs(node, path):
        if not node:
            return
        path.append(str(node.val))

        if not node.left and not node.right:   # Leaf!
            result.append("->".join(path))

        dfs(node.left, path)
        dfs(node.right, path)
        path.pop()   # BACKTRACK: remove current node when going back up

    dfs(root, [])
    return result
```

---

## Postorder DFS: Bottom-Up Info Gathering (MOST COMMON)

Most interview problems need you to gather info from children first.

### Example: Is the tree balanced? (LeetCode 110)

A tree is balanced if every node's left and right subtree heights differ by at most 1.

```python
def isBalanced(root):
    def check(node):
        if not node:
            return 0         # Height of empty tree

        left_h = check(node.left)
        if left_h == -1:     # Left subtree not balanced
            return -1

        right_h = check(node.right)
        if right_h == -1:    # Right subtree not balanced
            return -1

        if abs(left_h - right_h) > 1:   # Current node not balanced
            return -1

        return 1 + max(left_h, right_h)  # Return height

    return check(root) != -1
```

---

## How to Debug Recursion (Trace by Hand)

**Golden rule: Pick a TINY tree (3-5 nodes) and trace every call.**

```
        1
       / \
      2   3
```

Write it out like this:
```
call dfs(1):
  call dfs(2):
    call dfs(None) -> returns BASE
    call dfs(None) -> returns BASE
    2 combines: ... -> returns X
  call dfs(3):
    call dfs(None) -> returns BASE
    call dfs(None) -> returns BASE
    3 combines: ... -> returns Y
  1 combines X and Y: ... -> returns Z
```

If your answer for this tiny tree is correct, your recursion is almost certainly right.

---

## Top 5 Mistakes Beginners Make

1. **Forgetting the base case** — Always handle `if not node: return ...` first!
2. **Not returning from recursive calls** — You MUST use the return values from `dfs(node.left)` and `dfs(node.right)`.
3. **Confusing preorder and postorder** — Ask: "Do I need info from children first?" If yes, postorder.
4. **Mutating shared state without backtracking** — If you append to a list going down, you must pop going back up.
5. **Using global variables incorrectly** — Use `nonlocal` in Python if modifying a variable from an outer scope.

---

## Complexity

| | Time | Space |
|---|---|---|
| DFS (any order) | O(n) — visit each node once | O(h) — recursion stack depth |
| Balanced tree | O(n) | O(log n) |
| Skewed tree | O(n) | O(n) |

---

## What To Say In Interview

> "I will use a DFS approach. For each node, I will recursively solve the problem
> for the left and right subtrees, then combine the results.
> The base case is when the node is None, in which case I return [X].
> This gives me O(n) time since I visit each node once,
> and O(h) space for the recursion stack."

> "I am using a postorder traversal here because I need information from
> the children before I can compute the answer at the current node."
