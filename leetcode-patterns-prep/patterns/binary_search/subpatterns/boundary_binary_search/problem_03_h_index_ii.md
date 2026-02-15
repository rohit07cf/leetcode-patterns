# H-Index II

**Difficulty:** Medium
**Pattern:** Binary Search
**Subpattern:** Boundary Binary Search
**Link:** https://leetcode.com/problems/h-index-ii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of citations **sorted in ascending order**, find the researcher's h-index. The h-index is the maximum value `h` such that the researcher has at least `h` papers with at least `h` citations each. Must run in **O(log n)** time.

### 2. Clarification Questions

- **Input constraints?** `1 <= n <= 10^5`. Array is sorted ascending. `0 <= citations[i] <= 1000`.
- **Edge cases?** All zeros (h=0). Single paper. All citations are the same.
- **Expected output?** A single integer — the h-index.
- **Can input be modified?** Yes, but no need.

### 3. Brute Force Approach

- **Idea:** For each possible h from n down to 0, check if there are at least h papers with >= h citations. The first valid h is the answer.
- **Time:** O(n)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** Since the array is sorted, `n - mid` papers have citations `>= citations[mid]`. We need the **leftmost index** where `citations[mid] >= n - mid`. At that boundary, `h = n - mid`.
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n) | O(1) | Linear scan from right |
| Optimized | O(log n) | O(1) | Boundary binary search |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- We search for the **leftmost index** where `citations[mid] >= n - mid`.
- At that index, there are `n - mid` papers with at least `citations[mid]` citations, and since `citations[mid] >= n - mid`, h = `n - mid`.
- If no such index exists, h = 0.

```python
def hIndex(citations):
    n = len(citations)
    lo, hi = 0, n - 1
    result = n  # if no valid index found, h = n - result = 0

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if citations[mid] >= n - mid:
            result = mid  # candidate: h = n - mid, keep searching left for larger h
            hi = mid - 1
        else:
            lo = mid + 1  # not enough citations, search right

    return n - result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `citations = [0, 1, 3, 5, 6]`, `n = 5`

- `lo=0, hi=4` -> `mid=2`, `citations[2]=3 >= 5-2=3` -> `result=2`, `hi=1`
- `lo=0, hi=1` -> `mid=0`, `citations[0]=0 >= 5-0=5`? No -> `lo=1`
- `lo=1, hi=1` -> `mid=1`, `citations[1]=1 >= 5-1=4`? No -> `lo=2`
- Exit. **h = 5 - 2 = 3**

**Verification:** Papers with >= 3 citations: `[3, 5, 6]` — exactly 3 papers.

### Edge Case Testing

- **Empty input:** Not possible per constraints (n >= 1).
- **Single element:** `[0]` -> `citations[0]=0 >= 1`? No -> `result=1`, h = 1-1 = 0. `[100]` -> `result=0`, h = 1.
- **All zeros:** `[0,0,0]` -> no index satisfies condition, h = 0.
- **Extreme values:** `[100,100,100]` -> `result=0`, h = 3.

### Complexity

- **Time:** O(log n) — single binary search.
- **Space:** O(1) — constant extra space.

### Optimization Discussion

This is optimal for the sorted input constraint. For the unsorted variant (LC 274), sorting first gives O(n log n), or counting sort gives O(n).

### Follow-up Variations

- **H-Index I (LC 274):** Unsorted array — use counting sort for O(n).
- What if citations can be updated dynamically? Use a balanced BST or BIT.
- Find the h-index for multiple researchers and rank them.

### Common Traps

- **Getting the boundary condition wrong** — the key relationship is `citations[mid] >= n - mid`, not `citations[mid] >= mid`.
- **Confusing what `n - mid` represents** — it's the number of papers from index `mid` to the end (inclusive).
- **Returning `mid` instead of `n - mid`** — the h-index is the count of qualifying papers, not the index itself.
