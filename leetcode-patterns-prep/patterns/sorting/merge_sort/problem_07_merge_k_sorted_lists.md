# Merge k Sorted Lists

**Difficulty:** Hard
**Pattern:** Sorting
**Subpattern:** Merge Sort
**Link:** https://leetcode.com/problems/merge-k-sorted-lists/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of `k` linked lists, each sorted in ascending order, merge all lists into one sorted linked list and return its head.

### 2. Clarification Questions

- **Input constraints?** `0 <= k <= 10^4`, `0 <= list length <= 500`, total nodes across all lists up to `10^4`, `-10^4 <= Node.val <= 10^4`.
- **Edge cases?** `k = 0` (empty array), lists containing empty lists, `k = 1`, all lists have one element.
- **Expected output?** Head of the merged sorted linked list.
- **Can input be modified?** Yes, relink existing nodes.

### 3. Brute Force Approach

- **Idea:** Collect all values from all lists, sort them, then build a new linked list.
- **Time:** O(N log N) where N = total number of nodes
- **Space:** O(N)

### 4. Optimized Approach

- **Core Insight:** Apply **divide and conquer** (merge sort style). Pair up lists and merge each pair, reducing k lists to k/2, then k/4, and so on. Each merge of two sorted lists is O(n1 + n2). This mirrors merge sort's structure — log k levels, O(N) work per level.
- **Time:** O(N log k)
- **Space:** O(1) extra (just relinking nodes; O(log k) for recursion)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (collect + sort) | O(N log N) | O(N) | Simple but not optimal |
| Merge one by one | O(N * k) | O(1) | Merging into accumulator, slow |
| Divide and Conquer | O(N log k) | O(1) | Merge sort structure on lists |
| Min Heap | O(N log k) | O(k) | Also optimal, different approach |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Divide and conquer:** Repeatedly merge pairs of lists until one list remains.
- Each round halves the number of lists (like bottom-up merge sort).
- Merge two sorted lists using the standard two-pointer linked list merge.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        # Divide and conquer: merge pairs until one list remains
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self._merge_two(l1, l2))
            lists = merged

        return lists[0]

    def _merge_two(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        """Merge two sorted linked lists into one."""
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

        # Attach remaining nodes
        tail.next = l1 if l1 else l2
        return dummy.next
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `lists = [[1,4,5], [1,3,4], [2,6]]`

**Round 1** (3 lists -> 2 lists):
- Merge `[1,4,5]` + `[1,3,4]` -> `[1,1,3,4,4,5]`
- `[2,6]` has no pair, passes through.
- Lists: `[[1,1,3,4,4,5], [2,6]]`

**Round 2** (2 lists -> 1 list):
- Merge `[1,1,3,4,4,5]` + `[2,6]` -> `[1,1,2,3,4,4,5,6]`

**Output:** `1->1->2->3->4->4->5->6`

### Edge Case Testing

- **Empty input:** `lists = []` -> return `None`.
- **Single element:** `lists = [[1]]` -> return the single-node list.
- **Typical case:** As shown in dry run.
- **Extreme values:** `lists = [[], [], []]` -> all empty, returns `None`. The merge function handles `None` inputs gracefully.

### Complexity

- **Time:** O(N log k) — log k rounds of merging, each round processes all N nodes exactly once.
- **Space:** O(1) extra — just relinking existing nodes. The `merged` array is O(k) but shrinks each round. Recursion-free.

### Optimization Discussion

- **Min-heap approach:** Push the head of each list into a heap, pop the smallest, push its next. Also O(N log k) time, O(k) space for the heap. Equally valid in interviews.
- **Why divide and conquer over sequential merging?** Merging lists one by one into an accumulator is O(Nk) because early lists get re-scanned repeatedly. D&C ensures each node is involved in only log k merges.

### Follow-up Variations

- Merge Two Sorted Lists (LC 21) — the building block.
- Merge Sorted Array (LC 88) — array version.
- Smallest Range Covering Elements from K Lists (LC 632).
- Ugly Number II (LC 264) — conceptually merging k sequences.

### Common Traps

- **Merging lists sequentially** (one at a time into an accumulator). This is O(Nk), not O(N log k). The divide-and-conquer pairing is essential.
- **Not handling odd number of lists.** When `len(lists)` is odd, the last list has no pair. The `if i + 1 < len(lists)` guard handles this.
- **Forgetting the empty list case.** `lists = []` or `lists = [None, None]` must be handled. The merge function naturally handles `None` inputs by returning the other list.
