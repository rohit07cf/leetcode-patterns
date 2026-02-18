# Binary Search Tree (BST) Patterns

## Baby Explanation (ELI10)

- A **Binary Search Tree** is a special binary tree with ONE powerful rule: for every node, ALL values in the left subtree are SMALLER, and ALL values in the right subtree are BIGGER.
- Think of it like a dictionary: words before "M" go to the left half, words after "M" go to the right half. Then within each half, you split again. This lets you find any word super fast!
- Because of this rule, if you read a BST from left to right (inorder traversal), you get a **sorted list**. This is the SINGLE MOST IMPORTANT insight for BST problems.
- BSTs let you search, insert, and delete in O(log n) time on average — that is blazing fast compared to O(n) for a regular list.
- Many interview problems give you a BST to test if you can USE the BST property to make your solution faster.

---

## Pattern Recognition

**Use BST properties when you see:**
- "Given a binary search tree..."
- "Validate if a tree is a BST"
- "Find the kth smallest element"
- "Find the closest value"
- "Convert sorted array to BST"
- Any problem where left < root < right matters

**Avoid when:**
- The problem says "binary tree" (NOT "binary search tree") — do not assume BST!
- You are told values can be duplicates without clarification on placement

---

## The BST Rule — Deeply Explained

```
VALID BST:                   NOT a BST:
        8                        8
       / \                      / \
      3   10                   3   10
     / \    \                 / \    \
    1   6   14               1   6   14
       / \  /                   / \  /
      4  7 13                  4  9 13
                                  ^
                            9 > 8 but it is in
                            the LEFT subtree of 8!
```

**The rule is NOT just "left child < parent < right child".**
The rule is: **EVERY node in the left subtree must be less than the root, and EVERY node in the right subtree must be greater.**

This is a subtle but CRITICAL difference:
```
        5
       / \
      1   6
       \
        7      <-- 7 is in the LEFT subtree of 5, but 7 > 5. NOT a valid BST!
```
Node 7 is the right child of 1 (which is fine, 7 > 1), BUT it is also in the left subtree of 5, and 7 > 5. This violates the BST property.

---

## The Golden Insight: Inorder Traversal = Sorted Order

If you do an inorder traversal (left, root, right) of a valid BST, the values come out in **sorted ascending order**.

```
        8
       / \
      3   10
     / \    \
    1   6   14

Inorder: 1, 3, 6, 8, 10, 14    <-- SORTED!
```

This means:
- "Find kth smallest" = do inorder, return kth element
- "Validate BST" = do inorder, check if sorted
- "Find closest value" = use BST search to narrow down

---

## Searching in a BST

Because of the left-small, right-big rule, searching is like binary search:

```python
def searchBST(root, target):
    if not root:
        return None
    if target == root.val:
        return root
    elif target < root.val:
        return searchBST(root.left)    # Go left (smaller)
    else:
        return searchBST(root.right)   # Go right (bigger)
```

```
Search for 6 in:
        8
       / \
      3   10
     / \    \
    1   6   14

Step 1: 6 < 8, go LEFT
Step 2: 6 > 3, go RIGHT
Step 3: 6 == 6, FOUND!

Only visited 3 nodes out of 6. That is the power of BST!
```

---

## Inserting into a BST

Find the right spot (like searching), then add the new node.

```python
def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)    # Found the spot! Create node here.
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root
```

```
Insert 5 into:
        8                    8
       / \                  / \
      3   10      ->       3   10
     / \    \             / \    \
    1   6   14           1   6   14
                            /
                           5     <-- new node!
5 < 8, go left. 5 > 3, go right. 5 < 6, go left. Empty spot, insert!
```

---

## Deleting from a BST

This is trickier. Three cases:

**Case 1: Leaf node** — just remove it.
**Case 2: One child** — replace node with its child.
**Case 3: Two children** — replace with inorder successor (smallest in right subtree).

```python
def deleteNode(root, key):
    if not root:
        return None

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # Found the node to delete!
        if not root.left:        # Case 1 & 2: no left child
            return root.right
        if not root.right:       # Case 2: no right child
            return root.left
        # Case 3: two children
        # Find inorder successor (smallest in right subtree)
        successor = root.right
        while successor.left:
            successor = successor.left
        root.val = successor.val
        root.right = deleteNode(root.right, successor.val)

    return root
```

```
Delete 3 from:
        8                    8
       / \                  / \
      3   10      ->       4   10
     / \    \             / \    \
    1   6   14           1   6   14
       /
      4

Node 3 has two children. Inorder successor = 4 (smallest in right subtree).
Replace 3 with 4, then delete 4 from right subtree.
```

---

## Validate BST (LeetCode 98) — THE RANGE TRICK

