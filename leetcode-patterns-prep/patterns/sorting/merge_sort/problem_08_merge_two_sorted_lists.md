# Merge Two Sorted Lists

**Difficulty:** Easy
**Pattern:** Sorting
**Subpattern:** Merge Sort
**Link:** https://leetcode.com/problems/merge-two-sorted-lists/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given the heads of two sorted linked lists, merge them into one sorted list by splicing together the nodes of the two input lists. Return the head of the merged list.

### 2. Clarification Questions

- **Input constraints?** `0 <= list length <= 50`, `-100 <= Node.val <= 100`, both lists are sorted in non-decreasing order.
- **Edge cases?** One or both lists empty, lists of different lengths, all elements in one list smaller than the other.
- **Expected output?** Head of the merged sorted linked list.
- **Can input be modified?** Yes, relink existing nodes (no new nodes needed).

### 3. Brute Force Approach

- **Idea:** Collect all values into an array, sort, build a new linked list.
- **Time:** O(n log n) where n = total nodes
- **Space:** O(n)

### 4. Optimized Approach

- **Core Insight:** This is exactly the **merge step** of merge sort. Use a dummy head node and a tail pointer. Compare the current nodes of both lists, attach the smaller one to the tail, advance that list's pointer. This is the fundamental building block for all merge sort problems.
- **Time:** O(m + n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (collect + sort) | O(n log n) | O(n) | Overkill, ignores sorted property |
| Optimized (two-pointer merge) | O(m + n) | O(1) | Optimal, uses sorted order |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Create a **dummy node** to simplify edge cases (no special handling for the head).
- Use a `tail` pointer to build the result by relinking nodes.
- After one list is exhausted, attach the remainder of the other.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None,
                      list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)  # Dummy head avoids edge case handling
        tail = dummy

        # Compare and attach the smaller node
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach the remaining list (one of them is non-empty or both None)
        tail.next = list1 if list1 else list2

        return dummy.next
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `list1 = [1, 2, 4]`, `list2 = [1, 3, 4]`

| Step | list1 | list2 | Action | Merged so far |
|------|-------|-------|--------|---------------|
| 1 | 1 | 1 | 1 <= 1, pick list1 | 1 |
| 2 | 2 | 1 | 2 > 1, pick list2 | 1->1 |
| 3 | 2 | 3 | 2 <= 3, pick list1 | 1->1->2 |
| 4 | 4 | 3 | 4 > 3, pick list2 | 1->1->2->3 |
| 5 | 4 | 4 | 4 <= 4, pick list1 | 1->1->2->3->4 |
| 6 | None | 4 | Attach remainder | 1->1->2->3->4->4 |

### Edge Case Testing

- **Empty input:** Both `None` -> returns `None` (loop doesn't execute, `tail.next = None`).
- **Single element:** `[1]` and `[]` -> returns `[1]` (loop processes nothing, remainder attached).
- **Typical case:** As shown in dry run.
- **Extreme values:** One list entirely before the other: `[1,2]` + `[3,4]` -> loop exhausts list1 first, then attaches `[3,4]`.

### Complexity

- **Time:** O(m + n) — each node is visited exactly once.
- **Space:** O(1) — only relinking existing nodes, no extra space.

### Optimization Discussion

- **Recursive approach** is also clean: `if list1.val <= list2.val: list1.next = merge(list1.next, list2); return list1`. But it uses O(m + n) stack space.
- The iterative approach is preferred in interviews for O(1) space.

### Follow-up Variations

- Merge k Sorted Lists (LC 23) — generalization using this as the building block.
- Sort List (LC 148) — merge sort on a linked list uses this merge step.
- Merge Sorted Array (LC 88) — array version with in-place constraint.

### Common Traps

- **Not using a dummy node.** Without it, you need special logic to determine the head of the merged list, which is error-prone.
- **Forgetting to attach the remainder.** After the loop, one list may still have nodes. A single `tail.next = list1 if list1 else list2` handles it cleanly.
- **Creating new nodes instead of relinking.** The problem expects splicing existing nodes. Creating new nodes wastes O(n) space unnecessarily.
