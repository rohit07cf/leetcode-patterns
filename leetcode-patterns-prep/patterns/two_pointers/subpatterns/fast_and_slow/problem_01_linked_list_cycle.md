# Linked List Cycle

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Fast and Slow
**Link:** https://leetcode.com/problems/linked-list-cycle/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given the head of a linked list, determine if the list contains a cycle. A cycle exists if some node can be reached again by continuously following the `next` pointer.

### 2. Clarification Questions
- Input constraints? The number of nodes is in range `[0, 10^4]`. Node values range from `-10^5` to `10^5`.
- Edge cases? Empty list (`head` is `None`), single node with no cycle, single node pointing to itself.
- Expected output? Return `True` if a cycle exists, `False` otherwise.
- Can input be modified? Yes, but we should not modify the list structure.

### 3. Brute Force Approach
- **Idea:** Use a hash set to store visited nodes. Traverse the list; if we revisit a node, a cycle exists.
- **Time:** O(n)
- **Space:** O(n) — storing every node in the set.

### 4. Optimized Approach
- **Core Insight:** Use two pointers moving at different speeds. If a cycle exists, the fast pointer will eventually lap the slow pointer and they will meet. If no cycle, the fast pointer reaches the end.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (Hash Set) | O(n) | O(n) | Simple but uses extra memory |
| Optimized (Floyd's) | O(n) | O(1) | Constant space, interview gold standard |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Initialize `slow` and `fast` both at `head`.
- Move `slow` one step and `fast` two steps each iteration.
- If they meet, there is a cycle. If `fast` reaches `None`, no cycle.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # Fast moves 2x speed; if cycle exists, they must meet
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        # Fast reached end — no cycle
        return False
```

---

## PHASE 3 — AFTER CODING

### Dry Run
List: `1 -> 2 -> 3 -> 4 -> 2` (cycle back to node 2)

| Step | slow | fast |
|------|------|------|
| 0 | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | 2 (wrapped) |
| 3 | 4 | 4 |

`slow == fast` at node 4. Return `True`.

### Edge Case Testing
- **Empty input:** `head = None` — while loop doesn't execute, returns `False`.
- **Single element:** No cycle — `fast.next` is `None`, returns `False`. With self-cycle — `slow == fast` after one step, returns `True`.
- **Typical case:** Cycle in the middle — pointers meet inside the cycle.
- **Extreme values:** Long list with no cycle — fast reaches end in n/2 steps.

### Complexity
- **Time:** O(n) — in the worst case, the fast pointer traverses the cycle at most twice before meeting slow.
- **Space:** O(1) — only two pointer variables.

### Optimization Discussion
This is already optimal. The hash set approach trades O(n) space for simpler logic, which may be acceptable in non-interview contexts.

### Follow-up Variations
- **Find the cycle start node** (LeetCode 142 — Linked List Cycle II)
- **Find the length of the cycle** — once pointers meet, keep one stationary and move the other until they meet again, counting steps.
- **Detect cycle in a directed graph** — generalized DFS with coloring.

### Common Traps
- Checking `fast.next` before `fast` — always check `fast` is not `None` first.
- Comparing node **values** instead of node **references** — two nodes can share the same value without being the same node.
- Forgetting the single-node self-cycle case.
