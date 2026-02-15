# Increasing Triplet Subsequence

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Fix One + Two Pointers
**Link:** https://leetcode.com/problems/increasing-triplet-subsequence/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an integer array `nums`, return `true` if there exists a triple of indices `(i, j, k)` with `i < j < k` such that `nums[i] < nums[j] < nums[k]`. Otherwise return `false`.

### 2. Clarification Questions

- **Input constraints?** Array length 1 to 5*10^5, values from -2^31 to 2^31 - 1.
- **Edge cases?** Descending array (false). All equal (false). Exactly 3 elements.
- **Expected output?** Boolean — does an increasing triplet exist?
- **Can input be modified?** Prefer O(1) space solution; modification is acceptable but not needed.

### 3. Brute Force Approach

- **Idea:** Three nested loops checking `nums[i] < nums[j] < nums[k]`.
- **Time:** O(n^3)
- **Space:** O(1)

### 4. Optimized Approach

- **💡 Core Insight:** Maintain two variables: `first` (smallest so far) and `second` (smallest value greater than some earlier `first`). If we find a value greater than `second`, we have our triplet. This is a **greedy** approach that conceptually "fixes" the middle element and tracks the best candidates.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^3) | O(1) | Three nested loops |
| Fix middle + scan | O(n^2) | O(1) | Fix j, check left min and right max |
| Greedy two-variable | O(n) | O(1) | Optimal single pass |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Track `first` = smallest value seen so far.
- Track `second` = smallest value that is greater than some previous `first`.
- If any `nums[k] > second`, return `True` — we've found `first < second < nums[k]`.
- Update `first` and `second` greedily to keep them as small as possible.

```python
def increasingTriplet(nums: list[int]) -> bool:
    first = float('inf')   # smallest element seen
    second = float('inf')  # smallest element > some earlier first

    for num in nums:
        if num <= first:
            # New smallest — update first candidate
            first = num
        elif num <= second:
            # Bigger than first but smaller than second — update second
            second = num
        else:
            # num > second > (some earlier first) — triplet found
            return True

    return False
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [2, 1, 5, 0, 4, 6]`

- num=2: first=2, second=inf
- num=1: 1 <= 2, first=1, second=inf
- num=5: 5 > 1 and 5 <= inf? No, 5 <= inf. second=5
- num=0: 0 <= 1, first=0, second=5
- num=4: 4 > 0 and 4 <= 5. second=4
- num=6: 6 > 4. Return `True`.

**Key insight on correctness:** When `first` was updated to 0, `second` remained 5. Even though `first=0` came *after* the element that set `second=5`, the triplet `(1, 5, 6)` or `(0, 4, 6)` still exists. The algorithm doesn't track *which* first paired with second, but guarantees a valid triplet exists.

### Edge Case Testing

- **Empty input:** Length < 3, loop ends, returns `False`.
- **Single element:** Returns `False`.
- **Typical case:** `[2,1,5,0,4,6]` returns `True`.
- **Extreme values:** Descending `[5,4,3,2,1]` — first keeps decreasing, second never set, returns `False`.

### Complexity

- **Time:** O(n) — single pass through the array.
- **Space:** O(1) — two variables.

### Optimization Discussion

This is already optimal at O(n) time and O(1) space. An alternative O(n) approach uses prefix min array (left-to-right) and suffix max array (right-to-left), then checks if any middle element satisfies `prefix_min[j] < nums[j] < suffix_max[j]`. This uses O(n) space but is easier to understand.

```python
# Alternative: prefix/suffix approach (O(n) space)
def increasingTriplet_prefix(nums):
    n = len(nums)
    if n < 3: return False
    left_min = [0] * n
    right_max = [0] * n
    left_min[0] = nums[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], nums[i])
    right_max[-1] = nums[-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], nums[i])
    for j in range(1, n-1):
        if left_min[j] < nums[j] < right_max[j]:
            return True
    return False
```

### Follow-up Variations

- **Longest Increasing Subsequence (LC 300):** Generalize to length k using patience sorting.
- **Increasing Triplet with indices:** Return the actual indices (need to track more state).
- **132 Pattern (LC 456):** Find `i < j < k` with `nums[i] < nums[k] < nums[j]` — different ordering.

### Common Traps

- **Thinking updating `first` after `second` breaks correctness.** It doesn't — `second` implicitly remembers that a valid `first` existed before it.
- **Using strict `<` vs `<=`** — the problem requires *strictly* increasing, so `<=` comparisons for updating are correct (we skip equal values).
- **Returning the triplet values** — the problem only asks for boolean existence, not the actual triplet.
