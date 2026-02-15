# Merge k Sorted Lists

**Difficulty:** Hard
**Pattern:** Top K Elements
**Subpattern:** Max Heap for K Smallest
**Link:** https://leetcode.com/problems/merge-k-sorted-lists/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of `k` linked lists, each sorted in ascending order, merge all lists into one sorted linked list and return it.

### 2. Clarification Questions

- **Input constraints?** 0 <= k <= 10^4, 0 <= list length <= 500, total nodes <= 10^4, -10^4 <= node.val <= 10^4.
- **Edge cases?** Empty array of lists, lists containing empty lists, single list, all nodes have same value.
- **Expected output?** Head of the merged sorted linked list.
- **Can input be modified?** Yes, we can reuse existing nodes.

### 3. Brute Force Approach

- **Idea:** Collect all node values into an array, sort the array, then build a new linked list.
- **Time:** O(N log N) where N = total nodes
- **Space:** O(N)

### 4. Optimized Approach

- 💡 **Core Insight:** Use a **min heap of size k** to always extract the smallest current head across all lists. This is the classic "k-way merge" — at any moment the heap holds exactly one node from each non-empty list, and we always pop the minimum. While this uses a min heap, the pattern generalizes: for the k smallest elements across sorted streams, a heap of size k is the key structure.
- **Time:** O(N log k) — each of N nodes is pushed/popped once at O(log k)
- **Space:** O(k) — heap holds at most k nodes

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Collect + sort | O(N log N) | O(N) | Simple but not optimal |
| Merge one by one | O(kN) | O(1) | k-1 merge passes |
| Min heap k-way merge | O(N log k) | O(k) | Optimal, interview standard |
| Divide and conquer | O(N log k) | O(log k) | Same time, recursive stack |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Initialize a min heap with the head of each non-empty list.
- Pop the smallest node, append it to the result, push its `.next` if it exists.
- Use a counter as tiebreaker since ListNode isn't comparable.

```python
import heapq

class Solution:
    def mergeKLists(self, lists):
        # Min heap: (value, tiebreaker, node)
        heap = []
        counter = 0

        # Seed heap with head of each non-empty list
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, counter, head))
                counter += 1

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            # Push the next node from the same list
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next
```

---

## PHASE 3 — AFTER CODING

### Dry Run

Lists: `[1->4->5, 1->3->4, 2->6]`

- Heap init: [(1,0,node), (1,1,node), (2,2,node)]
- Pop (1,0,node1→4→5) → result: 1, push 4 → heap: [(1,1,_), (2,2,_), (4,3,_)]
- Pop (1,1,node1→3→4) → result: 1→1, push 3 → heap: [(2,2,_), (4,3,_), (3,4,_)]
- Pop (2,2,node2→6) → result: 1→1→2, push 6 → heap: [(3,4,_), (4,3,_), (6,5,_)]
- Pop (3,4,node3→4) → result: ...→3, push 4
- Continue... → final: **1→1→2→3→4→4→5→6** ✓

### Edge Case Testing

- **Empty input:** `lists = []` → heap is empty → return `None`.
- **Single element:** One list with one node → popped directly, no next to push.
- **Typical case:** Multiple lists of varying lengths — all merged correctly.
- **Extreme values:** All nodes have same value — tiebreaker counter prevents comparison errors.

### Complexity

- **Time:** O(N log k) — N total nodes, each heap operation is O(log k).
- **Space:** O(k) — heap holds at most k elements (one per list).

### Optimization Discussion

**Divide and conquer** also achieves O(N log k) by merging pairs of lists in log k rounds. It avoids the heap overhead and can be slightly faster in practice, but the heap approach is cleaner for interviews.

### Follow-up Variations

- **Merge k sorted arrays** — same approach, use index tracking instead of `.next`.
- **External sort** — same k-way merge pattern for disk-based sorting.

### ⚠️ Common Traps

- **ListNode comparison error** — Python heapq compares tuples element-by-element. Without a tiebreaker, equal values cause `ListNode < ListNode` which crashes.
- **Not checking for empty lists** — `lists` may contain `None` entries; skip them during seeding.
- **Losing the head** — always use a dummy node to simplify head management.
