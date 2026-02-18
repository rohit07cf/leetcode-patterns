# Linked List Basics

## Baby Explanation (ELI10)

- Imagine a treasure hunt. Each clue is on a piece of paper. Each paper tells you a fun fact AND points you to where the next clue is hidden. You follow the chain clue by clue until you reach the end.
- That's a **Linked List!** Each piece of paper is a "node." Each node holds a value and a pointer to the next node.
- Unlike arrays, linked list nodes are scattered everywhere in memory. You can't jump to node #5 directly -- you have to start at the beginning and follow the chain.
- **Why use them?** Inserting or removing a node in the middle is super fast (O(1)) if you already have a pointer there. In an array, you'd have to shift everything over.
- The first node is called the **head**. The last node points to `None` (null) -- that's how you know you've reached the end.
- A **doubly linked list** is like a two-way treasure hunt: each clue points to both the next AND previous clue.

## Pattern Recognition

Use this when you see:
- "Reverse a linked list"
- "Detect a cycle in a linked list"
- "Find the middle of a linked list"
- "Merge two sorted lists"
- "Remove the Nth node from end"
- The problem literally says "linked list"

Avoid when:
- You need random access by index (use an array)
- The problem involves sorting large data (linked list sort is awkward)
- You need to search for values quickly (use a hash map or BST)

## ASCII Diagram: Linked List

### Singly Linked List

```
  head
   |
   v
  [3] --> [7] --> [1] --> [9] --> None
   ^       ^       ^       ^
  node   node    node    node
  val=3  val=7   val=1   val=9
  next-->  next--> next--> next=None
```

### Reversing a Linked List

```
  Before:  [1] --> [2] --> [3] --> None

  Step 1:  prev=None, curr=[1]
           Save next: nxt=[2]
           Reverse pointer: [1] --> None
           Move forward: prev=[1], curr=[2]

           None <-- [1]    [2] --> [3] --> None
                    prev   curr

  Step 2:  Save next: nxt=[3]
           Reverse pointer: [2] --> [1]
           Move forward: prev=[2], curr=[3]

           None <-- [1] <-- [2]    [3] --> None
                            prev   curr

  Step 3:  Save next: nxt=None
           Reverse pointer: [3] --> [2]
           Move forward: prev=[3], curr=None

           None <-- [1] <-- [2] <-- [3]
                                    prev   curr=None (STOP)

  After:   [3] --> [2] --> [1] --> None
           ^ new head = prev
```

### Cycle Detection (Fast & Slow Pointer)

```
  [1] --> [2] --> [3] --> [4] --> [5]
                   ^               |
                   |               v
                   + <--- [7] <-- [6]

  slow moves 1 step.  fast moves 2 steps.

  Step 0:  slow=1, fast=1
  Step 1:  slow=2, fast=3
  Step 2:  slow=3, fast=5
  Step 3:  slow=4, fast=7
  Step 4:  slow=5, fast=3
  Step 5:  slow=6, fast=5
  Step 6:  slow=7, fast=7   --> THEY MET! Cycle detected!
```

## Minimal Python Template

### Node Definition

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Pattern 1: Traverse a Linked List

```python
def traverse(head):
    curr = head
    while curr:
        print(curr.val)   # process the node
        curr = curr.next
```

### Pattern 2: Reverse a Linked List

```python
def reverse_list(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next    # save next node before we break the link
        curr.next = prev   # reverse the pointer
        prev = curr        # move prev forward
        curr = nxt         # move curr forward

    return prev  # prev is the new head
```

### Pattern 3: Detect Cycle (Floyd's Algorithm)

```python
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next         # 1 step
        fast = fast.next.next    # 2 steps

        if slow == fast:
            return True          # they met --> cycle!

    return False  # fast reached the end --> no cycle
```

### Pattern 4: Merge Two Sorted Lists

```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)     # dummy node to simplify edge cases
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2    # attach whatever's left

    return dummy.next       # skip the dummy, return real head
```

### Pattern 5: Find Middle Node

```python
def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # slow is at the middle when fast reaches the end
```

