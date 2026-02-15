# Count Number of Nice Subarrays

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Minimum Window Pattern
**Link:** https://leetcode.com/problems/count-number-of-nice-subarrays/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays that contain **exactly** `k` odd numbers.

### 2. Clarification Questions
- Input constraints? `1 <= nums.length <= 5 * 10^4`, `1 <= nums[i] <= 10^5`, `1 <= k <= nums.length`.
- Edge cases? No odd numbers in array (return 0), all odd numbers, `k = 1`.
- Expected output? An integer count.
- Can input be modified? Yes.

### 3. Brute Force Approach
- **Idea:** Check every subarray, count odd numbers in each, tally those with exactly `k`.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** Use the **exactly(k) = atMost(k) - atMost(k-1)** trick. Replace each number with `1` (odd) or `0` (even), then count subarrays with sum exactly `k`. The `atMost` helper counts subarrays with at most `k` ones using a sliding window.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Enumerate all subarrays |
| Optimized | O(n) | O(1) | atMost subtraction trick |
| Alt: Prefix count | O(n) | O(n) | HashMap of odd-count prefixes |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Define `atMost(k)`: sliding window counting subarrays with at most `k` odd numbers.
- Expand `right`. If `nums[right]` is odd, decrement `k`.
- When `k < 0`, shrink `left` until `k >= 0`.
- For each `right`, add `right - left + 1` valid subarrays.
- Result: `atMost(k) - atMost(k - 1)`.

```python
def numberOfSubarrays(nums: list[int], k: int) -> int:
    def atMost(k: int) -> int:
        """Count subarrays with at most k odd numbers."""
        left = 0
        odd_count = 0
        result = 0

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1

            # shrink if too many odds
            while odd_count > k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1

            result += right - left + 1

        return result

    return atMost(k) - atMost(k - 1)
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `nums = [1,1,2,1,1]`, `k = 3`

**atMost(3):**

| right | nums[r] | odd_count | left | subarrays added |
|-------|---------|-----------|------|-----------------|
| 0 | 1 (odd) | 1 | 0 | 1 |
| 1 | 1 (odd) | 2 | 0 | 2 |
| 2 | 2 (even) | 2 | 0 | 3 |
| 3 | 1 (odd) | 3 | 0 | 4 |
| 4 | 1 (odd) | 4→shrink: remove 1 at idx 0, odd=3, left=1 | 1 | 4 |

atMost(3) = 1+2+3+4+4 = **14**

**atMost(2):**

| right | nums[r] | odd_count | left | subarrays added |
|-------|---------|-----------|------|-----------------|
| 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 2 | 0 | 2 |
| 2 | 2 | 2 | 0 | 3 |
| 3 | 1 | 3→shrink: remove idx0 (odd), odd=2, left=1 | 1 | 3 |
| 4 | 1 | 3→shrink: remove idx1 (odd), odd=2, left=2 | 2 | 3 |

atMost(2) = 1+2+3+3+3 = **12**

**Answer:** 14 - 12 = **2**

The two nice subarrays: `[1,1,2,1]` and `[1,2,1,1]`.

### Edge Case Testing
- **Empty input:** Not possible per constraints.
- **Single element:** `nums = [1]`, `k = 1` → atMost(1) - atMost(0) = 1 - 0 = 1.
- **Typical case:** Shown in dry run.
- **Extreme values:** No odd numbers with `k >= 1` → atMost(k) = atMost(k-1), result = 0.

### Complexity
- **Time:** O(n) — two linear passes.
- **Space:** O(1) — only counters and pointers.

### Optimization Discussion
- **Prefix sum approach:** Build a prefix array of odd counts. Use a hashmap to count how many prefixes have each odd count. For each `j`, look up `prefix[j] - k` in the map. O(n) time, O(n) space.
- The sliding window approach is preferred for its O(1) space.

### Follow-up Variations
- Count subarrays with exactly `k` even numbers.
- Count subarrays with exactly `k` distinct integers (LC 992 — same trick).
- Maximum length subarray with exactly `k` odd numbers.

### Common Traps
- **Trying to count "exactly k" with a single window** — the window can't easily count exact matches. The subtraction trick is the clean solution.
- **Forgetting even numbers don't affect odd count** — even numbers expand the window freely without changing the odd count.
- **Not handling `k = 0`:** atMost(0) counts subarrays with all even numbers. atMost(-1) = 0 by convention (the while loop shrinks everything). This works correctly.
