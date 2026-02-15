# Shortest Unsorted Continuous Subarray

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction — Skip Logic
**Link:** https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums`, find the shortest contiguous subarray such that sorting **only** this subarray makes the whole array sorted. Return the length of that subarray (0 if already sorted).

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 10^4`, `-10^5 <= nums[i] <= 10^5`
- **Edge cases?** Already sorted, reverse sorted, single element, all identical, unsorted only at edges
- **Expected output?** Integer — length of the shortest unsorted subarray
- **Can input be modified?** Prefer not to — O(1) space approach doesn't need to

### 3. Brute Force Approach

- **Idea:** Sort a copy, compare with original. The first and last positions where they differ define the boundaries.
- **Time:** O(n log n)
- **Space:** O(n)

### 4. Optimized Approach

- **💡 Core Insight:** Use two passes with skip logic from opposite directions. **From the left**, find the rightmost position where an element is **smaller** than the running max — that's the right boundary of the unsorted region. **From the right**, find the leftmost position where an element is **larger** than the running min — that's the left boundary. We skip all positions that are "in order" relative to their running extreme.

- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort + Compare | O(n log n) | O(n) | Simple but not optimal |
| Two-Pass Scan | O(n) | O(1) | Track running max/min from both ends |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Left-to-right pass:** Track running max. Whenever `nums[i] < max_seen`, this element is "out of place" — update right boundary.
- **Right-to-left pass:** Track running min. Whenever `nums[i] > min_seen`, this element is "out of place" — update left boundary.
- If no out-of-place element found, array is already sorted → return 0.

```python
def findUnsortedSubarray(nums: list[int]) -> int:
    n = len(nums)
    right_bound = -1
    left_bound = n

    # Left to right: find the rightmost element smaller than running max
    max_seen = float('-inf')
    for i in range(n):
        if nums[i] < max_seen:
            right_bound = i  # This element is out of place
        else:
            max_seen = nums[i]  # Skip — element is in order

    # Right to left: find the leftmost element larger than running min
    min_seen = float('inf')
    for i in range(n - 1, -1, -1):
        if nums[i] > min_seen:
            left_bound = i  # This element is out of place
        else:
            min_seen = nums[i]  # Skip — element is in order

    # If no out-of-place elements found, array is sorted
    if right_bound == -1:
        return 0

    return right_bound - left_bound + 1
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [2, 6, 4, 8, 10, 9, 15]`

**Left-to-right pass (find right_bound):**

| i | nums[i] | max_seen | out of place? | right_bound |
|---|---------|----------|---------------|-------------|
| 0 | 2 | 2 | no | -1 |
| 1 | 6 | 6 | no | -1 |
| 2 | 4 | 6 | **yes (4 < 6)** | 2 |
| 3 | 8 | 8 | no | 2 |
| 4 | 10 | 10 | no | 2 |
| 5 | 9 | 10 | **yes (9 < 10)** | 5 |
| 6 | 15 | 15 | no | 5 |

**Right-to-left pass (find left_bound):**

| i | nums[i] | min_seen | out of place? | left_bound |
|---|---------|----------|---------------|------------|
| 6 | 15 | 15 | no | 7 |
| 5 | 9 | 9 | no | 7 |
| 4 | 10 | 9 | **yes (10 > 9)** | 4 |
| 3 | 8 | 8 | no | 4 |
| 2 | 4 | 4 | no | 4 |
| 1 | 6 | 4 | **yes (6 > 4)** | 1 |
| 0 | 2 | 2 | no | 1 |

**Result:** `right_bound - left_bound + 1 = 5 - 1 + 1 = 5` ✓

Sorting `nums[1:6] = [6,4,8,10,9]` → `[4,6,8,9,10]` gives `[2,4,6,8,9,10,15]` ✓

### Edge Case Testing

- **Empty input:** Constraints guarantee `n >= 1`.
- **Single element:** Max/min never violated → `right_bound = -1` → returns 0. Correct.
- **Typical case:** Works as shown.
- **Extreme values:** Already sorted → no violations → returns 0. Fully reversed → returns `n`.

### Complexity

- **Time:** O(n) — two linear passes
- **Space:** O(1) — only tracking variables

### Optimization Discussion

The sort-and-compare approach is simpler to code and reason about. In an interview, it's a fine first answer. The two-pass approach is the optimal follow-up when the interviewer asks for O(1) space.

### Follow-up Variations

- **Is Array Sorted? (simple check):** Single pass — `nums[i] <= nums[i+1]` for all `i`.
- **Minimum Swaps to Sort:** Related but requires a graph/cycle approach.
- **Sort Array By Parity (LC 905):** Different sorting criteria with two-pointer partitioning.

### ⚠️ Common Traps

- **Only scanning from one direction** — you need BOTH passes. Left-to-right finds the right boundary, right-to-left finds the left boundary.
- **Using strict inequality only** — `nums[i] < max_seen` is correct (equal elements are fine); using `<=` would incorrectly flag duplicates.
- **Forgetting the "already sorted" check** — if `right_bound` is never updated, the array is sorted; return 0, not a negative number.
- **Trying to find boundaries with a single scan** — a single scan can find one boundary but not both correctly.
