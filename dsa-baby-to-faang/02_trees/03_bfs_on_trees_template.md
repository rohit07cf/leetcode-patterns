# BFS on Trees — Level by Level Exploration

## Baby Explanation (ELI10)

- **BFS** stands for Breadth-First Search. Imagine you are in a building with many floors. You explore EVERY room on floor 1 before going to floor 2, then every room on floor 2 before floor 3, and so on.
- In a tree, BFS visits ALL nodes at depth 0 (the root), then ALL nodes at depth 1, then ALL at depth 2, etc.
- BFS uses a **queue** (first-in, first-out line), NOT recursion. Think of it like a line at a store — first person in line gets served first.
- BFS is perfect when the problem talks about "levels", "layers", "floors", or "shortest distance".
- DFS goes DEEP. BFS goes WIDE. That is the core difference.
- BFS on trees is simpler than BFS on graphs because trees have no cycles — you never visit the same node twice.

---

## Pattern Recognition

**Use BFS when you see:**
- "Level order traversal"
- "Find all nodes at depth K"
- "Minimum depth of a tree"
- "Right side view" / "Left side view"
- "Zigzag level order"
- "Connect nodes at the same level"
- Anything that says "level by level" or "floor by floor"

**Avoid BFS when:**
- You need to compute bottom-up (height, diameter) — use DFS postorder
- You need root-to-leaf paths — easier with DFS
- The problem is naturally recursive (most tree problems)

---

## How BFS Works — Visual Walkthrough

```
        1
       / \
      2   3
     / \   \
    4   5   6
```

BFS visits nodes level by level:
```
Level 0:  [1]
Level 1:  [2, 3]
Level 2:  [4, 5, 6]

Visit order: 1, 2, 3, 4, 5, 6
```

Here is what happens step by step with the queue:

```
Step 1: Queue = [1]              Process 1, add its children
Step 2: Queue = [2, 3]          Process 2, add 4 and 5
Step 3: Queue = [3, 4, 5]      Process 3, add 6
Step 4: Queue = [4, 5, 6]      Process 4 (leaf, no children)
Step 5: Queue = [5, 6]          Process 5 (leaf)
Step 6: Queue = [6]             Process 6 (leaf)
Step 7: Queue = []               DONE!
```

---

## The BFS Template (Memorize This)

```python
from collections import deque

def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)      # How many nodes on this level?
        level = []

        for _ in range(level_size):  # Process ALL nodes on this level
            node = queue.popleft()   # Take from the FRONT of the line
            level.append(node.val)

            if node.left:
                queue.append(node.left)   # Add children to BACK of line
            if node.right:
                queue.append(node.right)

        result.append(level)         # Save this level's results

    return result
```

**Why `deque` and not a regular list?**
- `deque.popleft()` is O(1) — instant
- `list.pop(0)` is O(n) — slow because it shifts everything
- Always use `deque` for BFS. Interviewers notice!

---

## Step-by-Step Example: Level Order Traversal (LeetCode 102)

**Input:**
```
        3
       / \
      9   20
         / \
        15  7
```

**Walkthrough:**

```
Start: queue = [3]

--- Level 0 ---
level_size = 1
  Process 3 -> add 9 and 20
  level = [3]
queue = [9, 20]
result = [[3]]

--- Level 1 ---
level_size = 2
  Process 9 -> no children
  Process 20 -> add 15 and 7
  level = [9, 20]
queue = [15, 7]
result = [[3], [9, 20]]

--- Level 2 ---
level_size = 2
  Process 15 -> no children
  Process 7 -> no children
  level = [15, 7]
queue = []
result = [[3], [9, 20], [15, 7]]

--- Queue empty, DONE ---
```

**Output:** `[[3], [9, 20], [15, 7]]`

---

## Example 2: Minimum Depth of Binary Tree (LeetCode 111)

BFS finds the FIRST leaf — which is at the minimum depth. DFS would have to explore the entire tree.

```
        1
       / \
      2   3         <-- 3 is a leaf at depth 1!
     / \
    4   5
```

DFS would go all the way down to 4 (depth 2) before checking 3.
BFS finds 3 at level 1 and returns immediately. Much faster!

```python
from collections import deque

def minDepth(root):
    if not root:
        return 0

    queue = deque([(root, 1)])    # (node, depth)

    while queue:
        node, depth = queue.popleft()

        # First leaf we encounter = minimum depth!
        if not node.left and not node.right:
            return depth

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
```

