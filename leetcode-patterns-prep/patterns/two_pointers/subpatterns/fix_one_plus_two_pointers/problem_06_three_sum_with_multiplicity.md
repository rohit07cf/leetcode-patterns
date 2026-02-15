# 3Sum With Multiplicity

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Fix One + Two Pointers
**Link:** https://leetcode.com/problems/3sum-with-multiplicity/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `arr` and an integer `target`, return the number of tuples `(i, j, k)` such that `i < j < k` and `arr[i] + arr[j] + arr[k] == target`. Since the answer can be large, return it modulo 10^9 + 7.

### 2. Clarification Questions

- **Input constraints?** Array length 3 to 3000, values 0 to 100, target 0 to 300.
- **Edge cases?** All elements identical. Many duplicates (values capped at 100). Answer requires modulo.
- **Expected output?** Single integer count, modulo 10^9 + 7.
- **Can input be modified?** Yes — sorting is fine since we count ordered index tuples.

### 3. Brute Force Approach

- **Idea:** Three nested loops checking every triplet.
- **Time:** O(n^3)
- **Space:** O(1)

### 4. Optimized Approach

- **💡 Core Insight:** Sort the array. Fix `arr[i]`, use two pointers. The twist: when `arr[lo] == arr[hi]`, we need **combinatorial counting** — choose 2 from the group of equal elements. When `arr[lo] != arr[hi]`, multiply the counts of each value.
- **Time:** O(n^2)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^3) | O(1) | Too slow for n=3000 |
| Counting (hash) | O(n + 101^2) | O(101) | Count freq, iterate value pairs |
| Two Pointers | O(n^2) | O(1) | Sort + fix one + two pointers with multiplicity |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort the array. Fix `arr[i]`, two pointers on `[i+1, n-1]`.
- When a match is found and `arr[lo] == arr[hi]`: all elements in `[lo, hi]` are equal. The number of pairs is C(count, 2) = count*(count-1)/2.
- When a match is found and `arr[lo] != arr[hi]`: count duplicates of each value and multiply.
- Apply modulo at each addition.

```python
def threeSumMulti(arr: list[int], target: int) -> int:
    MOD = 10**9 + 7
    arr.sort()
    n = len(arr)
    count = 0

    for i in range(n - 2):
        remaining = target - arr[i]
        lo, hi = i + 1, n - 1

        while lo < hi:
            two_sum = arr[lo] + arr[hi]

            if two_sum < remaining:
                lo += 1
            elif two_sum > remaining:
                hi -= 1
            else:
                if arr[lo] == arr[hi]:
                    # All elements in [lo, hi] are equal
                    # Choose 2 from (hi - lo + 1) elements
                    span = hi - lo + 1
                    count = (count + span * (span - 1) // 2) % MOD
                    break  # No more pairs to find with this i
                else:
                    # Count duplicates of arr[lo] and arr[hi]
                    left_count = 1
                    while lo + left_count < hi and arr[lo + left_count] == arr[lo]:
                        left_count += 1

                    right_count = 1
                    while hi - right_count > lo and arr[hi - right_count] == arr[hi]:
                        right_count += 1

                    count = (count + left_count * right_count) % MOD
                    lo += left_count
                    hi -= right_count

    return count
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target = 8`

After sort (already sorted).

- **i=0, arr[i]=1**, remaining=7, lo=1, hi=9:
  - arr[1]+arr[9] = 1+5 = 6 < 7. lo++.
  - arr[2]+arr[9] = 2+5 = 7. arr[lo]!=arr[hi]. left_count=2 (two 2s), right_count=2 (two 5s). count += 4. lo=4, hi=7.
  - arr[4]+arr[7] = 3+4 = 7. left_count=2, right_count=2. count += 4. lo=6, hi=5. Stop.
- **i=1, arr[i]=1**, remaining=7: same pattern. count += 4 + 4 = 8.
- Continues for other fixed values...

**Output:** `20` (for this input)

### Edge Case Testing

- **Empty input:** Not possible (n >= 3).
- **Single element:** Not possible.
- **Typical case:** `[1,1,2,2,3,3,4,4,5,5]`, target=8 returns correct count.
- **Extreme values:** All zeros, target=0. Every triplet works: C(n, 3). All same value, target = 3*value: C(n, 3).

### Complexity

- **Time:** O(n^2) — outer loop O(n), inner two-pointer O(n) amortized.
- **Space:** O(1) — in-place sort, constant variables.

### Optimization Discussion

**Alternative approach:** Since values are in [0, 100], count frequency of each value. Then iterate over all pairs `(a, b)` where `a <= b`, compute `c = target - a - b`, and use combinatorics. This runs in O(n + 101^2) which is faster for large `n`.

```python
# Alternative: counting approach
from collections import Counter
def threeSumMulti_counting(arr, target):
    MOD = 10**9 + 7
    freq = Counter(arr)
    keys = sorted(freq)
    count = 0
    for i, a in enumerate(keys):
        for b in keys[i:]:
            c = target - a - b
            if c < b: continue
            if c not in freq: continue
            if a == b == c:
                count += freq[a] * (freq[a]-1) * (freq[a]-2) // 6
            elif a == b:
                count += freq[a] * (freq[a]-1) // 2 * freq[c]
            elif b == c:
                count += freq[a] * freq[b] * (freq[b]-1) // 2
            else:
                count += freq[a] * freq[b] * freq[c]
            count %= MOD
    return count
```

### Follow-up Variations

- **3Sum (LC 15):** Find unique triplet values instead of counting index tuples.
- **Count pairs with given sum:** Two-pointer or hash map.
- **k-Sum with multiplicity:** Generalize with dynamic programming.

### Common Traps

- **Forgetting the `arr[lo] == arr[hi]` case** — must use C(n, 2) formula, not multiply.
- **Not applying modulo** — answer can be astronomically large.
- **Double-counting** — the `i < j < k` ordering is maintained by fixing `i` and using `lo > i`, `hi > lo`.
- **Breaking vs continuing** — after handling the `arr[lo] == arr[hi]` case, must `break` out of the while loop.
