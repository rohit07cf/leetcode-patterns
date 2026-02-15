# Trapping Rain Water

**Difficulty:** Hard
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction — Skip Logic
**Link:** https://leetcode.com/problems/trapping-rain-water/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given `n` non-negative integers representing an elevation map where each bar has width 1, compute how much water can be trapped after raining.

### 2. Clarification Questions

- **Input constraints?** `n <= 2 * 10^4`, `0 <= height[i] <= 10^5`
- **Edge cases?** All same height (no water), strictly ascending/descending (no water), single bar, two bars
- **Expected output?** Single integer — total units of trapped water
- **Can input be modified?** Not necessary

### 3. Brute Force Approach

- **Idea:** For each bar, find the max height to its left and right. Water at that bar = `min(left_max, right_max) - height[i]`.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach

- **💡 Core Insight:** Use two pointers from both ends, tracking `left_max` and `right_max`. The key skip logic: **process the side with the smaller max first**, because that side is the bottleneck. If `left_max <= right_max`, we know the water at `left` is determined by `left_max` (regardless of what's further right), so we process left and skip right. Vice versa.

- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Scan left/right max per bar |
| Prefix Arrays | O(n) | O(n) | Pre-compute left_max[], right_max[] |
| Two Pointers | O(n) | O(1) | Best — skip toward larger side |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Left and right pointers start at the ends.
- Track running `left_max` and `right_max`.
- **Skip logic:** always process the pointer with the smaller max — that side is the limiting wall.
- Water at current position = `current_max - height[pointer]` (never negative since max >= current).
- Advance the processed pointer inward.

```python
def trap(height: list[int]) -> int:
    if len(height) < 3:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
        if left_max <= right_max:
            # Left side is the bottleneck — process left
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            # Right side is the bottleneck — process right
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`

| Step | left | right | left_max | right_max | action | water_added | total |
|------|------|-------|----------|-----------|--------|-------------|-------|
| 1 | 0 | 11 | 0 | 1 | L→1 | max(0,1)-1=0 | 0 |
| 2 | 1 | 11 | 1 | 1 | L→2 | max(1,0)-0=1 | 1 |
| 3 | 2 | 11 | 1 | 1 | L→3 | max(1,2)-2=0 | 1 |
| 4 | 3 | 11 | 2 | 1 | R→10 | max(1,2)-2=0 | 1 |
| 5 | 3 | 10 | 2 | 2 | L→4 | max(2,1)-1=1 | 2 |
| 6 | 4 | 10 | 2 | 2 | L→5 | max(2,0)-0=2 | 4 |
| 7 | 5 | 10 | 2 | 2 | L→6 | max(2,1)-1=1 | 5 |
| 8 | 6 | 10 | 2 | 2 | L→7 | max(2,3)-3=0 | 5 |
| 9 | 7 | 10 | 3 | 2 | R→9 | max(2,1)-1=1 | 6 |
| 10 | 7 | 9 | 3 | 2 | R→8 | max(2,2)-2=0 | 6 |

**Output:** `6` ✓

### Edge Case Testing

- **Empty input:** `len < 3` → returns 0 (need at least 3 bars to trap).
- **Single element:** Returns 0.
- **Typical case:** Works as shown above.
- **Extreme values:** Monotonically increasing/decreasing → no water trapped (correct).

### Complexity

- **Time:** O(n) — each element visited exactly once
- **Space:** O(1) — only a few tracking variables

### Optimization Discussion

The prefix-array approach (O(n) space) is more intuitive for beginners: precompute `left_max[i]` and `right_max[i]` arrays, then sum `min(left_max[i], right_max[i]) - height[i]`. The two-pointer approach is strictly better on space but harder to reason about correctness.

### Follow-up Variations

- **Trapping Rain Water II (LC 407):** 3D version on a 2D grid — uses a priority queue (min-heap) from borders inward.
- **Container With Most Water (LC 11):** Pick two bars for max area instead of summing all trapped water.
- **Pour Water (LC 755):** Simulate water pouring at a specific index.

### ⚠️ Common Traps

- **Processing the wrong side** — always process the side with the **smaller** max; that's the bottleneck wall.
- **Adding negative water** — updating max before computing water ensures `max - height >= 0`.
- **Off-by-one with pointer movement** — advance the pointer *before* updating max and computing water (we process the new position, not the old one).
- **Forgetting the `len < 3` guard** — two bars cannot trap water between them.
