# 4Sum

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Fix One + Two Pointers
**Link:** https://leetcode.com/problems/4sum/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums` and an integer `target`, find all unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that all indices are distinct and the four values sum to `target`. No duplicate quadruplets allowed.

### 2. Clarification Questions

- **Input constraints?** Array length 1 to 200, values from -10^9 to 10^9, target from -10^9 to 10^9.
- **Edge cases?** Fewer than 4 elements (return []). Large values causing overflow (use Python, no issue). Many duplicates.
- **Expected output?** List of lists of four integers.
- **Can input be modified?** Yes — sorting is expected.

### 3. Brute Force Approach

- **Idea:** Four nested loops over all combinations, use a set to deduplicate.
- **Time:** O(n^4)
- **Space:** O(n) for deduplication

### 4. Optimized Approach

- **💡 Core Insight:** Sort the array. Fix **two** elements with nested loops (`i`, `j`), then use two pointers on the remaining range. Skip duplicates at all four levels. This generalizes the 3Sum pattern by adding one more fixed layer.
- **Time:** O(n^3)
- **Space:** O(1) extra

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^4) | O(n) | Impractical |
| Optimized | O(n^3) | O(1) | Fix two + two pointers |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort array. Two outer loops fix `nums[i]` and `nums[j]`.
- Skip duplicates at both outer loop levels.
- Two pointers `lo = j+1`, `hi = n-1` find the remaining pair.
- Early termination: if min possible sum > target or max possible sum < target, prune.

```python
def fourSum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 3):
        # Skip duplicate first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Early termination — min sum too large
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break

        # Skip — max sum with nums[i] too small
        if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
            continue

        for j in range(i + 1, n - 2):
            # Skip duplicate second element
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # Early termination for inner loop
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break

            if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                continue

            lo, hi = j + 1, n - 1
            remaining = target - nums[i] - nums[j]

            while lo < hi:
                two_sum = nums[lo] + nums[hi]

                if two_sum < remaining:
                    lo += 1
                elif two_sum > remaining:
                    hi -= 1
                else:
                    result.append([nums[i], nums[j], nums[lo], nums[hi]])
                    # Skip duplicates
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [1, 0, -1, 0, -2, 2], target = 0`

After sort: `[-2, -1, 0, 0, 1, 2]`

- **i=0 (-2), j=1 (-1)**, remaining=3, lo=2, hi=5:
  - 0+2=2 < 3, lo++. 0+2=2 < 3, lo++. 1+2=3 == 3. Append `[-2,-1,1,2]`. lo=5, hi=4. Stop.
- **i=0 (-2), j=2 (0)**, remaining=2, lo=3, hi=5:
  - 0+2=2 == 2. Append `[-2,0,0,2]`. Skip dups. lo=4, hi=4. Stop.
- **i=0 (-2), j=3 (0)**: duplicate j, skip.
- **i=1 (-1), j=2 (0)**, remaining=1, lo=3, hi=5:
  - 0+2=2 > 1, hi--. 0+1=1 == 1. Append `[-1,0,0,1]`. Stop.

**Output:** `[[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]`

### Edge Case Testing

- **Empty input:** `n < 4`, loops don't execute, returns `[]`.
- **Single element:** Returns `[]`.
- **Typical case:** `[1,0,-1,0,-2,2]`, target=0 returns 3 quadruplets.
- **Extreme values:** Large values won't overflow in Python. `[10^9, 10^9, 10^9, 10^9]`, target=4*10^9 works fine.

### Complexity

- **Time:** O(n^3) — two nested loops O(n^2) x two-pointer O(n). Pruning helps in practice.
- **Space:** O(1) extra — in-place sort, constant variables.

### Optimization Discussion

The **early termination** checks (min/max sum pruning) dramatically reduce runtime in practice. Without them, worst case is still O(n^3) but average case improves significantly.

### Follow-up Variations

- **kSum generalization:** Recursive approach fixing one element and reducing to (k-1)Sum.
- **4Sum II (LC 454):** Four separate arrays — use hash map approach instead.
- **Count quadruplets with sum equal to target:** Same structure, count instead of collect.

### Common Traps

- **Integer overflow** in other languages (C++/Java) — sum of four 10^9 values exceeds 32-bit int.
- **Duplicate skipping at wrong level** — must handle duplicates for `i`, `j`, `lo`, and `hi` independently.
- **Missing early termination** — correct but slow; pruning is critical for interview performance.
- **Off-by-one in duplicate skip condition** — `j > i + 1` not `j > 0`.
