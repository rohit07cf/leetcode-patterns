# Longest Repeating Character Replacement

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Variable Window
**Link:** https://leetcode.com/problems/longest-repeating-character-replacement/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a string `s` and an integer `k`, you can replace at most `k` characters in the string. Return the length of the **longest substring** containing the same letter after performing at most `k` replacements.

### 2. Clarification Questions
- Input constraints? `1 <= s.length <= 10^5`, `0 <= k <= s.length`, `s` consists of uppercase English letters only.
- Edge cases? `k >= len(s)` means entire string is valid. `k = 0` means find longest run of a single character.
- Expected output? An integer — the maximum window length.
- Can input be modified? Yes, but we won't modify it.

### 3. Brute Force Approach
- **Idea:** For every substring, count the most frequent character. If `(length - max_freq) <= k`, the substring is valid. Track the maximum length.
- **Time:** O(n^2 * 26) — two loops for substrings, count frequencies each time.
- **Space:** O(26) = O(1)

### 4. Optimized Approach
- **Core Insight:** In a window of size `W`, if the most frequent character appears `max_freq` times, we need `W - max_freq` replacements. The window is valid when `W - max_freq <= k`. Expand right always; shrink left only when the window becomes invalid.
- **Time:** O(n)
- **Space:** O(26) = O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Check all substrings |
| Sliding Window | O(n) | O(1) | Track max frequency in window |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Maintain a frequency map for characters in the current window.
- Track `max_freq` — the count of the most frequent character **ever seen** in any window position.
- **Key trick:** We never decrement `max_freq` when shrinking. This is safe because we only care about finding a window **longer** than the current best — that requires a **higher** `max_freq`.
- Shrink `left` by 1 whenever `(right - left + 1) - max_freq > k`.

```python
def characterReplacement(self, s: str, k: int) -> int:
    freq = {}
    left = 0
    max_freq = 0  # max frequency of any single char in current window
    max_len = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        max_freq = max(max_freq, freq[s[right]])

        # Window is invalid: chars to replace exceed k
        if (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `s = "AABABBA"`, `k = 1`

| right | char | freq | max_freq | window_size | replacements | action | max_len |
|-------|------|------|----------|-------------|-------------|--------|---------|
| 0 | A | {A:1} | 1 | 1 | 0 | valid | 1 |
| 1 | A | {A:2} | 2 | 2 | 0 | valid | 2 |
| 2 | B | {A:2,B:1} | 2 | 3 | 1 | valid | 3 |
| 3 | A | {A:3,B:1} | 3 | 4 | 1 | valid | 4 |
| 4 | B | {A:3,B:2} | 3 | 5 | 2 | shrink | 4 |
| 5 | B | {A:2,B:3} | 3 | 5 | 2 | shrink | 4 |
| 6 | A | {A:3,B:2} | 3 | 5 | 2 | shrink | 4 |

Output: **4** (substring "AABA" with 1 replacement)

### Edge Case Testing
- **Empty input:** Constraint says `len >= 1`, not applicable.
- **Single element:** `s = "A", k = 0` — returns 1.
- **Typical case:** `s = "AABABBA", k = 1` — returns 4.
- **Extreme values:** `k >= len(s)` — entire string is valid, returns `len(s)`.

### Complexity
- **Time:** O(n) — single pass through the string.
- **Space:** O(1) — frequency map holds at most 26 entries.

### Optimization Discussion
The trick of **never decrementing `max_freq`** avoids scanning the frequency map each step. The window only grows when a new `max_freq` is found, so the result is always correct. This keeps the solution strictly O(n) without the O(26) inner scan.

### Follow-up Variations
- **Max Consecutive Ones III** (LC 1004) — binary version of this problem (replace 0s with 1s).
- **Longest Substring with At Most K Distinct Characters** (LC 340) — different constraint on what makes window valid.

### Common Traps
- Trying to update `max_freq` on shrink by scanning the map — unnecessary and adds O(26) per step.
- Using `while` instead of `if` for shrinking — both work, but `if` is cleaner here since we only shrink by 1 per expansion.
- Forgetting that `max_freq` is a **historical max** that never decreases — this is the key insight that makes O(n) work.
