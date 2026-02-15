# Subarrays with K Different Integers

**Difficulty:** Hard
**Pattern:** Sliding Window
**Subpattern:** Minimum Window Pattern
**Link:** https://leetcode.com/problems/subarrays-with-k-different-integers/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an integer array `nums` and an integer `k`, return the number of contiguous subarrays that contain **exactly** `k` distinct integers.

### 2. Clarification Questions
- Input constraints? `1 <= nums.length <= 2 * 10^4`, `1 <= nums[i], k <= nums.length`.
- Edge cases? `k = 1` (all subarrays of identical elements), `k > number of distinct elements` (answer is 0).
- Expected output? An integer count.
- Can input be modified? Yes.

### 3. Brute Force Approach
- **Idea:** Enumerate all subarrays, count distinct elements in each, tally those with exactly `k`.
- **Time:** O(n^2)
- **Space:** O(n)

### 4. Optimized Approach
- **Core Insight:** **exactly(k) = atMost(k) - atMost(k-1)**. Counting "at most k distinct" subarrays is a standard minimum window sliding problem. Subtracting gives exactly k.
- **Time:** O(n)
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(n) | Enumerate all subarrays |
| Optimized | O(n) | O(n) | atMost(k) - atMost(k-1) |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Define a helper `atMost(k)` that counts subarrays with at most `k` distinct values.
- In `atMost(k)`, expand `right`, shrink `left` when distinct count exceeds `k`.
- For each valid `right`, all subarrays `[left..right], [left+1..right], ..., [right..right]` are valid → add `right - left + 1`.
- Final answer: `atMost(k) - atMost(k - 1)`.

```python
from collections import defaultdict

def subarraysWithKDistinct(nums: list[int], k: int) -> int:
    def atMost(k: int) -> int:
        """Count subarrays with at most k distinct integers."""
        count = defaultdict(int)
        distinct = 0
        left = 0
        result = 0

        for right in range(len(nums)):
            if count[nums[right]] == 0:
                distinct += 1
            count[nums[right]] += 1

            # shrink until we have at most k distinct
            while distinct > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    distinct -= 1
                left += 1

            # all subarrays ending at right with start in [left, right]
            result += right - left + 1

        return result

    return atMost(k) - atMost(k - 1)
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `nums = [1,2,1,2,3]`, `k = 2`

**atMost(2):**

| right | nums[r] | distinct | left | count added |
|-------|---------|----------|------|-------------|
| 0 | 1 | 1 | 0 | 1 |
| 1 | 2 | 2 | 0 | 2 |
| 2 | 1 | 2 | 0 | 3 |
| 3 | 2 | 2 | 0 | 4 |
| 4 | 3 | 3→shrink to left=2 (drop 1 at idx0, but distinct still 3... drop 2 at idx1, distinct=2), left=2 | 2 | 3 |

Wait — let me re-trace index 4:
- Add 3: distinct=3. Shrink: remove nums[0]=1, count[1]=1 (still >0), distinct still 3. Remove nums[1]=2, count[2]=1 (still >0), distinct still 3. Remove nums[2]=1, count[1]=0, distinct=2. left=3.
- result += 4-3+1 = 2

atMost(2) = 1+2+3+4+2 = 12

**atMost(1):** Only subarrays of identical consecutive values = 1+1+1+1+1 = 5

**Answer:** 12 - 5 = **7**

### Edge Case Testing
- **Empty input:** Not possible per constraints.
- **Single element:** `nums = [1]`, `k = 1` → atMost(1) - atMost(0) = 1 - 0 = 1.
- **Typical case:** Shown in dry run.
- **Extreme values:** `k > distinct(nums)` → atMost(k) = atMost(k-1) → result = 0.

### Complexity
- **Time:** O(n) — two passes of the sliding window (one for `atMost(k)`, one for `atMost(k-1)`).
- **Space:** O(n) — frequency map holding at most `n` distinct values.

### Optimization Discussion
- The "exactly = atMost(k) - atMost(k-1)" trick is a **fundamental pattern** for converting "exactly k" problems into easier "at most k" problems.
- An alternative approach uses two left pointers (one for the smallest window with k distinct, one for the smallest with k+1 distinct) in a single pass.

### Follow-up Variations
- Count subarrays with **at least** k distinct integers.
- Count subarrays with exactly k **odd** numbers (LC 1248).
- Longest subarray with at most k distinct integers (LC 340).

### Common Traps
- **Trying to solve "exactly k" directly with one window** — the window boundaries become ambiguous. The subtraction trick avoids this entirely.
- **Forgetting to decrement `distinct`** when a count drops to 0 during shrinking.
- **Off-by-one in `atMost(0)`:** Should return 0 (no non-empty subarray has 0 distinct values), which the code handles because `distinct >= 1` after adding any element.
