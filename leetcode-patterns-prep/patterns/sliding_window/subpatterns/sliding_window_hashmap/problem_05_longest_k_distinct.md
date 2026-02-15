# Longest Substring with At Most K Distinct Characters

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Sliding Window + Hashmap
**Link:** https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a string `s` and an integer `k`, find the length of the **longest substring** that contains at most `k` distinct characters.

### 2. Clarification Questions
- **Input constraints?** `1 <= s.length <= 5 * 10^4`, `0 <= k <= 50`.
- **Edge cases?** `k == 0` → return 0 (no characters allowed). `k >= 26` → entire string is valid.
- **Expected output?** An integer — the maximum substring length.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach
- **Idea:** Check every substring, count distinct characters, track the longest with at most `k` distinct.
- **Time:** O(n^2)
- **Space:** O(k) — for the character set.

### 4. Optimized Approach
- **Core Insight:** Variable-size sliding window. Expand `right` to grow the window. When distinct characters exceed `k`, shrink `left` until we're back to `k` distinct. A hashmap tracks character counts in the current window.
- **Time:** O(n)
- **Space:** O(k)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(k) | Check every substring |
| Sliding Window + Hashmap | O(n) | O(k) | Optimal single pass |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use a hashmap `char_count` to track character frequencies in the window.
- Expand `right` every iteration.
- When distinct count (`len(char_count)`) exceeds `k`, shrink from `left`.
- Track maximum window size.

```python
from collections import defaultdict

def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    if k == 0:
        return 0

    char_count = defaultdict(int)  # char -> frequency in window
    left = 0
    max_len = 0

    for right in range(len(s)):
        char_count[s[right]] += 1

        # Shrink until we have at most k distinct chars
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `s = "eceba"`, `k = 2`

| right | ch  | char_count      | left | window  | max_len |
|-------|-----|-----------------|------|---------|---------|
| 0     | 'e' | {e:1}           | 0    | "e"     | 1       |
| 1     | 'c' | {e:1, c:1}      | 0    | "ec"    | 2       |
| 2     | 'e' | {e:2, c:1}      | 0    | "ece"   | 3       |
| 3     | 'b' | {e:2, c:1, b:1} → shrink | | |         |
|       |     | remove 'e' → {e:1, c:1, b:1} | 1 | | |
|       |     | remove 'c' → {e:1, b:1} | 2 | "eb"  | 3       |
| 4     | 'a' | {e:1, b:1, a:1} → shrink | | |         |
|       |     | remove 'e' → {b:1, a:1} | 3 | "ba"  | 3       |

**Output:** `3` (substring `"ece"`)

### Edge Case Testing
- **Empty input:** Not possible per constraints (length >= 1).
- **Single element:** `s = "a"`, `k = 1` → returns 1.
- **Typical case:** `s = "eceba"`, `k = 2` → returns 3.
- **Extreme values:** `k = 0` → returns 0. `k >= distinct chars in s` → returns `len(s)`.

### Complexity
- **Time:** O(n) — each character added and removed at most once.
- **Space:** O(k) — hashmap holds at most `k + 1` entries (briefly during expansion, before shrinking back to `k`).

### Optimization Discussion
- This is the **generalized template** for many sliding window + hashmap problems.
- "Fruit Into Baskets" is this problem with `k = 2` on an integer array.
- "Longest Substring with At Most Two Distinct Characters" is this with `k = 2` on a string.

### Follow-up Variations
- **Fruit Into Baskets** (LeetCode 904) — same pattern, `k = 2`, integer array.
- **Subarrays with K Different Integers** (LeetCode 992) — exact K distinct (use `atMost(K) - atMost(K-1)`).
- **Longest Substring Without Repeating Characters** (LeetCode 3) — each char appears at most once.

### Common Traps
- Forgetting the `k == 0` edge case — the while loop condition `len(char_count) > 0` would always be true once any character is added.
- Not deleting zero-count keys — `len(char_count)` becomes unreliable.
- Returning `max_len` before updating after the last right expansion — but since we update inside the loop, this is handled.
