# Opposite Direction + Skip Logic

## What This Subpattern Means

- Same as opposite direction, but you **skip certain characters/elements** that don't matter (e.g., non-alphanumeric chars) or you're allowed to **delete/skip one element** to make the condition work.
- Think of it as: "two pointers walking toward each other, but sometimes one of them hops over an obstacle."

---

## The Trigger (How You Recognize It)

- "Is it a palindrome if we **ignore** non-alphanumeric characters?"
- "Is it a palindrome if we can **remove at most one** character?"
- "Reverse only the **vowels** of a string"
- Anytime opposite-direction pointers need a **filter** or **one-skip allowance**

---

## Template

```python
def palindrome_with_skip(s):
    """Check palindrome, ignoring non-alphanumeric characters."""
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

## Mistakes

- **Forgetting the inner `while left < right` guard** in skip loops — without it, pointers can cross.
- **Case sensitivity.** Always `.lower()` or `.upper()` when comparing characters.
- **Not handling empty string** after skipping — if all characters are non-alphanumeric, the answer is True.
- **Valid Palindrome II trap:** when chars don't match, you need to check BOTH options (skip left OR skip right), not just one.

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Valid Palindrome | Opposite Direction + Skip Logic | DONE | |
| Valid Palindrome II | Opposite Direction + Skip Logic | DONE | |
| Reverse Vowels of a String | Opposite Direction + Skip Logic | DONE | |

---

## TL;DR

- Same as opposite direction, but add skip/filter logic inside the loop
- Watch out for the `while left < right` guard in inner loops
- Valid Palindrome II: try BOTH skip-left and skip-right when mismatch occurs
