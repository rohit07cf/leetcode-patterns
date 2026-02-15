# Permutation in String

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Sliding Window + Hashmap
**Link:** https://leetcode.com/problems/permutation-in-string/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given two strings `s1` and `s2`, return `True` if any permutation of `s1` exists as a **contiguous substring** within `s2`.

### 2. Clarification Questions
- **Input constraints?** `1 <= s1.length, s2.length <= 10^4`. Both are lowercase English letters only.
- **Edge cases?** `s1` longer than `s2` → impossible, return `False`. `s1 == s2` → `True`.
- **Expected output?** Boolean — `True` or `False`.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach
- **Idea:** Generate all permutations of `s1` and check if any appears in `s2`.
- **Time:** O(k! * n) — factorial permutations, each checked in O(n).
- **Space:** O(k!) — storing permutations.

### 4. Optimized Approach
- **Core Insight:** A permutation of `s1` is just a rearrangement — it has the **same character frequencies**. Slide a window of size `len(s1)` over `s2` and check if the window's frequency matches `s1`'s frequency.
- **Time:** O(n)
- **Space:** O(1) — bounded by 26 letters.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(k! * n) | O(k!) | Generate all permutations |
| Sort + Slide | O(n * k log k) | O(k) | Sort each window |
| Fixed Window + Counter | O(n) | O(1) | Frequency matching |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Build a frequency counter for `s1`.
- Initialize a window counter for the first `len(s1)` characters of `s2`.
- Slide the window across `s2`, adding/removing one character at a time.
- Return `True` the moment the counters match.

```python
from collections import Counter

def checkInclusion(self, s1: str, s2: str) -> bool:
    k = len(s1)
    if k > len(s2):
        return False

    target = Counter(s1)
    window = Counter(s2[:k])

    if window == target:
        return True

    for i in range(k, len(s2)):
        # Expand: add new right character
        window[s2[i]] += 1

        # Shrink: remove leftmost character of previous window
        left_ch = s2[i - k]
        window[left_ch] -= 1
        if window[left_ch] == 0:
            del window[left_ch]  # clean for == comparison

        if window == target:
            return True

    return False
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `s1 = "ab"`, `s2 = "eidbaooo"`

`target = {a:1, b:1}`, `k = 2`

| i | window chars | window counter | match? |
|---|-------------|----------------|--------|
| — | "ei"        | {e:1, i:1}     | No     |
| 2 | "id"        | {i:1, d:1}     | No     |
| 3 | "db"        | {d:1, b:1}     | No     |
| 4 | "ba"        | {b:1, a:1}     | **Yes** → return True |

**Output:** `True`

### Edge Case Testing
- **Empty input:** Not possible per constraints.
- **Single element:** `s1 = "a"`, `s2 = "a"` → `True`.
- **Typical case:** `s1 = "ab"`, `s2 = "eidbaooo"` → `True`.
- **Extreme values:** `s1` longer than `s2` → `False`. No match found → `False` (e.g., `s1 = "ab"`, `s2 = "aaa"`).

### Complexity
- **Time:** O(n) — single pass through `s2`. Counter comparison is O(26) = O(1).
- **Space:** O(1) — at most 26 entries in each counter.

### Optimization Discussion
- **Matches count approach:** Instead of comparing counters each step (O(26)), maintain a running count of how many characters have matching frequencies. When `matches == 26`, return `True`. This is O(1) per step.
- For interviews, the counter comparison approach is cleaner and sufficient.

### Follow-up Variations
- **Find All Anagrams in a String** (LeetCode 438) — return all start indices instead of boolean.
- **Minimum Window Substring** (LeetCode 76) — variable-size window, harder.

### Common Traps
- Not deleting zero-count keys from the counter — breaks `==` comparison.
- Forgetting the early return when `len(s1) > len(s2)`.
- Confusing `s1` and `s2` — `s1` is the pattern, `s2` is the text to search in.
