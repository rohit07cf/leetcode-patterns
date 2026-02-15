# Next Permutation

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction — Skip Logic
**Link:** https://leetcode.com/problems/next-permutation/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given an array of integers `nums`, rearrange it into the **lexicographically next greater permutation**. If no such permutation exists (array is in descending order), rearrange to the lowest possible order (ascending). Must be done **in-place** with O(1) extra memory.

### 2. Clarification Questions

- **Input constraints?** `1 <= nums.length <= 100`, `0 <= nums[i] <= 100`
- **Edge cases?** Already the largest permutation (descending), single element, all identical, two elements
- **Expected output?** Modify `nums` in-place — no return value
- **Can input be modified?** Yes — required

### 3. Brute Force Approach

- **Idea:** Generate all permutations in sorted order, find current one, return the next.
- **Time:** O(n!)
- **Space:** O(n!)

### 4. Optimized Approach

- **💡 Core Insight:** Work from the right. Find the first **descent** (`nums[i] < nums[i+1]`) — this is where the permutation can be incremented. Then, from the right, find the smallest element **larger than** `nums[i]` and swap them. Finally, **reverse** the suffix after position `i` (it was descending, now make it ascending for the smallest next permutation). The reversal uses opposite-direction two pointers.

- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n!) | O(n!) | Generate all permutations |
| Optimized | O(n) | O(1) | Find pivot + swap + reverse |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Step 1:** Scan from right to find the pivot — first index `i` where `nums[i] < nums[i + 1]`.
- **Step 2:** If no pivot found, array is fully descending — reverse entire array.
- **Step 3:** From right, find first element `> nums[i]` — skip elements `<= nums[i]`.
- **Step 4:** Swap pivot with that element.
- **Step 5:** Reverse the suffix after `i` using two pointers from opposite ends.

```python
def nextPermutation(nums: list[int]) -> None:
    n = len(nums)

    # Step 1: Find the pivot — rightmost ascent
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1  # Skip descending elements

    if i >= 0:
        # Step 2: Find rightmost element greater than pivot
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1  # Skip elements not greater than pivot

        # Step 3: Swap pivot with that element
        nums[i], nums[j] = nums[j], nums[i]

    # Step 4: Reverse the suffix (two pointers, opposite direction)
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
```

---

## PHASE 3 — AFTER CODING

### Dry Run

**Input:** `nums = [1, 2, 3]`

1. **Find pivot:** `i=1` → `nums[1]=2 < nums[2]=3` ✓
2. **Find swap target:** `j=2` → `nums[2]=3 > nums[1]=2` ✓
3. **Swap:** `[1, 3, 2]`
4. **Reverse suffix after i=1:** only `[2]` — nothing to reverse

**Output:** `[1, 3, 2]` ✓

**Input:** `nums = [3, 2, 1]` (largest permutation)

1. **Find pivot:** `i` goes to `-1` — no pivot found
2. **Reverse entire array:** `left=0, right=2` → swap → `[1, 2, 3]`

**Output:** `[1, 2, 3]` ✓

**Input:** `nums = [1, 1, 5]`

1. **Find pivot:** `i=1` → `nums[1]=1 < nums[2]=5` ✓
2. **Find swap target:** `j=2` → `nums[2]=5 > 1` ✓
3. **Swap:** `[1, 5, 1]`
4. **Reverse suffix:** `[1]` — nothing to reverse

**Output:** `[1, 5, 1]` ✓

### Edge Case Testing

- **Empty input:** Constraints guarantee `n >= 1`.
- **Single element:** `i` starts at -1 → reverse does nothing → unchanged. Correct.
- **Typical case:** Works as shown.
- **Extreme values:** All identical `[2,2,2]` → no pivot → reverse (still `[2,2,2]`). Correct.

### Complexity

- **Time:** O(n) — at most three linear scans (find pivot, find swap, reverse)
- **Space:** O(1) — all operations in-place

### Optimization Discussion

This is the textbook optimal solution. The key insight is that the suffix after the pivot is always in descending order, which is why:
- Binary search could find the swap target in O(log n), but overall is still O(n) due to the reverse step.
- The reverse converts the descending suffix to ascending, giving the smallest possible suffix.

### Follow-up Variations

- **Previous Permutation (similar logic):** Find rightmost ascent from right, find largest element smaller than pivot, swap, reverse.
- **Permutations (LC 46):** Generate all permutations — backtracking.
- **Permutation Sequence (LC 60):** Find the k-th permutation directly — math-based.

### ⚠️ Common Traps

- **Using `>` instead of `>=` when finding the pivot** — `nums[i] >= nums[i+1]` must use `>=` to handle duplicates correctly.
- **Using `<` instead of `<=` when finding the swap target** — `nums[j] <= nums[i]` must use `<=` to skip duplicates and find a strictly larger element.
- **Forgetting the reverse step** — swapping alone doesn't give the next permutation; the suffix must be minimized.
- **Not handling the "no pivot" case** — when the entire array is descending, wrap around to ascending order.
