# Reverse Pairs

**Difficulty:** Hard
**Pattern:** Sorting
**Subpattern:** Merge Sort
**Link:** https://leetcode.com/problems/reverse-pairs/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums`, return the number of **reverse pairs** where `i < j` and `nums[i] > 2 * nums[j]`. A reverse pair is an "important inversion" with a 2x multiplier condition.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 5 * 10^4`, `-2^31 <= nums[i] <= 2^31 - 1` (full 32-bit range).
- **Edge cases?** Single element (0 pairs), all equal elements, large values that could cause overflow with `2 * nums[j]`.
- **Expected output?** A single integer — the total count of reverse pairs.
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Check all pairs `(i, j)` where `i < j` and count those where `nums[i] > 2 * nums[j]`.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach

- **Core Insight:** During merge sort, **before merging** two sorted halves, count cross-half reverse pairs. For each element in the left half, use a pointer to find how many elements in the right half satisfy `left[i] > 2 * right[j]`. Since both halves are sorted, this counting step is O(n) total per level using a two-pointer sweep.
- **Time:** O(n log n)
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | TLE for n = 5 * 10^4 |
| Merge Sort | O(n log n) | O(n) | Count before merge, sort during merge |
| BIT | O(n log n) | O(n) | Coordinate compression needed |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Key difference from standard inversion count:** The condition `nums[i] > 2 * nums[j]` doesn't align with the merge comparison. So we **separate** counting from merging.
- **Step 1:** Count cross-half pairs with a two-pointer sweep.
- **Step 2:** Perform the standard merge to sort.

```python
class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        return self._merge_sort(nums, 0, len(nums) - 1)

    def _merge_sort(self, nums: list[int], lo: int, hi: int) -> int:
        if lo >= hi:
            return 0

        mid = (lo + hi) // 2
        count = 0
        count += self._merge_sort(nums, lo, mid)
        count += self._merge_sort(nums, mid + 1, hi)

        # Count cross-half reverse pairs BEFORE merging
        count += self._count_pairs(nums, lo, mid, hi)

        # Standard merge to maintain sorted order
        self._merge(nums, lo, mid, hi)
        return count

    def _count_pairs(self, nums: list[int], lo: int, mid: int, hi: int) -> int:
        """Count pairs where left[i] > 2 * right[j] using two pointers."""
        count = 0
        j = mid + 1
        for i in range(lo, mid + 1):
            # Advance j while condition holds (both halves sorted)
            while j <= hi and nums[i] > 2 * nums[j]:
                j += 1
            # All elements from mid+1 to j-1 form valid pairs with nums[i]
            count += (j - (mid + 1))
        return count

    def _merge(self, nums: list[int], lo: int, mid: int, hi: int) -> None:
        """Standard in-place merge using temp array."""
        temp = []
        i, j = lo, mid + 1

        while i <= mid and j <= hi:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= hi:
            temp.append(nums[j])
            j += 1

        nums[lo:hi + 1] = temp
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [1, 3, 2, 3, 1]`

1. Split into `[1, 3, 2]` and `[3, 1]`
2. Recurse on `[1, 3, 2]`:
   - Split `[1, 3]` and `[2]`
   - `[1, 3]`: split `[1]`, `[3]` -> count pairs: 3 > 2*1? No (3 > 2, yes!) -> count=0 between these. Merge: `[1, 3]`
   - Count `[1,3]` vs `[2]`: 1 > 4? No. 3 > 4? No. Count = 0. Merge: `[1, 2, 3]`
3. Recurse on `[3, 1]`:
   - Count: 3 > 2*1 = 2? Yes -> count = 1. Merge: `[1, 3]`
4. Count `[1, 2, 3]` vs `[1, 3]`:
   - i=0: nums[0]=1, j checks: 1 > 2*1=2? No. count += 0
   - i=1: nums[1]=2, j still at start: 2 > 2? No. count += 0
   - i=2: nums[2]=3, 3 > 2*1=2? Yes, j++. 3 > 2*3=6? No. count += 1
   - Total from this level: 1
5. **Total: 0 + 0 + 1 + 1 = 2**

### Edge Case Testing

- **Empty input:** Not possible (length >= 1).
- **Single element:** Returns 0 (base case, no pairs).
- **Typical case:** `[1, 3, 2, 3, 1]` -> 2.
- **Extreme values:** `nums[i]` near INT_MAX. Python handles big integers natively, so `2 * nums[j]` won't overflow. In Java/C++, use `long`.

### Complexity

- **Time:** O(n log n) — counting step is O(n) per level (j pointer only moves forward), merge is O(n) per level, log n levels.
- **Space:** O(n) — temporary array for merge.

### Optimization Discussion

- The counting pointer `j` **does not reset** for each `i` because both halves are sorted. As `i` increases, `j` only moves forward. This makes the counting step O(n) total, not O(n^2).
- BIT/Fenwick tree is an alternative but requires coordinate compression and careful handling of the 2x condition.

### Follow-up Variations

- Count of Smaller Numbers After Self (LC 315) — similar merge sort counting.
- Count of Range Sum (LC 327) — range condition during merge.
- Global and Local Inversions (LC 775).

### Common Traps

- **Trying to combine counting and merging in one pass.** The `> 2x` condition doesn't match the `<=` comparison used for merge ordering. You **must** separate the counting step from the merging step.
- **Integer overflow** in languages like Java/C++. `2 * nums[j]` can overflow 32-bit integers. Use `long` or rearrange: `nums[i] / 2.0 > nums[j]`.
- **Resetting the j pointer** for each i in the counting step. Since both halves are sorted, j should persist across iterations of i — otherwise it becomes O(n^2).
