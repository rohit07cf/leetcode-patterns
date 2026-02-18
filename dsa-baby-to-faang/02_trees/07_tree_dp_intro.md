# Tree DP — Dynamic Programming on Trees

## Baby Explanation (ELI10)

- **Tree DP** is when you compute an answer at each node by combining answers from its children. Think of it like a company: each manager asks their employees for a report, combines the reports, and sends the result UP to their boss.
- It is called "DP" because we compute and REUSE smaller results (subtree answers) to build bigger results (whole tree answer).
- The information always flows UPWARD: leaves compute first, then their parents, then THEIR parents, all the way up to the root. This is just postorder DFS!
- Tree DP is the pattern behind many classic interview problems: diameter of a tree, maximum path sum, longest path, house robber on a tree.
- The trick is that sometimes the answer to the PROBLEM is NOT the same as what the FUNCTION returns. You often need a global variable to track the best answer seen so far.
- If you can do postorder DFS, you can do Tree DP. They are the same thing with a purpose.

---

## Pattern Recognition

**Use Tree DP when you see:**
- "Find the diameter / longest path in a tree"
- "Find the maximum path sum"
- "Choose nodes with constraints" (like house robber)
- "Compute some property of all subtrees"
- Anything where you need bottom-up computation + combining children's results

**Avoid when:**
- The problem is top-down only (just use preorder DFS with parameter passing)
- The problem is about levels (use BFS)
- The problem does not involve combining subtree information

---

## The Core Pattern

Every Tree DP problem follows this structure:

```python
def treeDPProblem(root):
    best_answer = [initial_value]    # Global tracker

    def dfs(node):
        if not node:
            return BASE_VALUE

        left_info = dfs(node.left)     # Get info from left subtree
        right_info = dfs(node.right)   # Get info from right subtree

        # UPDATE GLOBAL ANSWER (this might use both left + right)
        best_answer[0] = max(best_answer[0],
                             COMBINE(left_info, right_info, node))

        # RETURN INFO UPWARD (can only go through ONE child, not both)
        return WHAT_PARENT_NEEDS(left_info, right_info, node)

    dfs(root)
    return best_answer[0]
```

**THE KEY INSIGHT:** The global answer and the return value are DIFFERENT things!
- The global answer considers paths that go through the current node (using BOTH children).
- The return value goes to the parent and can only use ONE child (because a path cannot fork).

**The two key questions for every Tree DP problem:**
1. What do I **update globally**? (can use both left and right)
2. What do I **return to parent**? (can only pick one direction)

---

## Classic Problem 1: Diameter of Binary Tree (LeetCode 543)

The **diameter** is the longest path between ANY two nodes (counted in edges). This path may or may not go through the root.

```
        1
       / \
      2   3
     / \
    4   5

Diameter = 3 (path: 4 -> 2 -> 1 -> 3, or 5 -> 2 -> 1 -> 3)
```

### Why is this Tree DP?

At each node, the longest path THROUGH this node = left_height + right_height.
But the answer we return to the parent is just the height (1 + max(left, right)), because you can only go up through ONE side.

```
At node 2:
  left_height = 1 (from node 4)
  right_height = 1 (from node 5)
  Path through node 2 = 1 + 1 = 2  (4 -> 2 -> 5)
  Return to parent: 1 + max(1, 1) = 2  (height)

At node 1:
  left_height = 2 (from node 2)
  right_height = 1 (from node 3)
  Path through node 1 = 2 + 1 = 3  (this IS the diameter)
  Return: 1 + max(2, 1) = 3
```

### The Code:

```python
def diameterOfBinaryTree(root):
    diameter = [0]

    def height(node):
        if not node:
            return 0

        left_h = height(node.left)
        right_h = height(node.right)

        # Update diameter: path through this node
        diameter[0] = max(diameter[0], left_h + right_h)

        # Return height to parent
        return 1 + max(left_h, right_h)

    height(root)
    return diameter[0]
```

### Full Trace:
```
        1
       / \
      2   3
     / \
    4   5

height(4):
  left=0, right=0
  diameter = max(0, 0+0) = 0
  return 1 + max(0,0) = 1

height(5):
  left=0, right=0
  diameter = max(0, 0+0) = 0
  return 1 + max(0,0) = 1

height(2):
  left=1, right=1
  diameter = max(0, 1+1) = 2         <-- path: 4->2->5
  return 1 + max(1,1) = 2

height(3):
  left=0, right=0
  diameter = max(2, 0+0) = 2
  return 1 + max(0,0) = 1

height(1):
  left=2, right=1
  diameter = max(2, 2+1) = 3         <-- path: 4->2->1->3  THE ANSWER!
  return 1 + max(2,1) = 3

Final diameter = 3
```

