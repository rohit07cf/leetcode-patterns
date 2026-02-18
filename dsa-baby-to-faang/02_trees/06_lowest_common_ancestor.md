# Lowest Common Ancestor (LCA) — A FAANG Favorite

## Baby Explanation (ELI10)

- Imagine your family tree. You and your cousin both have parents, grandparents, great-grandparents, etc. The **Lowest Common Ancestor** is the CLOSEST person who is an ancestor of BOTH of you.
- If you and your sibling pick your LCA, it is your parent (you share the same parent).
- If you and your cousin pick your LCA, it is your grandparent (the first person you both descend from).
- In a tree data structure, the LCA of two nodes is the deepest node that has BOTH nodes as descendants (a node can be a descendant of itself).
- This problem shows up ALL THE TIME in FAANG interviews. It tests whether you truly understand recursion.

---

## Pattern Recognition

**Use LCA when you see:**
- "Find the lowest common ancestor of two nodes"
- "Find the distance between two nodes" (hint: distance = depth(p) + depth(q) - 2 * depth(LCA))
- "Find the path between two nodes" (path goes through LCA)
- "Find the first common manager of two employees"

**Avoid when:**
- The tree is a BST (use the simpler BST version instead)
- You only need ancestors of ONE node (just walk up)

---

## Visualizing LCA

```
             3
           /   \
          5     1
         / \   / \
        6   2 0   8
           / \
          7   4
```

| Node p | Node q | LCA | Why? |
|--------|--------|-----|------|
| 5 | 1 | 3 | 3 is the first node that has both 5 and 1 below it |
| 5 | 4 | 5 | 5 is an ancestor of 4, and a node is its own ancestor |
| 6 | 4 | 5 | Both 6 and 4 are in the subtree of 5 |
| 6 | 0 | 3 | 6 is on the left side, 0 is on the right side; they meet at 3 |
| 7 | 8 | 3 | 7 is deep left, 8 is deep right; they meet at root |

---

## The Key Insight (Read This 3 Times)

At each node, we ask: "Is p or q in my LEFT subtree? Is p or q in my RIGHT subtree?"

Three possible answers:
1. **Both are in my LEFT subtree** -> the LCA must be in my left subtree. Return whatever left returns.
2. **Both are in my RIGHT subtree** -> the LCA must be in my right subtree. Return whatever right returns.
3. **One is in LEFT and one is in RIGHT** -> I AM the LCA! The paths to p and q split at me.

Also: if **I am p or q** -> I might be the LCA (if the other node is below me).

---

## Minimal Python Template (LeetCode 236)

```python
def lowestCommonAncestor(root, p, q):
    # Base case: reached the end, or found one of the targets
    if not root or root == p or root == q:
        return root

    # Search in left and right subtrees
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # If both sides found something, current node is the LCA
    if left and right:
        return root

    # Otherwise, return whichever side found something
    return left if left else right
```

That is it. 10 lines. One of the most elegant recursive solutions in all of computer science.

---

## Step-by-Step Trace (Tiny Input)

**Input:** Find LCA of 5 and 1 in this tree:
```
             3
           /   \
          5     1
         / \   / \
        6   2 0   8
```

**Walkthrough:**
```
LCA(3, p=5, q=1):
    3 is not None, not 5, not 1. Keep going.

    left = LCA(5, p=5, q=1):
        5 == p! Return 5.       <-- Found p on the left!

    right = LCA(1, p=5, q=1):
        1 == q! Return 1.       <-- Found q on the right!

    left = 5 (not None)
    right = 1 (not None)
    BOTH sides found something! Return root = 3.

Answer: 3
```

**Another example:** Find LCA of 5 and 4:
```
             3
           /   \
          5     1
         / \   / \
        6   2 0   8
           / \
          7   4
```

```
LCA(3, p=5, q=4):
    left = LCA(5, p=5, q=4):
        5 == p! Return 5.       <-- Found p, stop here. Don't go deeper.

    right = LCA(1, p=5, q=4):
        left = LCA(0, ...) -> None
        right = LCA(8, ...) -> None
        Both None. Return None.  <-- Neither p nor q on the right.

    left = 5 (not None)
    right = None
    Only left found something. Return left = 5.

Answer: 5  (because 5 is an ancestor of 4, and 5 itself is p)
```

---

## Why This Works — The Logic Explained

The function returns:
- **The node itself** if the node is p or q
- **None** if neither p nor q is in this subtree
- **The LCA** if both p and q are found in this subtree

At any node:
```
Case 1: left=None, right=None   -> neither p nor q below me. Return None.
Case 2: left=Node, right=None   -> both p and q are in my left subtree. Return left.
Case 3: left=None, right=Node   -> both p and q are in my right subtree. Return right.
Case 4: left=Node, right=Node   -> p is on one side, q is on the other. I AM THE LCA!
```

```
                3          <- Case 4: left found 5, right found 1
              /   \            I am the LCA!
            5       1
          (found)  (found)
```

---

## LCA in a BST (Simpler! LeetCode 235)

