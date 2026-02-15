# Minimum Window Substring

**Difficulty:** Hard
**Pattern:** Sliding Window
**Subpattern:** Sliding Window + Hashmap
**Link:** https://leetcode.com/problems/minimum-window-substring/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given strings `s` and `t`, find the **minimum-length substring** of `s` that contains **every character in `t`** (including duplicates). If no such substring exists, return `""`.

### 2. Clarification Questions
- **Input constraints?** `1 <= s.length, t.length <= 10^5`. Both consist of uppercase and lowercase English letters.
- **Edge cases?** `t` longer than `s` → impossible. `t` has chars not in `s` → impossible. `s == t` → return `s`.
- **Expected output?** The minimum window substring, or `""` if none exists.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach
- **Idea:** Check every substring of `s`, verify it contains all characters of `t` using a frequency check.
- **Time:** O(n^2 * m) where m = len(t).
- **Space:** O(m)

### 4. Optimized Approach
- **Core Insight:** Use a variable-size sliding window with two hashmaps. Expand `right` to satisfy the requirement, then shrink `left` to minimize the window. Track a `formed` counter that counts how many **unique characters** in `t` have their required frequency met in the window. When `formed == required`, we have a valid window.
- **Time:** O(n + m)
- **Space:** O(m)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2 * m) | O(m) | Check every substring |
| Sliding Window + Hashmap | O(n + m) | O(m) | Optimal |
| Filtered s (optimization) | O(n + m) | O(m) | Skip chars not in t |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Build `need` — frequency map of `t`.
- Track `have` — how many distinct characters satisfy their required count.
- Expand `right` to grow the window. When a character's count in the window meets its requirement, increment `have`.
- When `have == len(need)` (all requirements met), try shrinking from `left` to minimize the window, recording the best.

```python
from collections import Counter, defaultdict

def minWindow(self, s: str, t: str) -> str:
    if len(t) > len(s):
        return ""

    need = Counter(t)           # char -> required count
    window = defaultdict(int)   # char -> count in current window
    have = 0                    # distinct chars satisfying requirement
    required = len(need)        # distinct chars we need to satisfy

    best = (float('inf'), 0, 0)  # (length, left, right)
    left = 0

    for right in range(len(s)):
        ch = s[right]
        window[ch] += 1

        # Check if this char now meets its requirement
        if ch in need and window[ch] == need[ch]:
            have += 1

        # Shrink window while all requirements are met
        while have == required:
            # Update best if current window is smaller
            window_len = right - left + 1
            if window_len < best[0]:
                best = (window_len, left, right)

            # Remove leftmost character
            left_ch = s[left]
            window[left_ch] -= 1
            if left_ch in need and window[left_ch] < need[left_ch]:
                have -= 1  # requirement no longer met
            left += 1

    return "" if best[0] == float('inf') else s[best[1]: best[2] + 1]
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `s = "ADOBECODEBANC"`, `t = "ABC"`

`need = {A:1, B:1, C:1}`, `required = 3`

| right | ch  | window (relevant)  | have | shrink? | best          |
|-------|-----|--------------------|------|---------|---------------|
| 0     | A   | {A:1}              | 1    | No      |               |
| 1     | D   | {A:1,D:1}          | 1    | No      |               |
| 2     | O   | ...                | 1    | No      |               |
| 3     | B   | {A:1,B:1,...}      | 2    | No      |               |
| 4     | E   | ...                | 2    | No      |               |
| 5     | C   | {A:1,B:1,C:1,...}  | 3    | **Yes** |               |
|       |     | shrink left=0 (A)  | → 2  |         | (6,0,5) "ADOBEC" |
| 6-9   | O,D,E,B |                | ...  |         |               |
| 9     | B   | {A:0,B:2,C:1,...}  | 2    | No      |               |
| 10    | A   | {A:1,B:2,C:1,...}  | 3    | **Yes** |               |
|       |     | shrink multiple... |      |         | (4,9,12)? let's see |
| 11    | N   |                    |      |         |               |
| 12    | C   | {B:1,A:1,N:1,C:1} | 3    | **Yes** |               |
|       |     | shrink to "BANC"   |      |         | (4,9,12) "BANC" |

**Output:** `"BANC"`

### Edge Case Testing
- **Empty input:** Not possible per constraints.
- **Single element:** `s = "a"`, `t = "a"` → `"a"`. `s = "a"`, `t = "b"` → `""`.
- **Typical case:** `s = "ADOBECODEBANC"`, `t = "ABC"` → `"BANC"`.
- **Extreme values:** `t` longer than `s` → `""`. `t` has duplicates: `s = "aa"`, `t = "aa"` → `"aa"`.

### Complexity
- **Time:** O(n + m) — `right` traverses `s` once (O(n)), `left` traverses at most once (O(n)), building `need` is O(m).
- **Space:** O(m + k) where k is the character set size — `need` stores at most m entries, `window` stores at most k unique chars.

### Optimization Discussion
- **Filtered `s`:** Precompute a list of `(index, char)` for only characters that appear in `t`. Slide the window over this filtered list. Helps when `s` is much longer than `t` and most characters are irrelevant.
- **Using `have`/`required` avoids comparing full hashmaps each step** — O(1) validity check.

### Follow-up Variations
- **Minimum Window Subsequence** (LeetCode 727) — characters must appear in order.
- **Smallest Range Covering Elements from K Lists** (LeetCode 632) — similar "cover all" pattern.
- **Find All Anagrams** (LeetCode 438) — fixed-size window, exact match.

### Common Traps
- Only checking `window[ch] == need[ch]` when **incrementing** `have`, but forgetting to check `window[ch] < need[ch]` when **decrementing**. Must use the correct threshold in both directions.
- Not handling duplicate characters in `t` — e.g., `t = "AABC"` requires `A` to appear twice.
- Returning the window length instead of the actual substring.
- Off-by-one in slicing: `s[left:right+1]` not `s[left:right]`.
