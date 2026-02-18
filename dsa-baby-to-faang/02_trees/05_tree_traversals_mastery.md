# Tree Traversals Mastery — All 4 Ways to Walk a Tree

## Baby Explanation (ELI10)

- "Traversal" just means "visiting every node in the tree in some order." Think of it like reading every room number in a building — but there are different routes you can take.
- There are 4 main traversals. Three use DFS (going deep), one uses BFS (going wide).
- The DFS ones differ only in WHEN you "read" the current node: before your children, between your children, or after your children.
- Memorize all four. Interviewers LOVE asking you to trace them on a tree by hand.
- The iterative versions (using a stack instead of recursion) are asked less often but show up at top companies. Know at least the iterative preorder.

---

## Pattern Recognition

**Use this when you see:**
- "Return the [preorder/inorder/postorder/level-order] traversal"
- "Construct tree from traversals"
- Any problem where the traversal order matters
- BST problems (inorder = sorted)

**Avoid when:**
- You need to compute something at each node (use the DFS template instead)
- The problem does not care about visit order

---

## Our Reference Tree

We will trace ALL traversals on this tree:
```
        1
       / \
      2   3
     / \   \
    4   5   6
```

---

## Traversal 1: Preorder (Root, Left, Right)

**Order:** Visit me FIRST, then go left, then go right.
**Memory trick:** "Pre" = me first, before my children.

```
Visit order: 1, 2, 4, 5, 3, 6

        1  (1st)
       / \
      2   3  (2nd) (5th)
     / \   \
    4   5   6  (3rd) (4th) (6th)
```

### Recursive:
```python
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)
```

### Iterative (using stack):
```python
def preorderIterative(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()          # Pop from top (LIFO)
        result.append(node.val)

        # Push RIGHT first, then LEFT (so left gets popped first!)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
```

**Why push right before left?** The stack is Last-In-First-Out. We want to process left first, so we push it LAST (so it comes out first).

```
Stack trace:
  stack = [1]          pop 1, push 3 then 2
  stack = [3, 2]       pop 2, push 5 then 4
  stack = [3, 5, 4]    pop 4 (leaf)
  stack = [3, 5]       pop 5 (leaf)
  stack = [3]          pop 3, push 6
  stack = [6]          pop 6 (leaf)
  stack = []           DONE

Result: [1, 2, 4, 5, 3, 6]
```

---

## Traversal 2: Inorder (Left, Root, Right)

**Order:** Go ALL the way left first, then visit me, then go right.
**Memory trick:** "In" = me in the middle, between my children.

```
Visit order: 4, 2, 5, 1, 3, 6

        1  (4th)
       / \
      2   3  (2nd) (5th)
     / \   \
    4   5   6  (1st) (3rd) (6th)
```

### Recursive:
```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```

### Iterative (using stack):
```python
def inorderIterative(root):
    result = []
    stack = []
    current = root

    while current or stack:
        # Go as far left as possible
        while current:
            stack.append(current)
            current = current.left

        # Process the leftmost unvisited node
        current = stack.pop()
        result.append(current.val)

        # Now go right
        current = current.right

    return result
```

**How it works:** Keep going left and pushing onto the stack. When you cannot go left anymore, pop the top (that is the leftmost unvisited), process it, then go right.

```
Trace:
  Go left: push 1, push 2, push 4. Can't go left.
  Pop 4, process 4. Go right (None).
  Pop 2, process 2. Go right to 5.
  Push 5. Can't go left.
  Pop 5, process 5. Go right (None).
  Pop 1, process 1. Go right to 3.
  Push 3. Can't go left.
  Pop 3, process 3. Go right to 6.
  Push 6. Can't go left.
  Pop 6, process 6. Go right (None).
  Stack empty, DONE.

Result: [4, 2, 5, 1, 3, 6]
```

---

## Traversal 3: Postorder (Left, Right, Root)

**Order:** Visit BOTH children first, then visit me.
**Memory trick:** "Post" = me last, after my children.

```
Visit order: 4, 5, 2, 6, 3, 1

        1  (6th)
       / \
      2   3  (3rd) (5th)
     / \   \
    4   5   6  (1st) (2nd) (4th)
```