In a BST, you do not need to search both sides. The BST property tells you which direction to go.

```python
def lowestCommonAncestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left        # Both smaller -> go left
        elif p.val > root.val and q.val > root.val:
            root = root.right       # Both larger -> go right
        else:
            return root             # Split point -> this is the LCA!
```

```
BST:        6
           / \
          2   8
         / \ / \
        0  4 7  9

LCA(0, 4): Both < 6, go left to 2. 0 < 2, 4 > 2 -> split! LCA = 2
LCA(2, 8): 2 < 6, 8 > 6 -> split! LCA = 6
LCA(7, 9): Both > 6, go right to 8. 7 < 8, 9 > 8 -> split! LCA = 8
```

Time: O(h) — only go down one path. Much faster than O(n) for general trees!

---

## Variation 1: LCA with Parent Pointers

Some problems give you nodes with a `parent` pointer. This turns into the "intersection of two linked lists" problem!

```
             3
           /   \
          5     1
         / \   / \
        6   2 0   8

Path from 6 to root: 6 -> 5 -> 3
Path from 0 to root: 0 -> 1 -> 3
                              ^
                         They meet at 3!
```

```python
def lowestCommonAncestor(p, q):
    # Get depths
    def get_depth(node):
        depth = 0
        while node:
            node = node.parent
            depth += 1
        return depth

    # Align to same depth
    dp, dq = get_depth(p), get_depth(q)
    while dp > dq:
        p = p.parent
        dp -= 1
    while dq > dp:
        q = q.parent
        dq -= 1

    # Walk up together until they meet
    while p != q:
        p = p.parent
        q = q.parent

    return p
```

**Alternative (set-based):**
```python
def lowestCommonAncestor(p, q):
    ancestors = set()

    # Add all ancestors of p to the set
    while p:
        ancestors.add(p)
        p = p.parent

    # Walk up from q until we hit an ancestor of p
    while q not in ancestors:
        q = q.parent

    return q
```

---

## Variation 2: LCA of Multiple Nodes

What if you have a list of nodes instead of just two? Same idea, just extend it.

```python
def lowestCommonAncestor(root, nodes):
    target_set = set(nodes)

    def dfs(node):
        if not node:
            return None
        if node in target_set:
            return node

        left = dfs(node.left)
        right = dfs(node.right)

        if left and right:
            return node
        return left if left else right

    return dfs(root)
```

---

## Variation 3: Distance Between Two Nodes

The distance between nodes p and q = depth(p) + depth(q) - 2 * depth(LCA).

```
             3          depth 0
           /   \
          5     1       depth 1
         / \   / \
        6   2 0   8    depth 2

Distance(6, 0):
  LCA(6, 0) = 3
  depth(6) = 2, depth(0) = 2, depth(3) = 0
  distance = 2 + 2 - 2*0 = 4
  Path: 6 -> 5 -> 3 -> 1 -> 0 (4 edges)
```

---

## Common Variations Summary

1. **LCA of two nodes in binary tree** — the classic template (LeetCode 236)
2. **LCA in BST** — use BST property to avoid full search (LeetCode 235)
3. **LCA with parent pointers** — intersecting linked lists approach (LeetCode 1650)
4. **LCA of deepest leaves** — combine LCA with depth tracking (LeetCode 1123)
5. **LCA of multiple nodes** — extend the classic to a set of targets
6. **Distance between two nodes** — find LCA, then compute depths

---

## Top 5 Mistakes Beginners Make

1. **Not handling the case where a node is its own ancestor** — The problem says "a node can be a descendant of itself." So if p is an ancestor of q, then LCA(p, q) = p.
2. **Searching the entire tree when it is a BST** — If the tree is a BST, you can solve LCA in O(h) instead of O(n). Use the BST property!
3. **Forgetting the base case** — `if not root or root == p or root == q: return root` handles both "nothing found" and "found target."
4. **Confusing what the function returns** — It returns p, q, or the LCA node. Not True/False. Not a count.
5. **Not tracing through a small example** — This problem is tricky enough that you should ALWAYS trace through a 5-7 node tree before coding.

---

## Complexity

| Variant | Time | Space |
|---------|------|-------|
| Binary tree LCA | O(n) | O(h) recursion stack |
| BST LCA | O(h) | O(1) iterative |
| Parent pointer LCA | O(h) | O(h) for set, O(1) for two-pointer |
| Multiple nodes LCA | O(n) | O(h) recursion stack |

---

## What To Say In Interview

> "I will use a recursive approach. At each node, I search for p and q in the
> left and right subtrees. If both subtrees return non-null, the current node
> is the LCA because p and q are on different sides. If only one side returns
> non-null, the LCA is in that subtree."

> "The base case handles three situations: reaching a null node, finding p,
> or finding q. In all three cases, I return the current node."

> "Since this is a BST, I can optimize by using the ordering property.
> If both values are smaller than the root, I only need to search the left
> subtree. If both are larger, only the right. Otherwise, the root is the
> split point and therefore the LCA."