---

## How Info Flows Up — Visualized

```
        1           height(1) returns 3
       / \          diameter updated to 3 here
      2   3         height(2) returns 2       height(3) returns 1
     / \            diameter updated to 2 here
    4   5           height(4) returns 1       height(5) returns 1

Info flows UPWARD like bubbles rising in water:

    Step 1: Leaves compute (height = 1 each)
    Step 2: Node 2 combines left=1, right=1 -> returns height 2
    Step 3: Root combines left=2, right=1 -> returns height 3

    At each step, we also check: "Is the path THROUGH me the longest so far?"
```

---

## Why the Diameter Might NOT Go Through the Root

This is the key reason we need a global variable:

```
        1
       /
      2
     / \
    3   4
   /     \
  5       6

Diameter = 4 (path: 5 -> 3 -> 2 -> 4 -> 6)
This path goes through node 2, NOT through root 1!

If we only returned the answer from the root, we would miss this.
The global variable catches it when we process node 2.
```

---

## Classic Problem 2: Maximum Path Sum (LeetCode 124)

Find the path with the largest sum. The path can start and end at ANY node.

```
       -10
       / \
      9   20
         / \
        15  7

Maximum path: 15 -> 20 -> 7 = 42
```

This is just like diameter, but instead of counting edges, we sum values.

```python
def maxPathSum(root):
    max_sum = [float('-inf')]

    def dfs(node):
        if not node:
            return 0

        # Only take positive contributions from children
        left_gain = max(dfs(node.left), 0)     # Ignore if negative!
        right_gain = max(dfs(node.right), 0)

        # Path through current node (using both children)
        path_sum = node.val + left_gain + right_gain
        max_sum[0] = max(max_sum[0], path_sum)

        # Return max gain through ONE child (for parent's use)
        return node.val + max(left_gain, right_gain)

    dfs(root)
    return max_sum[0]
```

### Trace:
```
       -10
       / \
      9   20
         / \
        15  7

dfs(9):   left=0, right=0
          path = 9+0+0 = 9          max_sum = 9
          return 9+max(0,0) = 9

dfs(15):  left=0, right=0
          path = 15+0+0 = 15        max_sum = 15
          return 15

dfs(7):   left=0, right=0
          path = 7+0+0 = 7          max_sum = 15
          return 7

dfs(20):  left_gain=15, right_gain=7
          path = 20+15+7 = 42       max_sum = 42  <-- THE ANSWER!
          return 20+max(15,7) = 35

dfs(-10): left_gain=max(9,0)=9, right_gain=max(35,0)=35
          path = -10+9+35 = 34      max_sum stays 42
          return -10+max(9,35) = 25

Answer: 42  (path: 15 -> 20 -> 7)
```

**Key trick:** `max(dfs(child), 0)` means "if this child's path has negative sum, do not include it." You always have the option of not extending into a subtree.

---

## Classic Problem 3: House Robber III (LeetCode 337)

A thief robs houses arranged in a tree. Cannot rob two directly-connected houses. Find max money.

```
        3
       / \
      2   3
       \   \
        3   1

Option A: Rob 3 (root) + 3 (left grandchild) + 1 (right grandchild) = 7
Option B: Rob 2 + 3 (right child) = 5
Answer: 7
```

At each node, two choices:
- **Rob this node:** take its value + results from grandchildren (children must be skipped)
- **Skip this node:** take the best results from children (each child can be robbed or skipped)

```python
def rob(root):
    def dfs(node):
        # Returns (rob_this_node, skip_this_node)
        if not node:
            return (0, 0)

        left_rob, left_skip = dfs(node.left)
        right_rob, right_skip = dfs(node.right)

        # If we rob this node, children must be skipped
        rob_this = node.val + left_skip + right_skip

        # If we skip this node, take the best from each child
        skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)

        return (rob_this, skip_this)

    return max(dfs(root))
```

This is the "return a tuple" trick -- the function returns multiple pieces of info.

### Trace:
```
        3
       / \
      2   3
       \   \
        3   1

dfs(3, left-grandchild):  return (3, 0)
dfs(2):   left=(0,0), right=(3,0)
          rob = 2 + 0 + 0 = 2
          skip = max(0,0) + max(3,0) = 3
          return (2, 3)

dfs(1):   left=(0,0), right=(0,0)
          return (1, 0)
dfs(3, right-child): left=(0,0), right=(1,0)
          rob = 3 + 0 + 0 = 3
          skip = 0 + max(1,0) = 1
          return (3, 1)

dfs(3, root): left=(2,3), right=(3,1)
          rob = 3 + 3 + 1 = 7          <-- rob root + skip both children
          skip = max(2,3) + max(3,1) = 3 + 3 = 6
          return (7, 6)

Answer: max(7, 6) = 7
```

