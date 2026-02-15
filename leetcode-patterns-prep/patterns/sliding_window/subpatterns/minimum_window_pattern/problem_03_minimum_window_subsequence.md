# Minimum Window Subsequence

**Difficulty:** Hard
**Pattern:** Sliding Window
**Subpattern:** Minimum Window Pattern
**Link:** https://leetcode.com/problems/minimum-window-subsequence/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given strings `s1` and `s2`, find the smallest substring of `s1` that contains `s2` as a **subsequence**. Return `""` if no such window exists.

### 2. Clarification Questions
- Input constraints? `1 <= s1.length <= 2 * 10^4`, `1 <= s2.length <= 100`.
- Edge cases? `s2` not a subsequence of `s1`, `s2` is a single char, `s1 == s2`.
- Expected output? The minimum-length substring of `s1` containing `s2` as a subsequence.
- Can input be modified? Yes.

### 3. Brute Force Approach
- **Idea:** For every starting position in `s1`, greedily match `s2` as a subsequence. Track the smallest window found.
- **Time:** O(n * m) — for each of `n` starts, scan up to `m` matches.
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** Use a **forward-backward** sliding technique. First, scan forward to find where `s2` is fully matched as a subsequence. Then scan **backward** from that endpoint to find the tightest starting point. This minimizes each window greedily.
- **Time:** O(n * m)
- **Space:** O(1)

**Alt: DP approach** — O(n * m) time, O(n * m) space, but the sliding technique is more interview-friendly.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n * m) | O(1) | Forward scan from each index |
| Forward-Backward | O(n * m) | O(1) | Greedy shrink after each match |
| DP | O(n * m) | O(n * m) | `dp[i][j]` = earliest start |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Forward pass:** Walk through `s1` matching characters of `s2` left to right. When all of `s2` is matched, record the endpoint.
- **Backward pass:** From that endpoint, walk backward through `s1` matching `s2` right to left. This finds the latest possible start, yielding the shortest window ending at that point.
- Advance the start pointer past this window and repeat.

```python
def minWindow(s1: str, s2: str) -> str:
    n, m = len(s1), len(s2)
    best_start = -1
    best_len = float('inf')
    i = 0  # pointer in s1

    while i < n:
        # forward pass: match s2 as subsequence starting from i
        j = 0
        start = i
        while start < n and j < m:
            if s1[start] == s2[j]:
                j += 1
            start += 1

        if j < m:  # couldn't match all of s2
            break

        # start is now one past the end of the match
        end = start - 1  # last matched char in s1

        # backward pass: shrink window from end
        j = m - 1
        while j >= 0:
            if s1[end] == s2[j]:
                j -= 1
            end -= 1
        end += 1  # first matched char in s1

        # update best
        window_len = start - end
        if window_len < best_len:
            best_len = window_len
            best_start = end

        # advance past this start to find next window
        i = end + 1

    return "" if best_start == -1 else s1[best_start:best_start + best_len]
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `s1 = "abcdebdde"`, `s2 = "bde"`

**Iteration 1:**
- Forward from i=0: match b(1), d(3), e(4) → end at index 4, start=5
- Backward from index 4: e(4), d(3), b(1) → end=1
- Window: `s1[1:5]` = `"bcde"` (length 4)

**Iteration 2:**
- Forward from i=2: match b(4→no, wait)... d(3), e(4)... actually match b at index 4? No — `s2[0]='b'`, find b at index 4='e'... Let me re-trace.
- Forward from i=2: c(2)≠b, d(3)≠b, e(4)≠b, b(5)=b✓, d(6)=d✓, d(7)≠e, e(8)=e? No, s1="abcdebdde" so index 7='d', 8='e'. Match: b(5), d(6), e(8) → start=9
- Backward from index 8: e(8)✓, d(7)✓, b(5)✓ → end=5
- Window: `s1[5:9]` = `"bdde"` (length 4)

**Iteration 3:** i=6, forward: d(6)≠b, d(7)≠b, e(8)≠b → j<m, break.

**Output:** `"bcde"` (length 4, found first)

### Edge Case Testing
- **Empty input:** `s2 = ""` → trivially `""` (no subsequence to match).
- **Single element:** `s1 = "a"`, `s2 = "a"` → returns `"a"`.
- **Typical case:** Shown in dry run.
- **Extreme values:** `s2` not found in `s1` at all → returns `""`.

### Complexity
- **Time:** O(n * m) — in the worst case, each forward+backward pass takes O(n), and we may do O(n/m) passes. Total bounded by O(n * m).
- **Space:** O(1) — only pointers and tracking variables.

### Optimization Discussion
- **DP approach:** Build `dp[i][j]` = starting index of the smallest window ending at `s1[i]` that contains `s2[0..j]` as a subsequence. This is O(n * m) time and space but avoids the backward pass.
- **Next-character index arrays** can speed up the forward pass to O(m) per window using preprocessing in O(n * 26).

### Follow-up Variations
- Minimum window containing `t` with all characters (not subsequence) — this is LC 76.
- What if `s2` can have wildcards?
- Count the number of distinct minimum windows.

### Common Traps
- **Confusing substring vs subsequence:** This problem requires subsequence matching, not character frequency matching.
- **Off-by-one in backward pass:** After the backward loop, `end` is one before the first match — must do `end += 1`.
- **Not advancing `i` correctly:** Must set `i = end + 1` (not `i = start`) to avoid missing overlapping windows.
