# Minimum Window Substring

**Difficulty:** Hard
**Pattern:** Sliding Window
**Subpattern:** Minimum Window Pattern
**Link:** https://leetcode.com/problems/minimum-window-substring/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given strings `s` and `t`, find the smallest substring of `s` that contains every character in `t` (including duplicates). Return `""` if no such window exists.

### 2. Clarification Questions
- Input constraints? `1 <= s.length, t.length <= 10^5`, `s` and `t` consist of English letters.
- Edge cases? `t` longer than `s` (impossible), `t` has duplicate characters, `s == t`.
- Expected output? The minimum window substring, or `""` if none exists.
- Can input be modified? Yes, strings are immutable in Python anyway.

### 3. Brute Force Approach
- **Idea:** Check every substring of `s`, verify if it contains all characters of `t`.
- **Time:** O(n^2 * m) — enumerate all substrings, check each against `t`.
- **Space:** O(m) — frequency map for `t`.

### 4. Optimized Approach
- **Core Insight:** Use two pointers to maintain a sliding window. Expand `right` to satisfy the requirement, then shrink `left` to minimize the window. Track how many required characters are "formed" to avoid re-scanning the frequency map each time.
- **Time:** O(n + m)
- **Space:** O(m)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2 * m) | O(m) | Check all substrings |
| Optimized | O(n + m) | O(m) | Sliding window with `formed` counter |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Build a frequency map of `t` to know what characters (and counts) we need.
- Use a `formed` counter: tracks how many *unique characters* in `t` have their required count met in the current window.
- Expand `right` until `formed == required`. Then shrink `left` while window is still valid, updating the best result.

```python
from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not s or not t or len(t) > len(s):
        return ""

    need = Counter(t)            # frequency each char must appear
    required = len(need)         # number of unique chars to satisfy
    formed = 0                   # unique chars currently satisfied
    window = {}                  # current window frequencies

    best_len = float('inf')
    best_start = 0
    left = 0

    for right in range(len(s)):
        ch = s[right]
        window[ch] = window.get(ch, 0) + 1

        # check if this char's count now meets the requirement
        if ch in need and window[ch] == need[ch]:
            formed += 1

        # shrink from left while window is valid
        while formed == required:
            # update best if this window is smaller
            window_size = right - left + 1
            if window_size < best_len:
                best_len = window_size
                best_start = left

            # remove leftmost char and shrink
            left_ch = s[left]
            window[left_ch] -= 1
            if left_ch in need and window[left_ch] < need[left_ch]:
                formed -= 1
            left += 1

    return "" if best_len == float('inf') else s[best_start:best_start + best_len]
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `s = "ADOBECODEBANC"`, `t = "ABC"`

| right | char | window (relevant) | formed | left shrink? | best |
|-------|------|--------------------|--------|-------------|------|
| 0 | A | A:1 | 0→1 | no | — |
| 1 | D | D:1 | 1 | no | — |
| 2 | O | O:1 | 1 | no | — |
| 3 | B | B:1 | 1→2 | no | — |
| 4 | E | E:1 | 2 | no | — |
| 5 | C | C:1 | 2→3 | yes→shrink to left=1 | "ADOBEC" (6) |
| ... | ... | ... | ... | ... | ... |
| 12 | C | ... | 3 | shrink to left=10 | "BANC" (4) |

**Output:** `"BANC"`

### Edge Case Testing
- **Empty input:** `t = ""` → returns `""` (no chars needed).
- **Single element:** `s = "a"`, `t = "a"` → returns `"a"`.
- **Typical case:** Shown in dry run above.
- **Extreme values:** `t` longer than `s` → returns `""` immediately.

### Complexity
- **Time:** O(n + m) — each character in `s` is visited at most twice (once by `right`, once by `left`). Building `need` takes O(m).
- **Space:** O(m) — `need` and `window` maps hold at most the character set size.

### Optimization Discussion
- The `formed` counter avoids scanning the entire frequency map to check validity, reducing the inner check to O(1).
- A filtered version can skip characters not in `t`, useful when `|t| << |s|` and `s` has many irrelevant characters.

### Follow-up Variations
- Return all minimum windows (not just one).
- Minimum window containing `t` as a **subsequence** (see Problem 727).
- What if characters are case-insensitive?

### Common Traps
- **Forgetting duplicates in `t`:** `t = "AAB"` requires two A's. Use a frequency map, not a set.
- **Off-by-one on `formed` counter:** Only increment when `window[ch] == need[ch]`, not `>=`.
- **Not handling "no valid window" case:** Must check `best_len == inf` before slicing.
