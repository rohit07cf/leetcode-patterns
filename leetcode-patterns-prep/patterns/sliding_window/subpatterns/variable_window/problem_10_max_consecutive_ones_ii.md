# Max Consecutive Ones II

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Variable Window
**Link:** https://leetcode.com/problems/max-consecutive-ones-ii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a binary array `nums`, return the maximum number of **consecutive 1s** if you can flip **at most one** 0 to a 1.

### 2. Clarification Questions
- Input constraints? `1 <= nums.length <= 10^5`, `nums[i]` is 0 or 1.
- Edge cases? All 1s — return `len(nums)`. All 0s — return 1 (flip one). Single element — return 1.
- Expected output? An integer — max consecutive 1s after at most one flip.
- Can input be modified? Yes, but we won't.

### 3. Brute Force Approach
- **Idea:** For each 0 in the array, pretend to flip it, then count the max consecutive 1s. Also consider flipping no 0s.
- **Time:** O(n^2) — for each of up to n zeros, scan left and right.
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** This is **Max Consecutive Ones III with k=1**. Find the longest subarray with **at most one 0**. Use a sliding window tracking zero count.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Try flipping each 0 |
| Sliding Window | O(n) | O(1) | At most 1 zero in window |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Track `zero_count` in the window. Since k=1, shrink when `zero_count > 1`.
- Expand `right` each step. If `nums[right] == 0`, increment zero_count.
- Shrink `left` until `zero_count <= 1`.
- Track `max_len`.

```python
def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
    left = 0
    zero_count = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        # Shrink until at most 1 zero in window
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `nums = [1,0,1,1,0]`

| right | nums[r] | zero_count | left | window | max_len |
|-------|---------|------------|------|--------|---------|
| 0 | 1 | 0 | 0 | [1] | 1 |
| 1 | 0 | 1 | 0 | [1,0] | 2 |
| 2 | 1 | 1 | 0 | [1,0,1] | 3 |
| 3 | 1 | 1 | 0 | [1,0,1,1] | 4 |
| 4 | 0 | 2 | 0 | too many zeros | 4 |
| | | shrink: nums[0]=1 | 1 | [0,1,1,0] still 2 | 4 |
| | | shrink: nums[1]=0 | 2 | [1,1,0] zero_count=1 | 4 |

Output: **4** (subarray `[1,0,1,1]` — flip the 0 at index 1)

### Edge Case Testing
- **Empty input:** Constraint says `len >= 1`, not applicable.
- **Single element:** `nums = [0]` — zero_count=1 (allowed), returns 1. `nums = [1]` — returns 1.
- **Typical case:** `nums = [1,0,1,1,0]` — returns 4.
- **Extreme values:** All 1s `[1,1,1,1]` — zero_count=0, returns 4. All 0s `[0,0,0]` — window always has 1 zero max, returns 1.

### Complexity
- **Time:** O(n) — each element enters and leaves the window at most once.
- **Space:** O(1) — only counters and pointers.

### Optimization Discussion

**Follow-up: What if the input is a data stream?** You can't go back to re-read elements. Instead of tracking `zero_count`, store the **index of the previous zero** (`prev_zero`). When you hit a new zero, move `left` to `prev_zero + 1` and update `prev_zero`.

```python
def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
    left = 0
    prev_zero = -1  # index of the previous zero
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            left = prev_zero + 1  # jump past previous zero
            prev_zero = right

        max_len = max(max_len, right - left + 1)

    return max_len
```

This approach uses O(1) space and handles streams — no need to re-read `nums[left]`.

### Follow-up Variations
- **Max Consecutive Ones III** (LC 1004) — generalized to k flips.
- **Max Consecutive Ones** (LC 485) — no flips allowed (k=0).
- **Flip String to Monotone Increasing** (LC 926) — different structure, prefix sums.

### Common Traps
- Forgetting that you can flip **at most** one 0 — you don't have to flip any. The window condition `zero_count <= 1` handles this naturally.
- For the stream follow-up, forgetting to initialize `prev_zero = -1` — starting at 0 would incorrectly skip the first element.
- Returning 0 for all-zeros input — wrong! You can still flip one 0, so the answer is 1.
- This is a premium problem on LeetCode — practice with LC 1004 (k=any) which is freely available.
