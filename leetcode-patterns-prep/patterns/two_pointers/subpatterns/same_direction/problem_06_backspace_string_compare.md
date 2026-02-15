# Backspace String Compare

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Same Direction
**Link:** https://leetcode.com/problems/backspace-string-compare/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given two strings `s` and `t`, determine if they are equal when both are typed into text editors. The `#` character represents a backspace (deletes the previous character). Return `true` if they produce the same result.

### 2. Clarification Questions
- Input constraints? `1 <= s.length, t.length <= 200`, only lowercase letters and `#`
- Edge cases? All backspaces, backspace on empty, strings of different lengths that match
- Expected output? Boolean
- Can input be modified? Strings are immutable in Python, but we can process them

### 3. Brute Force Approach
- **Idea:** Use a stack for each string. Push characters, pop on `#`. Compare final stacks.
- **Time:** O(n + m)
- **Space:** O(n + m)

### 4. Optimized Approach
- **Core Insight:** Process both strings **from right to left** using two pointers. Track how many backspaces to apply. Skip characters that would be deleted. Compare characters one at a time. This achieves O(1) space.
- **Time:** O(n + m)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Stack | O(n+m) | O(n+m) | Simple and clear |
| Two Pointers (reverse) | O(n+m) | O(1) | Follow-up optimal |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

**Stack approach** (clean and interview-friendly):

- Build the "typed" result for each string using a stack.
- `#` pops the last character (if any).

```python
def backspaceCompare(s: str, t: str) -> bool:
    def build(string: str) -> list:
        stack = []
        for ch in string:
            if ch != '#':
                stack.append(ch)
            elif stack:
                stack.pop()  # backspace deletes previous char
        return stack

    return build(s) == build(t)
```

**O(1) space approach** (follow-up):

```python
def backspaceCompare(s: str, t: str) -> bool:
    def next_valid(string: str, idx: int) -> int:
        """Move idx to the next valid (non-deleted) character."""
        skip = 0
        while idx >= 0:
            if string[idx] == '#':
                skip += 1
                idx -= 1
            elif skip > 0:
                skip -= 1  # this char is deleted by a backspace
                idx -= 1
            else:
                break  # found a valid character
        return idx

    i, j = len(s) - 1, len(t) - 1

    while i >= 0 or j >= 0:
        i = next_valid(s, i)
        j = next_valid(t, j)

        # both exhausted — strings match
        if i < 0 and j < 0:
            return True
        # one exhausted, other not — mismatch
        if i < 0 or j < 0:
            return False
        # compare valid characters
        if s[i] != t[j]:
            return False

        i -= 1
        j -= 1

    return True
```

---

## PHASE 3 — AFTER CODING

### Dry Run (Stack approach)
Input: `s = "ab#c", t = "ad#c"`

**build("ab#c"):** `a` -> [a], `b` -> [a,b], `#` -> [a], `c` -> [a,c]
**build("ad#c"):** `a` -> [a], `d` -> [a,d], `#` -> [a], `c` -> [a,c]

`[a, c] == [a, c]` -> `True`

### Edge Case Testing
- **Empty input:** Not possible (length >= 1), but `"#"` and `""` style: build returns `[]`
- **Single element:** `"a"` vs `"a"` -> True. `"a"` vs `"b"` -> False
- **Typical case:** `"ab##"` vs `"c#d#"` -> both produce `[]`, True
- **Extreme values:** `"######"` vs `""` -> both `[]`, True. Backspace on empty is a no-op

### Complexity
- **Time:** O(n + m) — each character processed once in both approaches
- **Space:** O(n + m) for stack approach, O(1) for two-pointer approach

### Optimization Discussion
The O(1) space approach is the follow-up. It processes characters right-to-left, counting `#` characters to know how many to skip. More complex code but meets the O(1) space constraint.

### Follow-up Variations
- **Can you solve it in O(1) space?** — the reverse two-pointer approach above
- **What if backspace deletes K characters?** — adjust skip counter
- **Stream comparison** — what if strings arrive character by character?

### Common Traps
- Applying backspace when the stack is empty (backspace on nothing is a no-op, don't crash)
- In the O(1) approach, forgetting to handle the case where one pointer is exhausted but the other isn't
- Not processing **all** consecutive `#` characters before comparing