---

## Example 3: Binary Tree Right Side View (LeetCode 199)

Imagine standing to the RIGHT of the tree. What nodes can you see?

```
        1          <-- you see 1
       / \
      2   3        <-- you see 3 (it blocks 2)
     / \
    4   5          <-- you see 5 (rightmost on this level)

Right side view: [1, 3, 5]
```

**Trick:** The rightmost node at each level = the LAST node processed at each level.

```python
from collections import deque

def rightSideView(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            if i == level_size - 1:    # Last node in this level!
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
```

---

## Example 4: Zigzag Level Order (LeetCode 103)

Same as level order, but alternate direction each level.

```
        3
       / \
      9   20
         / \
        15  7

Level 0 (left to right):  [3]
Level 1 (right to left):  [20, 9]
Level 2 (left to right):  [15, 7]
```

```python
from collections import deque

def zigzagLevelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

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

        if not left_to_right:
            level.reverse()          # Flip this level!

        result.append(level)
        left_to_right = not left_to_right   # Toggle direction

    return result
```

---

## BFS vs DFS — When to Use Which?

| Scenario | Best Choice | Why |
|----------|-------------|-----|
| Level-by-level processing | **BFS** | Naturally processes one level at a time |
| Minimum depth / shortest path | **BFS** | Finds nearest target first |
| Right/left side view | **BFS** | Needs last/first node per level |
| Height / diameter | **DFS** | Needs bottom-up computation |
| Root-to-leaf paths | **DFS** | Naturally follows paths |
| Validate BST | **DFS** | Needs range passing (top-down) |
| Check if balanced | **DFS** | Needs subtree heights (bottom-up) |

**Rule of thumb:** If the word "level" appears in the problem, use BFS. Otherwise, DFS is usually simpler.

---

## ASCII Diagram: BFS Wave Pattern

Think of BFS as a wave spreading outward from the root:

```
Wave 1:     ->  1  <-           Level 0
               / \
Wave 2:   -> 2   3 <-          Level 1
             / \   \
Wave 3: -> 4   5   6 <-        Level 2

Each wave = one level of the queue processing
```

---

## Common Variations

1. **Level order traversal** — collect nodes level by level
2. **Reverse level order** — same but reversed (bottom to top)
3. **Zigzag traversal** — alternate left-right and right-left
4. **Average of levels** — compute average value per level
5. **Largest value in each row** — max per level
6. **Right/Left side view** — last/first node per level
7. **Connect next pointers** — link nodes at the same level

All of these use the SAME BFS template with small tweaks!

---

## Top 5 Mistakes Beginners Make

1. **Using a list instead of deque** — `list.pop(0)` is O(n), `deque.popleft()` is O(1).
2. **Forgetting `level_size = len(queue)`** — You MUST capture the size BEFORE the inner loop, because the queue grows during the loop.
3. **Not handling the empty tree** — Always check `if not root` first.
4. **Confusing BFS and DFS** — BFS uses a queue (FIFO). DFS uses a stack (LIFO) or recursion.
5. **Adding None children to the queue** — Always check `if node.left` before appending.

---

## Complexity

| | Time | Space |
|---|---|---|
| BFS | O(n) — visit each node once | O(w) — max width of tree |
| Balanced tree | O(n) | O(n/2) = O(n) at the widest level |
| Skewed tree | O(n) | O(1) — only one node per level |

**Note:** BFS space is O(w) where w is the maximum width. For a balanced tree, the bottom level can have ~n/2 nodes, so space is O(n). This is actually MORE space than DFS for balanced trees!

```
BFS space (balanced):         BFS space (skewed):
        1                     1
       / \                     \
      2   3                     2
     / \ / \                     \
    4  5 6  7  <-- 4 nodes       3  <-- 1 node per level
                    in queue
    Space: O(n)                 Space: O(1)
```

---

## What To Say In Interview

> "Since this problem requires level-by-level processing, I will use BFS
> with a queue. I will process all nodes at the current level before
> moving to the next level. I will use a deque for O(1) popleft operations."

> "The time complexity is O(n) since I visit each node once.
> The space complexity is O(w) where w is the maximum width of the tree,
> which in the worst case is O(n) for a balanced tree."