### Recursive:
```python
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

### Iterative (using two stacks — easier to understand):
```python
def postorderIterative(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push LEFT first, then RIGHT (opposite of preorder)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return result[::-1]   # REVERSE the result!
```

**The trick:** This is actually a modified preorder (Root, Right, Left) and then we REVERSE the result to get (Left, Right, Root) = postorder.

```
Before reverse: [1, 3, 6, 2, 5, 4]   (Root, Right, Left order)
After reverse:  [4, 5, 2, 6, 3, 1]   (Left, Right, Root = postorder!)
```

---

## Traversal 4: Level-Order (BFS)

**Order:** Visit all nodes on level 0, then level 1, then level 2, etc.

```
Visit order: 1, 2, 3, 4, 5, 6

Level 0:    1  (1st)
           / \
Level 1:  2   3  (2nd) (3rd)
         / \   \
Level 2: 4  5   6  (4th) (5th) (6th)
```

### Using queue:
```python
from collections import deque

def levelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
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

# Output: [[1], [2, 3], [4, 5, 6]]
```

---

## Side-by-Side Comparison

```
        1
       / \
      2   3
     / \   \
    4   5   6

Preorder  (Root,L,R):  1, 2, 4, 5, 3, 6    "I go first"
Inorder   (L,Root,R):  4, 2, 5, 1, 3, 6    "I go in the middle"
Postorder (L,R,Root):  4, 5, 2, 6, 3, 1    "I go last"
Level-order:           1, 2, 3, 4, 5, 6    "Floor by floor"
```

---

## When to Use Which Traversal

| Traversal | Best For |
|-----------|----------|
| **Preorder** | Copying a tree, serialization, passing info top-down |
| **Inorder** | BST problems (gives sorted order!), kth smallest |
| **Postorder** | Computing subtree info (height, size), deleting a tree |
| **Level-order** | Level-based problems, shortest path, right-side view |

---

## Practice: Trace All 4 on This Tree

Try it yourself before looking at the answer!

```
        10
       /  \
      5    15
     / \     \
    3   7    18
```

**Answers:**
```
Preorder:    10, 5, 3, 7, 15, 18
Inorder:     3, 5, 7, 10, 15, 18    <-- Sorted! (This is a BST)
Postorder:   3, 7, 5, 18, 15, 10
Level-order: 10, 5, 15, 3, 7, 18
```

---

## Morris Traversal (Advanced — Brief Mention)

Morris traversal does inorder traversal in O(1) space (no stack, no recursion!) by temporarily modifying the tree using "threaded" pointers.

```python
def morrisInorder(root):
    result = []
    current = root

    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            # Find inorder predecessor
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if not predecessor.right:
                # Make current the right child of its predecessor
                predecessor.right = current
                current = current.left
            else:
                # Restore the tree
                predecessor.right = None
                result.append(current.val)
                current = current.right

    return result
```

**When to mention:** Only if the interviewer asks "Can you do this in O(1) space?" or if you have already solved the problem and want to show off. Do not start with Morris.

---

## Common Variations

1. **Reverse level-order** — BFS then reverse the result
2. **Vertical order traversal** — group by column index
3. **Boundary traversal** — left boundary + leaves + right boundary
4. **Diagonal traversal** — group by diagonal index
5. **Spiral/Zigzag** — alternate level directions

---

## Top 5 Mistakes Beginners Make

1. **Mixing up the three DFS orders** — Draw the tree and label visit order by hand.
2. **Iterative inorder is the hardest** — Practice it until the while-loop pattern clicks.
3. **Forgetting postorder iterative trick** — It is just reversed modified-preorder. Do not overcomplicate it.
4. **Not pushing right before left in iterative preorder** — Stack is LIFO, so push right first!
5. **Confusing traversal with computation** — Traversal is about visit ORDER. Computation (height, diameter) uses the DFS template from the previous file.

---

## Complexity (All Traversals)

| Traversal | Time | Space |
|-----------|------|-------|
| Preorder (recursive) | O(n) | O(h) call stack |
| Preorder (iterative) | O(n) | O(h) stack |
| Inorder (recursive) | O(n) | O(h) call stack |
| Inorder (iterative) | O(n) | O(h) stack |
| Postorder (recursive) | O(n) | O(h) call stack |
| Postorder (iterative) | O(n) | O(n) for result reversal |
| Level-order | O(n) | O(w) queue width |
| Morris | O(n) | O(1) no extra space! |

---

## What To Say In Interview

> "I will trace through the traversal to verify my approach. For this tree,
> the inorder traversal gives [X], which confirms the BST property."

> "I am using an iterative approach with an explicit stack to avoid
> recursion stack overflow for very deep trees."

> "For the iterative postorder, I am using the trick of doing a
> modified preorder (root, right, left) and reversing the result."
