# Add Two Numbers II

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Merge Style
**Link:** https://leetcode.com/problems/add-two-numbers-ii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given two non-empty linked lists representing non-negative integers (most significant digit first), return their **sum** as a linked list. The digits are stored in **forward order** (not reversed).

### 2. Clarification Questions
- Input constraints? `1 <= list length <= 100`, digit values `[0, 9]`, no leading zeros (except the number 0)
- Edge cases? Different lengths; carry propagation across all digits (e.g., 999 + 1); one list is just `[0]`
- Expected output? Head of a new linked list representing the sum
- Can input be modified? Follow-up asks to not reverse the lists

### 3. Brute Force Approach
- **Idea:** Reverse both lists, add digit-by-digit with carry (like LeetCode 2), then reverse the result.
- **Time:** O(m + n)
- **Space:** O(max(m, n)) for the result

### 4. Optimized Approach
- **Core Insight:** Use **stacks** to access digits from least significant to most significant without reversing the lists. Pop from both stacks simultaneously (merge-style), sum with carry, and build the result list by **prepending** nodes.
- **Time:** O(m + n)
- **Space:** O(m + n) for the stacks

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Reverse + Add + Reverse | O(m+n) | O(max(m,n)) | Modifies input (or copies) |
| Stacks | O(m+n) | O(m+n) | No input modification, clean |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Push all digits of each list onto separate stacks.
- Pop from both stacks simultaneously, add with carry.
- Build the result by **prepending** each new digit node (so MSB ends up at the head).

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Push digits onto stacks to access LSB first
    stack1, stack2 = [], []

    while l1:
        stack1.append(l1.val)
        l1 = l1.next
    while l2:
        stack2.append(l2.val)
        l2 = l2.next

    carry = 0
    head = None  # build result by prepending

    # Merge-style: pop from both stacks, sum with carry
    while stack1 or stack2 or carry:
        digit1 = stack1.pop() if stack1 else 0
        digit2 = stack2.pop() if stack2 else 0

        total = digit1 + digit2 + carry
        carry = total // 10
        digit = total % 10

        # Prepend new node — builds the list from LSB to MSB
        new_node = ListNode(digit)
        new_node.next = head
        head = new_node

    return head
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`l1 = 7→2→4→3`, `l2 = 5→6→4`

Stacks after loading: `stack1 = [7,2,4,3]`, `stack2 = [5,6,4]`

| Step | pop1 | pop2 | carry_in | total | digit | carry_out | head |
|------|------|------|----------|-------|-------|-----------|------|
| 1 | 3 | 4 | 0 | 7 | 7 | 0 | 7 |
| 2 | 4 | 6 | 0 | 10 | 0 | 1 | 0→7 |
| 3 | 2 | 5 | 1 | 8 | 8 | 0 | 8→0→7 |
| 4 | 7 | 0 | 0 | 7 | 7 | 0 | 7→8→0→7 |

Result: `7→8→0→7` (7243 + 564 = 7807)

### Edge Case Testing
- **Empty input:** Not possible per constraints (non-empty lists)
- **Single element:** `[5]` + `[5]` → carry produces `1→0`
- **Typical case:** As shown above
- **Extreme values:** `[9,9,9]` + `[1]` → `1→0→0→0` (carry propagation to a new digit)

### Complexity
- **Time:** O(m + n) — push all digits, then pop all digits
- **Space:** O(m + n) — for the two stacks

### Optimization Discussion

**Without extra space (follow-up):** Reverse both lists in-place, perform addition like LeetCode 2, then reverse the result. This uses O(1) extra space but modifies input.

**Recursive approach:** Pad the shorter list with leading zeros, then recurse. The carry propagates back up the recursion. Elegant but uses O(max(m,n)) stack space.

### Follow-up Variations
- Add Two Numbers (LeetCode 2) — digits in reverse order (simpler)
- Plus One (LeetCode 66) — add 1 to a number stored as an array
- Add Strings (LeetCode 415) — same pattern but with string digits
- Multiply Strings (LeetCode 43)

### Common Traps
- Forgetting the final carry — `999 + 1 = 1000` requires a leading 1 node
- Building the result in the wrong order (appending instead of prepending)
- Not handling lists of different lengths (one stack empties before the other)
- Off-by-one when the carry creates an extra digit at the front
