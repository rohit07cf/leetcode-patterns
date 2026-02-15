# Two Sum II - Input Array Is Sorted

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction
**Link:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a **1-indexed** sorted array, find two numbers that add up to a specific target. Return their indices (1-based). Exactly one solution is guaranteed.

### 2. Clarification Questions
- Input constraints? Array is sorted in non-decreasing order. Length 2 to 3 * 10^4. Values from -1000 to 1000.
- Edge cases? Minimum array length is 2 (always at least one pair to check). Negative numbers are possible.
- Expected output? Two 1-based indices `[index1, index2]` where `index1 < index2`.
- Can input be modified? No need to modify; read-only access is sufficient.

### 3. Brute Force Approach
- **Idea:** Try every pair `(i, j)` where `i < j` and check if `numbers[i] + numbers[j] == target`.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach
- 💡 **Core Insight:** Because the array is **sorted**, placing one pointer at the start and one at the end lets us adjust the sum directionally. If the sum is too small, move `left` right to increase it. If too large, move `right` left to decrease it.
- **Time:** O(n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Ignores sorted property |
| Hash Map | O(n) | O(n) | Works but wastes space |
| Two Pointers | O(n) | O(1) | Best — leverages sorted order |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Initialize `left = 0`, `right = len(numbers) - 1`.
- Compute `current_sum`. Move pointers inward based on comparison with target.
- Return 1-based indices when match is found.

```python
def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # convert to 1-indexed
        elif current_sum < target:
            left += 1  # need a larger sum
        else:
            right -= 1  # need a smaller sum

    return []  # guaranteed to have a solution, but safe fallback
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `numbers = [2, 7, 11, 15]`, `target = 9`

| Step | left | right | sum | Action |
|------|------|-------|-----|--------|
| 1 | 0 | 3 | 2+15=17 | 17 > 9, move right |
| 2 | 0 | 2 | 2+11=13 | 13 > 9, move right |
| 3 | 0 | 1 | 2+7=9 | Match! Return [1, 2] |

### Edge Case Testing
- **Empty input:** Not possible per constraints (length >= 2).
- **Single element:** Not possible per constraints.
- **Typical case:** `[2,7,11,15], target=9` -> `[1,2]`. Works.
- **Extreme values:** `[-1000, 1000], target=0` -> `[1,2]`. Negative numbers handled naturally.

### Complexity
- **Time:** O(n) — each pointer moves at most n times total.
- **Space:** O(1) — only two pointer variables.

### Optimization Discussion
This is already optimal. O(n) time and O(1) space is the best possible since every element may need inspection.

### Follow-up Variations
- What if the array is **unsorted**? Use a hash map (O(n) time, O(n) space).
- What if there are **multiple valid pairs**? Return all pairs — need to handle duplicates carefully.
- What if you need to find **three numbers** summing to a target? Classic 3Sum — fix one, two-pointer on the rest.

### ⚠️ Common Traps
- Forgetting to return **1-based** indices (the problem is 1-indexed!).
- Using a hash map when the problem explicitly asks for O(1) space — interviewers expect two pointers here.
