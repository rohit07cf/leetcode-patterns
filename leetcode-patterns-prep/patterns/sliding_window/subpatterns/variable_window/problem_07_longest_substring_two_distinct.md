# Longest Substring with At Most Two Distinct Characters

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Variable Window
**Link:** https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a string `s`, find the length of the **longest substring** that contains **at most two distinct characters**.

### 2. Clarification Questions
- Input constraints? `1 <= s.length <= 10^5`, `s` consists of English letters.
- Edge cases? String with 1 or 2 distinct characters — return `len(s)`. Single character — return 1.
- Expected output? An integer — maximum window length.
- Can input be modified? Yes, but we won't.

### 3. Brute Force Approach
- **Idea:** Check every substring, count distinct characters using a set. Track the longest with at most 2 distinct.
- **Time:** O(n^2)
- **Space:** O(1) — set has at most 3 entries.

### 4. Optimized Approach
- **Core Insight:** Classic **"at most K distinct"** sliding window with K=2. Maintain a frequency map of characters in the window. When the map has more than 2 keys, shrink from the left until it drops back to 2.
- **Time:** O(n)
- **Space:** O(1) — at most 3 entries in the map.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Check all substrings |
| Sliding Window | O(n) | O(1) | Shrink when > 2 distinct |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use a frequency map (`char_count`) to track character counts in the window.
- Expand `right` each step, adding the character.
- When `len(char_count) > 2`, shrink from `left`, removing characters and deleting map entries when count reaches 0.
- Track `max_len` at each valid state.

```python
def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
    char_count = {}  # char -> frequency in window
    left = 0
    max_len = 0

    for right in range(len(s)):
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1

        # Too many distinct characters — shrink
        while len(char_count) > 2:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `s = "eceba"`

| right | char | char_count | left | window | max_len |
|-------|------|------------|------|--------|---------|
| 0 | e | {e:1} | 0 | "e" | 1 |
| 1 | c | {e:1,c:1} | 0 | "ec" | 2 |
| 2 | e | {e:2,c:1} | 0 | "ece" | 3 |
| 3 | b | {e:2,c:1,b:1} | 0 | 3 distinct → shrink | 3 |
| | | {e:1,c:1,b:1} | 1 | still 3 → shrink | 3 |
| | | {e:1,b:1} | 2 | "eb" valid | 3 |
| 4 | a | {e:1,b:1,a:1} | 2 | 3 distinct → shrink | 3 |
| | | {b:1,a:1} | 3 | "ba" valid | 3 |

Wait, let me re-check right=3 shrinking:
- Remove s[0]='e': `{e:1,c:1,b:1}`, still 3. Remove s[1]='c': `{e:1,b:1}`, left=2. Window="eb", size=2.
- right=4: add 'a': `{e:1,b:1,a:1}`, 3 distinct. Remove s[2]='e': `{b:1,a:1}`, left=3. Window="ba", size=2.

Output: **3** (substring "ece")

### Edge Case Testing
- **Empty input:** Constraint says `len >= 1`, not applicable.
- **Single element:** `s = "a"` — returns 1.
- **Typical case:** `s = "eceba"` — returns 3.
- **Extreme values:** `s = "aaaa"` — only 1 distinct, returns 4.

### Complexity
- **Time:** O(n) — each character enters and leaves the window at most once.
- **Space:** O(1) — map holds at most 3 entries.

### Optimization Discussion
This is the **template problem** for "at most K distinct" sliding windows. To generalize to K distinct characters, simply replace `2` with `k` in the condition. This template solves:
- LC 159 (K=2, this problem)
- LC 340 (arbitrary K)
- LC 904 Fruit Into Baskets (K=2, integer array)

### Follow-up Variations
- **Longest Substring with At Most K Distinct Characters** (LC 340) — generalize to K.
- **Fruit Into Baskets** (LC 904) — same problem on integer arrays.
- **Subarrays with K Different Integers** (LC 992) — exactly K = atMost(K) - atMost(K-1).

### Common Traps
- Not deleting zero-count entries from the map — `len(char_count)` will overcount distinct characters.
- Confusing "at most 2 distinct" with "exactly 2 distinct" — different problems requiring different approaches.
- This is a premium problem on LeetCode — practice with LC 904 (Fruit Into Baskets) which is the same problem with a different story.
