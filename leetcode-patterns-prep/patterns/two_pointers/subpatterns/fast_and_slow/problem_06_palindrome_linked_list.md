# Palindrome Linked List

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Fast and Slow
**Link:** https://leetcode.com/problems/palindrome-linked-list/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given the head of a singly linked list, determine if it is a palindrome (reads the same forwards and backwards).

### 2. Clarification Questions
- Input constraints? Number of nodes in range `[1, 10^5]`. Node values in `[0, 9]`.
- Edge cases? Single node (always palindrome), two nodes (same or different values), even vs. odd length.
- Expected output? `True` if palindrome, `False` otherwise.
- Can input be modified? Ideally restore the list, but modification during processing is acceptable.

### 3. Brute Force Approach
- **Idea:** Copy values to an array, then use two pointers from both ends to check palindrome.
- **Time:** O(n)
- **Space:** O(n)

### 4. Optimized Approach
- **Core Insight:** Combine three techniques: (1) find the middle using fast/slow, (2) reverse the second half in-place, (3) compare both halves. This avoids copying to an array.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Copy to array | O(n) | O(n) | Simple, non-destructive |
| Recursive stack | O(n) | O(n) | Implicit stack space |
| Reverse second half | O(n) | O(1) | Modifies then restores list |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Step 1:** Find the middle using fast/slow pointers.
- **Step 2:** Reverse the second half of the list.
- **Step 3:** Compare the first half and reversed second half.
- **Step 4 (optional):** Restore the list by reversing the second half back.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Find the middle (slow ends at second middle for even)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half starting from slow
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # prev is now the head of the reversed second half

        # Step 3: Compare both halves
        left = head
        right = prev
        result = True
        while right:  # right half is same length or shorter
            if left.val != right.val:
                result = False
                break
            left = left.next
            right = right.next

        # (Optional) Step 4: Restore the list by re-reversing
        # Omitted for brevity but recommended in production code

        return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `1 -> 2 -> 2 -> 1`

**Step 1 — Find middle:**

| Step | slow | fast |
|------|------|------|
| 0 | 1 | 1 |
| 1 | 2 | 2 |
| 2 | 2(second) | None |

Slow at second `2`.

**Step 2 — Reverse second half:** `2 -> 1` becomes `1 -> 2`

**Step 3 — Compare:**
- left=1, right=1: match
- left=2, right=2: match
- right is None: stop. Return `True`.

### Edge Case Testing
- **Empty input:** Not possible per constraints, but guarded with `if not head`.
- **Single element:** Returns `True` immediately.
- **Typical case:** `1 -> 2 -> 1` (odd palindrome) — middle is `2`, second half is `2 -> 1`, reversed to `1 -> 2`. Wait, we compare left `1` with right `1`, left `2` with right `2`. Correct because for odd, the middle is included in the reversed half but comparison stops when the shorter half ends.
- **Extreme values:** `1 -> 2 -> 3` (not palindrome) — left=1 vs right=3, mismatch. Returns `False`.

### Complexity
- **Time:** O(n) — finding middle O(n/2), reversing O(n/2), comparing O(n/2).
- **Space:** O(1) — only pointer variables, reversal is done in-place.

### Optimization Discussion
If the interviewer requires the list to remain unmodified, either:
1. Add a restore step (re-reverse the second half).
2. Use the O(n) space approach with an array.

A recursive approach can also solve this in O(n) time but uses O(n) stack space.

### Follow-up Variations
- **Palindrome with doubly linked list** — trivial, use two pointers from head and tail.
- **Longest palindromic sublist** — significantly harder, requires different techniques.
- **Check palindrome for first k nodes only** — find the kth node, then apply the same technique.

### Common Traps
- Off-by-one when finding the middle — for even-length lists, `slow` should be at the start of the second half.
- Forgetting to handle odd-length lists — the middle element doesn't need comparison since it matches itself.
- Not restoring the list — can cause issues if the list is used elsewhere after the check.
- Reversing the wrong half — always reverse starting from `slow`, not from `slow.next`.
