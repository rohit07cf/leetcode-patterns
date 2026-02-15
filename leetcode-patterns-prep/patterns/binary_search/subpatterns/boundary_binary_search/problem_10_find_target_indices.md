# Find Target Indices After Sorting Array

**Difficulty:** Easy
**Pattern:** Binary Search
**Subpattern:** Boundary Binary Search
**Link:** https://leetcode.com/problems/find-target-indices-after-sorting-array/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a 0-indexed array `nums` and an integer `target`, return a list of indices where `target` would appear **after sorting** the array in non-decreasing order. Return the indices in increasing order.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 100`. `1 <= nums[i], target <= 100`.
- **Edge cases?** Target not in array. All elements are the target. Single element.
- **Expected output?** A sorted list of indices (could be empty).
- **Can input be modified?** Yes — sorting is the core operation.

### 3. Brute Force Approach

- **Idea:** Sort the array, then linear scan to collect all indices where `nums[i] == target`.
- **Time:** O(n log n)
- **Space:** O(1) extra (excluding sort and output)

### 4. Optimized Approach

- **Core Insight:** After sorting, all occurrences of `target` are **contiguous**. Use **two boundary binary searches** — one for the **first occurrence** (left bound) and one for the **last occurrence** (right bound). The result is all indices from left to right inclusive.
- **Time:** O(n log n) — sorting dominates
- **Space:** O(1) extra

**Even better (O(n) without sorting):** Count elements less than target (gives starting index) and count elements equal to target (gives range length). No sorting needed.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort + Linear Scan | O(n log n) | O(1) | Simple but suboptimal scan |
| Sort + Binary Search | O(n log n) | O(1) | Boundary search for range |
| Counting (no sort) | O(n) | O(1) | Count less-than and equal-to |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

**Approach 1: Sort + Boundary Binary Search (demonstrates the pattern)**

- Sort the array.
- Find the **left boundary** (first occurrence of target).
- Find the **right boundary** (last occurrence of target).
- Return all indices in `[left, right]`.

```python
def targetIndices(nums, target):
    nums.sort()
    n = len(nums)

    # Find first occurrence of target
    lo, hi = 0, n - 1
    left = n  # default: target not found
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] >= target:
            left = mid
            hi = mid - 1
        else:
            lo = mid + 1

    # Find last occurrence of target
    lo, hi = 0, n - 1
    right = -1  # default: target not found
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] <= target:
            right = mid
            lo = mid + 1
        else:
            hi = mid - 1

    # Only return range if target actually exists
    if left <= right:
        return list(range(left, right + 1))
    return []
```

**Approach 2: O(n) counting (optimal):**

```python
def targetIndices(nums, target):
    less = sum(1 for x in nums if x < target)   # starting index
    equal = sum(1 for x in nums if x == target)  # how many targets
    return list(range(less, less + equal))
```

---

## PHASE 3 — AFTER CODING

### Dry Run (Binary Search Approach)

**Input:** `nums = [1, 2, 5, 2, 3]`, `target = 2`

**After sorting:** `[1, 2, 2, 3, 5]`

**Left boundary (first >= 2):**
- `lo=0, hi=4` -> `mid=2`, `nums[2]=2 >= 2` -> `left=2`, `hi=1`
- `lo=0, hi=1` -> `mid=0`, `nums[0]=1 >= 2`? No -> `lo=1`
- `lo=1, hi=1` -> `mid=1`, `nums[1]=2 >= 2` -> `left=1`, `hi=0`
- Exit. **left = 1**

**Right boundary (last <= 2):**
- `lo=0, hi=4` -> `mid=2`, `nums[2]=2 <= 2` -> `right=2`, `lo=3`
- `lo=3, hi=4` -> `mid=3`, `nums[3]=3 <= 2`? No -> `hi=2`
- Exit. **right = 2**

**Output:** `list(range(1, 3))` = `[1, 2]`

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `nums=[5], target=5` -> sorted `[5]`, left=0, right=0. Returns `[0]`.
- **Target not found:** `nums=[1,3,5], target=2` -> left=1 (first >= 2 is index 1, value 3), right=0 (last <= 2 is index 0, value 1). `left > right` -> returns `[]`.
- **All same:** `nums=[2,2,2], target=2` -> left=0, right=2. Returns `[0, 1, 2]`.

### Complexity

- **Time:** O(n log n) for sort + binary search approach. O(n) for counting approach.
- **Space:** O(1) extra — excluding the output list.

### Optimization Discussion

The **counting approach** is O(n) and avoids sorting entirely. It's simpler and faster. However, the binary search approach is valuable for demonstrating the boundary binary search pattern, and it generalizes to cases where the array is **already sorted** (making it O(log n)).

### Follow-up Variations

- Find target indices in an **already sorted** array — pure O(log n) boundary search.
- Return indices in the **original unsorted** array (requires index tracking).
- Find indices of all elements in a **range** [lo, hi] after sorting.

### Common Traps

- **Forgetting to sort first** — the problem asks for indices in the sorted array, not the original.
- **Returning wrong indices when target is absent** — make sure `left <= right` before generating the range. If target is not present, the boundaries will cross.
- **Using the wrong boundary condition** — for first occurrence use `>= target` (search left), for last use `<= target` (search right). Mixing these up gives wrong bounds.
