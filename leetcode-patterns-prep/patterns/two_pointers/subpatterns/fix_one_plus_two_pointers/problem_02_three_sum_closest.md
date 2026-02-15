# 3Sum Closest

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Fix One + Two Pointers
**Link:** https://leetcode.com/problems/3sum-closest/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums` and an integer `target`, find three integers in `nums` such that their sum is closest to `target`. Return the sum. Exactly one solution is guaranteed.

### 2. Clarification Questions

- **Input constraints?** Array length 3 to 500, values from -1000 to 1000, target from -10^4 to 10^4.
- **Edge cases?** Array of exactly 3 elements (only one triplet possible). Exact match exists.
- **Expected output?** A single integer — the closest sum.
- **Can input be modified?** Yes — sorting is fine.

### 3. Brute Force Approach

- **Idea:** Try all O(n^3) triplets, track the one with the smallest absolute difference to target.
- **Time:** O(n^3)
- **Space:** O(1)

### 4. Optimized Approach

- **💡 Core Insight:** Sort the array. Fix one element, use two pointers on the rest. Track the closest sum seen so far. Move pointers based on whether the current sum is less than or greater than target.
- **Time:** O(n^2)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^3) | O(1) | Simple but slow |
| Optimized | O(n^2) | O(1) | Sort + fix one + two pointers |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort the array for two-pointer technique.
- Fix `nums[i]`. Use `lo = i+1`, `hi = n-1`.
- Compute sum. If it equals target, return immediately (can't do better).
- Otherwise update closest if current difference is smaller, then adjust pointers.

```python
def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    closest = float('inf')  # tracks closest sum

    for i in range(n - 2):
        # Skip duplicate fixed element (optional optimization)
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        lo, hi = i + 1, n - 1

        while lo < hi:
            current_sum = nums[i] + nums[lo] + nums[hi]

            # Exact match — impossible to be closer
            if current_sum == target:
                return target

            # Update closest if this sum is nearer
            if abs(current_sum - target) < abs(closest - target):
                closest = current_sum

            # Move pointers toward target
            if current_sum < target:
                lo += 1
            else:
                hi -= 1

    return closest
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [-1, 2, 1, -4], target = 1`

After sort: `[-4, -1, 1, 2]`

- **i=0, nums[i]=-4**, lo=1, hi=3:
  - sum = -4 + (-1) + 2 = -3. diff=|−3−1|=4. closest=-3. sum < target, lo++.
  - sum = -4 + 1 + 2 = -1. diff=|−1−1|=2. closest=-1. sum < target, lo++. lo=hi, stop.
- **i=1, nums[i]=-1**, lo=2, hi=3:
  - sum = -1 + 1 + 2 = 2. diff=|2−1|=1. closest=2. sum > target, hi--. lo=hi, stop.
- **i=2**: only two elements remain, loop ends.

**Output:** `2` (closest to target 1)

### Edge Case Testing

- **Empty input:** Not possible (n >= 3).
- **Single element:** Not possible.
- **Typical case:** `[-1,2,1,-4]`, target=1 returns `2`.
- **Extreme values:** Exact match found — returns target immediately.

### Complexity

- **Time:** O(n^2) — O(n log n) sort + O(n) outer loop x O(n) two-pointer scan.
- **Space:** O(1) — in-place sort, constant extra variables.

### Optimization Discussion

Skipping duplicate fixed elements is optional here (doesn't affect correctness, minor speedup). Early return on exact match is a valuable optimization.

### Follow-up Variations

- **3Sum (LC 15):** Find exact zero-sum triplets with deduplication.
- **3Sum Smaller (LC 259):** Count triplets below a threshold.
- **What if multiple closest sums exist?** Problem guarantees unique answer.

### Common Traps

- **Initializing closest to 0** instead of infinity — could accidentally match target.
- **Forgetting early return on exact match** — works without it but misses optimization.
- **Using `min()` on absolute differences but returning the difference** instead of the actual sum.
