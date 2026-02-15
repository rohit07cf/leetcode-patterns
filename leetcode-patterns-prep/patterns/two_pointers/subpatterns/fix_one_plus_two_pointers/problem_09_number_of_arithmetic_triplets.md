# Number of Arithmetic Triplets

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Fix One + Two Pointers
**Link:** https://leetcode.com/problems/number-of-arithmetic-triplets/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a **strictly increasing** array `nums` and a positive integer `diff`, count the number of triplets `(i, j, k)` with `i < j < k` such that `nums[j] - nums[i] == diff` and `nums[k] - nums[j] == diff`.

### 2. Clarification Questions

- **Input constraints?** Array length 3 to 200, values 1 to 200, diff 1 to 50. Array is strictly increasing.
- **Edge cases?** No valid triplets (return 0). Every consecutive triple is arithmetic. Minimum array size of 3.
- **Expected output?** Single integer count.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach

- **Idea:** Three nested loops, check both difference conditions.
- **Time:** O(n^3)
- **Space:** O(1)

### 4. Optimized Approach

- **💡 Core Insight:** Fix the middle element `nums[j]`. Check if both `nums[j] - diff` and `nums[j] + diff` exist in the array. Since the array is strictly increasing, use a **hash set** for O(1) lookups. Alternatively, use **three pointers** moving forward together.
- **Time:** O(n) with hash set
- **Space:** O(n) with hash set, O(1) with three pointers

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^3) | O(1) | Three nested loops |
| Hash Set | O(n) | O(n) | Fix middle, O(1) lookups |
| Three Pointers | O(n) | O(1) | Exploit sorted property |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

**Approach 1: Hash Set (simplest)**
- Build a set of all values. For each `nums[j]`, check if `nums[j] - diff` and `nums[j] + diff` exist.

**Approach 2: Three Pointers (fix one + two pointers pattern)**
- Pointer `i` tracks the first element, `j` the middle (fixed), `k` the third.
- Since array is sorted, advance `i` and `k` as `j` moves right.

```python
def arithmeticTriplets(nums: list[int], diff: int) -> int:
    # Hash set approach — clean and O(n)
    num_set = set(nums)
    count = 0

    for num in nums:
        # Fix num as middle element
        if (num - diff) in num_set and (num + diff) in num_set:
            count += 1

    return count
```

```python
def arithmeticTriplets_three_pointers(nums: list[int], diff: int) -> int:
    # Three pointers approach — O(1) space
    n = len(nums)
    i, k = 0, 2
    count = 0

    for j in range(1, n - 1):
        # Advance i until nums[j] - nums[i] <= diff
        while i < j and nums[j] - nums[i] > diff:
            i += 1

        # Advance k until nums[k] - nums[j] >= diff
        while k < n and nums[k] - nums[j] < diff:
            k += 1

        # Check if both conditions are exactly met
        if i < j and k < n and nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
            count += 1

    return count
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [0, 1, 4, 6, 7, 10], diff = 3`

**Hash set approach:**
- num_set = {0, 1, 4, 6, 7, 10}
- num=0: 0-3=-3 not in set. Skip.
- num=1: 1-3=-2 not in set. Skip.
- num=4: 4-3=1 in set, 4+3=7 in set. Count! Triplet: (1, 4, 7).
- num=6: 6-3=3 not in set. Skip.
- num=7: 7-3=4 in set, 7+3=10 in set. Count! Triplet: (4, 7, 10).
- num=10: 10-3=7 in set, 10+3=13 not in set. Skip.

**Output:** `2`

### Edge Case Testing

- **Empty input:** Not possible (n >= 3).
- **Single element:** Not possible.
- **Typical case:** `[0,1,4,6,7,10]`, diff=3 returns `2`.
- **Extreme values:** `[1,2,3]`, diff=1: triplet (1,2,3) exists, returns `1`. No arithmetic progression possible: returns `0`.

### Complexity

**Hash Set Approach:**
- **Time:** O(n) — build set O(n) + single pass O(n).
- **Space:** O(n) — hash set.

**Three Pointers Approach:**
- **Time:** O(n) — each pointer moves forward at most n times total.
- **Space:** O(1) — three pointer variables.

### Optimization Discussion

Both approaches are O(n) time. The hash set approach is simpler to code and explain. The three-pointer approach demonstrates the "fix one + two pointers" pattern more directly and uses O(1) space, making it a better pattern demonstration for interviews.

### Follow-up Variations

- **Arithmetic Slices (LC 413):** Count contiguous arithmetic subarrays.
- **Arithmetic Slices II (LC 446):** Count all arithmetic subsequences (DP).
- **3Sum (LC 15):** Same fix-one-search-two pattern with sum instead of difference.

### Common Traps

- **Confusing the middle element** — the triplet is `(num-diff, num, num+diff)`, fix the middle for cleanest code.
- **Not leveraging strictly increasing property** — the array has no duplicates, so set lookups are unambiguous.
- **Three pointers: forgetting to keep `k` ahead of `j`** — initialize `k = 2` and never let it fall behind `j`.
