# Kth Smallest Element in a BST

**Difficulty:** Medium
**Pattern:** Top K Elements
**Subpattern:** Max Heap for K Smallest
**Link:** https://leetcode.com/problems/kth-smallest-element-in-a-bst/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given the root of a BST and an integer `k`, return the `k`th smallest value (1-indexed) among all node values in the tree.

### 2. Clarification Questions

- **Input constraints?** 1 <= k <= n <= 10^4, node values are unique.
- **Edge cases?** k = 1 (smallest element), k = n (largest element), single-node tree.
- **Expected output?** A single integer — the kth smallest value.
- **Can input be modified?** Yes, the tree is not expected to remain unchanged.

### 3. Brute Force Approach

- **Idea:** Perform a full inorder traversal, collect all values into a sorted list, and return `list[k-1]`.
- **Time:** O(n)
- **Space:** O(n) — storing all node values

### 4. Optimized Approach

- 💡 **Core Insight:** Maintain a **max heap of size k** while traversing. The heap root always holds the kth smallest seen so far. Alternatively, an inorder traversal with early termination at the kth node is O(H + k) and often preferred for BSTs — but the max heap approach generalizes to non-BST structures and demonstrates the subpattern.
- **Time:** O(n log k)
- **Space:** O(k)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Inorder + list | O(n) | O(n) | Simple, collects everything |
| Max heap of size k | O(n log k) | O(k) | General pattern, works on any collection |
| Inorder early stop | O(H + k) | O(H) | BST-specific, optimal for BSTs |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Traverse every node and push its value into a max heap (negate for Python's min heap).
- If heap size exceeds k, pop the largest — this keeps only the k smallest.
- After traversal, the heap root is the kth smallest.

```python
import heapq

class Solution:
    def kthSmallest(self, root, k):
        # Max heap of size k (negate values for Python min heap)
        max_heap = []

        def traverse(node):
            if not node:
                return
            # Push negated value to simulate max heap
            heapq.heappush(max_heap, -node.val)
            # Evict largest if heap exceeds size k
            if len(max_heap) > k:
                heapq.heappop(max_heap)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        # Root of max heap = kth smallest (negated back)
        return -max_heap[0]
```

Also showing the **BST-optimal inorder early stop** (commonly expected in interviews):

```python
class Solution:
    def kthSmallest(self, root, k):
        # Iterative inorder — stop at kth node
        stack = []
        curr = root
        count = 0

        while stack or curr:
            # Go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.right
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Tree: `[3, 1, 4, null, 2]`, k = 1

- Inorder visits: 1 → 2 → 3 → 4
- Max heap approach: push 3 → heap [-3], push 1 → heap [-3, -1], pop -3 → heap [-1], push 4 → heap [-4, -1], pop -4 → heap [-1], push 2 → heap [-2, -1], pop -2 → heap [-1]
- Result: -(-1) = **1** ✓

### Edge Case Testing

- **Empty input:** Constraints guarantee at least one node; not applicable.
- **Single element:** k = 1, single node — returned directly.
- **Typical case:** Balanced BST with k in the middle — works via traversal.
- **Extreme values:** k = n — heap keeps all n elements, returns the max.

### Complexity

- **Time:** O(n log k) — each of n nodes does a heap push/pop in O(log k).
- **Space:** O(k) — heap stores at most k elements (plus O(H) recursion stack).

### Optimization Discussion

For **frequent queries** on the same BST, augment each node with a left-subtree count. This enables O(H) lookup per query. The inorder early stop is O(H + k) which beats the heap approach for BSTs but doesn't demonstrate the max-heap pattern.

### Follow-up Variations

- **Follow-up (LC 230):** If the BST is modified often, how would you optimize? → Augmented BST with subtree sizes.
- What if k changes frequently but the tree is static? → Flatten once to sorted array, then O(1) lookup.

### ⚠️ Common Traps

- **Forgetting k is 1-indexed** — off-by-one errors when converting to 0-indexed.
- **Using min heap instead of max heap** — a min heap doesn't let you evict the largest of the k smallest efficiently.
