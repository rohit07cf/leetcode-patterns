# Reverse String

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction
**Link:** https://leetcode.com/problems/reverse-string/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a character array, reverse it **in-place** using O(1) extra memory. Do not allocate another array.

### 2. Clarification Questions
- Input constraints? Array length 1 to 10^5. Characters are printable ASCII.
- Edge cases? Single character -> already reversed. Two characters -> one swap.
- Expected output? Modify the array in place; return nothing.
- Can input be modified? Yes — in-place modification is required.

### 3. Brute Force Approach
- **Idea:** Create a reversed copy and overwrite the original.
- **Time:** O(n)
- **Space:** O(n) — violates the O(1) space requirement.

### 4. Optimized Approach
- 💡 **Core Insight:** Swap characters from **both ends moving inward**. Each swap places two characters in their final position. After n/2 swaps, the entire array is reversed.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Copy + Reverse | O(n) | O(n) | Violates constraint |
| Two Pointers | O(n) | O(1) | Meets all requirements |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Place `left` at start, `right` at end.
- Swap characters at both pointers.
- Move both pointers inward until they meet.

```python
def reverseString(s: list[str]) -> None:
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]  # swap in place
        left += 1
        right -= 1
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `s = ['h', 'e', 'l', 'l', 'o']`

| Step | left | right | Swap | Array State |
|------|------|-------|------|-------------|
| 1 | 0 | 4 | h <-> o | ['o','e','l','l','h'] |
| 2 | 1 | 3 | e <-> l | ['o','l','l','e','h'] |
| 3 | 2 | 2 | left == right, stop | ['o','l','l','e','h'] |

Result: `['o', 'l', 'l', 'e', 'h']`

### Edge Case Testing
- **Empty input:** Not possible per constraints (length >= 1).
- **Single element:** `['a']` -> `left == right` immediately, no swap needed. Correct.
- **Typical case:** `['h','e','l','l','o']` -> `['o','l','l','e','h']`. Correct.
- **Extreme values:** Even-length array `['a','b']` -> `['b','a']`. Odd-length middle element stays.

### Complexity
- **Time:** O(n) — exactly n/2 swaps.
- **Space:** O(1) — only two pointer variables, swap is in place.

### Optimization Discussion
This is as optimal as it gets. You must touch every element at least once to reverse, so O(n) is a lower bound.

### Follow-up Variations
- **Reverse words in a string** (LeetCode 151): Reverse the whole string, then reverse each word individually.
- **Reverse only vowels** (LeetCode 345): Same two-pointer approach but skip non-vowels.
- **Reverse a linked list** (LeetCode 206): Different data structure, iterative pointer manipulation.

### ⚠️ Common Traps
- Returning a new string instead of modifying in place — the problem requires in-place.
- Using Python slicing `s[:] = s[::-1]` — technically works but interviewers want to see the two-pointer logic.
- Forgetting the function returns `None` — don't return the array.
