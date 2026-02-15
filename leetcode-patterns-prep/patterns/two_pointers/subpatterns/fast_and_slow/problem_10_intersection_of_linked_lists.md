# Intersection of Two Linked Lists

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Fast and Slow
**Link:** https://leetcode.com/problems/intersection-of-two-linked-lists/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given the heads of two singly linked lists, find the node where the two lists intersect. If they don't intersect, return `None`. The lists retain their original structure after the function returns.

### 2. Clarification Questions
- Input constraints? List lengths in range `[1, 3 * 10^4]`. Node values in `[1, 10^5]`. Lists are guaranteed to have no cycles.
- Edge cases? No intersection, intersection at the head, one list entirely contained in the other, lists of different lengths.
- Expected output? The intersecting **node** (by reference, not value), or `None`.
- Can input be modified? No, lists must retain original structure.

### 3. Brute Force Approach
- **Idea:** For each node in list A, traverse all of list B to check for a match.
- **Time:** O(m * n)
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** If pointer A traverses list A then list B, and pointer B traverses list B then list A, they both travel the same total distance `(m + n)`. If the lists intersect, the pointers align at the intersection node on their second pass. If they don't intersect, both reach `None` simultaneously.

**Why it works:** Let `a` = length unique to A, `b` = length unique to B, `c` = shared suffix. Pointer A travels `a + c + b` steps to reach the intersection on B's side. Pointer B travels `b + c + a` steps. Both equal `a + b + c`.

- **Time:** O(m + n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(m * n) | O(1) | Nested loops |
| Hash Set | O(m + n) | O(m) | Store one list, search the other |
| Two-pointer swap | O(m + n) | O(1) | Elegant, no extra space |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Initialize two pointers at the respective heads.
- Advance each pointer one step at a time.
- When a pointer reaches the end, redirect it to the **other** list's head.
- They meet at the intersection or both become `None`.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pointer_a = headA
        pointer_b = headB

        # Each pointer traverses both lists — total distance is equal
        # They either meet at the intersection or both reach None
        while pointer_a != pointer_b:
            # Switch to other list's head when reaching the end
            pointer_a = pointer_a.next if pointer_a else headB
            pointer_b = pointer_b.next if pointer_b else headA

        return pointer_a  # intersection node or None
```

---

## PHASE 3 — AFTER CODING

### Dry Run
List A: `4 -> 1 -> 8 -> 4 -> 5` (length 5)
List B: `5 -> 6 -> 1 -> 8 -> 4 -> 5` (length 6)
Intersection at node 8.

Unique to A: `4 -> 1` (a=2), Unique to B: `5 -> 6 -> 1` (b=3), Shared: `8 -> 4 -> 5` (c=3).

| Step | pointer_a | pointer_b |
|------|-----------|-----------|
| 0 | 4 | 5 |
| 1 | 1 | 6 |
| 2 | 8 | 1 |
| 3 | 4 | 8 |
| 4 | 5 | 4 |
| 5 | None | 5 |
| 6 | headB(5) | None |
| 7 | 6 | headA(4) |
| 8 | 1 | 1 |
| 9 | **8** | **8** |

Both arrive at node **8**. Return node 8.

### Edge Case Testing
- **Empty input:** Either head is `None`, return `None` immediately.
- **Single element:** Both lists are just one node — if same node, return it; if different, pointers both become `None` after crossing.
- **Typical case:** Different-length lists with intersection — the swap trick equalizes path lengths.
- **Extreme values:** No intersection — both pointers reach `None` after `m + n` steps. `pointer_a == pointer_b == None`. Loop exits, returns `None`.

### Complexity
- **Time:** O(m + n) — each pointer traverses at most `m + n` nodes.
- **Space:** O(1) — only two pointer variables.

### Optimization Discussion
This is the optimal approach. The hash set alternative uses O(m) or O(n) space but is simpler to understand.

**Alternative O(1) space approach:** Compute lengths, advance the longer list's pointer by the length difference, then walk together. Same complexity but less elegant.

### Follow-up Variations
- **Find intersection of two sorted arrays** — different problem, use merge-like technique.
- **What if lists could have cycles?** — need Floyd's cycle detection first, then this technique within the cycle.
- **Find the intersection point of Y-shaped linked lists** — same problem, different phrasing.

### Common Traps
- Comparing node **values** instead of node **references** — two different nodes can have the same value.
- Redirecting `pointer_a` to `headA` instead of `headB` — the whole point is to **swap** to the other list.
- Using `pointer_a = pointer_a.next if pointer_a.next else headB` — this skips the `None` step and causes an infinite loop when there is no intersection. The correct check is `if pointer_a` (not `pointer_a.next`).
- Forgetting that "no intersection" is a valid case — the algorithm handles it naturally because both pointers become `None` after `m + n + 1` steps.
