# Permutation in String

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Fixed Window
**Link:** https://leetcode.com/problems/permutation-in-string/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given two strings `s1` and `s2`, return `True` if any **permutation of `s1`** is a substring of `s2`. In other words, check if any anagram of `s1` exists in `s2`.

### 2. Clarification Questions

- **Input constraints?** `1 <= s1.length, s2.length <= 10^4`. Lowercase English letters only.
- **Edge cases?** `s1` longer than `s2`. Both strings identical. `s1` is a single character.
- **Expected output?** Boolean — `True` or `False`.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** Generate all permutations of `s1`, check if any appears in `s2`.
- **Time:** O(m! * n) — factorial permutations, each checked against `s2`.
- **Space:** O(m!) — storing permutations.

### 4. Optimized Approach

- **Core Insight:** A permutation is just an anagram. Slide a window of size `len(s1)` over `s2` and compare **character frequency counts**. If they match at any position, return `True`.
- **Time:** O(n)
- **Space:** O(1) — 26-char arrays

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (all perms) | O(m! * n) | O(m!) | Completely infeasible |
| Sliding window + freq map | O(n) | O(1) | Optimal |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Build frequency array for `s1`.
- Initialize frequency array for first `len(s1)` chars of `s2`.
- Count `matches` across 26 letters.
- Slide the window: update entering/leaving char, adjust matches.
- Return `True` the moment `matches == 26`.

```python
def checkInclusion(s1, s2):
    m, n = len(s1), len(s2)
    if m > n:
        return False

    s1_count = [0] * 26
    w_count = [0] * 26

    for ch in s1:
        s1_count[ord(ch) - ord('a')] += 1
    for i in range(m):
        w_count[ord(s2[i]) - ord('a')] += 1

    # Count initial matches
    matches = sum(1 for i in range(26) if s1_count[i] == w_count[i])
    if matches == 26:
        return True

    # Slide window across s2
    for i in range(m, n):
        # Add entering character
        idx = ord(s2[i]) - ord('a')
        w_count[idx] += 1
        if w_count[idx] == s1_count[idx]:
            matches += 1
        elif w_count[idx] == s1_count[idx] + 1:
            matches -= 1

        # Remove leaving character
        idx = ord(s2[i - m]) - ord('a')
        w_count[idx] -= 1
        if w_count[idx] == s1_count[idx]:
            matches += 1
        elif w_count[idx] == s1_count[idx] - 1:
            matches -= 1

        if matches == 26:
            return True

    return False
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `s1 = "ab", s2 = "eidbaooo"`

| Step | Window | matches == 26? |
|------|--------|-----------------|
| Init | "ei" | No (a:0 vs 1, b:0 vs 1) |
| i=2 | "id" | No |
| i=3 | "db" | No (b matches, but a doesn't) |
| i=4 | "ba" | Yes — return True |

**Output:** `True` (window "ba" is a permutation of "ab")

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `s1 = "a", s2 = "a"` returns `True`.
- **Typical case:** Covered in dry run.
- **Extreme values:** `s1` and `s2` both length 10^4 — O(n) handles easily.

### Complexity

- **Time:** O(n) — single pass over `s2`. Each step is O(1).
- **Space:** O(1) — two fixed arrays of size 26.

### Optimization Discussion

This is identical to "Find All Anagrams" but with early termination. We return `True` at the **first** match instead of collecting all indices. This makes it marginally faster on average.

### Follow-up Variations

- **Find All Anagrams in a String** (LC 438): Collect all starting indices instead of boolean.
- **Minimum Window Substring** (LC 76): Variable window, must contain all chars.
- What if the input contains **Unicode** characters? The 26-size array won't work — use a hash map.

### Common Traps

- **Confusing s1 and s2.** `s1` is the pattern, `s2` is the text to search in. The window size is `len(s1)`.
- **Returning False too early.** Must check all windows before returning False.
- **Off-by-one in matches logic.** The `+1` and `-1` checks track the **transition** from matching to non-matching (or vice versa), not the absolute state.