## Step-by-Step Example (Tiny Input)

### Merge Two Sorted Lists: l1 = [1, 3, 5], l2 = [2, 4, 6]

```
dummy --> None
tail = dummy

Step 1: l1=1, l2=2 --> 1 < 2 --> pick l1
        dummy --> [1]
        l1 moves to 3, tail moves to [1]

Step 2: l1=3, l2=2 --> 2 < 3 --> pick l2
        dummy --> [1] --> [2]
        l2 moves to 4, tail moves to [2]

Step 3: l1=3, l2=4 --> 3 < 4 --> pick l1
        dummy --> [1] --> [2] --> [3]
        l1 moves to 5, tail moves to [3]

Step 4: l1=5, l2=4 --> 4 < 5 --> pick l2
        dummy --> [1] --> [2] --> [3] --> [4]
        l2 moves to 6, tail moves to [4]

Step 5: l1=5, l2=6 --> 5 < 6 --> pick l1
        dummy --> [1] --> [2] --> [3] --> [4] --> [5]
        l1 = None, tail moves to [5]

Step 6: l1 is None, exit loop. Attach remaining l2.
        dummy --> [1] --> [2] --> [3] --> [4] --> [5] --> [6]

Return dummy.next = [1] --> [2] --> [3] --> [4] --> [5] --> [6]
```

- **Input:** l1 = [1, 3, 5], l2 = [2, 4, 6]
- **Output:** [1, 2, 3, 4, 5, 6]

## Common Variations

1. **Reverse** -- Reverse the entire list, or reverse a portion between positions m and n. The three-variable dance: prev, curr, nxt.

2. **Cycle Detection** -- Floyd's fast/slow pointer. Fast moves 2 steps, slow moves 1. If they meet, there's a cycle. To find cycle START: reset one pointer to head, then both move 1 step until they meet again.

3. **Fast/Slow for Middle** -- Same fast/slow idea but no cycle. When fast reaches the end, slow is at the middle. Useful as a building block for merge sort on linked lists.

4. **Dummy Node Trick** -- Create a fake "dummy" node before the real head. This avoids messy edge cases when the head itself might change (like in merge or remove operations). Return `dummy.next` at the end.

5. **Remove Nth from End** -- Use two pointers, n nodes apart. When the front pointer reaches the end, the back pointer is at the node to remove.

## Top 5 Mistakes Beginners Make

1. **Losing the reference to next before reassigning.** When reversing, ALWAYS save `nxt = curr.next` BEFORE you change `curr.next`. Otherwise you lose the rest of the list forever.

2. **Forgetting the dummy node.** Without a dummy, you need special handling for "what if I need to delete the head?" The dummy node eliminates that headache.

3. **Not checking `fast.next` in cycle detection.** The condition must be `while fast and fast.next` (not just `while fast`). Since fast moves 2 steps, `fast.next` could be None, and `fast.next.next` would crash.

4. **Returning `head` instead of `prev` after reversal.** After reversing, the original head is now the TAIL. The new head is `prev`. This trips up many beginners.

5. **Off-by-one in "remove Nth from end."** If you advance the front pointer N times, the back pointer ends up right BEFORE the node to remove. Make sure you're deleting the right one. Using a dummy node helps here too.

## Complexity

- **Time:** O(n) for all basic linked list operations (traverse, reverse, merge, cycle detection). You visit each node a constant number of times.
- **Space:** O(1) for iterative solutions (just a few pointers). Recursive reversal uses O(n) stack space.

## What To Say In Interview (Talk Track)

- "For reversal, I'll use three pointers -- prev, curr, and nxt -- to reverse each link one at a time in a single pass."
- "For cycle detection, I'll use Floyd's fast and slow pointer algorithm. If they ever meet, there's a cycle."
- "I'll use a dummy node to simplify edge cases around the head of the list."
- "This is O(n) time since I visit each node once, and O(1) space since I'm only using a constant number of pointers."
- "For finding the middle, I'll use the fast/slow pointer trick -- when fast reaches the end, slow is at the midpoint."
