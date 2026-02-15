# First Bad Version

**Difficulty:** Easy
**Pattern:** Binary Search
**Subpattern:** Classic Binary Search
**Link:** https://leetcode.com/problems/first-bad-version/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

You have n versions [1, 2, ..., n]. One version is bad, and all versions after it are also bad. Given an API `isBadVersion(version)`, find the **first** bad version while minimizing API calls.

### 2. Clarification Questions

- **Input constraints?** 1 <= n <= 2^31 - 1. There is always at least one bad version.
- **Edge cases?** Version 1 is bad (all bad), only last version is bad, n = 1.
- **Expected output?** Integer — the first bad version number.
- **Can input be modified?** No array — searching a range with an API.

### 3. Brute Force Approach

- **Idea:** Check versions 1, 2, 3, ... until `isBadVersion()` returns true.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- 💡 **Core Insight:** Versions form a pattern: `[good, good, ..., good, bad, bad, ..., bad]`. This is a **sorted boolean array**. We need the **leftmost** `true`. Binary search for the boundary — when `mid` is bad, the answer is at `mid` or left of it; when good, the answer is right of it.
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Linear scan |
| Optimized | O(log n) | O(1) | Binary search on boolean boundary |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use `left < right` (not `<=`) because we're finding a **boundary**, not a specific value.
- When `mid` is bad, it could be the first bad, so set `right = mid` (not `mid - 1`).
- When `mid` is good, first bad must be after it, so `left = mid + 1`.

```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def firstBadVersion(n: int) -> int:
    left, right = 1, n

    while left < right:  # WHY: converging to the boundary, not searching for exact match
        mid = left + (right - left) // 2

        if isBadVersion(mid):
            right = mid  # WHY: mid could be the first bad version
        else:
            left = mid + 1  # WHY: mid is good, first bad is after it

    return left  # WHY: left == right, both point to first bad version
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `n = 5`, first bad = `4`

Versions: `[G, G, G, B, B]`

| Step | left | right | mid | isBad(mid) | Action |
|------|------|-------|-----|------------|--------|
| 1 | 1 | 5 | 3 | false | left = 4 |
| 2 | 4 | 5 | 4 | true | right = 4 |
| 3 | left == right | — | — | — | Return 4 |

### Edge Case Testing

- **Empty input:** Not applicable — n >= 1.
- **Single element:** n = 1, version 1 is bad → left = right = 1, return 1.
- **Typical case:** First bad somewhere in middle → logarithmic convergence.
- **Extreme values:** Version 1 is bad → right keeps shrinking to 1. Last version is bad → left keeps growing to n.

### Complexity

- **Time:** O(log n) — halving the search space each step.
- **Space:** O(1) — constant extra space.

### Optimization Discussion

This is the optimal solution. The key difference from standard binary search: we use `left < right` with `right = mid` instead of `left <= right` with `right = mid - 1`. This is the **left boundary binary search** template.

### Follow-up Variations

- What if you need the **last good** version? (Same boundary, return `left - 1`.)
- What if the API is unreliable and can give wrong answers? (Majority voting with multiple calls.)

### Common Traps

- **Using `right = mid - 1`:** This skips `mid`, which might be the first bad version. Must use `right = mid`.
- **Using `left <= right` with `right = mid`:** This causes an infinite loop when `left == right`.
- **Integer overflow:** Same concern with `mid` calculation for large n in typed languages.
- **Confusing this with exact-match binary search:** This is a **boundary search** — different template.
