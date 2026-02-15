# Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Sliding Window + Hashmap
**Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a string `s`, find the length of the **longest substring** that contains no duplicate characters.

### 2. Clarification Questions
- **Input constraints?** `0 <= s.length <= 5 * 10^4`, string consists of English letters, digits, symbols, and spaces.
- **Edge cases?** Empty string returns 0. All identical characters returns 1.
- **Expected output?** An integer — the length of the longest valid substring.
- **Can input be modified?** Yes, but we won't need to.

### 3. Brute Force Approach
- **Idea:** Check every substring, use a set to verify uniqueness, track the maximum length.
- **Time:** O(n^3) — O(n^2) substrings, each checked in O(n).
- **Space:** O(n) — for the set.

### 4. Optimized Approach
- **Core Insight:** Use a sliding window with a hashmap that stores each character's **last seen index**. When a duplicate is found, jump the left pointer directly past the previous occurrence — no need to shrink one step at a time.
- **Time:** O(n)
- **Space:** O(min(n, m)) where m is the charset size.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^3) | O(n) | Check all substrings |
| Sliding Window + Set | O(2n) | O(n) | Shrink left one by one |
| Sliding Window + Hashmap | O(n) | O(min(n, m)) | Jump left pointer directly |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Maintain a hashmap `char_index` mapping each character to its most recent index.
- Expand `right` each iteration. If the character was seen **within the current window**, jump `left` past it.
- Update the character's index and track `max_len`.

```python
def lengthOfLongestSubstring(self, s: str) -> int:
    char_index = {}  # char -> last seen index
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        # If char seen and its last index is within current window
        if ch in char_index and char_index[ch] >= left:
            left = char_index[ch] + 1  # jump past duplicate

        char_index[ch] = right  # update last seen position
        max_len = max(max_len, right - left + 1)

    return max_len
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `s = "abcabcbb"`

| right | ch  | char_index (relevant) | left | window  | max_len |
|-------|-----|-----------------------|------|---------|---------|
| 0     | 'a' | {a:0}                 | 0    | "a"     | 1       |
| 1     | 'b' | {a:0, b:1}            | 0    | "ab"    | 2       |
| 2     | 'c' | {a:0, b:1, c:2}       | 0    | "abc"   | 3       |
| 3     | 'a' | {a:3, b:1, c:2}       | 1    | "bca"   | 3       |
| 4     | 'b' | {a:3, b:4, c:2}       | 2    | "cab"   | 3       |
| 5     | 'c' | {a:3, b:4, c:5}       | 3    | "abc"   | 3       |
| 6     | 'b' | {a:3, b:6, c:5}       | 5    | "cb"    | 3       |
| 7     | 'b' | {a:3, b:7, c:5}       | 7    | "b"     | 3       |

**Output:** `3`

### Edge Case Testing
- **Empty input:** `""` → returns 0 (loop never runs).
- **Single element:** `"a"` → returns 1.
- **Typical case:** `"abcabcbb"` → returns 3 (`"abc"`).
- **Extreme values:** All same chars `"aaaa"` → returns 1. All unique `"abcd"` → returns 4.

### Complexity
- **Time:** O(n) — single pass, each character visited once by `right`.
- **Space:** O(min(n, m)) — hashmap stores at most `m` entries where `m` is charset size (128 for ASCII).

### Optimization Discussion
- Could use a fixed-size array `[0]*128` instead of a hashmap for ASCII input — slightly faster constant factor.
- The hashmap approach generalizes to Unicode.

### Follow-up Variations
- **Longest substring with at most K distinct characters** (LeetCode 340)
- **Longest substring with at most 2 distinct characters** (LeetCode 159)
- **Minimum window substring** (LeetCode 76)

### Common Traps
- Forgetting the `char_index[ch] >= left` check — stale entries from before the window can cause false duplicate detection.
- Off-by-one: moving `left` to `char_index[ch]` instead of `char_index[ch] + 1`.
- Deleting old entries from the hashmap (unnecessary and slow — the `>= left` check handles staleness).
