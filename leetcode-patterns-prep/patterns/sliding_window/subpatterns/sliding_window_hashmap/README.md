# Sliding Window + HashMap

## What This Subpattern Means

- A sliding window where you track element frequencies (or counts) using a **HashMap/dict**.
- The HashMap tells you what's currently inside the window.
- Think of it as: "a window with an inventory sheet — you know exactly what's inside at all times."

---

## The Trigger (How You Recognize It)

- "Check if a **permutation** of string t exists in string s"
- "Find all **anagrams** of t in s"
- "**Minimum window** containing all characters of t"
- "Count **distinct** elements in every window of size k"
- Any problem where you need to match character/element frequencies within a window

---

## Template

```python
from collections import Counter

def sliding_window_hashmap(s, t):
    need = Counter(t)        # what we need to find
    window = {}              # what we have in current window
    have, required = 0, len(need)

    left = 0

    for right in range(len(s)):
        # EXPAND: add s[right] to window
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in need and window[char] == need[char]:
            have += 1

        # SHRINK: while window satisfies the condition
        while have == required:
            # window is valid — process it here

            # remove from left
            left_char = s[left]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                have -= 1
            left += 1

    return result
```

---

## Mistakes

- **Comparing the wrong counts.** Use `have == required` to check if ALL required chars are satisfied, not just one.
- **Not tracking `have` correctly.** Increment `have` only when `window[char]` REACHES `need[char]`, not every time you add a char.
- **Decrement `have` only when `window[char]` DROPS BELOW `need[char]`**, not every time you remove a char.
- **Not using Counter for the "need" map.** Manual counting is error-prone; use `collections.Counter`.

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Longest Substring Without Repeating Chars | Sliding Window + HashMap | | |
| Permutation in String | Sliding Window + HashMap | | |
| Minimum Window Substring | Sliding Window + HashMap | | |
| Count Distinct Elements in Every Window | Sliding Window + HashMap | | |

---

## TL;DR

- Use a dict to track what's inside the window
- `have` / `required` pattern: count how many required chars are fully matched
- Increment `have` only when count reaches the target, not every addition
- This is the core of "find anagram" and "minimum window" problems
