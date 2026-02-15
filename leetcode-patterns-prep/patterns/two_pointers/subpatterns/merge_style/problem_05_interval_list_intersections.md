# Interval List Intersections

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Merge Style
**Link:** https://leetcode.com/problems/interval-list-intersections/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given two lists of **sorted, disjoint** intervals, return the list of intervals representing their intersection. Each interval is `[start, end]`.

### 2. Clarification Questions
- Input constraints? `0 <= len(A), len(B) <= 1000`, intervals sorted by start, no overlaps within a list
- Edge cases? One list empty; no overlap at all; one interval spans many in the other list
- Expected output? List of `[start, end]` intervals representing all overlapping regions
- Can input be modified? Yes, but we don't need to — read-only traversal

### 3. Brute Force Approach
- **Idea:** For every interval in A, check every interval in B for overlap. Collect intersections.
- **Time:** O(m * n)
- **Space:** O(1) extra

### 4. Optimized Approach
- **Core Insight:** Both lists are sorted. Use **two pointers**, one per list. At each step, check if the two current intervals overlap. If they do, the intersection is `[max(starts), min(ends)]`. Then **advance the pointer whose interval ends first** — it can't overlap with anything further in the other list.
- **Time:** O(m + n)
- **Space:** O(1) extra

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(m * n) | O(1) | Check all pairs |
| Optimized | O(m + n) | O(1) | Sorted order lets us advance smartly |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use pointer `i` for list A, pointer `j` for list B.
- At each step, compute the potential overlap: `lo = max(A[i][0], B[j][0])`, `hi = min(A[i][1], B[j][1])`.
- If `lo <= hi`, it's a valid intersection — record it.
- Advance whichever pointer has the **earlier endpoint**.

```python
def intervalIntersection(
    firstList: list[list[int]],
    secondList: list[list[int]]
) -> list[list[int]]:
    result = []
    i, j = 0, 0

    while i < len(firstList) and j < len(secondList):
        # Compute the overlap window
        lo = max(firstList[i][0], secondList[j][0])
        hi = min(firstList[i][1], secondList[j][1])

        if lo <= hi:
            result.append([lo, hi])  # valid intersection

        # Advance the interval that ends first —
        # it can't intersect anything else in the other list
        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`A = [[0,2],[5,10],[13,23],[24,25]]`
`B = [[1,5],[8,12],[15,24],[25,26]]`

| Step | i | j | A[i] | B[j] | lo,hi | Overlap? | Advance |
|------|---|---|------|------|-------|----------|---------|
| 1 | 0 | 0 | [0,2] | [1,5] | 1,2 | Yes → [1,2] | i (2<5) |
| 2 | 1 | 0 | [5,10] | [1,5] | 5,5 | Yes → [5,5] | j (5<10) |
| 3 | 1 | 1 | [5,10] | [8,12] | 8,10 | Yes → [8,10] | i (10<12) |
| 4 | 2 | 1 | [13,23] | [8,12] | 13,12 | No | j (12<23) |
| 5 | 2 | 2 | [13,23] | [15,24] | 15,23 | Yes → [15,23] | i (23<24) |
| 6 | 3 | 2 | [24,25] | [15,24] | 24,24 | Yes → [24,24] | j (24<25) |
| 7 | 3 | 3 | [24,25] | [25,26] | 25,25 | Yes → [25,25] | i (25<26) |

Result: `[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]`

### Edge Case Testing
- **Empty input:** One or both lists empty → return `[]` (while loop never executes)
- **Single element:** `[[0,0]]` and `[[0,0]]` → `[[0,0]]` (point intersection)
- **Typical case:** As shown above
- **Extreme values:** Completely non-overlapping lists → return `[]`

### Complexity
- **Time:** O(m + n) — each pointer advances at most m or n times
- **Space:** O(1) extra — only pointers and variables (output not counted)

### Optimization Discussion

Already optimal for two sorted interval lists. The `max/min` trick for computing intersections is a **universal pattern** for interval overlap problems.

### Follow-up Variations
- Merge Intervals (LeetCode 56) — merge overlapping intervals in a single list
- Insert Interval (LeetCode 57) — insert and merge a new interval
- Employee Free Time (LeetCode 759) — find common free slots across schedules

### Common Traps
- Using `<` instead of `<=` in the overlap check — `[5,5]` is a valid single-point interval
- Advancing the wrong pointer (must advance the one with the smaller **end**)
- Forgetting that both lists are already sorted and disjoint (no need to sort/merge within a list)
