# Fast & Slow Pointers (Cycle / Middle Detection)

## What This Subpattern Means

- Two pointers that move at **different speeds**: slow moves 1 step, fast moves 2 steps.
- If there's a cycle, they'll eventually meet. If there's no cycle, fast reaches the end.
- Think of it as: "a runner and a jogger on a circular track — the runner will lap the jogger."

---

## The Trigger (How You Recognize It)

- "Detect a **cycle** in a linked list"
- "Find the **middle** of a linked list"
- "**Happy Number**" (digit-square process eventually cycles or reaches 1)
- Any problem involving sequences that might loop back
- Constraint: O(1) extra space for linked list cycle detection

---

## Template

```python
def has_cycle(head):
    """Detect cycle in linked list."""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next          # 1 step
        fast = fast.next.next     # 2 steps

        if slow == fast:
            return True           # cycle detected

    return False  # fast reached end → no cycle


def find_middle(head):
    """Find middle node of linked list."""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # slow is at the middle when fast reaches end
```

---

## Mistakes

- **Checking `fast.next` without checking `fast` first.** Always: `while fast and fast.next`.
- **For "find middle" in even-length lists:** slow ends up at the second middle node. Some problems want the first — adjust the condition to `while fast.next and fast.next.next`.
- **Happy Number:** the "linked list" is implicit — each number leads to the next via digit-square sum. Same cycle detection logic applies.

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Linked List Cycle | Fast & Slow | | |
| Middle of the Linked List | Fast & Slow | | |
| Happy Number | Fast & Slow | | |

---

## TL;DR

- Slow = 1 step, Fast = 2 steps
- If they meet → cycle. If fast hits end → no cycle.
- Same technique finds the middle (when fast reaches end, slow is at middle)
- Always guard: `while fast and fast.next`
