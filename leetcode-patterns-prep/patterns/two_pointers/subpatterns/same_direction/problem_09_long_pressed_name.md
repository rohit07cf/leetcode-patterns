# Long Pressed Name

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Same Direction
**Link:** https://leetcode.com/problems/long-pressed-name/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Your friend types a name on a keyboard. Sometimes a key is held too long, causing a character to repeat. Given the `name` and the `typed` string, determine if `typed` could have been produced by long-pressing characters in `name`.

### 2. Clarification Questions
- Input constraints? `1 <= name.length, typed.length <= 1000`, only lowercase English letters
- Edge cases? Typed shorter than name, extra characters that don't match, first character mismatch
- Expected output? Boolean
- Can input be modified? No modification needed

### 3. Brute Force Approach
- **Idea:** Group consecutive characters in both strings, compare groups: same characters, typed group count >= name group count.
- **Time:** O(n + m)
- **Space:** O(n + m) for groups

### 4. Optimized Approach
- **Core Insight:** Use two pointers `i` (in `name`) and `j` (in `typed`) moving in the same direction. If characters match, advance both. If they don't match but `typed[j] == typed[j-1]`, it's a long press — advance only `j`. Otherwise, return False.
- **Time:** O(n + m)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Group comparison | O(n+m) | O(n+m) | Clear but extra space |
| Two Pointers | O(n+m) | O(1) | Optimal |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Pointer `i` scans through `name`, pointer `j` scans through `typed`.
- Match: advance both. Long press (typed repeats previous): advance only `j`.
- After the loop, ensure `i` has consumed all of `name` and remaining `typed` chars are valid long presses.

```python
def isLongPressedName(name: str, typed: str) -> bool:
    i = 0  # pointer in name
    j = 0  # pointer in typed

    while j < len(typed):
        if i < len(name) and name[i] == typed[j]:
            # characters match — advance both
            i += 1
            j += 1
        elif j > 0 and typed[j] == typed[j - 1]:
            # long press — skip extra repeated character
            j += 1
        else:
            # mismatch that can't be explained by long press
            return False

    # all of name must be consumed
    return i == len(name)
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `name = "alex", typed = "aaleex"`

| Step | i | j | name[i] | typed[j] | Action |
|------|---|---|---------|----------|--------|
| 0 | 0 | 0 | 'a' | 'a' | match, i=1, j=1 |
| 1 | 1 | 1 | 'l' | 'a' | typed[1]==typed[0]='a', long press, j=2 |
| 2 | 1 | 2 | 'l' | 'l' | match, i=2, j=3 |
| 3 | 2 | 3 | 'e' | 'e' | match, i=3, j=4 |
| 4 | 3 | 4 | 'x' | 'e' | typed[4]==typed[3]='e', long press, j=5 |
| 5 | 3 | 5 | 'x' | 'x' | match, i=4, j=6 |

`i == 4 == len(name)` -> `True`

### Edge Case Testing
- **Empty input:** Not possible per constraints
- **Single element:** `name="a", typed="a"` -> True. `name="a", typed="b"` -> False
- **Typical case:** `"alex"` / `"aaleex"` -> True
- **Extreme values:** `"saeed"` / `"ssaaedd"` -> False (missing second 'e'). `name = "a"` / `typed = "aaaaaa"` -> True

### Complexity
- **Time:** O(n + m) — each pointer advances at least once per iteration
- **Space:** O(1) — only two integer pointers

### Optimization Discussion
Already optimal. The two-pointer approach handles all cases in a single pass. An alternative group-based approach compares run-length encoded versions but uses extra space.

### Follow-up Variations
- **Backspace String Compare (LC 844)** — similar two-pointer character comparison
- **What if multiple keys can be long-pressed simultaneously?**
- **Longest Common Subsequence (LC 1143)** — generalized matching

### Common Traps
- Forgetting to check `i == len(name)` at the end (typed might end before all of name is matched)
- Not checking `j > 0` before accessing `typed[j-1]` (index out of bounds on first character mismatch)
- Accepting cases where typed has **fewer** repetitions than name (e.g., name="aab", typed="ab")
