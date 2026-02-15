# Container With Most Water

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction
**Link:** https://leetcode.com/problems/container-with-most-water/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an array of heights representing vertical lines, find two lines that together with the x-axis form a container holding the **most water**. Return the maximum area.

### 2. Clarification Questions
- Input constraints? Array length 2 to 10^5. Heights 0 to 10^4.
- Edge cases? All heights equal — any pair gives the same per-unit area. One height is 0 — that side contributes nothing.
- Expected output? A single integer representing the maximum area.
- Can input be modified? No modification needed.

### 3. Brute Force Approach
- **Idea:** Check every pair `(i, j)`, compute `min(height[i], height[j]) * (j - i)`, track the max.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach
- 💡 **Core Insight:** Start with the **widest container** (left=0, right=end). The only way to find a larger area is to find a **taller** shorter side. Always move the pointer pointing to the **shorter line** inward — keeping the taller side can never hurt, but keeping the shorter side can never help since width is decreasing.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | TLE on large inputs |
| Two Pointers | O(n) | O(1) | Greedy + two pointers |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Start with the widest container: `left = 0`, `right = n - 1`.
- Calculate area using the shorter of the two heights.
- Move the pointer at the **shorter** height inward (greedy choice).
- Track and return the maximum area seen.

```python
def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        # Area limited by the shorter line
        width = right - left
        h = min(height[left], height[right])
        max_area = max(max_area, width * h)

        # Move the shorter side inward — only chance to improve
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`

| Step | left | right | h_left | h_right | area | max_area |
|------|------|-------|--------|---------|------|----------|
| 1 | 0 | 8 | 1 | 7 | 1*8=8 | 8 |
| 2 | 1 | 8 | 8 | 7 | 7*7=49 | 49 |
| 3 | 1 | 7 | 8 | 3 | 3*6=18 | 49 |
| 4 | 1 | 6 | 8 | 8 | 5*8=40 | 49 |
| 5 | 2 | 6 | 6 | 8 | 4*6=24 | 49 |
| ... | ... | ... | ... | ... | ... | 49 |

Result: **49**

### Edge Case Testing
- **Empty input:** Not possible per constraints (length >= 2).
- **Single element:** Not possible.
- **Typical case:** `[1,8,6,2,5,4,8,3,7]` -> 49. Correct.
- **Extreme values:** All heights = 0 -> area = 0. All heights equal -> area = `height[0] * (n-1)`.

### Complexity
- **Time:** O(n) — each pointer moves at most n steps total.
- **Space:** O(1) — only pointers and a running max.

### Optimization Discussion
This is provably optimal. Every skipped pair is guaranteed to produce a smaller or equal area than the current best, so no valid candidate is missed.

### Follow-up Variations
- **Trapping Rain Water** (LeetCode 42): Instead of two lines, compute water trapped across ALL bars. Harder — requires tracking max heights from both sides.
- What if lines can be **tilted**? Changes the geometry entirely — different problem.
- What if you must pick **exactly k lines**? Becomes a combinatorial optimization problem.

### ⚠️ Common Traps
- Confusing this with **Trapping Rain Water** — they are different problems. This picks two lines; that sums water over all bars.
- Moving the **taller** pointer instead of the shorter one — this breaks the greedy invariant.
- Using `height[left] <= height[right]` vs `<` — either works since equal heights means moving either side is fine.
