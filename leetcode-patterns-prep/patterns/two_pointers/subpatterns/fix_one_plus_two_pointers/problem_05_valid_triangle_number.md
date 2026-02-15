# Valid Triangle Number

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Fix One + Two Pointers
**Link:** https://leetcode.com/problems/valid-triangle-number/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums`, return the number of triplets that can form a valid triangle. Three sides form a triangle if the sum of any two sides is greater than the third. Since the array is non-negative and sorted, we only need to check `a + b > c` where `a <= b <= c`.

### 2. Clarification Questions

- **Input constraints?** Array length 1 to 1000, values 0 to 1000.
- **Edge cases?** Zeros in the array (can't form triangles). All identical positive values. Fewer than 3 elements.
- **Expected output?** A single integer count of valid triplets.
- **Can input be modified?** Yes — sorting is fine since we only need the count.

### 3. Brute Force Approach

- **Idea:** Three nested loops, check triangle inequality for each triplet.
- **Time:** O(n^3)
- **Space:** O(1)

### 4. Optimized Approach

- **💡 Core Insight:** Sort the array. Fix the **largest** side `nums[k]` (iterate from right). Use two pointers `lo` and `hi` on `[0, k-1]`. If `nums[lo] + nums[hi] > nums[k]`, then all pairs `(lo, hi), (lo+1, hi), ..., (hi-1, hi)` are valid — that's `hi - lo` triplets. This is a **batch counting** technique.
- **Time:** O(n^2)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^3) | O(1) | Check every triplet |
| Optimized | O(n^2) | O(1) | Fix largest side, batch count |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort the array. Fix the largest side `nums[k]` from right to left.
- Two pointers: `lo = 0`, `hi = k - 1`.
- If `nums[lo] + nums[hi] > nums[k]`: every element from `lo` to `hi-1` also pairs with `hi` to satisfy the condition. Count `hi - lo`, move `hi` left.
- Otherwise: `lo` is too small, move `lo` right.

```python
def triangleNumber(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    count = 0

    # Fix the largest side and work backwards
    for k in range(n - 1, 1, -1):
        lo, hi = 0, k - 1

        while lo < hi:
            if nums[lo] + nums[hi] > nums[k]:
                # All indices from lo to hi-1 paired with hi are valid
                count += hi - lo
                hi -= 1
            else:
                lo += 1

    return count
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [2, 2, 3, 4]`

After sort: `[2, 2, 3, 4]`

- **k=3, nums[k]=4**, lo=0, hi=2:
  - nums[0]+nums[2] = 2+3 = 5 > 4. count += 2-0 = 2. Triplets: (2,3,4) and (2,3,4). hi=1.
  - nums[0]+nums[1] = 2+2 = 4. Not > 4. lo=1. lo=hi, stop.
- **k=2, nums[k]=3**, lo=0, hi=1:
  - nums[0]+nums[1] = 2+2 = 4 > 3. count += 1-0 = 1. Triplet: (2,2,3). hi=0. Stop.

**Output:** `3`

### Edge Case Testing

- **Empty input:** `n < 3`, outer loop doesn't run, returns `0`.
- **Single element:** Returns `0`.
- **Typical case:** `[2,2,3,4]` returns `3`.
- **Extreme values:** Array with zeros: `[0,0,1,2]`. No triplet with zero sides works since 0+0 is not > anything positive.

### Complexity

- **Time:** O(n^2) — O(n log n) sort + O(n) outer loop x O(n) two-pointer scan.
- **Space:** O(1) — in-place sort, constant extra space.

### Optimization Discussion

**Fixing the largest side** (not the smallest) is key. It lets us use the batch counting trick: when `a + b > c`, all values between `a` and `b` also work with `b`. Fixing the smallest side doesn't enable this optimization as cleanly.

### Follow-up Variations

- **3Sum Smaller (LC 259):** Same batch-counting pattern, different condition.
- **Largest Perimeter Triangle (LC 976):** Find max perimeter, sort and check adjacent triples.
- **Count triangles with perimeter in range:** Combine with binary search.

### Common Traps

- **Fixing the smallest side** instead of the largest — makes batch counting harder.
- **Using strict inequality wrong** — triangle inequality requires `a + b > c`, not `>=`.
- **Forgetting zeros** — `0 + 0 > 0` is false, so zeros never form valid triangle sides.
- **Counting direction confusion** — when sum > c, we count `hi - lo` and decrement `hi`, not `lo`.
