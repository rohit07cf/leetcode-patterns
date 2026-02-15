# Repeated DNA Sequences

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Fixed Window
**Link:** https://leetcode.com/problems/repeated-dna-sequences/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a string `s` representing a DNA sequence (characters `A`, `C`, `G`, `T`), find **all 10-letter-long substrings** that occur more than once. Return them in any order.

### 2. Clarification Questions

- **Input constraints?** `1 <= s.length <= 10^5`. Characters are only `A`, `C`, `G`, `T`.
- **Edge cases?** String shorter than 10 (return empty). All characters identical. Overlapping repeated sequences.
- **Expected output?** List of strings — each repeated 10-char subsequence, appearing once per unique sequence.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** Extract every 10-char substring, store in a hash set. If already seen, add to result set.
- **Time:** O(n * 10) — O(n) substrings, each takes O(10) to hash/copy.
- **Space:** O(n * 10) — storing up to n substrings of length 10.

### 4. Optimized Approach

- **Core Insight:** The brute force with hash sets is actually quite practical here. For a more advanced optimization, use a **rolling hash** (Rabin-Karp style) to avoid O(10) string hashing per step. But for interviews, the hash set approach is clean and sufficient.
- **Time:** O(n) with rolling hash; O(10n) with string hashing (effectively O(n))
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| HashSet of substrings | O(10n) | O(10n) | Simple, clean |
| Rolling hash (Rabin-Karp) | O(n) | O(n) | Faster, more complex |
| Bit manipulation (2-bit encoding) | O(n) | O(n) | Compact, interview showoff |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

**Approach 1: Clean HashSet (recommended for interviews)**

- Slide a window of size 10 across `s`.
- Track `seen` and `repeated` sets.
- If substring is in `seen`, add to `repeated`.

```python
def findRepeatedDnaSequences(s):
    if len(s) <= 10:
        return []

    seen = set()
    repeated = set()

    for i in range(len(s) - 9):  # window of size 10
        substring = s[i:i + 10]
        if substring in seen:
            repeated.add(substring)
        else:
            seen.add(substring)

    return list(repeated)
```

**Approach 2: Bit manipulation (advanced)**

- Encode each nucleotide as 2 bits: `A=00, C=01, G=10, T=11`.
- Maintain a 20-bit rolling hash for the current 10-char window.
- This avoids string hashing entirely.

```python
def findRepeatedDnaSequences_bits(s):
    if len(s) <= 10:
        return []

    # 2-bit encoding: A=0, C=1, G=2, T=3
    char_to_bits = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    mask = (1 << 20) - 1  # 20 bits for 10 characters

    # Build initial hash for first 10 chars
    rolling_hash = 0
    for i in range(10):
        rolling_hash = (rolling_hash << 2) | char_to_bits[s[i]]

    seen = {rolling_hash}
    repeated = set()

    for i in range(10, len(s)):
        # Slide: shift left 2, add new char, mask to 20 bits
        rolling_hash = ((rolling_hash << 2) | char_to_bits[s[i]]) & mask

        if rolling_hash in seen:
            repeated.add(s[i - 9:i + 1])
        else:
            seen.add(rolling_hash)

    return list(repeated)
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"`

| Window | Substring | In seen? | Action |
|--------|-----------|----------|--------|
| 0-9 | AAAAACCCCC | No | Add to seen |
| 1-10 | AAAACCCCCA | No | Add to seen |
| ... | ... | ... | ... |
| 5-14 | CCCCCAAAAA | No | Add to seen |
| ... | ... | ... | ... |
| 10-19 | AAAAACCCCC | Yes | Add to repeated |
| 11-20 | AAAACCCCCC | No | Add to seen |
| ... | ... | ... | ... |

**Output:** `["AAAAACCCCC", "CCCCCAAAAA"]`

### Edge Case Testing

- **Empty input:** Length <= 10 returns `[]`.
- **Single element:** `s = "A"` returns `[]`.
- **Typical case:** Covered in dry run.
- **Extreme values:** All same character (e.g., "AAA...A") — many repeated sequences, all correctly captured.

### Complexity

**HashSet approach:**
- **Time:** O(10n) = O(n) — slicing a 10-char string is O(10) per step.
- **Space:** O(10n) = O(n) — storing up to n strings of length 10.

**Bit manipulation approach:**
- **Time:** O(n) — true O(1) per step.
- **Space:** O(n) — storing integers instead of strings (more compact).

### Optimization Discussion

The bit manipulation approach stores **integers (20 bits)** instead of strings, using far less memory. However, we still need to convert back to strings for the output. In practice, the simple HashSet approach is preferred in interviews unless the interviewer specifically asks for optimization.

### Follow-up Variations

- **Find sequences of length L that appear at least K times.** Generalize the window size and use a Counter.
- **Longest repeated substring** (binary search + rolling hash).
- **Find repeated sequences across two DNA strings.**

### Common Traps

- **Off-by-one in loop range.** `range(len(s) - 9)` gives windows `[0..9], [1..10], ...` The last window starts at index `len(s) - 10`.
- **Returning duplicates.** Using a list instead of a set for `repeated` will produce duplicates if a sequence appears 3+ times.
- **Forgetting `len(s) <= 10` guard.** If the string is exactly 10 chars, there's only one window — it can't be "repeated".
