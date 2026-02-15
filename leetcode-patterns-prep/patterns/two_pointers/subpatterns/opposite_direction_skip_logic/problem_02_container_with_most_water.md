# Container With Most Water

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction — Skip Logic
**Link:** https://leetcode.com/problems/container-with-most-water/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given `n` vertical lines where the i-th line has height `height[i]`, find two lines that together with the x-axis form a container holding the most water. Return the maximum area.

### 2. Clarification Questions

- **Input constraints?** `2 <= n <= 10^5`, `0 <= height[i] <= 10^4`
- **Edge cases?** All same height, strictly increasing, strictly decreasing, contains zeros
- **Expected output?** A single integer — the maximum water area
- **Can input be modified?** Not necessary; we only read values

### 3. Brute Force Approach

- **Idea:** Try every pair `(i, j)` and compute `min(height[i], height[j]) * (j - i)`.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach

- **💡 Core Insight:** Start with the widest container (pointers at both ends). The area is limited by the **shorter** side. Moving the taller side inward can only decrease width without any guarantee of increasing height, so always **skip (move) the shorter side** — that's the only way to potentially find a taller line and a larger area.

- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Check all pairs |
| Optimized | O(n) | O(1) | Greedy skip of shorter side |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Place left/right pointers at both ends for maximum width.
- Calculate area at each step using the shorter height.
- **Skip logic:** always advance the pointer pointing to the shorter line — moving the taller one can never help.
- When heights are equal, moving either is fine (both lose width equally).

```python
def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        # Area = width * min height
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)

        # Skip the shorter side — only chance to find taller line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`

| left | right | h_left | h_right | width | area | max_water | move |
|------|-------|--------|---------|-------|------|-----------|------|
| 0 | 8 | 1 | 7 | 8 | 8 | 8 | left++ |
| 1 | 8 | 8 | 7 | 7 | 49 | 49 | right-- |
| 1 | 7 | 8 | 3 | 6 | 18 | 49 | right-- |
| 1 | 6 | 8 | 8 | 5 | 40 | 49 | right-- |
| 1 | 5 | 8 | 4 | 4 | 16 | 49 | right-- |
| 1 | 4 | 8 | 5 | 3 | 15 | 49 | right-- |
| 1 | 3 | 8 | 2 | 2 | 4 | 49 | right-- |
| 1 | 2 | 8 | 6 | 1 | 6 | 49 | right-- |

**Output:** `49` ✓

### Edge Case Testing

- **Empty input:** Constraints guarantee `n >= 2`.
- **Single element:** N/A per constraints.
- **Typical case:** Mixed heights — works as shown.
- **Extreme values:** All zeros → area = 0. All same height → first iteration gives max area (widest).

### Complexity

- **Time:** O(n) — each pointer moves at most n times total
- **Space:** O(1) — only a few variables

### Optimization Discussion

An advanced skip optimization: after computing area, skip all lines on the shorter side that are `<=` the current shorter height, since they can't produce a larger area with a narrower width. This doesn't change worst-case O(n) but speeds up many inputs.

```python
# Advanced skip variant
if height[left] < height[right]:
    cur = height[left]
    while left < right and height[left] <= cur:
        left += 1
```

### Follow-up Variations

- **Trapping Rain Water (LC 42):** Instead of a single container, compute total trapped water across all bars.
- **Largest Rectangle in Histogram (LC 84):** Related area maximization using a stack.

### ⚠️ Common Traps

- **Moving the taller side** — this is never beneficial; you lose width without gaining height.
- **Confusing with Trapping Rain Water** — that problem sums water per column; this one picks just two lines.
- **Forgetting the equal-height case** — moving either side works; don't overthink it.
