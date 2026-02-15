# String Compression

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Same Direction
**Link:** https://leetcode.com/problems/string-compression/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a character array `chars`, compress it in-place using the following rule: each group of consecutive repeating characters is replaced by the character followed by its count (if count > 1). Return the new length. The compressed result must be stored in the **same** array.

### 2. Clarification Questions
- Input constraints? `1 <= chars.length <= 2000`, each char is a lowercase/uppercase English letter, digit, or symbol
- Edge cases? Single character, all same characters, all unique characters
- Expected output? Return new length; `chars` modified in-place
- Can input be modified? Yes, compress in-place

### 3. Brute Force Approach
- **Idea:** Build a new compressed string, then copy back into the array.
- **Time:** O(n)
- **Space:** O(n)

### 4. Optimized Approach
- **Core Insight:** Use a `read` pointer to scan groups of identical characters and a `write` pointer to overwrite the array with compressed data. Count each group's length, then write the character and its digit(s). The `write` pointer is always behind or at `read`, so we never overwrite unread data.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Build new string | O(n) | O(n) | Simple but extra space |
| Two Pointers in-place | O(n) | O(1) | Meets constraint |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use `read` to identify each group of consecutive identical characters.
- Count the group size, then write the character at `write`.
- If count > 1, write each digit of the count as separate characters.

```python
def compress(chars: list[str]) -> int:
    write = 0
    read = 0
    n = len(chars)

    while read < n:
        current_char = chars[read]
        count = 0

        # count consecutive identical characters
        while read < n and chars[read] == current_char:
            read += 1
            count += 1

        # write the character
        chars[write] = current_char
        write += 1

        # write the count digits (only if count > 1)
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `["a","a","b","b","c","c","c"]`

| Group | current_char | count | Write actions | write after |
|-------|-------------|-------|---------------|-------------|
| 1 | 'a' | 2 | write 'a', write '2' | 2 |
| 2 | 'b' | 2 | write 'b', write '2' | 4 |
| 3 | 'c' | 3 | write 'c', write '3' | 6 |

Result: `["a","2","b","2","c","3"]`, return `6`.

### Edge Case Testing
- **Empty input:** Length >= 1 per constraints
- **Single element:** `["a"]` -> write 'a', count=1 (no digits), return 1
- **Typical case:** Shown above
- **Extreme values:** All same char `["a"]*2000` -> writes 'a','2','0','0','0', return 5. All unique `["a","b","c"]` -> no counts written, return 3

### Complexity
- **Time:** O(n) — each character read once, each write operation is bounded by total characters
- **Space:** O(1) — in-place modification (only `str(count)` creates a small temporary, bounded by log10(n))

### Optimization Discussion
Already optimal. The key subtlety is that `write <= read` always holds because:
- A group of 1 character writes 1 char (same size)
- A group of 2-9 writes 2 chars (same or smaller)
- A group of 10+ writes fewer chars than the group size

So we never overwrite data we haven't read yet.

### Follow-up Variations
- **String Compression II (LC 1531)** — minimize length with at most k deletions (DP, Hard)
- **Run-length encoding/decoding**
- **Decode String (LC 394)** — reverse operation with nesting

### Common Traps
- Writing count digits as a single multi-digit string instead of **individual characters** (`"12"` must be written as `'1','2'`)
- Writing count when count == 1 (problem says only write count if > 1)
- Off-by-one when the last group reaches the end of the array
- Forgetting `str(count)` conversion — count 12 needs two character writes
