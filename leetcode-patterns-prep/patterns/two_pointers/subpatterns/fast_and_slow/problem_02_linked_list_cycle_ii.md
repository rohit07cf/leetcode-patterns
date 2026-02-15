# Linked List Cycle II

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Fast and Slow
**Link:** https://leetcode.com/problems/linked-list-cycle-ii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return `None`.

### 2. Clarification Questions
- Input constraints? Number of nodes in range `[0, 10^4]`. Node values range from `-10^6` to `10^6`.
- Edge cases? Empty list, single node (with or without self-cycle), no cycle at all.
- Expected output? The **node** (not value) where the cycle starts, or `None`.
- Can input be modified? Should not modify the list.

### 3. Brute Force Approach
- **Idea:** Use a hash set to track visited nodes. The first node visited twice is the cycle start.
- **Time:** O(n)
- **Space:** O(n)

### 4. Optimized Approach
- **Core Insight:** After Floyd's detection finds the meeting point, the distance from `head` to cycle start equals the distance from the meeting point to cycle start (going forward in the cycle). Reset one pointer to `head` and advance both one step at a time — they meet at the cycle start.
- **Time:** O(n)
- **Space:** O(1)

**Why this works mathematically:**
Let `a` = distance from head to cycle start, `b` = distance from cycle start to meeting point, `c` = cycle length.
- Slow traveled: `a + b`
- Fast traveled: `a + b + k*c` (for some integer k >= 1)
- Since fast moves 2x: `2(a + b) = a + b + k*c` => `a = k*c - b`
- So moving `a` steps from the meeting point lands exactly at the cycle start.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (Hash Set) | O(n) | O(n) | Simple, one-pass |
| Optimized (Floyd's Phase 2) | O(n) | O(1) | Two-phase, constant space |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Phase 1:** Detect cycle using fast/slow pointers.
- **Phase 2:** Reset one pointer to `head`, advance both at speed 1 — they meet at cycle start.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Phase 1: Detect if cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Phase 2: Find cycle start
                # Distance from head to start == distance from meeting to start
                entry = head
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry

        # No cycle found
        return None
```

---

## PHASE 3 — AFTER CODING

### Dry Run
List: `3 -> 2 -> 0 -> -4 -> 2` (cycle starts at node with value 2, index 1)

**Phase 1 (Detection):**

| Step | slow | fast |
|------|------|------|
| 0 | 3 | 3 |
| 1 | 2 | 0 |
| 2 | 0 | 2 (wrapped) |
| 3 | -4 | 0 |
| 4 | 2 | 2 |

Meet at node with value 2 (but this is the `-4 -> 2` node, index 1).

**Phase 2 (Find start):**
- `entry` starts at node 3 (head), `slow` at meeting point.
- Both move one step: `entry = 2`, `slow = 0`, `entry = 0`... they meet at node 2 (index 1). Return that node.

### Edge Case Testing
- **Empty input:** `head = None` — while condition fails, returns `None`.
- **Single element:** No cycle — returns `None`. Self-cycle — detected in Phase 1, Phase 2 returns the node itself immediately.
- **Typical case:** Cycle in the middle — Phase 2 correctly locates the start.
- **Extreme values:** Entire list is a cycle (tail points to head) — Phase 2 walks from head and meeting point to converge at head.

### Complexity
- **Time:** O(n) — Phase 1 takes at most O(n) steps, Phase 2 takes at most O(n) steps.
- **Space:** O(1) — only pointer variables.

### Optimization Discussion
This is the optimal solution. The hash set approach is simpler to code and may be preferred when space is not a constraint.

### Follow-up Variations
- **Find cycle length** — after meeting point, count steps until pointers meet again.
- **Remove the cycle** — find cycle start, then find the node whose `next` is the cycle start and set it to `None`.
- **Linked List Cycle in a functional/immutable context** — must use Floyd's since hash set requires reference identity.

### Common Traps
- Forgetting Phase 2 entirely and returning the meeting point instead of the cycle start — the meeting point is generally **not** the cycle start.
- Off-by-one in Phase 2: both pointers must start simultaneously (one at head, one at meeting point).
- Not handling the case where the cycle starts at the head itself.
