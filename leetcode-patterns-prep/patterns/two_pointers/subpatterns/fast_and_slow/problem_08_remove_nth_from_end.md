# Remove Nth Node From End of List

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Fast and Slow
**Link:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given the head of a linked list, remove the nth node from the **end** of the list and return its head. Do this in **one pass**.

### 2. Clarification Questions
- Input constraints? Number of nodes in range `[1, 30]`. `1 <= n <= size of list`.
- Edge cases? Removing the head (n equals list length), removing the tail (n = 1), single node list.
- Expected output? The head of the modified list.
- Can input be modified? Yes, we need to remove a node.

### 3. Brute Force Approach
- **Idea:** Two-pass: first count total nodes, then traverse to node `(total - n - 1)` and remove the next node.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** Use two pointers with a **gap of n** between them. Advance the fast pointer n steps first. Then move both together. When fast reaches the end, slow is right before the node to remove. This is a **leader-follower** variant of fast/slow.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Two-pass counting | O(n) | O(1) | Two traversals |
| One-pass with gap | O(n) | O(1) | Single traversal, elegant |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use a **dummy node** before head to handle edge case of removing the head.
- Advance `fast` by `n + 1` steps (so `slow` lands one node **before** the target).
- Move both until `fast` is `None`.
- Delete by skipping: `slow.next = slow.next.next`.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node handles edge case of removing the head
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Advance fast by n+1 steps to create the gap
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # slow is now one node before the target — skip it
        slow.next = slow.next.next

        return dummy.next
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `1 -> 2 -> 3 -> 4 -> 5`, `n = 2`

**Advance fast by 3 steps (n+1):**
- fast: dummy -> 1 -> 2 -> 3

**Move together:**

| Step | slow | fast |
|------|------|------|
| 0 | dummy | 3 |
| 1 | 1 | 4 |
| 2 | 2 | 5 |
| 3 | 3 | None |

`slow` is at node 3. Remove `slow.next` (node 4). Result: `1 -> 2 -> 3 -> 5`.

### Edge Case Testing
- **Empty input:** Not possible per constraints.
- **Single element:** `n = 1`. Fast advances past the only node. Slow stays at dummy. `dummy.next = None`. Returns `None`. Correct.
- **Typical case:** Removing from the middle — handled by the gap approach.
- **Extreme values:** `n = list length` (remove head). Fast advances to `None`. Slow at dummy. `dummy.next = head.next`. Correctly removes head.

### Complexity
- **Time:** O(L) where L is the list length — single traversal.
- **Space:** O(1) — only pointer variables plus one dummy node.

### Optimization Discussion
This is already optimal for a single pass. The dummy node technique is crucial — without it, removing the head requires special-case handling.

**Key technique:** The dummy/sentinel node pattern appears in many linked list problems. Always consider using it when the head might change.

### Follow-up Variations
- **Remove all nodes with value equal to the nth from end** — find the value first, then remove all occurrences.
- **Remove the nth node from the beginning** — trivial, just traverse n-1 steps.
- **What if n could be invalid?** — Add a length check or handle `fast` becoming `None` during the initial advance.

### Common Traps
- Not using a dummy node — leads to special-case code for removing the head, which is error-prone.
- Advancing fast by `n` instead of `n + 1` — slow ends up **on** the target node instead of **before** it, making deletion impossible in a singly linked list.
- Returning `head` instead of `dummy.next` — when the head is removed, `head` still points to the deleted node.
- Not handling `n = list length` — this is the "remove head" case, which the dummy node handles seamlessly.
