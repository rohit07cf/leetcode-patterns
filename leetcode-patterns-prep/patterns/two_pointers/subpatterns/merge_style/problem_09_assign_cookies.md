# Assign Cookies

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Merge Style
**Link:** https://leetcode.com/problems/assign-cookies/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Each child `i` has a greed factor `g[i]`, and each cookie `j` has a size `s[j]`. A child is content if `s[j] >= g[i]`. Each child gets at most one cookie, each cookie goes to at most one child. Maximize the number of content children.

### 2. Clarification Questions
- Input constraints? `1 <= g.length, s.length <= 3 * 10^4`, values in `[1, 2^31 - 1]`
- Edge cases? No cookies; all cookies too small; more cookies than children
- Expected output? Integer — maximum number of content children
- Can input be modified? Yes — sorting is fine

### 3. Brute Force Approach
- **Idea:** Try all possible assignments (backtracking or matching).
- **Time:** O(n! * m!) in the worst case
- **Space:** O(n + m)

### 4. Optimized Approach
- **Core Insight:** **Greedy + merge-style two pointers.** Sort both arrays. Walk through children (smallest greed first) and cookies (smallest size first). Give the **smallest sufficient cookie** to the **least greedy child**. This is optimal because wasting a large cookie on a small-greed child cannot improve the total.
- **Time:** O(n log n + m log m)
- **Space:** O(1) extra

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | Exponential | O(n+m) | Enumerate assignments |
| Greedy Two Pointers | O(n log n + m log m) | O(1) | Sort then merge-walk |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort both `g` (greed) and `s` (cookie sizes).
- Use pointer `child` for children and `cookie` for cookies.
- If the current cookie satisfies the current child, advance both (assignment made).
- If not, the cookie is too small for anyone remaining — skip it (advance cookie only).

```python
def findContentChildren(g: list[int], s: list[int]) -> int:
    g.sort()  # children sorted by greed (ascending)
    s.sort()  # cookies sorted by size (ascending)

    child = 0
    cookie = 0

    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            # This cookie satisfies this child
            child += 1  # child is content, move to next child
        # Either way, this cookie is used up or too small — move on
        cookie += 1

    return child  # number of content children
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`g = [1, 2, 3]`, `s = [1, 1]`

After sorting: `g = [1, 2, 3]`, `s = [1, 1]`

| Step | child | cookie | g[child] | s[cookie] | Action |
|------|-------|--------|----------|-----------|--------|
| 1 | 0 | 0 | 1 | 1 | 1 >= 1 → assign, child=1, cookie=1 |
| 2 | 1 | 1 | 2 | 1 | 1 < 2 → skip cookie, cookie=2 |
| 3 | — | — | — | — | cookie out of bounds, done |

Result: `1` (only child with greed 1 gets a cookie)

### Edge Case Testing
- **Empty input:** `s = []` → cookie pointer never valid, return 0
- **Single element:** `g = [1]`, `s = [1]` → 1 content child
- **Typical case:** As shown above
- **Extreme values:** All cookies huge → all children satisfied; all cookies tiny → 0

### Complexity
- **Time:** O(n log n + m log m) — dominated by sorting
- **Space:** O(1) extra — only two pointers

### Optimization Discussion

The greedy correctness proof: assigning the smallest sufficient cookie to the least greedy child is optimal because:
1. If a cookie can satisfy a more greedy child, it can also satisfy a less greedy one.
2. Saving large cookies for more greedy children maximizes total assignments.

This is a **merge of two sorted sequences** — matching elements from one to the other.

### Follow-up Variations
- Two City Scheduling (LeetCode 1029) — greedy assignment with costs
- Boats to Save People (LeetCode 881) — two-pointer greedy pairing
- Candy (LeetCode 135) — greedy distribution with neighbor constraints

### Common Traps
- Advancing the child pointer when the cookie is too small (child should stay, cookie advances)
- Forgetting to sort both arrays before starting
- Trying to give the biggest cookie to the greediest child first (works, but smallest-first is more intuitive)
