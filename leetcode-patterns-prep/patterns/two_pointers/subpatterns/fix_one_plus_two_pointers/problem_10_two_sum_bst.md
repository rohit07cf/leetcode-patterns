# Two Sum BSTs

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Fix One + Two Pointers
**Link:** https://leetcode.com/problems/two-sum-bsts/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given two binary search trees `root1` and `root2`, return `true` if there exists a node in the first BST and a node in the second BST such that their values sum to a given `target`.

### 2. Clarification Questions

- **Input constraints?** Each BST has 1 to 5000 nodes, values from -10^9 to 10^9. Target from -10^9 to 10^9.
- **Edge cases?** Single node in each tree. No valid pair exists. Trees of vastly different sizes.
- **Expected output?** Boolean.
- **Can input be modified?** Trees shouldn't be modified, but we can extract values.

### 3. Brute Force Approach

- **Idea:** Traverse tree1, for each node value search tree2 for `target - value`. BST search is O(h) per query.
- **Time:** O(n1 * h2) where h2 is the height of tree2
- **Space:** O(h1) for recursion stack

### 4. Optimized Approach

- **💡 Core Insight:** Perform inorder traversal on both BSTs to get sorted arrays. Then use **two pointers** — one at the start of the first array (smallest) and one at the end of the second array (largest). This is the classic "fix one + two pointers on sorted data" pattern applied to two separate sorted sequences.
- **Time:** O(n1 + n2)
- **Space:** O(n1 + n2)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n1 * h2) | O(h1) | Search tree2 for each node in tree1 |
| Hash Set | O(n1 + n2) | O(n1) | Store tree1 values, check tree2 |
| Two Pointers | O(n1 + n2) | O(n1 + n2) | Inorder + two pointers |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Inorder traverse both BSTs to get sorted lists.
- Use two pointers: `i` starts at beginning of list1 (smallest), `j` starts at end of list2 (largest).
- If `list1[i] + list2[j] == target`, return True.
- If sum < target, move `i` right (need larger value from tree1).
- If sum > target, move `j` left (need smaller value from tree2).

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def twoSumBSTs(root1: TreeNode, root2: TreeNode, target: int) -> bool:
    def inorder(root: TreeNode) -> list[int]:
        """Return sorted values via inorder traversal."""
        if not root:
            return []
        return inorder(root.left) + [root.val] + inorder(root.right)

    list1 = inorder(root1)  # sorted ascending
    list2 = inorder(root2)  # sorted ascending

    # Two pointers: start of list1, end of list2
    i, j = 0, len(list2) - 1

    while i < len(list1) and j >= 0:
        current_sum = list1[i] + list2[j]

        if current_sum == target:
            return True
        elif current_sum < target:
            i += 1  # need a larger value from tree1
        else:
            j -= 1  # need a smaller value from tree2

    return False
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:**
```
Tree1:     2         Tree2:     1
          / \                  / \
         1   4                0   3
```
`target = 5`

- list1 = [1, 2, 4] (inorder of tree1)
- list2 = [0, 1, 3] (inorder of tree2)

Two pointers: i=0, j=2

- list1[0] + list2[2] = 1 + 3 = 4 < 5. i++.
- list1[1] + list2[2] = 2 + 3 = 5 == 5. Return `True`.

**Output:** `True` (nodes 2 and 3)

### Edge Case Testing

- **Empty input:** Not possible (each tree has >= 1 node).
- **Single element:** Each tree has one node. Check if their sum equals target.
- **Typical case:** Trees shown above, target=5, returns `True`.
- **Extreme values:** Large values near +/-10^9. Sum could approach 2*10^9, but Python handles big integers natively.

### Complexity

- **Time:** O(n1 + n2) — inorder traversal O(n1 + n2) + two-pointer scan O(n1 + n2).
- **Space:** O(n1 + n2) — storing both sorted arrays plus recursion stack O(h1 + h2).

### Optimization Discussion

**Hash set approach** uses less space in practice:

```python
def twoSumBSTs_hashset(root1, root2, target):
    # Store all values from tree1
    values = set()
    def collect(node):
        if not node: return
        values.add(node.val)
        collect(node.left)
        collect(node.right)
    collect(root1)

    # Check tree2 nodes against the set
    def search(node):
        if not node: return False
        if (target - node.val) in values:
            return True
        return search(node.left) or search(node.right)

    return search(root2)
```

This uses O(n1) space instead of O(n1 + n2), and still runs in O(n1 + n2) time.

**BST iterator approach** (most space-efficient for the two-pointer variant) uses O(h1 + h2) space by maintaining stacks for forward/backward iteration:

```python
def twoSumBSTs_iterators(root1, root2, target):
    # Forward iterator for tree1 (smallest to largest)
    stack1, node = [], root1
    while node:
        stack1.append(node)
        node = node.left

    # Backward iterator for tree2 (largest to smallest)
    stack2, node = [], root2
    while node:
        stack2.append(node)
        node = node.right

    while stack1 and stack2:
        val1 = stack1[-1].val
        val2 = stack2[-1].val
        s = val1 + val2
        if s == target:
            return True
        elif s < target:
            # Advance forward iterator on tree1
            node = stack1.pop().right
            while node:
                stack1.append(node)
                node = node.left
        else:
            # Advance backward iterator on tree2
            node = stack2.pop().left
            while node:
                stack2.append(node)
                node = node.right
    return False
```

### Follow-up Variations

- **Two Sum IV - Input is a BST (LC 653):** Same tree for both values — use set or BST iterator.
- **Two Sum (LC 1):** Array version with hash map.
- **Two Sum in sorted array (LC 167):** Direct two-pointer on single sorted array.

### Common Traps

- **Searching within the same tree** — this problem uses *two different* BSTs. Each value must come from a different tree.
- **Not leveraging BST sorted property** — using a generic tree traversal + hash set works but misses the two-pointer optimization.
- **Pointer direction confusion** — `i` moves forward in list1, `j` moves backward in list2. Both lists are ascending, so we pair smallest with largest.
- **Forgetting the inorder traversal produces sorted output** — this is the key property that enables two pointers.
