# 3Sum Smaller

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Fix One + Two Pointers
**Link:** https://leetcode.com/problems/3sum-smaller/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of `n` integers and a `target`, find the number of index triplets `(i, j, k)` with `i < j < k` such that `nums[i] + nums[j] + nums[k] < target`.

### 2. Clarification Questions

- **Input constraints?** Array length 0 to 3500, values from -100 to 100, target from -100 to 100.
- **Edge cases?** Array with fewer than 3 elements (return 0). All elements identical.
- **Expected output?** A single integer count of valid triplets.
- **Can input be modified?** Yes — sorting is fine since we count index triplets, not specific indices.

### 3. Brute Force Approach

- **Idea:** Three nested loops, check every triplet sum against target.
- **Time:** O(n^3)
- **Space:** O(1)

### 4. Optimized Approach

- **💡 Core Insight:** Sort the array. Fix `nums[i]`, then use two pointers `lo` and `hi`. When `nums[i] + nums[lo] + nums[hi] < target`, **all pairs** `(lo, lo+1), (lo, lo+2), ..., (lo, hi)` are valid — that's `hi - lo` triplets in one step.
- **Time:** O(n^2)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^3) | O(1) | Simple triple loop |
| Optimized | O(n^2) | O(1) | Batch-count valid pairs |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort the array. Fix `nums[i]` as the smallest element.
- Two pointers `lo = i+1`, `hi = n-1`.
- If sum < target: all elements between `lo` and `hi` pair with `lo` to form valid triplets. Add `hi - lo` to count. Move `lo` right.
- If sum >= target: move `hi` left to decrease sum.

```python
def threeSumSmaller(nums: list[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    count = 0

    for i in range(n - 2):
        lo, hi = i + 1, n - 1

        while lo < hi:
            current_sum = nums[i] + nums[lo] + nums[hi]

            if current_sum < target:
                # All pairs (lo, lo+1..hi) satisfy the condition
                count += hi - lo
                lo += 1
            else:
                hi -= 1

    return count
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [-2, 0, 1, 3], target = 2`

After sort: `[-2, 0, 1, 3]`

- **i=0, nums[i]=-2**, lo=1, hi=3:
  - sum = -2+0+3 = 1 < 2. count += 3-1 = 2. Triplets: (-2,0,3), (-2,0,1). lo=2.
  - sum = -2+1+3 = 2. Not < 2. hi=2. lo=hi, stop.
- **i=1, nums[i]=0**, lo=2, hi=3:
  - sum = 0+1+3 = 4. Not < 2. hi=2. lo=hi, stop.

**Output:** `2`

### Edge Case Testing

- **Empty input:** `n < 3`, outer loop doesn't execute, returns `0`.
- **Single element:** Same — returns `0`.
- **Typical case:** `[-2,0,1,3]`, target=2 returns `2`.
- **Extreme values:** All elements are -100, target=100. Every triplet sums to -300 < 100, so count = C(n,3).

### Complexity

- **Time:** O(n^2) — O(n log n) sort + O(n) outer x O(n) two-pointer.
- **Space:** O(1) — in-place sort, constant extra variables.

### Optimization Discussion

The key insight is **batch counting**. When `nums[lo] + nums[hi] < remaining`, everything between `lo` and `hi` also works with `lo`. This avoids enumerating each valid pair individually.

### Follow-up Variations

- **3Sum (LC 15):** Find exact zero-sum triplets.
- **3Sum Closest (LC 16):** Find closest sum to target.
- **Count pairs with sum less than target:** 2-pointer variant of same idea.

### Common Traps

- **Counting one triplet at a time** instead of batch-counting `hi - lo` — leads to O(n^3) disguised as two pointers.
- **Forgetting sorting changes indices** — problem asks for count, not actual indices, so this is fine.
- **Moving the wrong pointer** — when sum < target, move `lo` right (we've counted all of lo's valid pairs); when sum >= target, move `hi` left.
