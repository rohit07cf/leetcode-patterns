# Merge k Sorted Lists

**Difficulty:** Hard
**Pattern:** Two Pointers
**Subpattern:** Merge Style
**Link:** https://leetcode.com/problems/merge-k-sorted-lists/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of `k` sorted linked lists, merge them all into **one sorted linked list** and return its head.

### 2. Clarification Questions
- Input constraints? `0 <= k <= 10^4`, `0 <= list length <= 500`, values in `[-10^4, 10^4]`
- Edge cases? `k=0`; all lists empty; only one non-empty list; lists of vastly different lengths
- Expected output? Head of one merged sorted linked list
- Can input be modified? Yes — we re-link existing nodes

### 3. Brute Force Approach
- **Idea:** Collect all node values into an array, sort, build a new linked list.
- **Time:** O(N log N) where N = total number of nodes
- **Space:** O(N)

### 4. Optimized Approach
- **Core Insight:** Use **divide and conquer** — repeatedly merge pairs of lists, halving the number of lists each round. This is the merge-sort merge step generalized to k lists. Each node is touched O(log k) times across all rounds.
- **Time:** O(N log k)
- **Space:** O(1) extra (O(log k) recursion stack if recursive)

**Alternative:** A **min-heap** of size k also achieves O(N log k) and is conceptually simpler.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Collect + Sort | O(N log N) | O(N) | Simple, ignores sorted property |
| Merge one by one | O(N * k) | O(1) | Slow for large k |
| Min-Heap | O(N log k) | O(k) | Clean, good for streaming |
| Divide and Conquer | O(N log k) | O(1) | Optimal time & space |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Divide and conquer:** Pair up lists and merge each pair using the standard two-list merge.
- Repeat until one list remains.
- Reuse the `mergeTwoLists` helper from LeetCode 21.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: list[ListNode]) -> ListNode:
    if not lists:
        return None

    # Repeatedly merge pairs until one list remains
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(merge_two(l1, l2))
        lists = merged

    return lists[0]

def merge_two(l1: ListNode, l2: ListNode) -> ListNode:
    """Standard two-pointer merge of two sorted linked lists."""
    dummy = ListNode(-1)
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`lists = [[1,4,5], [1,3,4], [2,6]]`

**Round 1** — 3 lists, merge pairs:
- Merge `[1,4,5]` + `[1,3,4]` → `[1,1,3,4,4,5]`
- `[2,6]` has no pair → passes through

**Round 2** — 2 lists:
- Merge `[1,1,3,4,4,5]` + `[2,6]` → `[1,1,2,3,4,4,5,6]`

Result: `1→1→2→3→4→4→5→6`

### Edge Case Testing
- **Empty input:** `lists = []` → return None
- **Single element:** `lists = [[1]]` → return that single node
- **Typical case:** As shown above
- **Extreme values:** All lists empty `[[], [], []]` → merge_two handles None inputs gracefully

### Complexity
- **Time:** O(N log k) — log k merge rounds, each round processes all N nodes
- **Space:** O(1) extra — in-place merging via pointer manipulation (the `merged` list holds references, not copies)

### Optimization Discussion

**Min-Heap alternative:**

```python
import heapq

def mergeKLists_heap(lists):
    heap = []
    for idx, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, idx, node))

    dummy = ListNode(-1)
    tail = dummy
    while heap:
        val, idx, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))

    return dummy.next
```

The heap approach is O(N log k) time, O(k) space. Use the `idx` tiebreaker to avoid comparing `ListNode` objects.

### Follow-up Variations
- Merge Two Sorted Lists (LeetCode 21) — the building block
- Ugly Number II (LeetCode 264) — merge k streams conceptually
- Smallest Range Covering Elements from K Lists (LeetCode 632)

### Common Traps
- In the heap approach, forgetting a **tiebreaker** causes crashes when node values are equal
- Merging lists one-by-one sequentially (O(Nk)) instead of pairwise (O(N log k))
- Not handling the odd-list-out case in pairwise merging (when k is odd)
