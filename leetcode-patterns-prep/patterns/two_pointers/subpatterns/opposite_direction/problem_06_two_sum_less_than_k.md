# Two Sum Less Than K

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction
**Link:** https://leetcode.com/problems/two-sum-less-than-k/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an array of integers and an integer `k`, find the **maximum sum** of any pair `nums[i] + nums[j]` such that `i != j` and the sum is **strictly less than** `k`. Return -1 if no such pair exists.

### 2. Clarification Questions
- Input constraints? Array length 1 to 100. Values 1 to 1000. k is 1 to 2000.
- Edge cases? Array length 1 -> no pair exists, return -1. All pairs sum >= k -> return -1.
- Expected output? The maximum pair sum less than k, or -1.
- Can input be modified? Yes — we can sort the array.

### 3. Brute Force Approach
- **Idea:** Check all pairs `(i, j)`, track the maximum sum that is less than `k`.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach
- 💡 **Core Insight:** **Sort the array**, then use opposite-direction two pointers. If the sum of the smallest and largest remaining values is less than `k`, it's a candidate — record it, then try to increase the sum by moving `left` right. If the sum is >= `k`, decrease it by moving `right` left.
- **Time:** O(n log n)
- **Space:** O(1) (or O(n) depending on sort implementation)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Simple but slow |
| Sort + Two Pointers | O(n log n) | O(1) | Optimal for this problem |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort the array so we can use two pointers.
- Start with `left = 0`, `right = n - 1`.
- If sum < k, it's a valid candidate — update answer and try a larger sum.
- If sum >= k, shrink by moving `right` left.

```python
def twoSumLessThanK(nums: list[int], k: int) -> int:
    nums.sort()
    left, right = 0, len(nums) - 1
    result = -1  # -1 means no valid pair found

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum < k:
            result = max(result, current_sum)  # valid pair, track best
            left += 1  # try to get a larger valid sum
        else:
            right -= 1  # sum too large, decrease it

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `nums = [34, 23, 1, 24, 75, 33, 54, 8]`, `k = 60`

Sorted: `[1, 8, 23, 24, 33, 34, 54, 75]`

| Step | left | right | sum | Action | result |
|------|------|-------|-----|--------|--------|
| 1 | 0 | 7 | 1+75=76 | >= 60, move right | -1 |
| 2 | 0 | 6 | 1+54=55 | < 60, record 55, move left | 55 |
| 3 | 1 | 6 | 8+54=62 | >= 60, move right | 55 |
| 4 | 1 | 5 | 8+34=42 | < 60, record 42, move left | 55 |
| 5 | 2 | 5 | 23+34=57 | < 60, record 57, move left | 57 |
| 6 | 3 | 5 | 24+34=58 | < 60, record 58, move left | 58 |
| 7 | 4 | 5 | 33+34=67 | >= 60, move right | 58 |
| 8 | 4 | 4 | left == right, stop | — | 58 |

Result: **58** (from pair 24 + 34)

### Edge Case Testing
- **Empty input:** Not possible per constraints (length >= 1).
- **Single element:** `[5], k=10` -> `left == right` immediately, returns -1. Correct.
- **Typical case:** `[34,23,1,24,75,33,54,8], k=60` -> 58. Correct.
- **Extreme values:** All pairs sum >= k -> every step moves `right` left, returns -1. All pairs sum < k -> result is the two largest elements' sum.

### Complexity
- **Time:** O(n log n) — dominated by sorting. The two-pointer scan is O(n).
- **Space:** O(1) — sorting in place (Python's Timsort uses O(n) internally, but logically O(1) extra).

### Optimization Discussion
O(n log n) is optimal here. You could use a brute force O(n^2) approach that avoids sorting, but it's slower. The sorting cost pays for itself by enabling the linear scan.

### Follow-up Variations
- **Two Sum** (LeetCode 1): Find exact sum = target. Hash map or two pointers on sorted.
- **3Sum Smaller** (LeetCode 259): Count triplets with sum < target. Fix one, two-pointer on rest.
- What if we need the **pair of indices** instead of the sum? Store original indices before sorting.

### ⚠️ Common Traps
- Forgetting to return **-1** when no valid pair exists.
- Using `<=` instead of `<` when comparing with k — the problem requires **strictly less than** k.
- Not sorting the array first — two pointers require sorted input.
