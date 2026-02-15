# Valid Palindrome II

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction
**Link:** https://leetcode.com/problems/valid-palindrome-ii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a string, determine if it can become a palindrome by deleting **at most one** character.

### 2. Clarification Questions
- Input constraints? String length 1 to 10^5. Only lowercase English letters.
- Edge cases? Already a palindrome (0 deletions needed) -> True. Single character -> always True. Two characters -> always True (delete one).
- Expected output? Boolean `True` or `False`.
- Can input be modified? No modification needed.

### 3. Brute Force Approach
- **Idea:** Try deleting each character one at a time and check if the remaining string is a palindrome.
- **Time:** O(n^2) — n deletions, each palindrome check is O(n).
- **Space:** O(n) — creating substrings.

### 4. Optimized Approach
- 💡 **Core Insight:** Use two pointers from both ends. When a **mismatch** is found, we have exactly one chance: either skip the left character or skip the right character. Check if **either** resulting substring is a palindrome. If both fail, return False.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(n) | Try every deletion |
| Two Pointers | O(n) | O(1) | Skip at first mismatch |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use two pointers moving inward, comparing characters.
- On first mismatch, try two options: skip left char or skip right char.
- Check if either remaining substring is a palindrome using a helper.

```python
def validPalindrome(s: str) -> bool:
    def is_palindrome(lo: int, hi: int) -> bool:
        """Check if s[lo..hi] is a palindrome."""
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Mismatch — try skipping one character from either side
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -= 1

    return True  # already a palindrome, no deletion needed
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `s = "abca"`

| Step | left | right | chars | Action |
|------|------|-------|-------|--------|
| 1 | 0 | 3 | 'a' vs 'a' | Match, continue |
| 2 | 1 | 2 | 'b' vs 'c' | Mismatch! |
| — | — | — | Try skip left: "ca" -> is_palindrome(2,2) = True | Return True |

Result: **True** (delete 'b' -> "aca" is a palindrome)

### Edge Case Testing
- **Empty input:** Not possible per constraints (length >= 1).
- **Single element:** `"a"` -> no loop iterations, returns `True`.
- **Typical case:** `"abca"` -> True (delete 'b' or 'c'). Correct.
- **Extreme values:** Already a palindrome like `"racecar"` -> returns `True` without any deletion. Non-fixable like `"abc"` -> tries "bc" and "ab", both fail, returns `False`.

### Complexity
- **Time:** O(n) — main scan is O(n), each `is_palindrome` helper call is at most O(n), and we call it at most once (two calls total but combined they scan at most n characters).
- **Space:** O(1) — only pointer variables, no extra data structures.

### Optimization Discussion
Already optimal. Each character is examined at most twice (once in the main loop, once in the helper), so it's still O(n).

### Follow-up Variations
- **Valid Palindrome I** (LeetCode 125): No deletions allowed, just skip non-alphanumeric chars.
- **Valid Palindrome III** (LeetCode 1216): Can delete at most `k` characters. Requires DP — O(n^2) time.
- What if you can **insert** characters instead of delete? Equivalent problem due to palindrome symmetry.

### ⚠️ Common Traps
- Trying to be greedy about **which** character to delete — you must check **both** options (skip left OR skip right).
- Recursing more than once — after the first mismatch, the remaining check must be a strict palindrome (no more deletions).
- Forgetting that a string already being a palindrome is valid (0 deletions <= 1 deletion).
