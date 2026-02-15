# Smallest Range Covering Elements from K Lists

**Difficulty:** Hard
**Pattern:** Sliding Window
**Subpattern:** Minimum Window Pattern
**Link:** https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given `k` sorted lists of integers, find the smallest range `[a, b]` such that at least one element from each list falls within this range. If ties, return the range with the smallest start.

### 2. Clarification Questions
- Input constraints? `1 <= k <= 3500`, `1 <= list[i].length <= 50`, `-10^5 <= list[i][j] <= 10^5`. Lists are sorted in non-decreasing order.
- Edge cases? All lists have one element, all lists contain the same value, single list.
- Expected output? A list `[a, b]` representing the smallest range.
- Can input be modified? Yes.

### 3. Brute Force Approach
- **Idea:** Try every pair of elements from different lists as range endpoints. Check if the range covers all `k` lists.
- **Time:** O(n^2 * k) where `n` is total number of elements.
- **Space:** O(k)

### 4. Optimized Approach
- **Core Insight:** Merge all elements into one sorted list (keeping track of which list each came from). Then apply **minimum window** sliding window: find the smallest window in this merged list that contains at least one element from every list. This is exactly LC 76 but with list IDs instead of characters.
- **Time:** O(n log n)
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2 * k) | O(k) | Check all range pairs |
| Optimized (Sliding Window) | O(n log n) | O(n) | Merge + minimum window |
| Alt: Min-Heap | O(n log k) | O(k) | Expand smallest pointer |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Flatten all lists into `(value, list_index)` pairs and sort by value.
- Slide a window over the sorted array. Track how many distinct lists are represented in the window using a counter map.
- When all `k` lists are covered, try to shrink from the left.
- The range is `[sorted[left].value, sorted[right].value]`.

```python
from collections import defaultdict

def smallestRange(nums: list[list[int]]) -> list[int]:
    k = len(nums)

    # merge all elements with their list index
    merged = []
    for list_idx, lst in enumerate(nums):
        for val in lst:
            merged.append((val, list_idx))
    merged.sort()  # sort by value

    count = defaultdict(int)  # list_index -> count in current window
    covered = 0               # how many distinct lists are in window
    best = [-10**6, 10**6]    # best range found
    left = 0

    for right in range(len(merged)):
        val_r, idx_r = merged[right]
        count[idx_r] += 1
        if count[idx_r] == 1:  # new list covered
            covered += 1

        # shrink window while all k lists are covered
        while covered == k:
            val_l, idx_l = merged[left]
            # update best range (prefer smaller range, then smaller start)
            if val_r - val_l < best[1] - best[0]:
                best = [val_l, val_r]

            count[idx_l] -= 1
            if count[idx_l] == 0:  # lost a list
                covered -= 1
            left += 1

    return best
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]`

Merged sorted: `[(0,1),(4,0),(5,2),(9,1),(10,0),(12,1),(15,0),(18,2),(20,1),(22,2),(24,0),(26,0),(30,2)]`

| right | val | covered | shrink? | best |
|-------|-----|---------|---------|------|
| 0 | (0,1) | 1 | no | — |
| 1 | (4,0) | 2 | no | — |
| 2 | (5,2) | 3 | yes→left moves to 1 | [0,5] |
| ... | ... | ... | ... | ... |

Eventually finds `[20,24]` as the smallest range covering all 3 lists.

**Output:** `[20, 24]`

### Edge Case Testing
- **Empty input:** Not possible per constraints (each list has >= 1 element).
- **Single element:** Each list has one element → range is `[min, max]` of those elements.
- **Typical case:** Shown in dry run.
- **Extreme values:** Large lists with overlapping values — still O(n log n).

### Complexity
- **Time:** O(n log n) — sorting the merged array dominates. The sliding window itself is O(n).
- **Space:** O(n) — storing the merged array where `n` is total elements across all lists.

### Optimization Discussion
- **Min-heap alternative:** Maintain a pointer per list in a min-heap. Always advance the minimum. Track current max. This gives O(n log k) time and O(k) space, which is better when `k << n`.
- The sliding window approach is more intuitive and directly maps to the minimum window pattern.

### Follow-up Variations
- What if the lists are unsorted?
- What if you need the range to cover at least `m` out of `k` lists?
- Return all smallest ranges of equal size.

### Common Traps
- **Forgetting to track which list each element belongs to** after merging.
- **Tie-breaking:** When ranges have equal length, return the one with the smaller start. The `<` comparison handles this naturally.
- **Not handling duplicate values** from the same list — the count map handles this correctly.
