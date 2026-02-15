# Merge Two Sorted Lists

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Merge Style
**Link:** https://leetcode.com/problems/merge-two-sorted-lists/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given the heads of two sorted linked lists, merge them into one sorted linked list built from the nodes of the two input lists.

### 2. Clarification Questions
- Input constraints? `0 <= list length <= 50`, node values in `[-100, 100]`
- Edge cases? One or both lists empty; lists of different lengths
- Expected output? Head of the merged sorted linked list
- Can input be modified? Yes — we splice existing nodes

### 3. Brute Force Approach
- **Idea:** Collect all values into an array, sort, build a new linked list.
- **Time:** O((m+n) log(m+n))
- **Space:** O(m + n)

### 4. Optimized Approach
- **Core Insight:** Use a **dummy head** and a `tail` pointer. At each step, compare the two current nodes and attach the smaller one to `tail`. Advance that list's pointer. When one list is exhausted, attach the remainder of the other.
- **Time:** O(m + n)
- **Space:** O(1) — only pointer manipulation

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O((m+n) log(m+n)) | O(m+n) | Ignores sorted property |
| Optimized | O(m + n) | O(1) | Classic merge with dummy head |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Create a **dummy node** to simplify edge cases (no special-casing the head).
- Walk both lists, always appending the smaller current node.
- When one list is exhausted, attach the other's remainder directly.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(-1)  # dummy head avoids special-casing
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Attach whichever list still has remaining nodes
    tail.next = list1 if list1 else list2

    return dummy.next
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`list1 = 1→2→4`, `list2 = 1→3→4`

| Step | list1 | list2 | Action | Merged so far |
|------|-------|-------|--------|---------------|
| 1 | 1→2→4 | 1→3→4 | 1 <= 1, take list1 | 1 |
| 2 | 2→4 | 1→3→4 | 2 > 1, take list2 | 1→1 |
| 3 | 2→4 | 3→4 | 2 < 3, take list1 | 1→1→2 |
| 4 | 4 | 3→4 | 4 > 3, take list2 | 1→1→2→3 |
| 5 | 4 | 4 | 4 <= 4, take list1 | 1→1→2→3→4 |
| 6 | None | 4 | Attach remainder | 1→1→2→3→4→4 |

### Edge Case Testing
- **Empty input:** Both None → returns None; one None → returns the other list
- **Single element:** One node each → compares once, attaches remainder
- **Typical case:** As shown above
- **Extreme values:** All values equal → all come from list1 first (stable), then list2

### Complexity
- **Time:** O(m + n) — each node visited once
- **Space:** O(1) — only pointer reassignment, no new nodes created

### Optimization Discussion

A **recursive** approach is elegant but uses O(m+n) stack space. The iterative version is preferred in interviews for O(1) space.

### Follow-up Variations
- Merge k sorted lists (LeetCode 23) — use a min-heap or divide and conquer
- Merge sorted arrays (LeetCode 88) — same logic, array form
- Sort a linked list (LeetCode 148) — merge sort on linked list

### Common Traps
- Forgetting the dummy node and writing complex head-initialization logic
- Not handling the case where one list is exhausted before the other
- Creating new nodes instead of re-linking existing ones (wastes space)
