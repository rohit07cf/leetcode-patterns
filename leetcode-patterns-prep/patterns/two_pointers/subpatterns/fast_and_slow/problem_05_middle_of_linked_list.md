# Middle of the Linked List

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Fast and Slow
**Link:** https://leetcode.com/problems/middle-of-the-linked-list/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given the head of a singly linked list, return the middle node. If there are two middle nodes (even-length list), return the **second** middle node.

### 2. Clarification Questions
- Input constraints? Number of nodes in range `[1, 100]`. Node values in `[1, 100]`.
- Edge cases? Single node (return it), two nodes (return second), even vs. odd length.
- Expected output? The middle **node** (not just the value).
- Can input be modified? Yes, but no modification needed.

### 3. Brute Force Approach
- **Idea:** Two-pass: first count the total nodes, then traverse to node `count // 2`.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** When a fast pointer (2x speed) reaches the end, the slow pointer (1x speed) is exactly at the middle. This solves it in a **single pass** — critical for streaming or large data scenarios.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Two-pass counting | O(n) | O(1) | Two traversals, simple |
| Fast & Slow | O(n) | O(1) | Single pass, elegant |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Both pointers start at `head`.
- Slow moves 1 step, fast moves 2 steps.
- When fast reaches end (or goes past it), slow is at the middle.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # When fast reaches end, slow is at middle
        # Condition handles both odd and even lengths
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Odd length:** `1 -> 2 -> 3 -> 4 -> 5`

| Step | slow | fast |
|------|------|------|
| 0 | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | 5 |

`fast.next` is `None`. Stop. Return node 3.

**Even length:** `1 -> 2 -> 3 -> 4 -> 5 -> 6`

| Step | slow | fast |
|------|------|------|
| 0 | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | 5 |
| 3 | 4 | None (past end) |

`fast` is `None`. Stop. Return node 4 (second middle).

### Edge Case Testing
- **Empty input:** Not possible (constraint guarantees at least 1 node).
- **Single element:** `fast.next` is `None` immediately, return `head`. Correct.
- **Typical case:** Odd and even lengths handled by the same condition.
- **Extreme values:** 100 nodes — fast reaches end after 50 steps, slow at node 50. Correct.

### Complexity
- **Time:** O(n) — fast pointer traverses the entire list once (n/2 iterations).
- **Space:** O(1) — two pointers only.

### Optimization Discussion
Both approaches are O(n) time and O(1) space. The fast/slow approach is preferred because:
- **Single pass** — important for streaming data.
- **Building block** — this technique is a prerequisite for palindrome checking, reorder list, and other problems.

### Follow-up Variations
- **Return the first middle** for even-length lists — modify condition to `while fast.next and fast.next.next`.
- **Delete the middle node** (LeetCode 2095) — need a `prev` pointer before slow.
- **Split the list into two halves** — this is the first step for merge sort on linked lists.

### Common Traps
- Getting the wrong middle for even-length lists — the `while fast and fast.next` condition naturally gives the **second** middle.
- Confusing the termination condition for "first middle" vs. "second middle."
- Forgetting that this is a **building block** pattern — interviewers often use this as the first step in a harder problem.