---

## The Two Flavors of Tree DP

| Flavor | What You Return | Global Variable? | Example |
|--------|----------------|-------------------|---------|
| Single value + global | One number (height, gain) | Yes -- tracks the real answer | Diameter, Max Path Sum |
| Tuple (no global) | Multiple values (rob/skip) | No -- answer is max of tuple at root | House Robber III |

**Flavor 1** is used when the optimal answer might pass through any node, not just the root.
**Flavor 2** is used when the state at each node has multiple options.

---

## How Tree DP Differs From Regular DP

| Regular DP | Tree DP |
|-----------|---------|
| Linear structure (array) | Tree structure |
| Fill table left to right | Fill bottom to top (postorder) |
| dp[i] depends on dp[i-1] | dp[node] depends on dp[children] |
| Iterative loop | Recursive DFS |
| Explicit dp array | Return values + global variable |
| State is index | State is a node |

---

## Classic Problem 4: Longest Univalue Path (LeetCode 687)

Find the longest path where all nodes have the same value.

```
        5
       / \
      4   5
     / \   \
    1   1   5

Longest univalue path = 2 (5 -> 5 -> 5 on the right side)
```

```python
def longestUnivaluePath(root):
    longest = [0]

    def dfs(node):
        if not node:
            return 0

        left_len = dfs(node.left)
        right_len = dfs(node.right)

        # Extend left path only if values match
        left_arrow = left_len + 1 if node.left and node.left.val == node.val else 0
        # Extend right path only if values match
        right_arrow = right_len + 1 if node.right and node.right.val == node.val else 0

        # Path through this node (both directions)
        longest[0] = max(longest[0], left_arrow + right_arrow)

        # Return longest single direction to parent
        return max(left_arrow, right_arrow)

    dfs(root)
    return longest[0]
```

---

## Common Variations

1. **Diameter / longest path** -- return height, track diameter globally
2. **Maximum path sum** -- same pattern, with `max(0, child)` trick
3. **House Robber III** -- return tuple (take, skip) for each node
4. **Longest univalue path** -- diameter variant where values must match
5. **Binary tree cameras** -- return tuple (covered, has_camera, not_covered)
6. **Count good nodes** -- track max value from root to current node (preorder variant)

---

## Step-by-Step Guide to Solving Any Tree DP Problem

1. **Identify what info you need from children.** (Height? Sum? Count? Multiple values?)
2. **Define the base case.** (What does an empty tree return?)
3. **Define what to return to the parent.** (Usually: best option going through ONE child.)
4. **Define the global update.** (Usually: best option going through BOTH children.)
5. **Trace through a tree with 5-7 nodes.** (Verify your logic before coding.)

---

## Top 5 Mistakes Beginners Make

1. **Confusing the global answer with the return value** -- The function returns info for the PARENT. The global variable tracks the OVERALL BEST. They serve different purposes.
2. **Forgetting to consider negative values** -- In max path sum, use `max(child_result, 0)` to optionally skip a subtree with negative contribution.
3. **Not returning the right thing** -- If the parent needs height, return height (not diameter). If the parent needs gain, return gain (not path sum).
4. **Using `global` instead of `nonlocal` or a list** -- In Python, use `nonlocal` or a mutable container like `[0]` to modify outer variables in nested functions.
5. **Not tracing through an example** -- Tree DP is hard to reason about abstractly. ALWAYS trace through a small tree before coding.

---

## Complexity

| Problem | Time | Space |
|---------|------|-------|
| Diameter | O(n) | O(h) |
| Max path sum | O(n) | O(h) |
| House Robber III | O(n) | O(h) |
| Longest univalue path | O(n) | O(h) |

All Tree DP problems visit each node exactly once = O(n) time.
Space is O(h) for the recursion stack, where h = height of tree.
- Balanced tree: O(log n)
- Skewed tree: O(n)

---

## What To Say In Interview

> "This is a Tree DP problem. At each node, I need to combine information
> from the left and right subtrees. I will use a postorder DFS where
> each call returns the subtree information upward to its parent."

> "The key insight is that the answer I track globally and the value I
> return to the parent are different things. The global answer can use
> both children, but the return value can only include one path direction
> since a valid path cannot fork."

> "For the diameter, my function returns the HEIGHT of each subtree.
> At each node, I update the global diameter as left_height + right_height.
> This is O(n) time and O(h) space."

> "Let me trace through this small example to verify my recurrence before
> coding it up."
