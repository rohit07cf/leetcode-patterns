# 3Sum

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction — Skip Logic
**Link:** https://leetcode.com/problems/3sum/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums`, find all unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j != k` and `nums[i] + nums[j] + nums[k] == 0`. The solution set must not contain duplicate triplets.

### 2. Clarification Questions

- **Input constraints?** `3 <= nums.length <= 3000`, `-10^5 <= nums[i] <= 10^5`
- **Edge cases?** All zeros, all positives, all negatives, many duplicates
- **Expected output?** List of lists of three integers; order doesn't matter
- **Can input be modified?** Yes — sorting is acceptable

### 3. Brute Force Approach

- **Idea:** Three nested loops checking every triplet, use a set to deduplicate.
- **Time:** O(n^3)
- **Space:** O(n) for the dedup set

### 4. Optimized Approach

- **💡 Core Insight:** Sort the array, fix one element, then use **two pointers** moving inward to find pairs that sum to the negative of the fixed element. **Skip duplicates** at every level — the fixed element, the left pointer, and the right pointer — to avoid repeated triplets.

- **Time:** O(n^2)
- **Space:** O(1) ignoring output (O(n) for sort in some languages)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^3) | O(n) | Set-based dedup is messy |
| Optimized | O(n^2) | O(1) | Sort + two pointers + skip logic |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort to enable two-pointer technique and duplicate skipping.
- Outer loop fixes one number; skip if it's the same as previous.
- Inner two pointers scan inward; skip duplicates after finding a valid triplet.
- Early exit: if `nums[i] > 0`, no triplet can sum to zero.

```python
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicate fixed element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Early exit — smallest remaining value is positive
        if nums[i] > 0:
            break

        left, right = i + 1, n - 1
        target = -nums[i]

        while left < right:
            two_sum = nums[left] + nums[right]

            if two_sum < target:
                left += 1
            elif two_sum > target:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # Skip duplicate left values
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # Skip duplicate right values
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [-1, 0, 1, 2, -1, -4]`

1. Sort: `[-4, -1, -1, 0, 1, 2]`
2. `i=0`, `nums[i]=-4`, target=4 → no pair sums to 4 → nothing found
3. `i=1`, `nums[i]=-1`, target=1 → `left=2(-1)`, `right=5(2)` → sum=1 ✓ → `[-1,-1,2]`
   - Skip left duplicates, now `left=3(0)`, `right=4(1)` → sum=1 ✓ → `[-1,0,1]`
4. `i=2`, `nums[i]=-1`, **skip** (duplicate of `i=1`)
5. `i=3`, `nums[i]=0` → no valid pair

**Output:** `[[-1,-1,2], [-1,0,1]]` ✓

### Edge Case Testing

- **Empty input:** Constraints guarantee `n >= 3`, but returning `[]` is safe.
- **Single element:** N/A per constraints.
- **Typical case:** Mixed positives/negatives — works as shown.
- **Extreme values:** All zeros `[0,0,0]` → `[[0,0,0]]`; all same nonzero → `[]`.

### Complexity

- **Time:** O(n^2) — outer loop O(n) x inner two-pointer scan O(n)
- **Space:** O(1) — ignoring output and sort overhead

### Optimization Discussion

The sort dominates at O(n log n) but is dwarfed by the O(n^2) main loop. A hash-map approach can also achieve O(n^2) but duplicate handling is much trickier and error-prone in interviews.

### Follow-up Variations

- **3Sum Closest (LC 16):** Instead of exact zero, find triplet closest to a target.
- **3Sum Smaller (LC 259):** Count triplets with sum less than target.
- **4Sum (LC 18):** Extend to four elements — same skip logic, one more layer.

### ⚠️ Common Traps

- **Forgetting to skip duplicates at all three levels** — the outer loop AND both inner pointers need skip logic.
- **Skipping before recording** — the duplicate skip must happen *after* appending a valid result, not before.
- **Off-by-one in skip comparisons** — left compares with `left - 1`, right compares with `right + 1`.
- **Not sorting first** — the entire approach relies on sorted order.
