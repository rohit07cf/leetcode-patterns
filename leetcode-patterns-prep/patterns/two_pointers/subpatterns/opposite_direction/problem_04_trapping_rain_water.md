# Trapping Rain Water

**Difficulty:** Hard
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction
**Link:** https://leetcode.com/problems/trapping-rain-water/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an elevation map (array of non-negative integers representing bar heights), compute how much **rainwater** can be trapped between the bars after raining.

### 2. Clarification Questions
- Input constraints? Array length 0 to 2 * 10^4. Heights 0 to 10^5.
- Edge cases? Empty array or length < 3 -> no water can be trapped. Monotonically increasing/decreasing -> no water.
- Expected output? A single integer — total units of trapped water.
- Can input be modified? No modification needed.

### 3. Brute Force Approach
- **Idea:** For each bar at index `i`, find the max height to its left and right. Water at `i` = `min(left_max, right_max) - height[i]`. Sum across all bars.
- **Time:** O(n^2) — scanning left and right for each bar.
- **Space:** O(1)

### 4. Optimized Approach
- 💡 **Core Insight:** Water above each bar depends on the **minimum of the tallest bar on its left and right**. With two pointers, we process from the side with the **smaller known max**. That side's water level is fully determined because the other side is guaranteed to be at least as tall.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Recomputes max each time |
| Prefix Arrays | O(n) | O(n) | Two passes for left_max, right_max |
| Two Pointers | O(n) | O(1) | Optimal — single pass |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Maintain `left`, `right` pointers and `left_max`, `right_max` running maximums.
- Process the side with the **smaller max** — its water contribution is certain.
- If `left_max <= right_max`, water at `left` is `left_max - height[left]` (guaranteed non-negative since `left_max >= height[left]`).
- Accumulate total water, advance the pointer.

```python
def trap(height: list[int]) -> int:
    if len(height) < 3:
        return 0  # need at least 3 bars to trap water

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, height[left])
            # Water here is determined by left_max (the smaller side)
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            # Water here is determined by right_max (the smaller side)
            water += right_max - height[right]

    return water
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`

| Step | left | right | left_max | right_max | action | water added | total |
|------|------|-------|----------|-----------|--------|-------------|-------|
| 1 | 0 | 11 | 0 | 1 | left_max<=right_max, left->1, left_max=1 | 1-1=0 | 0 |
| 2 | 1 | 11 | 1 | 1 | left_max<=right_max, left->2, left_max=1 | 1-0=1 | 1 |
| 3 | 2 | 11 | 1 | 1 | left_max<=right_max, left->3, left_max=2 | 2-2=0 | 1 |
| 4 | 3 | 11 | 2 | 1 | right_max<left_max, right->10, right_max=2 | 2-2=0 | 1 |
| 5 | 3 | 10 | 2 | 2 | left_max<=right_max, left->4, left_max=2 | 2-1=1 | 2 |
| ... | ... | ... | ... | ... | ... | ... | ... |

Final result: **6**

### Edge Case Testing
- **Empty input:** `[]` -> returns 0 (early return).
- **Single element:** `[5]` -> returns 0 (length < 3).
- **Typical case:** `[0,1,0,2,1,0,1,3,2,1,2,1]` -> 6. Correct.
- **Extreme values:** `[100000, 0, 100000]` -> 100000. Flat plateau `[3,3,3]` -> 0.

### Complexity
- **Time:** O(n) — each element visited exactly once.
- **Space:** O(1) — only pointers and two max trackers.

### Optimization Discussion
The two-pointer approach is already optimal at O(n) time and O(1) space. The prefix-array approach is equally fast but uses O(n) extra space. A monotonic stack approach also works in O(n)/O(n).

### Follow-up Variations
- **Trapping Rain Water II** (LeetCode 407): 2D grid version — use a min-heap BFS from the border.
- **Container With Most Water** (LeetCode 11): Pick two bars to maximize area (simpler greedy).
- What if bars have **variable width**? Multiply each trapped unit by bar width.

### ⚠️ Common Traps
- Confusing this with Container With Most Water — they compute different things.
- Forgetting to **update the max before computing water** — you must update `left_max`/`right_max` first, then subtract `height`.
- Off-by-one: advance the pointer **before** reading the new height, not after.
- Not handling arrays shorter than 3 — no water can be trapped with fewer than 3 bars.
