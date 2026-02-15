# Maximum Number of Vowels in a Substring of Given Length

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Fixed Window
**Link:** https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a string `s` and an integer `k`, return the **maximum number of vowels** in any substring of `s` with length `k`. Vowels are `a, e, i, o, u`.

### 2. Clarification Questions

- **Input constraints?** `1 <= k <= s.length <= 10^5`. Lowercase English letters only.
- **Edge cases?** No vowels in the string (return 0). Entire string is vowels.
- **Expected output?** An integer — the max vowel count.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** For every substring of length k, count vowels using a loop.
- **Time:** O(n * k)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** Instead of counting vowels from scratch, **maintain a running count**. When the window slides, check if the **leaving** character is a vowel (decrement) and if the **entering** character is a vowel (increment).
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n * k) | O(1) | Recounts vowels each window |
| Optimized | O(n) | O(1) | O(1) update per slide |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Define a set of vowels for O(1) lookup.
- Count vowels in the first window of size k.
- Slide: subtract if leaving char is vowel, add if entering char is vowel.
- Track the maximum count. **Early exit** if count equals k (can't do better).

```python
def maxVowels(s, k):
    vowels = set('aeiou')

    # Count vowels in first window
    count = sum(1 for ch in s[:k] if ch in vowels)
    max_count = count

    # Slide the window
    for i in range(k, len(s)):
        count += (s[i] in vowels) - (s[i - k] in vowels)
        max_count = max(max_count, count)

        # Early exit: can't have more than k vowels in a k-length window
        if max_count == k:
            return k

    return max_count
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `s = "abciiidef", k = 3`

| Step | Window | Leaving | Entering | Count | Max |
|------|--------|---------|----------|-------|-----|
| Init | "abc" | — | — | 1 (a) | 1 |
| i=3 | "bci" | a (vowel, -1) | i (vowel, +1) | 1 | 1 |
| i=4 | "cii" | b (no) | i (+1) | 2 | 2 |
| i=5 | "iii" | c (no) | i (+1) | 3 | 3 |

`max_count == k == 3` — **early exit!**

**Output:** `3`

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `k = 1` returns 1 if it's a vowel, 0 otherwise.
- **Typical case:** Covered in dry run.
- **Extreme values:** All consonants returns 0. All vowels returns k.

### Complexity

- **Time:** O(n) — single pass. Early exit can make it faster in practice.
- **Space:** O(1) — vowel set is fixed size (5 elements).

### Optimization Discussion

The early exit when `max_count == k` is a nice touch. A window of size k can have at most k vowels, so once we hit that ceiling, no further improvement is possible.

### Follow-up Variations

- **Maximum consonants** in a substring of length k (trivially: `k - max_vowels`).
- **Longest substring with at least m vowels** (variable window problem).
- **Count substrings of length k with exactly j vowels** (more complex counting).

### Common Traps

- **Using a list instead of a set for vowels.** `in` on a list is O(5) vs O(1) for a set. Both are effectively O(1) here, but a set is cleaner practice.
- **Forgetting Python bool-to-int coercion.** `(s[i] in vowels)` returns True/False which Python treats as 1/0 in arithmetic. This is idiomatic and clean.
- **Not considering early exit.** Not a correctness issue, but a good optimization to mention in interviews.
