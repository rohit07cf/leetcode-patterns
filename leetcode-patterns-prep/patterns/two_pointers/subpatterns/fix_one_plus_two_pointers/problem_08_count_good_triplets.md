# Count Good Triplets

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Fix One + Two Pointers
**Link:** https://leetcode.com/problems/count-good-triplets/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array `arr` and three integers `a`, `b`, `c`, count the number of **good triplets** — triplets `(arr[i], arr[j], arr[k])` where `i < j < k` and:
- `|arr[i] - arr[j]| <= a`
- `|arr[j] - arr[k]| <= b`
- `|arr[i] - arr[k]| <= c`

### 2. Clarification Questions

- **Input constraints?** Array length 3 to 100, values 0 to 1000, a/b/c from 0 to 1000.
- **Edge cases?** All elements identical (every triplet is good if a,b,c >= 0). a=b=c=0 (only identical-element triplets count).
- **Expected output?** Single integer count.
- **Can input be modified?** Not necessary — n is small enough for brute force.

### 3. Brute Force Approach

- **Idea:** Three nested loops, check all three conditions for each triplet. With n <= 100, O(n^3) = 10^6 which is fine.
- **Time:** O(n^3)
- **Space:** O(1)

### 4. Optimized Approach

- **💡 Core Insight:** Fix the middle element `arr[j]`. For each `j`, determine valid ranges for `arr[i]` (must be within `a` of `arr[j]`) and `arr[k]` (within `b` of `arr[j]`). Then check the `c` condition between `arr[i]` and `arr[k]`. This prunes invalid candidates early. For n=100, brute force is acceptable, but the "fix middle" approach teaches the pattern.
- **Time:** O(n^2) with pruning (fix middle, enumerate valid pairs)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^3) | O(1) | Acceptable for n <= 100 |
| Fix middle + prune | O(n^2) avg | O(1) | Skip invalid i/k early |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Since n <= 100, the clean brute force with all three condition checks is interview-appropriate.
- **Optimization:** Fix `j`, skip `i` values that fail the `a` condition, skip `k` values that fail the `b` condition, then check `c`.

```python
def countGoodTriplets(arr: list[int], a: int, b: int, c: int) -> int:
    n = len(arr)
    count = 0

    for j in range(1, n - 1):
        for i in range(j):
            # Prune: check condition on (i, j) first
            if abs(arr[i] - arr[j]) > a:
                continue

            for k in range(j + 1, n):
                # Check remaining two conditions
                if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    count += 1

    return count
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `arr = [3, 0, 1, 1, 9, 7], a = 7, b = 2, c = 3`

- **j=1 (arr[j]=0):**
  - i=0 (arr[i]=3): |3-0|=3 <= 7. Check k=2..5:
    - k=2 (1): |0-1|=1 <= 2, |3-1|=2 <= 3. Count!
    - k=3 (1): |0-1|=1 <= 2, |3-1|=2 <= 3. Count!
    - k=4 (9): |0-9|=9 > 2. Skip.
    - k=5 (7): |0-7|=7 > 2. Skip.
- **j=2 (arr[j]=1):**
  - i=0 (3): |3-1|=2 <= 7. k=3: |1-1|=0 <= 2, |3-1|=2 <= 3. Count! k=4: |1-9|=8 > 2. k=5: |1-7|=6 > 2.
  - i=1 (0): |0-1|=1 <= 7. k=3: |1-1|=0 <= 2, |0-1|=1 <= 3. Count!
- Continues...

**Output:** `4`

### Edge Case Testing

- **Empty input:** Not possible (n >= 3).
- **Single element:** Not possible.
- **Typical case:** `[3,0,1,1,9,7], a=7, b=2, c=3` returns `4`.
- **Extreme values:** `a=b=c=0` — only triplets of identical values. All same elements with a=b=c=1000 — C(n,3) triplets.

### Complexity

- **Time:** O(n^3) worst case, O(n^2) with good pruning — for n <= 100, this is ~10^6 max.
- **Space:** O(1) — no extra data structures.

### Optimization Discussion

For larger `n`, a more sophisticated approach would:
1. Fix `j` (middle element).
2. Precompute counts of valid `arr[i]` values (those within `a` of `arr[j]` and within `c` of potential `arr[k]` values).
3. Use a BIT/Fenwick tree to count valid left/right elements efficiently.

But for n <= 100, this is overkill.

### Follow-up Variations

- **3Sum (LC 15):** Exact sum condition instead of difference bounds.
- **Count triplets in sorted array:** Binary search for valid ranges.
- **Good triplets with larger n:** Would need BIT/segment tree for O(n^2) or O(n log n).

### Common Traps

- **Checking conditions in wrong order** — checking the `(i, k)` condition early doesn't help if you haven't pruned on `(i, j)` first.
- **Off-by-one in loop bounds** — `j` starts at 1 and ends at `n-2` to leave room for `i` and `k`.
- **Absolute value** — remember `|arr[i] - arr[j]|`, not `arr[i] - arr[j]`.
