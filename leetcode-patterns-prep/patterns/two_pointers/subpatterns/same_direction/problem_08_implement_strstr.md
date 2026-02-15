# Find the Index of the First Occurrence in a String

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Same Direction
**Link:** https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given two strings `haystack` and `needle`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not found.

### 2. Clarification Questions
- Input constraints? `1 <= haystack.length, needle.length <= 10^4`, only lowercase English letters
- Edge cases? Needle longer than haystack, needle equals haystack, needle at very end
- Expected output? Integer index (0-based) or -1
- Can input be modified? No modification needed

### 3. Brute Force Approach
- **Idea:** For each starting position in `haystack`, try to match `needle` character by character.
- **Time:** O(n * m) where n = len(haystack), m = len(needle)
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** The brute force is actually acceptable for interviews since it's O(n*m). For a truly optimized approach, use **KMP (Knuth-Morris-Pratt)** which preprocesses the needle to build a failure/prefix table, enabling O(n+m) matching by never re-scanning matched characters.
- **Time:** O(n + m)
- **Space:** O(m) for the prefix table

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n*m) | O(1) | Simple, often sufficient |
| KMP | O(n+m) | O(m) | Optimal, harder to code |
| Python built-in | O(n*m) worst | O(1) | `haystack.find(needle)` |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

**Brute Force (interview standard):**

- Try every starting position `i` in haystack.
- Use pointer `j` scanning through needle, matching character by character.

```python
def strStr(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)

    for i in range(n - m + 1):
        # try matching needle starting at position i
        j = 0
        while j < m and haystack[i + j] == needle[j]:
            j += 1
        if j == m:
            return i  # full match found

    return -1
```

**KMP (follow-up):**

```python
def strStr(haystack: str, needle: str) -> int:
    m = len(needle)

    # build prefix table (longest proper prefix that is also suffix)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]  # fall back, don't advance i
        else:
            lps[i] = 0
            i += 1

    # search using two pointers moving in same direction
    i = 0  # pointer in haystack
    j = 0  # pointer in needle
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == m:
                return i - m  # match found
        elif j > 0:
            j = lps[j - 1]  # use prefix table to skip
        else:
            i += 1

    return -1
```

---

## PHASE 3 — AFTER CODING

### Dry Run (Brute Force)
Input: `haystack = "sadbutsad", needle = "sad"`

| i | Comparison | j final | Match? |
|---|-----------|---------|--------|
| 0 | s==s, a==a, d==d | 3 | Yes! Return 0 |

Output: `0`

### Edge Case Testing
- **Empty input:** Not possible per constraints (length >= 1)
- **Single element:** `haystack="a", needle="a"` -> returns 0
- **Typical case:** `"hello", "ll"` -> returns 2
- **Extreme values:** Needle longer than haystack -> loop range is empty, returns -1. Needle at last position -> found at `n - m`

### Complexity
- **Time:** O(n * m) brute force, O(n + m) KMP
- **Space:** O(1) brute force, O(m) KMP for prefix table

### Optimization Discussion
- **KMP** is the classical O(n+m) algorithm. The two-pointer version is elegant: pointer `i` in haystack never backtracks; pointer `j` in needle jumps via the prefix table.
- **Rabin-Karp** (rolling hash) is another option with O(n+m) average but O(n*m) worst case.
- In interviews, brute force is usually expected. Mention KMP as a follow-up.

### Follow-up Variations
- **Repeated String Match (LC 686)** — how many times to repeat A so B is a substring
- **KMP / Z-algorithm** — pattern matching algorithms
- **Implement strStr with wildcards** — adds complexity with '.' or '*'

### Common Traps
- Loop bound: iterating `i` up to `n` instead of `n - m + 1` causes index out-of-bounds
- Returning the wrong index (returning `i + j` instead of `i`)
- In KMP, incorrect prefix table construction (the `elif length > 0` fallback is crucial)
