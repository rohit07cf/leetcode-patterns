# Kth Missing Positive Number

**Difficulty:** Easy
**Pattern:** Binary Search
**Subpattern:** Boundary Binary Search
**Link:** https://leetcode.com/problems/kth-missing-positive-number/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a sorted array of **positive integers** in strictly increasing order and an integer `k`, return the k-th positive integer that is **missing** from the array.

### 2. Clarification Questions

- **Input constraints?** `1 <= arr.length <= 1000`. `1 <= arr[i] <= 1000`. `1 <= k <= 1000`. Array is strictly increasing.
- **Edge cases?** All missing numbers come before the array. All missing numbers come after the array. k is larger than the total number of missing numbers within the array range.
- **Expected output?** A single integer — the k-th missing positive number.
- **Can input be modified?** Yes, but no need.

### 3. Brute Force Approach

- **Idea:** Walk through positive integers 1, 2, 3, ... and skip those in the array. Count missing numbers until we hit k.
- **Time:** O(n + k)
- **Space:** O(1) or O(n) with a set

### 4. Optimized Approach

- **Core Insight:** At index `i`, the number of missing positives before `arr[i]` is `arr[i] - (i + 1)`. Binary search for the **rightmost index** where `arr[mid] - (mid + 1) < k`. The answer is then `k + (that index + 1)`, which simplifies to `lo + k`.
- **Time:** O(log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n + k) | O(1) | Walk through integers |
| Optimized | O(log n) | O(1) | Binary search on missing count |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Define `missing(mid) = arr[mid] - (mid + 1)` — the count of missing positives before `arr[mid]`.
- Binary search for the boundary where the k-th missing number lies.
- If `missing(mid) < k`, the k-th missing is to the right -> `lo = mid + 1`.
- If `missing(mid) >= k`, the k-th missing is at or to the left -> `hi = mid - 1`.
- After the loop, `lo` is the first index where missing count >= k. The answer is `lo + k`.

```python
def findKthPositive(arr, k):
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        # Number of missing positives before arr[mid]
        missing = arr[mid] - (mid + 1)

        if missing < k:
            lo = mid + 1  # k-th missing is beyond arr[mid]
        else:
            hi = mid - 1  # k-th missing is before or at arr[mid]

    # lo + k: lo is the insertion point, k accounts for the missing numbers
    return lo + k
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `arr = [2, 3, 4, 7, 11]`, `k = 5`

Missing positives: 1, 5, 6, 8, 9, 10, ...

- `lo=0, hi=4` -> `mid=2`, `missing = 4 - 3 = 1 < 5` -> `lo=3`
- `lo=3, hi=4` -> `mid=3`, `missing = 7 - 4 = 3 < 5` -> `lo=4`
- `lo=4, hi=4` -> `mid=4`, `missing = 11 - 5 = 6 >= 5` -> `hi=3`
- `lo=4, hi=3` -> exit. **Return 4 + 5 = 9**

**Verification:** Missing: 1, 5, 6, 8, **9**. The 5th missing is 9.

### Edge Case Testing

- **Empty input:** Not in constraints, but if arr is empty, `lo=0`, return `0 + k = k`.
- **Single element:** `arr=[2], k=1` -> `missing=2-1=1 >= 1`, `hi=-1`, `lo=0`. Return `0 + 1 = 1`.
- **k-th missing is after array:** `arr=[1,2,3], k=2` -> all `missing=0 < 2`, `lo=3`. Return `3 + 2 = 5`.
- **k-th missing is before array:** `arr=[5], k=3` -> `missing=4 >= 3`, `hi=-1`, `lo=0`. Return `0 + 3 = 3`.

### Complexity

- **Time:** O(log n) — binary search over the array.
- **Space:** O(1) — constant extra space.

### Optimization Discussion

The formula `lo + k` works because `lo` represents how many array elements are positioned before the k-th missing number. Each such element "shifts" the answer forward by 1 from the naive position `k`.

### Follow-up Variations

- Find the **k-th missing negative** number in a sorted array.
- Given a stream of numbers, find the k-th missing dynamically.
- Count the total number of missing positives in a range [1, m].

### Common Traps

- **Getting the `missing` formula wrong** — it's `arr[mid] - (mid + 1)`, not `arr[mid] - mid`. Index is 0-based but positives start at 1.
- **Confusing the final answer formula** — the answer is `lo + k`, not `arr[lo] - (something)`. Think of it as: without any array elements, the k-th missing positive is just `k`. Each array element before the answer shifts it right by 1.
- **Off-by-one with `< k` vs `<= k`** — use `< k` to find the rightmost index with fewer than k missing numbers.
