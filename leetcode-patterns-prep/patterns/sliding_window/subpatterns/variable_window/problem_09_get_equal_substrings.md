# Get Equal Substrings Within Budget

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Variable Window
**Link:** https://leetcode.com/problems/get-equal-substrings-within-budget/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given two strings `s` and `t` of equal length, and an integer `maxCost`, return the **maximum length** of a substring of `s` that can be changed to the corresponding substring of `t` with a total cost of at most `maxCost`. The cost of changing `s[i]` to `t[i]` is `|s[i] - t[i]|` (absolute difference of ASCII values).

### 2. Clarification Questions
- Input constraints? `1 <= s.length, t.length <= 10^5`, `s.length == t.length`, `0 <= maxCost <= 10^6`, both strings are lowercase English letters.
- Edge cases? `maxCost = 0` — find longest substring where `s` and `t` already match. All costs are 0 — return full length.
- Expected output? An integer — maximum length of valid substring.
- Can input be modified? Yes, but we don't need to.

### 3. Brute Force Approach
- **Idea:** Precompute cost array `cost[i] = |s[i] - t[i]|`. Then check every substring's total cost. Track the longest with cost <= maxCost.
- **Time:** O(n^2)
- **Space:** O(n) — cost array.

### 4. Optimized Approach
- **Core Insight:** Transform the problem: compute `cost[i] = |s[i] - t[i]|` for each position. Now find the **longest subarray** of `cost` with sum <= `maxCost`. This is a classic variable-size sliding window on a non-negative array.
- **Time:** O(n)
- **Space:** O(n) for cost array (or O(1) computing cost on the fly).

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(n) | Check all substrings |
| Sliding Window | O(n) | O(1) | Longest subarray with sum <= budget |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Compute the cost of each position on the fly: `|ord(s[i]) - ord(t[i])|`.
- Maintain a running `window_cost`. Expand `right` each step.
- When `window_cost > maxCost`, shrink from `left`.
- Track `max_len` at each valid position.

```python
def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
    left = 0
    window_cost = 0
    max_len = 0

    for right in range(len(s)):
        # Cost to change s[right] to t[right]
        window_cost += abs(ord(s[right]) - ord(t[right]))

        # Shrink until cost is within budget
        while window_cost > maxCost:
            window_cost -= abs(ord(s[left]) - ord(t[left]))
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `s = "abcd"`, `t = "bcdf"`, `maxCost = 3`

Cost array: `|a-b|=1, |b-c|=1, |c-d|=1, |d-f|=2` → `[1, 1, 1, 2]`

| right | cost[r] | window_cost | left | window_len | max_len |
|-------|---------|-------------|------|------------|---------|
| 0 | 1 | 1 | 0 | 1 | 1 |
| 1 | 1 | 2 | 0 | 2 | 2 |
| 2 | 1 | 3 | 0 | 3 | 3 |
| 3 | 2 | 5 | 0 | exceeds budget | 3 |
| | | 4 | 1 | still exceeds | 3 |
| | | 3 | 2 | 2 | 3 |

Output: **3** (change "abc" to "bcd" with cost 1+1+1=3)

### Edge Case Testing
- **Empty input:** Constraint says `len >= 1`, not applicable.
- **Single element:** `s = "a", t = "z", maxCost = 25` — cost=25, exactly fits, returns 1.
- **Typical case:** `s = "abcd", t = "bcdf", maxCost = 3` — returns 3.
- **Extreme values:** `maxCost = 0` — only positions where `s[i] == t[i]` contribute, finds longest consecutive match.

### Complexity
- **Time:** O(n) — single pass, each index enters/leaves window once.
- **Space:** O(1) — computing cost on the fly, no extra arrays needed.

### Optimization Discussion
We could precompute the cost array for clarity, but computing `abs(ord(s[i]) - ord(t[i]))` on the fly saves O(n) space. The `while` can be replaced with `if` (non-shrinking window trick) for a minor optimization since we only care about the max length.

### Follow-up Variations
- **Minimum Size Subarray Sum** (LC 209) — find min window with sum >= target (flipped condition).
- **Max Consecutive Ones III** (LC 1004) — same structure: longest subarray with sum of "bad" elements <= k.
- **Longest Substring Without Repeating Characters** (LC 3) — different validity condition but same window technique.

### Common Traps
- Computing cost using character subtraction without `abs()` — differences can be negative.
- Precomputing the cost array when it's not needed — wastes space.
- Confusing this with "minimum cost" problems — this asks for the **longest** valid window, not the cheapest.
