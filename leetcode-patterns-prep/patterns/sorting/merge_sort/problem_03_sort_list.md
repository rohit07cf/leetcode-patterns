# Sort List

**Difficulty:** Medium
**Pattern:** Sorting
**Subpattern:** Merge Sort
**Link:** https://leetcode.com/problems/sort-list/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given the head of a linked list, sort it in ascending order using O(n log n) time and O(1) memory (the follow-up asks for constant space). Return the head of the sorted list.

### 2. Clarification Questions

- **Input constraints?** `0 <= list length <= 5 * 10^4`, `-10^5 <= Node.val <= 10^5`.
- **Edge cases?** Empty list, single node, two nodes, already sorted, reverse sorted.
- **Expected output?** Head of the sorted linked list.
- **Can input be modified?** Yes, rearrange the existing nodes.

### 3. Brute Force Approach

- **Idea:** Collect all values into an array, sort the array, then reconstruct the linked list (or overwrite values).
- **Time:** O(n log n)
- **Space:** O(n) — storing values

### 4. Optimized Approach

- **Core Insight:** Merge sort is **naturally suited** for linked lists. Finding the middle with slow/fast pointers splits in O(n). Merging two sorted lists is O(n) with O(1) space (just re-link pointers). No random access needed, unlike arrays.
- **Time:** O(n log n)
- **Space:** O(log n) for recursion stack (O(1) with bottom-up iterative approach)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (array sort) | O(n log n) | O(n) | Simple but defeats the purpose |
| Optimized (merge sort on list) | O(n log n) | O(log n) | Elegant, O(1) merge space |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Find middle** using slow/fast pointers. Cut the list into two halves.
- **Recursively sort** each half.
- **Merge** two sorted halves by relinking nodes (no new nodes created).

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        # Base case: empty or single node
        if not head or not head.next:
            return head

        # Split the list into two halves using slow/fast pointers
        mid = self._get_mid(head)
        right_head = mid.next
        mid.next = None  # Cut the list

        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(right_head)

        # Merge two sorted halves
        return self._merge(left, right)

    def _get_mid(self, head: ListNode) -> ListNode:
        # slow/fast: slow ends at the node BEFORE the midpoint
        # This ensures left half gets the smaller portion on even splits
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach whichever list still has remaining nodes
        tail.next = l1 if l1 else l2
        return dummy.next
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `4 -> 2 -> 1 -> 3`

1. **Find mid:** slow=4, fast=2 -> slow=2, fast stops. Mid = node(2). Split: `4->2` | `1->3`
2. **Sort `4->2`:** Mid = node(4). Split: `4` | `2`. Merge: `2->4`
3. **Sort `1->3`:** Mid = node(1). Split: `1` | `3`. Merge: `1->3`
4. **Merge `2->4` and `1->3`:**
   - 2 vs 1 -> pick 1
   - 2 vs 3 -> pick 2
   - 4 vs 3 -> pick 3
   - Append 4
   - Result: `1->2->3->4`

### Edge Case Testing

- **Empty input:** `None` -> returns `None` immediately.
- **Single element:** `[1]` -> returns the single node unchanged.
- **Typical case:** `4->2->1->3` -> `1->2->3->4`.
- **Extreme values:** All same values `3->3->3` -> stable sort preserves order.

### Complexity

- **Time:** O(n log n) — log n levels, O(n) work per level for split + merge.
- **Space:** O(log n) — recursion stack depth. The merge itself is O(1) since we relink existing nodes.

### Optimization Discussion

- **Bottom-up iterative merge sort** achieves true O(1) space by merging sublists of size 1, 2, 4, ... without recursion. More complex to implement but preferred if the interviewer insists on O(1) space.
- The recursive version is usually acceptable in interviews.

### Follow-up Variations

- Sort an array using merge sort (LC 912).
- Merge two sorted linked lists (LC 21).
- Insertion sort on a linked list (LC 147).

### Common Traps

- **Slow/fast pointer initialization:** Starting both at `head` causes `[1,2]` to split as `[1,2]` and `[]`, leading to infinite recursion. Start `fast = head.next` so the left half gets the smaller portion.
- **Forgetting to cut the list** (`mid.next = None`). Without this, the recursion processes the entire list every time, causing infinite recursion.
- **Not handling the dummy node pattern** in merge. Using a dummy head simplifies edge cases when building the merged result.
