# Find All Anagrams in a String

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Fixed Window
**Link:** https://leetcode.com/problems/find-all-anagrams-in-a-string/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given strings `s` and `p`, find **all start indices** in `s` where a substring is an anagram of `p`. Return them in any order.

### 2. Clarification Questions

- **Input constraints?** `1 <= s.length, p.length <= 3 * 10^4`. Lowercase English letters only.
- **Edge cases?** `len(p) > len(s)` (no possible anagram). `p` has repeated characters. `s == p`.
- **Expected output?** List of starting indices (0-based).
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** For every index `i` in `s`, sort `s[i:i+len(p)]` and compare to `sorted(p)`.
- **Time:** O(n * m log m) where n = len(s), m = len(p)
- **Space:** O(m) for sorting

### 4. Optimized Approach

- **Core Insight:** Use a **frequency map** for `p`. Slide a window of size `len(p)` over `s`, maintaining a frequency map of the current window. When the two maps match, we found an anagram. Use a `matches` counter to avoid comparing full maps each step.
- **Time:** O(n)
- **Space:** O(1) — at most 26 character counts

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort each window | O(n * m log m) | O(m) | Very slow |
| Frequency map compare | O(n * 26) | O(1) | Compare maps each step |
| Frequency + matches counter | O(n) | O(1) | Best — O(1) per slide |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Build frequency count of `p`.
- Initialize window frequency count for first `len(p)` chars of `s`.
- Track `matches` — number of characters with equal frequency in both maps.
- Slide: update counts for entering/leaving char, adjust `matches`.
- When `matches == 26`, all 26 character counts agree — it's an anagram.

```python
from collections import Counter

def findAnagrams(s, p):
    if len(p) > len(s):
        return []

    p_count = [0] * 26
    w_count = [0] * 26
    for ch in p:
        p_count[ord(ch) - ord('a')] += 1

    result = []
    k = len(p)

    # Initialize first window
    for i in range(k):
        w_count[ord(s[i]) - ord('a')] += 1

    # Count how many of the 26 chars already match
    matches = sum(1 for i in range(26) if p_count[i] == w_count[i])

    if matches == 26:
        result.append(0)

    # Slide the window
    for i in range(k, len(s)):
        # Add new character (right end)
        idx = ord(s[i]) - ord('a')
        w_count[idx] += 1
        if w_count[idx] == p_count[idx]:
            matches += 1
        elif w_count[idx] == p_count[idx] + 1:  # was matching, now off by one
            matches -= 1

        # Remove old character (left end)
        idx = ord(s[i - k]) - ord('a')
        w_count[idx] -= 1
        if w_count[idx] == p_count[idx]:
            matches += 1
        elif w_count[idx] == p_count[idx] - 1:  # was matching, now off by one
            matches -= 1

        if matches == 26:
            result.append(i - k + 1)

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `s = "cbaebabacd", p = "abc"`

| Step | Window | matches == 26? | Action |
|------|--------|-----------------|--------|
| Init | "cba" | Yes (all match) | append 0 |
| i=3 | "bae" | No ('c' removed, 'e' added) | skip |
| i=4 | "aeb" | No | skip |
| i=5 | "eba" | No | skip |
| i=6 | "bab" | No | skip |
| i=7 | "aba" | No | skip |
| i=8 | "bac" | Yes | append 6 |
| i=9 | "acd" | No | skip |

**Output:** `[0, 6]`

### Edge Case Testing

- **Empty input:** Constraints guarantee non-empty, but `len(p) > len(s)` returns `[]`.
- **Single element:** `s = "a", p = "a"` returns `[0]`.
- **Typical case:** Covered in dry run.
- **Extreme values:** `s` and `p` both length 30000 — O(n) handles this fine.

### Complexity

- **Time:** O(n) — each character is processed exactly once entering and once leaving the window. Matches update is O(1) per step.
- **Space:** O(1) — two arrays of size 26, regardless of input size.

### Optimization Discussion

The `matches` counter is the key optimization. Without it, we'd compare 26 entries per slide step (O(26n) vs O(n)). Both are technically O(n), but the matches trick is cleaner and faster in practice.

### Follow-up Variations

- **Permutation in String** (LC 567): Same logic, but return `True/False` instead of indices.
- **Minimum Window Substring** (LC 76): Variable-size window variant.
- **Count anagrams** instead of returning indices.

### Common Traps

- **Matches counter logic is tricky.** The increment/decrement conditions are subtle. A count going from `p_count - 1` to `p_count` gains a match. Going from `p_count` to `p_count + 1` loses a match. Think carefully about the direction.
- **Forgetting to check the initial window.** The first window must be checked before the loop starts.
- **Using Counter comparison each step.** Works but is O(26) per step — fine for interviews, but the matches approach is more impressive.
