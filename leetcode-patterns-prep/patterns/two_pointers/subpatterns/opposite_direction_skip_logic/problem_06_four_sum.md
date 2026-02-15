# 4Sum

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction — Skip Logic
**Link:** https://leetcode.com/problems/4sum/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array `nums` of `n` integers and an integer `target`, find all unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that `a, b, c, d` are distinct indices and the four values sum to `target`.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 200`, `-10^9 <= nums[i] <= 10^9`, `-10^9 <= target <= 10^9`
- **Edge cases?** Fewer than 4 elements, many duplicates, large values causing overflow
- **Expected output?** List of lists — all unique quadruplets, any order
- **Can input be modified?** Yes — sorting is acceptable

### 3. Brute Force Approach

- **Idea:** Four nested loops + set-based deduplication.
- **Time:** O(n^4)
- **Space:** O(n) for dedup set

### 4. Optimized Approach

- **💡 Core Insight:** Sort the array, fix two outer elements with nested loops, then use **two pointers** for the inner pair — identical to 3Sum but with one extra layer. **Skip duplicate values** at every level (both outer loops + both inner pointers) to guarantee unique quadruplets. Add early termination checks to prune aggressively.

- **Time:** O(n^3)
- **Space:** O(1) ignoring output

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^4) | O(n) | Four nested loops |
| Optimized | O(n^3) | O(1) | Sort + 2 loops + two pointers |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort the array.
- Outer loop fixes `nums[i]`; inner loop fixes `nums[j]` where `j > i`.
- Two pointers `left = j + 1`, `right = n - 1` scan inward.
- **Skip duplicates** at all four levels after processing.
- **Early termination:** if the smallest possible sum exceeds target, break. If the largest possible sum is below target, continue to next iteration.

```python
def fourSum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 3):
        # Skip duplicate first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Early termination — smallest possible sum too large
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break

        # Skip — largest possible sum with nums[i] too small
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue

        for j in range(i + 1, n - 2):
            # Skip duplicate second element
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # Early termination for inner loop
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break

            if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                continue

            left, right = j + 1, n - 1
            remain = target - nums[i] - nums[j]

            while left < right:
                two_sum = nums[left] + nums[right]

                if two_sum < remain:
                    left += 1
                elif two_sum > remain:
                    right -= 1
                else:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
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

**Input:** `nums = [1, 0, -1, 0, -2, 2]`, `target = 0`

1. Sort: `[-2, -1, 0, 0, 1, 2]`
2. `i=0 (-2)`, `j=1 (-1)`, remain=3 → `left=2(0), right=5(2)` → sum=2 < 3 → left++ → `left=3(0), right=5(2)` → sum=2 < 3 → left++ → `left=4(1), right=5(2)` → sum=3 ✓ → **[-2,-1,1,2]**
3. `i=0 (-2)`, `j=2 (0)`, remain=2 → `left=3(0), right=5(2)` → sum=2 ✓ → **[-2,0,0,2]** → skip → `left=4(1), right=4` → done
4. `i=0 (-2)`, `j=2 (0)`, continue... → `left=4(1), right=5(2)` already passed
5. `i=0 (-2)`, `j=3 (0)`, skip (duplicate of j=2)
6. `i=1 (-1)`, `j=2 (0)`, remain=1 → `left=3(0), right=5(2)` → sum=2 > 1 → right-- → `left=3(0), right=4(1)` → sum=1 ✓ → **[-1,0,0,1]**

**Output:** `[[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]` ✓

### Edge Case Testing

- **Empty input:** Constraints guarantee `n >= 1`; if `n < 4`, outer loop doesn't execute → `[]`.
- **Single element:** Returns `[]`.
- **Typical case:** Works as shown.
- **Extreme values:** Large values near `10^9` — no overflow in Python (arbitrary precision).

### Complexity

- **Time:** O(n^3) — two nested loops O(n^2) x inner two-pointer O(n); early termination helps in practice
- **Space:** O(1) — ignoring output and sort overhead

### Optimization Discussion

The early termination pruning (checking min/max possible sums) dramatically reduces real-world runtime. Without them, worst case is still O(n^3), but with pruning many branches are cut early. For `n = 200`, the worst case is ~8M operations — perfectly fine.

### Follow-up Variations

- **3Sum (LC 15):** Same pattern with one fewer loop.
- **4Sum II (LC 454):** Four separate arrays — use hash map approach instead (O(n^2) time, O(n^2) space).
- **kSum generalization:** Recursively reduce k-sum to 2-sum with two pointers at the base.

### ⚠️ Common Traps

- **Integer overflow** — in languages like Java/C++, summing four values near 10^9 overflows `int`. Use `long`.
- **Skipping duplicates at the wrong time** — skip *after* finding a match, not before. The skip condition for `j` is `j > i + 1` (not `j > 0`).
- **Missing early termination** — without pruning, solutions may TLE on edge cases with n=200.
- **Forgetting any of the four duplicate-skip levels** — all four (i, j, left, right) must be handled.
