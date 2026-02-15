# Max Consecutive Ones III

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Sliding Window + Hashmap
**Link:** https://leetcode.com/problems/max-consecutive-ones-iii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a binary array `nums` and an integer `k`, return the **maximum number of consecutive 1s** in the array if you can flip at most `k` 0s to 1s.

### 2. Clarification Questions
- **Input constraints?** `1 <= nums.length <= 10^5`, `nums[i]` is 0 or 1, `0 <= k <= nums.length`.
- **Edge cases?** All 1s → return `len(nums)`. All 0s with `k >= len(nums)` → return `len(nums)`. `k = 0` → longest run of 1s.
- **Expected output?** An integer — the maximum window length.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach
- **Idea:** For each starting index, expand as far as possible while counting flipped 0s <= k.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** Reframe: find the **longest subarray with at most `k` zeros**. Use a sliding window — expand `right`, count zeros. When zeros exceed `k`, shrink `left` until zeros <= `k` again.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Expand from each index |
| Sliding Window | O(n) | O(1) | Count zeros in window |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Maintain `zero_count` — number of 0s in the current window.
- Expand `right` every step. If `nums[right] == 0`, increment `zero_count`.
- When `zero_count > k`, shrink `left` (decrement `zero_count` if `nums[left] == 0`).
- Track maximum window size.

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

**Alternative (hashmap style, to match subpattern):**

```python
from collections import defaultdict

def longestOnes(self, nums: list[int], k: int) -> int:
    count = defaultdict(int)  # value -> frequency in window
    left = 0
    max_len = 0

    for right in range(len(nums)):
        count[nums[right]] += 1

        # Too many zeros — shrink
        while count[0] > k:
            count[nums[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `nums = [1,1,1,0,0,0,1,1,1,1,0]`, `k = 2`

| right | val | zero_count | left | window size | max_len |
|-------|-----|------------|------|-------------|---------|
| 0     | 1   | 0          | 0    | 1           | 1       |
| 1     | 1   | 0          | 0    | 2           | 2       |
| 2     | 1   | 0          | 0    | 3           | 3       |
| 3     | 0   | 1          | 0    | 4           | 4       |
| 4     | 0   | 2          | 0    | 5           | 5       |
| 5     | 0   | 3→shrink   | 0    |             |         |
|       |     | left=1(1)  |      |             |         |
|       |     | left=2(1)  |      |             |         |
|       |     | left=3(0)→2| 4   | 2           | 5       |
| 6     | 1   | 2          | 4    | 3           | 5       |
| 7     | 1   | 2          | 4    | 4           | 5       |
| 8     | 1   | 2          | 4    | 5           | 5       |
| 9     | 1   | 2          | 4    | 6           | 6       |
| 10    | 0   | 3→shrink   | 4    |             |         |
|       |     | left=4(0)→2| 5   | 6           | 6       |

**Output:** `6` (subarray indices 4-9: `[0,0,1,1,1,1]` → flip 2 zeros)

### Edge Case Testing
- **Empty input:** Not possible per constraints.
- **Single element:** `[1]`, k=0 → 1. `[0]`, k=0 → 0. `[0]`, k=1 → 1.
- **Typical case:** `[1,1,1,0,0,0,1,1,1,1,0]`, k=2 → 6.
- **Extreme values:** All 1s → `len(nums)`. `k = 0` → longest consecutive 1s. `k >= len(nums)` → `len(nums)`.

### Complexity
- **Time:** O(n) — each element added and removed from window at most once.
- **Space:** O(1) — only a counter variable (or O(1) hashmap with at most 2 keys).

### Optimization Discussion
- **Non-shrinking window trick:** Instead of `while`, use `if`. The window never shrinks below the current best, so the answer is just `len(nums) - left` at the end. This avoids `max_len` tracking entirely.

```python
def longestOnes(self, nums, k):
    left = 0
    for right in range(len(nums)):
        k -= (1 - nums[right])  # decrement k when we see a 0
        if k < 0:
            k += (1 - nums[left])  # restore k if removing a 0
            left += 1
    return len(nums) - left
```

### Follow-up Variations
- **Longest Repeating Character Replacement** (LeetCode 424) — generalized version with 26 characters.
- **Max Consecutive Ones** (LeetCode 485) — no flips allowed.
- **Max Consecutive Ones II** (LeetCode 487) — flip at most 1 zero, follow-up asks for O(1) space with streaming.

### Common Traps
- Forgetting to handle `k = 0` — the while loop condition `zero_count > 0` would aggressively shrink.
- Thinking you need to track **which** zeros to flip — you don't. The window implicitly handles this.
- Mixing up "flip k zeros" with "window contains at most k zeros" — they're equivalent reframings.
