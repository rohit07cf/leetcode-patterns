# Substring with Concatenation of All Words

**Difficulty:** Hard
**Pattern:** Sliding Window
**Subpattern:** Minimum Window Pattern
**Link:** https://leetcode.com/problems/substring-with-concatenation-of-all-words/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a string `s` and an array of equal-length words, find all starting indices in `s` where a substring is a concatenation of every word in `words` exactly once, in any order.

### 2. Clarification Questions
- Input constraints? `1 <= s.length <= 10^4`, `1 <= words.length <= 5000`, `1 <= words[i].length <= 30`. All words have the **same length**.
- Edge cases? Duplicate words in `words`, total concatenation length exceeds `s`, single word.
- Expected output? List of starting indices (any order).
- Can input be modified? Yes.

### 3. Brute Force Approach
- **Idea:** For every index in `s`, extract a substring of total length `word_len * num_words`, split into chunks of `word_len`, check if the chunks match `words`.
- **Time:** O(n * num_words * word_len)
- **Space:** O(num_words)

### 4. Optimized Approach
- **Core Insight:** Since all words have equal length `w`, we can run `w` independent sliding windows — one for each starting offset `0, 1, ..., w-1`. Each window processes `s` in word-sized chunks, maintaining a frequency map. This is the minimum window pattern applied to word-level tokens.
- **Time:** O(n * w) where `w = word_len`
- **Space:** O(num_words)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n * m * w) | O(m) | Check each index naively |
| Optimized | O(n * w) | O(m) | w sliding windows, word-level chunks |

*Where `n = len(s)`, `m = len(words)`, `w = word_len`.*

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Precompute word frequency map from `words`.
- For each offset in `[0, w)`, run a sliding window over word-sized chunks.
- Maintain a `window` frequency map and a `matched` counter (number of words fully matched).
- When the window exceeds `num_words` chunks, slide the left boundary by one word.

```python
from collections import Counter

def findSubstring(s: str, words: list[str]) -> list[int]:
    if not s or not words:
        return []

    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    need = Counter(words)
    result = []

    # run a sliding window for each starting offset
    for offset in range(word_len):
        window = {}
        matched = 0  # words fully matched in current window
        left = offset

        for right_start in range(offset, len(s) - word_len + 1, word_len):
            word = s[right_start:right_start + word_len]

            if word in need:
                window[word] = window.get(word, 0) + 1
                if window[word] == need[word]:
                    matched += 1
                # if we have excess of this word, shrink from left
                elif window[word] > need[word]:
                    # shrink until this word count is valid
                    while window[word] > need[word]:
                        left_word = s[left:left + word_len]
                        if window[left_word] == need.get(left_word, 0):
                            matched -= 1
                        window[left_word] -= 1
                        left += word_len
            else:
                # word not in dictionary, reset window
                window.clear()
                matched = 0
                left = right_start + word_len
                continue

            # check if all words are matched
            if matched == len(need):
                result.append(left)
                # shrink by one word from left
                left_word = s[left:left + word_len]
                window[left_word] -= 1
                if window[left_word] < need[left_word]:
                    matched -= 1
                left += word_len

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `s = "barfoothefoobarman"`, `words = ["foo", "bar"]`

`word_len = 3`, `num_words = 2`, `need = {"foo":1, "bar":1}`

**Offset 0:** chunks at indices 0,3,6,9,12,15
- i=0: "bar" → window={"bar":1}, matched=1
- i=3: "foo" → window={"bar":1,"foo":1}, matched=2 → **found at left=0!** Shrink: remove "bar", left=3
- i=6: "the" → not in need, reset. left=9
- i=9: "foo" → window={"foo":1}, matched=1
- i=12: "bar" → window={"foo":1,"bar":1}, matched=2 → **found at left=9!**
- i=15: "man" → not in need, reset.

**Output:** `[0, 9]`

### Edge Case Testing
- **Empty input:** `s = ""` or `words = []` → returns `[]`.
- **Single element:** `words = ["a"]`, `s = "a"` → returns `[0]`.
- **Typical case:** Shown in dry run.
- **Extreme values:** `total_len > len(s)` → no valid window, returns `[]`.

### Complexity
- **Time:** O(n * w) — we run `w` sliding windows, each processing O(n/w) words. Total: `w * (n/w) = n` per offset, times `w` offsets = O(n * w). In practice, very fast.
- **Space:** O(m) — frequency maps for `need` and `window` where `m = len(words)`.

### Optimization Discussion
- The key optimization over brute force is reusing the window state across consecutive starting positions within each offset group.
- If words had different lengths, this chunking trick wouldn't work — you'd need a different approach (e.g., trie + backtracking).

### Follow-up Variations
- What if words have **different** lengths?
- What if you need to find the minimum window containing all words (not exact concatenation)?
- What if words can overlap?

### Common Traps
- **Forgetting to run `w` independent windows:** A single pass misses valid starting indices that aren't aligned to offset 0.
- **Not resetting on unknown words:** When a word not in `words` appears, the entire window must reset.
- **Duplicate words:** `words = ["foo", "foo"]` means `need["foo"] = 2`. Must track counts, not just presence.
