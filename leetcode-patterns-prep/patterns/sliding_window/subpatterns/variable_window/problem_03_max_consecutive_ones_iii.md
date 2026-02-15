# Max Consecutive Ones III

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Variable Window
**Link:** https://leetcode.com/problems/max-consecutive-ones-iii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a binary array `nums` and an integer `k`, return the maximum number of **consecutive 1s** in the array if you can flip at most `k` 0s to 1s.

### 2. Clarification Questions
- Input constraints? `1 <= nums.length <= 10^5`, `nums[i]` is 0 or 1, `0 <= k <= nums.length`.
- Edge cases? All 1s — return `len(nums)`. All 0s with `k = 0` — return 0.
- Expected output? An integer — the maximum window length containing at most k zeros.
- Can input be modified? Yes, but we don't need to.

### 3. Brute Force Approach
- **Idea:** For every starting index, expand right while counting zeros. Stop when zeros exceed `k`. Track the max window size.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** Reframe the problem: find the **longest subarray with at most k zeros**. Use a sliding window — expand right always, shrink left when zero count exceeds `k`.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Try all starting positions |
| Sliding Window | O(n) | O(1) | Count zeros in window |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Track `zero_count` inside the window.
- Expand `right` each step. If `nums[right] == 0`, increment `zero_count`.
- When `zero_count > k`, shrink from `left` until a 0 is removed.
- Update `max_len` at each valid state.

```python
def longestOnes(self, nums: list[int], k: int) -> int:
    left = 0
    zero_count = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        # Shrink window until we have at most k zeros
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `nums = [1,1,1,0,0,0,1,1,1,1,0]`, `k = 2`

| right | nums[r] | zero_count | left | window | max_len |
|-------|---------|------------|------|--------|---------|
| 0 | 1 | 0 | 0 | [1] | 1 |
| 1 | 1 | 0 | 0 | [1,1] | 2 |
| 2 | 1 | 0 | 0 | [1,1,1] | 3 |
| 3 | 0 | 1 | 0 | [1,1,1,0] | 4 |
| 4 | 0 | 2 | 0 | [1,1,1,0,0] | 5 |
| 5 | 0 | 3->2 | 4 | [0,0,1,1,1,1]... shrink to [0,0,...] left=4 | 5 |
| ... | ... | ... | ... | ... | ... |
| 10 | 0 | >2 shrink | 5 | [0,1,1,1,1,0] | 6 |

Output: **6** (subarray `[0,0,1,1,1,1]` with indices 4-9, flipping zeros at 4,5)

### Edge Case Testing
- **Empty input:** Constraint says `len >= 1`, not applicable.
- **Single element:** `nums = [0], k = 0` — zero_count exceeds k, left catches up, returns 0.
- **Typical case:** `nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2` — returns 6.
- **Extreme values:** All 1s — zero_count never increases, returns `len(nums)`.

### Complexity
- **Time:** O(n) — each element is added and removed from the window at most once.
- **Space:** O(1) — only counters and pointers.

### Optimization Discussion
Can replace `while` with `if` (like LC 424) so the window never shrinks — it either grows or slides. This gives the same result because we only care about the **maximum** window:

```python
if zero_count > k:
    if nums[left] == 0:
        zero_count -= 1
    left += 1
```

### Follow-up Variations
- **Max Consecutive Ones II** (LC 487) — same problem with `k = 1`.
- **Max Consecutive Ones** (LC 485) — `k = 0`, basic version.
- **Longest Repeating Character Replacement** (LC 424) — generalized to any character.

### Common Traps
- Off-by-one: updating `max_len` **after** shrinking, not before.
- Forgetting to handle `k = 0` — the while loop naturally handles it (shrinks until no zeros in window).
- Using `if` vs `while` for shrinking — `while` is safer and more intuitive; `if` is an optimization that requires understanding why it works.
