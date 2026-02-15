# Valid Palindrome

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction
**Link:** https://leetcode.com/problems/valid-palindrome/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a string, determine if it reads the same forwards and backwards after **removing all non-alphanumeric characters** and converting to lowercase.

### 2. Clarification Questions
- Input constraints? String length 1 to 2 * 10^5. Contains printable ASCII characters.
- Edge cases? Empty string or all non-alphanumeric chars -> considered a palindrome. Single character -> palindrome.
- Expected output? Boolean `True` or `False`.
- Can input be modified? We won't modify it; we'll skip non-alphanumeric chars in place.

### 3. Brute Force Approach
- **Idea:** Filter the string to keep only alphanumeric chars, lowercase it, then compare with its reverse.
- **Time:** O(n)
- **Space:** O(n) — creates a new filtered string.

### 4. Optimized Approach
- 💡 **Core Insight:** Use two pointers from both ends, **skipping non-alphanumeric characters in place**. Compare lowercase versions without allocating a filtered copy.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Filter + Reverse | O(n) | O(n) | Simple but extra space |
| Two Pointers | O(n) | O(1) | Optimal — no extra string |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Place `left` at index 0, `right` at end.
- Skip non-alphanumeric characters from both sides.
- Compare lowercase characters; if mismatch, return `False`.

```python
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric from the left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from the right
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `"A man, a plan, a canal: Panama"`

| Step | left | right | chars | Match? |
|------|------|-------|-------|--------|
| 1 | 0 | 29 | 'A' vs 'a' | Yes (lowercase) |
| 2 | 1 | 28 | ' '->skip, 'm' vs 'm' | Yes |
| 3 | ... | ... | ... | All match |
| Final | left >= right | — | Return True |

### Edge Case Testing
- **Empty input:** `""` -> `left > right` immediately, returns `True`. Correct.
- **Single element:** `"a"` -> `left == right`, loop doesn't execute, returns `True`.
- **Typical case:** `"racecar"` -> all chars match, returns `True`.
- **Extreme values:** `",.;!@#"` -> all skipped, pointers cross, returns `True` (empty after filtering is a palindrome).

### Complexity
- **Time:** O(n) — each character visited at most once.
- **Space:** O(1) — only two integer pointers.

### Optimization Discussion
Already optimal. No way to beat O(n) time since every character must be examined.

### Follow-up Variations
- What if you can **remove at most one character**? That's LeetCode 680 (Valid Palindrome II).
- What if the string contains **Unicode**? `isalnum()` handles it in Python, but clarify with interviewer.
- Check if a **linked list** is a palindrome? Reverse the second half in place.

### ⚠️ Common Traps
- Forgetting to skip non-alphanumeric characters — comparing spaces or punctuation.
- Not handling case insensitivity — `'A'` vs `'a'` must match.
- Off-by-one: ensure the inner `while` loops also check `left < right` to avoid crossing.
