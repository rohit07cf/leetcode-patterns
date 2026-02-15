# Reorder List

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Fast and Slow
**Link:** https://leetcode.com/problems/reorder-list/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a singly linked list `L0 -> L1 -> ... -> Ln-1 -> Ln`, reorder it in-place to `L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...`. You may not modify node values, only rearrange the nodes themselves.

### 2. Clarification Questions
- Input constraints? Number of nodes in range `[1, 5 * 10^4]`. Node values in `[1, 1000]`.
- Edge cases? Single node, two nodes, three nodes (smallest interesting case).
- Expected output? Modified list in-place, no return value.
- Can input be modified? Yes, the problem requires in-place reordering.

### 3. Brute Force Approach
- **Idea:** Store all nodes in an array. Use two pointers from both ends to rebuild the list.
- **Time:** O(n)
- **Space:** O(n)

### 4. Optimized Approach
- **Core Insight:** Combine three classic linked list operations: (1) **find middle** with fast/slow, (2) **reverse** the second half, (3) **merge** the two halves by alternating nodes. Each is O(n) and uses O(1) space.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Array-based | O(n) | O(n) | Simple, stores all nodes |
| Three-step in-place | O(n) | O(1) | Elegant, tests 3 core skills |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Step 1:** Find the middle using fast/slow. Split the list into two halves.
- **Step 2:** Reverse the second half.
- **Step 3:** Merge by alternating nodes from each half.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find middle (for even length, first middle)
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Split: second half starts after slow
        second_half = slow.next
        slow.next = None  # terminate first half

        # Step 2: Reverse second half
        prev = None
        curr = second_half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second_half = prev  # new head of reversed second half

        # Step 3: Merge alternating — first takes one, second takes one
        first = head
        second = second_half
        while second:
            # Save next pointers
            first_next = first.next
            second_next = second.next

            # Interleave
            first.next = second
            second.next = first_next

            # Advance
            first = first_next
            second = second_next
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `1 -> 2 -> 3 -> 4 -> 5`

**Step 1 — Find middle:**
- slow stops at node 3. Split into `1 -> 2 -> 3` and `4 -> 5`.

**Step 2 — Reverse second half:**
- `4 -> 5` becomes `5 -> 4`.

**Step 3 — Merge:**

| Iteration | first | second | Result so far |
|-----------|-------|--------|---------------|
| 1 | 1 | 5 | 1 -> 5 -> 2 -> 3 |
| 2 | 2 | 4 | 1 -> 5 -> 2 -> 4 -> 3 |

Second is `None`. Stop. Final: `1 -> 5 -> 2 -> 4 -> 3`.

### Edge Case Testing
- **Empty input:** Not possible per constraints, but guarded.
- **Single element:** Returns immediately.
- **Typical case:** `1 -> 2 -> 3 -> 4` becomes `1 -> 4 -> 2 -> 3`.
- **Extreme values:** Long list with 50,000 nodes — three O(n) passes, well within time limits.

### Complexity
- **Time:** O(n) — each of the three steps is O(n/2) or O(n).
- **Space:** O(1) — all operations are in-place with pointer manipulation.

### Optimization Discussion
This is already optimal. The array approach is equally fast but uses O(n) space. The three-step approach is a **FAANG favorite** because it tests three fundamental linked list skills in one problem.

### Follow-up Variations
- **Reorder with groups** — instead of single nodes, alternate groups of k.
- **Odd-Even Linked List** (LeetCode 328) — group by position parity, similar merge logic.
- **What if the list is doubly linked?** — Much simpler, just use two pointers from head and tail.

### Common Traps
- Using `while fast and fast.next` instead of `while fast.next and fast.next.next` — the first gives the second middle for even lists, which leaves the first half shorter than the second. This causes the merge to fail.
- Forgetting to terminate the first half with `slow.next = None` — creates a cycle.
- Merge logic errors — save next pointers **before** overwriting them.
- Not handling the case where first half is one node longer than second — the merge loop condition `while second` handles this correctly since the extra node is already in place.
