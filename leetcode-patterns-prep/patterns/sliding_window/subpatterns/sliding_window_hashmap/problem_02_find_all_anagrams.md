# Find All Anagrams in a String

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Sliding Window + Hashmap
**Link:** https://leetcode.com/problems/find-all-anagrams-in-a-string/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given strings `s` and `p`, find all **start indices** of `p`'s anagrams in `s`. An anagram is a rearrangement using all original letters exactly once.

### 2. Clarification Questions
- **Input constraints?** `1 <= s.length, p.length <= 3 * 10^4`. Both consist of lowercase English letters.
- **Edge cases?** `len(p) > len(s)` → return empty list. `p` equals `s` → return `[0]`.
- **Expected output?** A list of starting indices (0-indexed), order doesn't matter.
- **Can input be modified?** Yes, but we won't need to.

### 3. Brute Force Approach
- **Idea:** For every window of size `len(p)` in `s`, sort the window and compare with sorted `p`.
- **Time:** O((n - k) * k log k) where k = len(p).
- **Space:** O(k) for sorting.

### 4. Optimized Approach
- **Core Insight:** Use a fixed-size sliding window of length `len(p)`. Maintain a frequency counter for the window and compare against `p`'s frequency counter. Track a `matches` count of how many of the 26 letters have equal frequency — when `matches == 26`, the window is an anagram.
- **Time:** O(n)
- **Space:** O(1) — counters are bounded by 26 letters.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (sort) | O(n * k log k) | O(k) | Sort each window |
| Counter comparison | O(n * 26) | O(1) | Compare full counters each step |
| Matches tracking | O(n) | O(1) | Maintain running match count |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Build frequency counts for `p` and the first window of `s`.
- Count how many of the 26 characters already match between the two counters.
- Slide the window: add the new right character, remove the old left character, updating `matches` incrementally.
- When `matches == 26`, record the start index.

```python
from collections import Counter

def findAnagrams(self, s: str, p: str) -> list[int]:
    if len(p) > len(s):
        return []

    p_count = Counter(p)
    s_count = Counter()
    result = []
    k = len(p)

    # Count how many of 26 chars have matching frequency
    matches = 0

    # Initialize: count matches for chars not in either counter (they match at 0==0)
    # We'll build this incrementally instead

    for i in range(len(s)):
        # Add right character
        s_count[s[i]] += 1
        if s_count[s[i]] == p_count.get(s[i], 0):
            matches += 1
        elif s_count[s[i]] == p_count.get(s[i], 0) + 1:
            matches -= 1  # was matching, now overshooting

        # Remove left character when window exceeds size k
        if i >= k:
            left_ch = s[i - k]
            if s_count[left_ch] == p_count.get(left_ch, 0):
                matches += 1
            elif s_count[left_ch] == p_count.get(left_ch, 0) + 1:
                matches -= 1  # removing will fix this match... wait

            s_count[left_ch] -= 1
            if s_count[left_ch] == 0:
                del s_count[left_ch]

        # Check: all 26 chars match?
        if i >= k - 1 and matches == len(p_count):
            # Also need to verify no extra chars in s_count
            if len(s_count) == len(p_count):
                result.append(i - k + 1)

    return result
```

**Cleaner version using direct counter comparison (simpler and interview-friendly):**

```python
from collections import Counter

def findAnagrams(self, s: str, p: str) -> list[int]:
    k = len(p)
    if k > len(s):
        return []

    p_count = Counter(p)
    window = Counter(s[:k])
    result = []

    if window == p_count:
        result.append(0)

    for i in range(k, len(s)):
        # Slide window: add right char, remove left char
        window[s[i]] += 1
        left_ch = s[i - k]
        window[left_ch] -= 1
        if window[left_ch] == 0:
            del window[left_ch]  # keep counter clean for == comparison

        if window == p_count:
            result.append(i - k + 1)

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `s = "cbaebabacd"`, `p = "abc"`

`p_count = {a:1, b:1, c:1}`, `k = 3`

| i | window chars | window counter | match? | result |
|---|-------------|----------------|--------|--------|
| — | "cba"       | {c:1,b:1,a:1}  | Yes    | [0]    |
| 3 | "bae"       | {b:1,a:1,e:1}  | No     | [0]    |
| 4 | "aeb"       | {a:1,e:1,b:1}  | No     | [0]    |
| 5 | "eba"       | {e:1,b:1,a:1}  | No     | [0]    |
| 6 | "bab"       | {b:2,a:1}      | No     | [0]    |
| 7 | "aba"       | {a:2,b:1}      | No     | [0]    |
| 8 | "bac"       | {b:1,a:1,c:1}  | Yes    | [0,6]  |
| 9 | "acd"       | {a:1,c:1,d:1}  | No     | [0,6]  |

**Output:** `[0, 6]`

### Edge Case Testing
- **Empty input:** Not possible per constraints (length >= 1).
- **Single element:** `s = "a"`, `p = "a"` → `[0]`.
- **Typical case:** `s = "cbaebabacd"`, `p = "abc"` → `[0, 6]`.
- **Extreme values:** `p` longer than `s` → `[]`. All same characters `s = "aaaa"`, `p = "aa"` → `[0, 1, 2]`.

### Complexity
- **Time:** O(n) — one pass through `s`. Counter comparison is O(26) = O(1) per step.
- **Space:** O(1) — counters hold at most 26 entries.

### Optimization Discussion
- The `matches` counting approach avoids the O(26) counter comparison per step, making it truly O(1) per step.
- For interviews, the clean counter comparison version is easier to code and explain.

### Follow-up Variations
- **Permutation in String** (LeetCode 567) — return `True/False` instead of indices.
- **Minimum Window Substring** (LeetCode 76) — variable-size window, superset matching.

### Common Traps
- Forgetting to `del` zero-count entries from `Counter` — Python's `Counter.__eq__` considers `{a:1, b:0}` different from `{a:1}`.
- Off-by-one on window boundaries — the left character to remove is at index `i - k`, not `i - k + 1`.
- Not handling `len(p) > len(s)` upfront.
