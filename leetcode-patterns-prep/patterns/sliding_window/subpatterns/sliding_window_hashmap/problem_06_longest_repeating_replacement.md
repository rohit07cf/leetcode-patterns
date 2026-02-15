# Longest Repeating Character Replacement

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Sliding Window + Hashmap
**Link:** https://leetcode.com/problems/longest-repeating-character-replacement/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a string `s` (uppercase English letters) and an integer `k`, you can replace **at most `k`** characters in the string. Return the length of the **longest substring** that contains all the same character after performing at most `k` replacements.

### 2. Clarification Questions
- **Input constraints?** `1 <= s.length <= 10^5`, `0 <= k <= s.length`. Only uppercase English letters.
- **Edge cases?** `k >= len(s)` → entire string. All same characters → `len(s)`. `k = 0` → longest run of same character.
- **Expected output?** An integer — the maximum length of a valid substring.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach
- **Idea:** For each starting index and each target character (A-Z), expand as far as possible while replacements needed <= k.
- **Time:** O(26 * n^2)
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** In a window of length `L`, the minimum replacements needed = `L - max_freq`, where `max_freq` is the count of the most frequent character. The window is valid when `L - max_freq <= k`. Slide the window: expand `right` always, shrink `left` only when the window becomes invalid.
- **Time:** O(n)
- **Space:** O(1) — hashmap has at most 26 entries.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(26 * n^2) | O(1) | Per-character expansion |
| Sliding Window + Hashmap | O(n) | O(1) | Track max frequency |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Maintain a hashmap `count` for character frequencies in the window.
- Track `max_freq` — the highest frequency of any single character in the current window.
- **Key trick:** We never decrease `max_freq` when shrinking. This is safe because we only care about finding a **longer** valid window. If `max_freq` is stale (too high), the window just won't grow — but it can never produce a wrong answer.
- When `window_size - max_freq > k`, the window is invalid — shrink `left` by 1.

```python
from collections import defaultdict

def characterReplacement(self, s: str, k: int) -> int:
    count = defaultdict(int)  # char -> frequency in window
    left = 0
    max_freq = 0  # max frequency of any single char in window
    max_len = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])

        # Window is invalid: need more than k replacements
        # Shrink by exactly 1 (not while loop — see explanation)
        if (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `s = "AABABBA"`, `k = 1`

| right | ch  | count             | max_freq | window_size | replacements | valid? | left | max_len |
|-------|-----|-------------------|----------|-------------|-------------|--------|------|---------|
| 0     | A   | {A:1}             | 1        | 1           | 0           | Yes    | 0    | 1       |
| 1     | A   | {A:2}             | 2        | 2           | 0           | Yes    | 0    | 2       |
| 2     | B   | {A:2,B:1}         | 2        | 3           | 1           | Yes    | 0    | 3       |
| 3     | A   | {A:3,B:1}         | 3        | 4           | 1           | Yes    | 0    | 4       |
| 4     | B   | {A:3,B:2}         | 3        | 5           | 2           | No     | 1    | 4       |
|       |     | {A:2,B:2}         |          |             |             |        |      |         |
| 5     | B   | {A:2,B:3}         | 3        | 5           | 2           | No     | 2    | 4       |
|       |     | {A:1,B:3}         |          |             |             |        |      |         |
| 6     | A   | {A:2,B:3}         | 3        | 5           | 2           | No     | 3    | 4       |
|       |     | {A:2,B:2}         |          |             |             |        |      |         |

**Output:** `4` (substring `"AABA"`)

### Edge Case Testing
- **Empty input:** Not possible per constraints.
- **Single element:** `"A"`, k=0 → returns 1.
- **Typical case:** `"AABABBA"`, k=1 → returns 4.
- **Extreme values:** `k >= len(s)` → returns `len(s)`. All same chars → returns `len(s)`.

### Complexity
- **Time:** O(n) — single pass, `right` moves n times, `left` moves at most n times.
- **Space:** O(1) — hashmap bounded by 26 uppercase letters.

### Optimization Discussion
- **Why we don't decrease `max_freq`:** Finding the true max frequency after removing a character would require O(26) scan. But we don't need to — the window size can only improve the answer when `max_freq` increases. A stale `max_freq` just means the window stays the same size (doesn't grow), which is fine.
- **`if` vs `while`:** Using `if` (shrink by 1) instead of `while` works because the window only becomes invalid by 1 when `right` advances by 1. The window size stays the same or grows — it **never shrinks below the current best**.

### Follow-up Variations
- **Max Consecutive Ones III** (LeetCode 1004) — binary version: replace at most k 0s with 1s.
- **Longest Substring with At Most K Distinct Characters** (LeetCode 340) — similar template.

### Common Traps
- Trying to update `max_freq` when shrinking (unnecessary and tricky).
- Using `while` instead of `if` for shrinking — both work, but `if` is the elegant insight.
- Confusing "replacements needed" with `k` — the condition is `window_size - max_freq > k`, not `>= k`.
