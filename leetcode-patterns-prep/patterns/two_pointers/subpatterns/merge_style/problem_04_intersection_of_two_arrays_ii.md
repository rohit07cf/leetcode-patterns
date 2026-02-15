# Intersection of Two Arrays II

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Merge Style
**Link:** https://leetcode.com/problems/intersection-of-two-arrays-ii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given two integer arrays, return an array of their intersection where **each element appears as many times as it shows in both arrays**. The order of the result doesn't matter.

### 2. Clarification Questions
- Input constraints? `1 <= nums1.length, nums2.length <= 1000`, values in `[0, 1000]`
- Edge cases? No overlap; one array is a subset; heavy duplicates
- Expected output? Array with duplicate-aware intersection
- Can input be modified? Yes — sorting is fine

### 3. Brute Force Approach
- **Idea:** Use a hash map to count elements in `nums1`, then iterate `nums2` and decrement counts.
- **Time:** O(m + n)
- **Space:** O(min(m, n)) for the counter

### 4. Optimized Approach
- **Core Insight:** Sort both arrays, then use **two pointers**. When elements match, add to result and advance both. When they differ, advance the smaller. Unlike problem 349, **don't skip duplicates** — each match consumes one copy from each side.
- **Time:** O(m log m + n log n)
- **Space:** O(1) extra — ideal when memory is constrained

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Hash Map | O(m + n) | O(min(m,n)) | Faster, uses extra space |
| Sort + Two Pointers | O(m log m + n log n) | O(1) extra | Better space, great for follow-ups |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort both arrays.
- Walk with two pointers; on match, record and advance both.
- On mismatch, advance the pointer pointing to the smaller value.

```python
def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1.sort()
    nums2.sort()
    result = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])  # keep every match (duplicates allowed)
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1  # nums1 value is smaller, advance it
        else:
            j += 1  # nums2 value is smaller, advance it

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums1 = [1,2,2,1]`, `nums2 = [2,2]`

After sorting: `nums1 = [1,1,2,2]`, `nums2 = [2,2]`

| Step | i | j | nums1[i] | nums2[j] | Action |
|------|---|---|----------|----------|--------|
| 1 | 0 | 0 | 1 | 2 | 1 < 2 → i=1 |
| 2 | 1 | 0 | 1 | 2 | 1 < 2 → i=2 |
| 3 | 2 | 0 | 2 | 2 | Match → result=[2], i=3, j=1 |
| 4 | 3 | 1 | 2 | 2 | Match → result=[2,2], i=4, j=2 |
| 5 | — | — | — | — | i out of bounds, done |

Result: `[2, 2]`

### Edge Case Testing
- **Empty input:** Not possible per constraints, but would return `[]`
- **Single element:** `[1]` and `[1]` → `[1]`; `[1]` and `[2]` → `[]`
- **Typical case:** As shown above
- **Extreme values:** All same value, e.g., `[2,2,2]` and `[2,2]` → `[2,2]`

### Complexity
- **Time:** O(m log m + n log n) — sorting dominates
- **Space:** O(1) extra — only pointers (output not counted)

### Optimization Discussion

If arrays are **already sorted**, this becomes O(m + n). The hash map approach is faster in general but uses more space. The two-pointer approach shines in the **follow-up scenarios**.

### Follow-up Variations
- **What if arrays are already sorted?** → Skip sorting, pure O(m+n)
- **What if `nums1` is small and `nums2` is huge?** → Hash map on `nums1`, iterate `nums2`
- **What if `nums2` is on disk?** → Sort both externally, stream merge with two pointers
- Intersection of Two Arrays (LeetCode 349) — unique elements only

### Common Traps
- Accidentally skipping duplicates (that's problem 349, not this one)
- Using a set instead of a counter/sorted merge
- Not advancing **both** pointers on a match
