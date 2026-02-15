# Valid Palindrome II

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction — Skip Logic
**Link:** https://leetcode.com/problems/valid-palindrome-ii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a string `s`, return `true` if it can be made a palindrome by deleting **at most one** character.

### 2. Clarification Questions

- **Input constraints?** `1 <= s.length <= 10^5`, lowercase English letters only
- **Edge cases?** Already a palindrome, single character, mismatch at the very ends, mismatch in the middle
- **Expected output?** Boolean — `true` or `false`
- **Can input be modified?** Not necessary; we only read characters

### 3. Brute Force Approach

- **Idea:** Try deleting each character one at a time, check if the remaining string is a palindrome.
- **Time:** O(n^2)
- **Space:** O(n) for creating substrings

### 4. Optimized Approach

- **💡 Core Insight:** Use two pointers from both ends. When they match, move inward normally. When they **mismatch**, you get exactly one chance to skip — try deleting the left character OR the right character, then check if the remaining substring is a palindrome. Only one skip is allowed.

- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(n) | Delete each char, check palindrome |
| Optimized | O(n) | O(1) | Two pointers with one skip chance |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Two pointers converge from ends.
- On match: advance both pointers inward.
- On mismatch: try **two branches** — skip left or skip right.
- Each branch does a simple palindrome check on the remaining window.
- At most one skip allowed, so we don't recurse further.

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
            # One skip chance — try deleting left char OR right char
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -= 1

    return True
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `s = "abca"`

1. `left=0('a')`, `right=3('a')` → match → advance
2. `left=1('b')`, `right=2('c')` → **mismatch**
3. Try skip left: `is_palindrome(2, 2)` → `"c"` → `True` ✓
4. Short-circuit returns `True`

**Input:** `s = "abc"`

1. `left=0('a')`, `right=2('c')` → mismatch
2. Try skip left: `is_palindrome(1, 2)` → `"bc"` → `False`
3. Try skip right: `is_palindrome(0, 1)` → `"ab"` → `False`
4. Returns `False` ✓

### Edge Case Testing

- **Empty input:** Constraints guarantee `n >= 1`, but would return `True`.
- **Single element:** `"a"` → pointers cross immediately → `True`.
- **Typical case:** `"abca"` → works as shown.
- **Extreme values:** Already a palindrome like `"racecar"` → no mismatch ever → `True`.

### Complexity

- **Time:** O(n) — at most two linear scans (outer + one inner palindrome check)
- **Space:** O(1) — only pointer variables

### Optimization Discussion

The helper `is_palindrome` is called at most once per branch, and each branch scans at most the remaining substring. Total work never exceeds 2n comparisons.

### Follow-up Variations

- **Valid Palindrome (LC 125):** No deletions allowed; just handle alphanumeric filtering.
- **Valid Palindrome III (LC 1216):** Allow at most `k` deletions — becomes a DP problem.
- **Minimum Insertions to Make Palindrome (LC 1312):** Related palindrome transformation.

### ⚠️ Common Traps

- **Trying both skips greedily instead of branching** — you can't commit to one skip direction without checking; you must try both.
- **Recursing more than once** — only one deletion is allowed; the inner check must be a strict palindrome check with no further skips.
- **Returning False too early** — must check BOTH skip options before concluding False.
