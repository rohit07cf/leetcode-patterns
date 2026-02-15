# Number of Substrings Containing All Three Characters

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Sliding Window + Hashmap
**Link:** https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a string `s` consisting only of characters `a`, `b`, and `c`, return the **number of substrings** that contain **at least one** of each character.

### 2. Clarification Questions
- **Input constraints?** `3 <= s.length <= 5 * 10^4`. Only contains 'a', 'b', 'c'.
- **Edge cases?** Minimum valid string is `"abc"` (length 3). String with only one or two distinct chars → 0.
- **Expected output?** An integer — the count of valid substrings.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach
- **Idea:** Check every substring using two nested loops. For each, verify it contains all three characters.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** Use a sliding window. Once a window `[left, right]` contains all three characters, **every extension to the right is also valid**. So the count of valid substrings starting at `left` is `n - right`. Then shrink `left` and repeat.
- Alternatively, track the **last seen index** of each character. At each position `i`, the smallest last-seen index determines where the earliest valid window starts. All substrings ending at `i` that start at or before that index are valid.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Check every substring |
| Sliding Window (shrink left) | O(n) | O(1) | Count extensions |
| Last-seen index | O(n) | O(1) | Elegant one-pass |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

**Approach: Last-seen index tracking**

- Maintain `last` — an array of size 3 tracking the last seen index of 'a', 'b', 'c' (initialized to -1).
- At each index `i`, the window must start at or before `min(last)` to include all three characters.
- Number of valid substrings ending at `i` = `min(last) + 1` (positions 0 through `min(last)`).

```python
def numberOfSubstrings(self, s: str) -> int:
    last = [-1, -1, -1]  # last seen index of a, b, c
    count = 0

    for i, ch in enumerate(s):
        last[ord(ch) - ord('a')] = i

        # min(last) is the bottleneck: earliest position where
        # all three chars are present in window ending at i
        count += min(last) + 1  # if any is -1, adds 0

    return count
```

**Alternative: Sliding window with counter**

```python
from collections import defaultdict

def numberOfSubstrings(self, s: str) -> int:
    freq = defaultdict(int)
    left = 0
    count = 0

    for right in range(len(s)):
        freq[s[right]] += 1

        # Shrink window while it's still valid (has all 3 chars)
        while len(freq) == 3:
            # All substrings from [left..right] to [left..n-1] are valid
            count += len(s) - right
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

    return count
```

---

## PHASE 3 — AFTER CODING

### Dry Run (last-seen approach)
**Input:** `s = "abcabc"`

| i | ch  | last        | min(last) | count += | total |
|---|-----|-------------|-----------|----------|-------|
| 0 | 'a' | [0,-1,-1]   | -1        | 0        | 0     |
| 1 | 'b' | [0, 1,-1]   | -1        | 0        | 0     |
| 2 | 'c' | [0, 1, 2]   | 0         | 1        | 1     |
| 3 | 'a' | [3, 1, 2]   | 1         | 2        | 3     |
| 4 | 'b' | [3, 4, 2]   | 2         | 3        | 6     |
| 5 | 'c' | [3, 4, 5]   | 3         | 4        | 10    |

**Output:** `10`

### Edge Case Testing
- **Empty input:** Not possible per constraints (length >= 3).
- **Single element:** Not possible per constraints.
- **Typical case:** `"abcabc"` → 10.
- **Extreme values:** Only two distinct chars `"aabb"` → 0. Minimum valid `"abc"` → 1.

### Complexity
- **Time:** O(n) — single pass through the string.
- **Space:** O(1) — only 3 entries tracked.

### Optimization Discussion
- The last-seen approach is cleaner and avoids the inner while loop entirely.
- The sliding window approach is more general and extends to "substrings with at least K distinct characters."

### Follow-up Variations
- **Subarrays with K Different Integers** (LeetCode 992) — exact K distinct.
- **Count Number of Nice Subarrays** (LeetCode 1248) — similar counting pattern.
- Generalize to "at least K distinct characters."

### Common Traps
- In the sliding window approach: counting `n - right` (valid extensions), not just 1 per valid window.
- In the last-seen approach: when any `last[i]` is -1, `min(last) + 1 = 0`, which correctly adds nothing.
- Confusing "at least one of each" with "exactly one of each."