The key insight: every node must be within a valid range (min, max).

```
        8           range: (-inf, inf)
       / \
      3   10        3 must be in (-inf, 8), 10 must be in (8, inf)
     / \    \
    1   6   14      1 in (-inf, 3), 6 in (3, 8), 14 in (10, inf)
```

```python
def isValidBST(root):
    def validate(node, low, high):
        if not node:
            return True

        if node.val <= low or node.val >= high:
            return False    # Out of valid range!

        return (validate(node.left, low, node.val) and    # Left: tighten upper bound
                validate(node.right, node.val, high))      # Right: tighten lower bound

    return validate(root, float('-inf'), float('inf'))
```

### Step-by-Step Trace:
```
        5
       / \
      1   7
         / \
        6   8

validate(5, -inf, inf) -> 5 is in range
  validate(1, -inf, 5) -> 1 is in range
    validate(None, -inf, 1) -> True
    validate(None, 1, 5) -> True
  -> True
  validate(7, 5, inf) -> 7 is in range
    validate(6, 5, 7) -> 6 is in range, True
    validate(8, 7, inf) -> 8 is in range, True
  -> True
-> True (VALID BST!)
```

---

## Kth Smallest Element (LeetCode 230)

Inorder traversal = sorted. So the kth element in inorder = kth smallest!

```python
def kthSmallest(root, k):
    count = [0]       # Use list to allow mutation in closure
    result = [0]

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return
        inorder(node.right)

    inorder(root)
    return result[0]
```

```
        5
       / \
      3   6
     / \
    2   4
   /
  1

Inorder: 1, 2, 3, 4, 5, 6

k=1 -> 1 (smallest)
k=3 -> 3
k=5 -> 5
```

---

## Convert Sorted Array to BST (LeetCode 108)

Pick the MIDDLE element as root. Left half becomes left subtree. Right half becomes right subtree. Recursion!

```python
def sortedArrayToBST(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    return root
```

```
Input: [1, 2, 3, 4, 5, 6, 7]

Mid = 4
         4
        / \
  [1,2,3] [5,6,7]

       4
      / \
     2   6
    / \ / \
   1  3 5  7    <-- Balanced BST!
```

---

## Lowest Common Ancestor in BST (LeetCode 235)

In a BST, LCA is simpler than in a regular tree. Use the BST property!

- If both values are smaller than root, LCA is in the left subtree.
- If both values are larger than root, LCA is in the right subtree.
- Otherwise, root IS the LCA (the values split here).

```python
def lowestCommonAncestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left        # Both in left subtree
        elif p.val > root.val and q.val > root.val:
            root = root.right       # Both in right subtree
        else:
            return root             # Split point = LCA!
```

```
        6
       / \
      2   8
     / \ / \
    0  4 7  9

LCA(0, 4):
  Both < 6, go left to 2
  0 < 2, 4 > 2 -> split! LCA = 2

LCA(2, 8):
  2 < 6, 8 > 6 -> split at root! LCA = 6
```

---

## Common Variations

1. **Validate BST** — range trick (pass min/max bounds down)
2. **Kth smallest** — inorder traversal
3. **Closest value** — binary search down the tree
4. **BST iterator** — simulate inorder with a stack
5. **Sorted array to BST** — pick middle, recurse on halves
6. **Two Sum in BST** — inorder to sorted array, then two pointers
7. **Recover BST** — find two swapped nodes via inorder

---

## Top 5 Mistakes Beginners Make

1. **Only checking immediate children** — "left.val < root.val" is NOT enough. You must check the ENTIRE subtree range.
2. **Forgetting BST means strict inequality** — usually BST means left < root < right (no duplicates). Clarify with interviewer!
3. **Not using BST property** — If the problem says "BST", you MUST use the ordering property. Do not treat it as a regular binary tree.
4. **Off-by-one in the range** — Use strict less than / greater than, not less-than-or-equal.
5. **Not recognizing that inorder = sorted** — This single insight solves half of all BST problems.

---

## Complexity

| Operation | Average | Worst (skewed) |
|-----------|---------|----------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Inorder | O(n) | O(n) |
| Validate | O(n) | O(n) |

A skewed BST is basically a linked list:
```
  1
   \
    2
     \
      3        <-- Worst case BST: everything to the right
       \
        4
```

---

## What To Say In Interview

> "Since this is a BST, I can take advantage of the ordering property.
> For every node, all left subtree values are smaller and all right
> subtree values are larger. This means an inorder traversal gives
> me sorted order."

> "I will use the BST property to prune my search. At each node,
> I only need to go left OR right, not both. This gives me
> O(log n) time for a balanced BST."

> "To validate the BST, I will pass down a valid range (low, high) to each
> node and check that the node's value falls within that range."
