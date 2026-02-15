# Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Variable Window
**Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a string `s`, find the length of the **longest substring** that contains no duplicate characters.

### 2. Clarification Questions
- Input constraints? `0 <= s.length <= 5 * 10^4`, string consists of English letters, digits, symbols, and spaces.
- Edge cases? Empty string returns 0. String with all identical characters returns 1.
- Expected output? An integer representing the max length.
- Can input be modified? Yes, but we won't need to modify it.

### 3. Brute Force Approach
- **Idea:** Check every possible substring using two nested loops. For each substring, use a set to verify all characters are unique. Track the maximum length.
- **Time:** O(n^3) — two loops to generate substrings, one pass to check uniqueness.
- **Space:** O(min(n, m)) — where m is the charset size (set storage).

### 4. Optimized Approach
- **Core Insight:** Use a sliding window with a hash map tracking the **last seen index** of each character. When a duplicate is found, jump `left` directly past the previous occurrence — no need to shrink one step at a time.
- **Time:** O(n)
- **Space:** O(min(n, m)) — where m is the charset size.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^3) | O(min(n, m)) | Check all substrings |
| Sliding Window (shrink) | O(n) | O(min(n, m)) | Shrink left one at a time |
| Sliding Window (jump) | O(n) | O(min(n, m)) | Jump left past duplicate — optimal |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Maintain a hash map `last_seen` mapping each character to its most recent index.
- Expand `right` each iteration. If `s[right]` was seen at or after `left`, jump `left` past that index.
- Update `max_len` at every step.

```python
def lengthOfLongestSubstring(self, s: str) -> int:
    last_seen = {}  # char -> most recent index
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        # If char was seen inside current window, shrink past it
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `s = "abcabcbb"`

| right | char | last_seen | left | window | max_len |
|-------|------|-----------|------|--------|---------|
| 0 | a | {a:0} | 0 | "a" | 1 |
| 1 | b | {a:0,b:1} | 0 | "ab" | 2 |
| 2 | c | {a:0,b:1,c:2} | 0 | "abc" | 3 |
| 3 | a | {a:3,b:1,c:2} | 1 | "bca" | 3 |
| 4 | b | {a:3,b:4,c:2} | 2 | "cab" | 3 |
| 5 | c | {a:3,b:4,c:5} | 3 | "abc" | 3 |
| 6 | b | {a:3,b:6,c:5} | 5 | "cb" | 3 |
| 7 | b | {a:3,b:7,c:5} | 7 | "b" | 3 |

Output: **3** (substring "abc")

### Edge Case Testing
- **Empty input:** `s = ""` — loop doesn't execute, returns 0.
- **Single element:** `s = "a"` — returns 1.
- **Typical case:** `s = "abcabcbb"` — returns 3.
- **Extreme values:** `s = "aaaaaa"` — left jumps each time, returns 1.

### Complexity
- **Time:** O(n) — each character is visited once by `right`.
- **Space:** O(min(n, m)) — hash map stores at most m distinct characters (m = charset size, e.g. 128 for ASCII).

### Optimization Discussion
Using the "jump" technique (`left = last_seen[char] + 1`) avoids the inner while-loop approach, making the code cleaner. For a fixed charset, space is O(1). An array of size 128 can replace the hash map for slight constant-factor speedup.

### Follow-up Variations
- **Longest substring with at most K distinct characters** — generalizes the constraint.
- **Longest substring with at most two distinct characters** (LC 159) — special case of K=2.
- **Minimum window substring** (LC 76) — find smallest window containing all target chars.

### Common Traps
- Forgetting to check `last_seen[char] >= left` — stale entries from before the current window can cause false jumps.
- Off-by-one: `left` should move to `last_seen[char] + 1`, not `last_seen[char]`.
- Returning `max_len` instead of computing it for each position (must update every iteration, not just on duplicates).
