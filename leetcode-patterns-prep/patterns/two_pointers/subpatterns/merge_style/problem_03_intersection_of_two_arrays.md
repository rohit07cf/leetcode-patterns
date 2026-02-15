# Intersection of Two Arrays

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Merge Style
**Link:** https://leetcode.com/problems/intersection-of-two-arrays/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given two integer arrays, return an array of their **unique** common elements. Each element in the result must be unique, and the order doesn't matter.

### 2. Clarification Questions
- Input constraints? `1 <= nums1.length, nums2.length <= 1000`, values in `[0, 1000]`
- Edge cases? No overlap at all; one array is a subset of the other; duplicates within a single array
- Expected output? Array of unique intersection elements (any order)
- Can input be modified? Yes — sorting is acceptable

### 3. Brute Force Approach
- **Idea:** Use two sets. `set(nums1) & set(nums2)` gives the intersection.
- **Time:** O(m + n)
- **Space:** O(m + n) for the sets

### 4. Optimized Approach
- **Core Insight:** Sort both arrays, then use **two pointers** to walk them in tandem. Skip duplicates as you go. When values match, record the element and advance both pointers. When they differ, advance the pointer with the smaller value.
- **Time:** O(m log m + n log n)
- **Space:** O(1) extra (excluding output) — useful when you can't use hash sets (e.g., limited memory)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Set intersection | O(m + n) | O(m + n) | Fastest, uses extra space |
| Sort + Two Pointers | O(m log m + n log n) | O(1) extra | Better space, good if data is already sorted |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort both arrays.
- Use two pointers `i` and `j` starting at 0.
- When values match and it's not a duplicate of the last recorded result, add to output.
- When they differ, advance the smaller pointer.

```python
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1.sort()
    nums2.sort()
    result = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        # Skip duplicates in nums1
        if i > 0 and nums1[i] == nums1[i - 1]:
            i += 1
            continue
        # Skip duplicates in nums2
        if j > 0 and nums2[j] == nums2[j - 1]:
            j += 1
            continue

        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1  # nums1 value too small, advance it
        else:
            j += 1  # nums2 value too small, advance it

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums1 = [4,9,5]`, `nums2 = [9,4,9,8,4]`

After sorting: `nums1 = [4,5,9]`, `nums2 = [4,4,8,9,9]`

| Step | i | j | nums1[i] | nums2[j] | Action |
|------|---|---|----------|----------|--------|
| 1 | 0 | 0 | 4 | 4 | Match → result=[4], i=1, j=1 |
| 2 | 1 | 1 | 5 | 4 | Skip dup nums2[1]==nums2[0] → j=2 |
| 3 | 1 | 2 | 5 | 8 | 5 < 8 → i=2 |
| 4 | 2 | 2 | 9 | 8 | 9 > 8 → j=3 |
| 5 | 2 | 3 | 9 | 9 | Match → result=[4,9], i=3, j=4 |
| 6 | 3 | — | — | — | i out of bounds, done |

Result: `[4, 9]`

### Edge Case Testing
- **Empty input:** Not possible per constraints (min length 1), but would return `[]`
- **Single element:** `[1]` and `[1]` → `[1]`; `[1]` and `[2]` → `[]`
- **Typical case:** As shown above
- **Extreme values:** All elements identical in both → single element in result

### Complexity
- **Time:** O(m log m + n log n) — dominated by sorting
- **Space:** O(1) extra — pointers only (output array not counted)

### Optimization Discussion

If arrays are **already sorted**, this becomes O(m + n) which beats the set approach in space. In interviews, mention both approaches and let the interviewer choose based on constraints.

### Follow-up Variations
- Intersection of Two Arrays II (LeetCode 350) — keep duplicates, count matters
- What if arrays are sorted? → Pure O(m+n) two-pointer scan
- What if `nums2` is stored on disk and memory is limited? → Sort + two-pointer is ideal

### Common Traps
- Forgetting to skip duplicates (returning `[4, 4]` instead of `[4]`)
- Not sorting before applying two pointers
- Advancing only one pointer on a match instead of both
