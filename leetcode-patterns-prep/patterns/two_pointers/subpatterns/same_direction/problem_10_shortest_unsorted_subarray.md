# Shortest Unsorted Continuous Subarray

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Same Direction
**Link:** https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an integer array `nums`, find the length of the **shortest subarray** such that sorting only that subarray makes the entire array sorted. Return 0 if the array is already sorted.

### 2. Clarification Questions
- Input constraints? `1 <= nums.length <= 10^4`, `-10^5 <= nums[i] <= 10^5`
- Edge cases? Already sorted, all same elements, reverse sorted, length 1
- Expected output? Integer (length of subarray)
- Can input be modified? Prefer not to for optimal approach

### 3. Brute Force Approach
- **Idea:** Sort a copy and compare with the original. The first and last positions where they differ define the subarray boundaries.
- **Time:** O(n log n)
- **Space:** O(n)

### 4. Optimized Approach
- **Core Insight:** Make **two passes** in the same direction:
  1. **Left to right:** Track the running max. Whenever an element is less than the running max, it's out of place — update the right boundary.
  2. **Right to left:** Track the running min. Whenever an element is greater than the running min, it's out of place — update the left boundary.
  The answer is `right - left + 1` (or 0 if no out-of-place elements found).
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort + compare | O(n log n) | O(n) | Simple, reliable |
| Two-pass (max/min) | O(n) | O(1) | Optimal |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Pass 1 (left to right):** Find the rightmost element that is smaller than some element to its left (i.e., smaller than running max).
- **Pass 2 (right to left):** Find the leftmost element that is larger than some element to its right (i.e., larger than running min).
- The window `[left, right]` is the shortest subarray to sort.

```python
def findUnsortedSubarray(nums: list[int]) -> int:
    n = len(nums)
    right = -1  # will hold rightmost out-of-place index
    left = n    # will hold leftmost out-of-place index

    # left-to-right: find right boundary
    max_seen = float('-inf')
    for i in range(n):
        if nums[i] < max_seen:
            right = i  # this element is out of place
        else:
            max_seen = nums[i]

    # right-to-left: find left boundary
    min_seen = float('inf')
    for i in range(n - 1, -1, -1):
        if nums[i] > min_seen:
            left = i  # this element is out of place
        else:
            min_seen = nums[i]

    # if right was never updated, array is already sorted
    return right - left + 1 if right > left else 0
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `[2, 6, 4, 8, 10, 9, 15]`

**Pass 1 (left to right):**

| i | nums[i] | max_seen | nums[i] < max_seen? | right |
|---|---------|----------|---------------------|-------|
| 0 | 2 | 2 | No | -1 |
| 1 | 6 | 6 | No | -1 |
| 2 | 4 | 6 | Yes | 2 |
| 3 | 8 | 8 | No | 2 |
| 4 | 10 | 10 | No | 2 |
| 5 | 9 | 10 | Yes | 5 |
| 6 | 15 | 15 | No | 5 |

**Pass 2 (right to left):**

| i | nums[i] | min_seen | nums[i] > min_seen? | left |
|---|---------|----------|---------------------|------|
| 6 | 15 | 15 | No | 7 |
| 5 | 9 | 9 | No | 7 |
| 4 | 10 | 9 | Yes | 4 |
| 3 | 8 | 8 | No | 4 |
| 2 | 4 | 4 | No | 4 |
| 1 | 6 | 4 | Yes | 1 |
| 0 | 2 | 2 | No | 1 |

Answer: `right - left + 1 = 5 - 1 + 1 = 5`. Subarray `[6, 4, 8, 10, 9]`.

### Edge Case Testing
- **Empty input:** Length >= 1 per constraints
- **Single element:** `[1]` -> max never violated, right stays -1, returns 0
- **Typical case:** Shown above, returns 5
- **Extreme values:** Already sorted `[1,2,3,4]` -> returns 0. Reverse sorted `[4,3,2,1]` -> returns 4

### Complexity
- **Time:** O(n) — two linear passes
- **Space:** O(1) — only tracking max, min, and two boundary indices

### Optimization Discussion
This is already the optimal O(n) time, O(1) space solution. The sort-and-compare approach is simpler to understand and implement, so mention it first in interviews, then optimize.

**Why this works:** If an element is less than the max of everything before it, it must be included in the subarray to sort (it's "out of order"). Similarly for the left boundary with the min from the right.

### Follow-up Variations
- **Can you do it in one pass?** — yes, track both max (left-to-right) and min (right-to-left) simultaneously using indices `i` and `n-1-i`
- **Maximum Unsorted Subarray** — always the full array minus sorted prefix/suffix
- **Minimum Swaps to Sort (LC 801)** — related concept, different technique

### Common Traps
- Initializing `right = 0` instead of `-1` — causes wrong answer when array is already sorted
- Confusing which direction finds which boundary (left-to-right finds **right** boundary, counterintuitively)
- Returning `right - left` instead of `right - left + 1` (off-by-one)
- Using strict `<=` or `>=` vs `<` or `>` — equal elements are fine in their current positions
