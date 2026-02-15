# 3Sum

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Fix One + Two Pointers
**Link:** https://leetcode.com/problems/3sum/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums`, find all unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j != k` and `nums[i] + nums[j] + nums[k] == 0`. The solution set must not contain duplicate triplets.

### 2. Clarification Questions

- **Input constraints?** Array length 3 to 3000, values from -10^5 to 10^5.
- **Edge cases?** All zeros, all positives (no solution), all negatives (no solution), duplicates in array.
- **Expected output?** List of lists of three integers. Order of triplets doesn't matter.
- **Can input be modified?** Yes — sorting is allowed and expected.

### 3. Brute Force Approach

- **Idea:** Three nested loops trying every combination of `(i, j, k)`. Use a set to deduplicate triplets.
- **Time:** O(n^3)
- **Space:** O(n) for the deduplication set

### 4. Optimized Approach

- **💡 Core Insight:** Sort the array. Fix one element (`nums[i]`), then use two pointers on the remaining subarray to find pairs that sum to `-nums[i]`. Skip duplicates at each level to avoid repeated triplets.
- **Time:** O(n^2)
- **Space:** O(1) extra (ignoring output)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^3) | O(n) | TLE on large inputs |
| Optimized | O(n^2) | O(1) | Sort + fix one + two pointers |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort the array so two pointers can work and duplicates are adjacent.
- Fix `nums[i]` as the first element. Skip if `nums[i] > 0` (no way to sum to zero).
- Skip duplicate values of `i` to avoid repeated triplets.
- Use `lo` and `hi` pointers on `[i+1, n-1]`. Move inward based on sum comparison.
- After finding a valid triplet, skip duplicates for both `lo` and `hi`.

```python
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
        # Early termination — smallest element is positive
        if nums[i] > 0:
            break

        # Skip duplicate fixed element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        lo, hi = i + 1, n - 1

        while lo < hi:
            two_sum = nums[lo] + nums[hi]

            if two_sum < target:
                lo += 1
            elif two_sum > target:
                hi -= 1
            else:
                result.append([nums[i], nums[lo], nums[hi]])
                # Skip duplicates for both pointers
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

**Input:** `nums = [-1, 0, 1, 2, -1, -4]`

After sort: `[-4, -1, -1, 0, 1, 2]`

- **i=0, nums[i]=-4**, target=4, lo=1, hi=5: max pair sum = -1+2 = 1 < 4. No match.
- **i=1, nums[i]=-1**, target=1, lo=2, hi=5:
  - `nums[2]+nums[5]` = -1+2 = 1. Match! Append `[-1,-1,2]`. Skip dups. lo=3, hi=4.
  - `nums[3]+nums[4]` = 0+1 = 1. Match! Append `[-1,0,1]`. lo=4, hi=3. Stop.
- **i=2, nums[i]=-1**: duplicate of i=1, skip.
- **i=3, nums[i]=0**, target=0, lo=4, hi=5: 1+2 = 3 > 0. hi=4. lo not < hi. Stop.

**Output:** `[[-1,-1,2], [-1,0,1]]`

### Edge Case Testing

- **Empty input:** Not possible per constraints (n >= 3).
- **Single element:** Not possible per constraints.
- **Typical case:** `[-1,0,1,2,-1,-4]` returns `[[-1,-1,2],[-1,0,1]]`.
- **Extreme values:** `[0,0,0]` returns `[[0,0,0]]`. All positives returns `[]`.

### Complexity

- **Time:** O(n^2) — O(n log n) sort + O(n) outer loop x O(n) two-pointer scan.
- **Space:** O(1) extra — sorting is in-place, ignoring output storage.

### Optimization Discussion

The O(n^2) approach is optimal for this problem. A hash-set approach also achieves O(n^2) but handling duplicates is trickier and uses O(n) space.

### Follow-up Variations

- **3Sum Closest (LC 16):** Return the sum closest to a target instead of exactly zero.
- **3Sum Smaller (LC 259):** Count triplets with sum less than target.
- **4Sum (LC 18):** Extend to four elements with an extra loop layer.

### Common Traps

- **Forgetting to skip duplicates** at the fixed element level — leads to duplicate triplets.
- **Skipping duplicates incorrectly** — must skip *after* recording a valid triplet, not before.
- **Not sorting first** — two-pointer technique requires a sorted array.
- **Off-by-one in early termination** — `nums[i] > 0` is correct (not `>=` since three zeros sum to zero).
