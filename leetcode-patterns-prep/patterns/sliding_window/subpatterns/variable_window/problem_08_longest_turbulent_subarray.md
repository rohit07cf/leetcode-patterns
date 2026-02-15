# Longest Turbulent Subarray

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Variable Window
**Link:** https://leetcode.com/problems/longest-turbulent-subarray/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an integer array `arr`, return the length of the **longest turbulent subarray**. A subarray is turbulent if the comparison sign between consecutive elements **alternates** between `>` and `<` (i.e., the array zigzags up and down).

### 2. Clarification Questions
- Input constraints? `1 <= arr.length <= 4 * 10^4`, `0 <= arr[i] <= 10^9`.
- Edge cases? Length 1 — return 1. All equal elements — return 1 (no valid turbulent pair). Two elements: return 2 if different, 1 if equal.
- Expected output? An integer — the max length of a turbulent subarray.
- Can input be modified? Yes, but we won't.

### 3. Brute Force Approach
- **Idea:** For every starting index, expand right checking the alternating condition. Track the max length.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** Use a sliding window. Compare `arr[i-1]` vs `arr[i]` to get a sign. The turbulent property breaks when:
  1. Two consecutive pairs have the **same** comparison sign, or
  2. Two consecutive elements are **equal**.

  When it breaks, reset the window. Track the max length.

- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Check all starting positions |
| Sliding Window | O(n) | O(1) | Reset on broken alternation |
| DP | O(n) | O(1) | Track inc/dec lengths |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use a single pass. Track the current turbulent subarray length.
- At each index `i`, compare the sign of `arr[i] - arr[i-1]` with the sign of `arr[i-1] - arr[i-2]`.
- If signs alternate (one positive, one negative), extend the window.
- If `arr[i] == arr[i-1]`, reset to length 1.
- If signs don't alternate but elements differ, reset to length 2.

```python
def maxTurbulenceSize(self, arr: list[int]) -> int:
    n = len(arr)
    if n < 2:
        return n

    max_len = 1
    cur_len = 1  # length of current turbulent subarray

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            sign = 1
        elif arr[i] < arr[i - 1]:
            sign = -1
        else:
            sign = 0

        if sign == 0:
            # Equal elements break turbulence
            cur_len = 1
        elif i == 1 or sign != prev_sign:
            # Sign alternates (or first pair) — extend
            cur_len += 1
        else:
            # Same sign as previous — reset to this pair
            cur_len = 2

        prev_sign = sign
        max_len = max(max_len, cur_len)

    return max_len
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `arr = [9,4,2,10,7,8,8,1,9]`

| i | arr[i-1]→arr[i] | sign | prev_sign | cur_len | max_len |
|---|------------------|------|-----------|---------|---------|
| 1 | 9→4 | -1 | — | 2 | 2 |
| 2 | 4→2 | -1 | -1 | 2 | 2 |
| 3 | 2→10 | 1 | -1 | 3 | 3 |
| 4 | 10→7 | -1 | 1 | 4 | 4 |
| 5 | 7→8 | 1 | -1 | 5 | 5 |
| 6 | 8→8 | 0 | 1 | 1 | 5 |
| 7 | 8→1 | -1 | 0 | 2 | 5 |
| 8 | 1→9 | 1 | -1 | 3 | 5 |

Output: **5** (subarray `[2,10,7,8]`... that's 4 elements. Let me recheck — subarray `[4,2,10,7,8]` is indices 1-5, that's 5 elements: 4>2 (down), 2<10 (up), 10>7 (down), 7<8 (up). Alternating!)

Output: **5**

### Edge Case Testing
- **Empty input:** Constraint says `len >= 1`, not applicable.
- **Single element:** `arr = [5]` — returns 1.
- **Typical case:** `arr = [9,4,2,10,7,8,8,1,9]` — returns 5.
- **Extreme values:** All equal `[3,3,3,3]` — sign is always 0, returns 1.

### Complexity
- **Time:** O(n) — single pass through the array.
- **Space:** O(1) — only counters and sign tracking.

### Optimization Discussion
An alternative **DP approach** tracks two variables: `inc` (length of turbulent subarray ending with an increase) and `dec` (length ending with a decrease). At each step:
- If `arr[i] > arr[i-1]`: `inc = dec + 1`, `dec = 1`
- If `arr[i] < arr[i-1]`: `dec = inc + 1`, `inc = 1`
- If equal: `inc = dec = 1`

Both approaches are O(n) time, O(1) space. The DP version avoids the `prev_sign` tracking.

### Follow-up Variations
- **Wiggle Subsequence** (LC 376) — subsequence (not subarray), can skip elements. Requires greedy/DP.
- **Alternating Subarray** — similar concept with different alternation rules.
- **Longest Mountain in Array** (LC 845) — must go up then down (not alternating).

### Common Traps
- Forgetting the **equal elements** case — `arr[i] == arr[i-1]` resets to 1, not 2.
- Off-by-one: when signs don't alternate, reset to 2 (the current pair is still valid), not 1.
- Not handling `prev_sign` initialization — using the `i == 1` guard handles the first iteration cleanly.
