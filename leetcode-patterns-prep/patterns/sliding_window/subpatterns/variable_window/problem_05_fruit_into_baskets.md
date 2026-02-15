# Fruit Into Baskets

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Variable Window
**Link:** https://leetcode.com/problems/fruit-into-baskets/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
You have a row of trees where `fruits[i]` is the type of fruit on tree `i`. You have **two baskets**, each holding one type of fruit. Starting from any tree, collect fruits moving right — you **must stop** when you encounter a third type. Return the **maximum number of fruits** you can collect.

**Translation:** Find the longest contiguous subarray with **at most 2 distinct values**.

### 2. Clarification Questions
- Input constraints? `1 <= fruits.length <= 10^5`, `0 <= fruits[i] < fruits.length`.
- Edge cases? Only 1 or 2 fruit types — return `len(fruits)`. All same type — return `len(fruits)`.
- Expected output? An integer — max fruits collected.
- Can input be modified? Yes, but we won't.

### 3. Brute Force Approach
- **Idea:** For every starting position, expand right counting distinct types. Stop at 3 distinct types. Track the maximum window length.
- **Time:** O(n^2)
- **Space:** O(1) — at most 3 types tracked.

### 4. Optimized Approach
- **Core Insight:** This is the classic **"longest subarray with at most K distinct elements"** problem with K=2. Use a sliding window with a frequency map. When distinct count exceeds 2, shrink from the left.
- **Time:** O(n)
- **Space:** O(1) — the map holds at most 3 entries.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Try all starting positions |
| Sliding Window | O(n) | O(1) | Frequency map with at most 3 keys |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use a frequency map (`basket`) to track fruit types in the current window.
- Expand `right` each step, adding the fruit to the map.
- When `len(basket) > 2`, shrink from `left` — decrement counts and remove types that reach 0.
- Update `max_fruits` at each valid state.

```python
def totalFruit(self, fruits: list[int]) -> int:
    basket = {}  # fruit_type -> count in window
    left = 0
    max_fruits = 0

    for right in range(len(fruits)):
        fruit = fruits[right]
        basket[fruit] = basket.get(fruit, 0) + 1

        # More than 2 types — shrink from left
        while len(basket) > 2:
            left_fruit = fruits[left]
            basket[left_fruit] -= 1
            if basket[left_fruit] == 0:
                del basket[left_fruit]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `fruits = [1,2,1,2,3]`

| right | fruit | basket | left | window | max_fruits |
|-------|-------|--------|------|--------|------------|
| 0 | 1 | {1:1} | 0 | [1] | 1 |
| 1 | 2 | {1:1,2:1} | 0 | [1,2] | 2 |
| 2 | 1 | {1:2,2:1} | 0 | [1,2,1] | 3 |
| 3 | 2 | {1:2,2:2} | 0 | [1,2,1,2] | 4 |
| 4 | 3 | {1:2,2:2,3:1} -> shrink | 0 | too many | 4 |
| | | {1:1,2:2,3:1} | 1 | still 3 types | 4 |
| | | {2:2,3:1} | 2 | [1,2,3] -> [2,3] wait... | 4 |

After shrinking: `left=2`, basket = `{1:1,2:2,3:1}` still 3 → shrink more → `left=3`, basket = `{2:2,3:1}` → valid, window size = 2. Actually let me retrace:
- right=4: add 3 → `{1:2,2:2,3:1}`, 3 types. Shrink: remove fruits[0]=1 → `{1:1,2:2,3:1}`, still 3. Remove fruits[1]=2 → `{1:1,2:1,3:1}`, still 3. Remove fruits[2]=1 → `{2:1,3:1}`, 2 types. left=3. Window=[2,3], size=2.

Output: **4** (subarray `[1,2,1,2]`)

### Edge Case Testing
- **Empty input:** Constraint says `len >= 1`, not applicable.
- **Single element:** `fruits = [5]` — returns 1.
- **Typical case:** `fruits = [1,2,1,2,3]` — returns 4.
- **Extreme values:** All same fruit — basket has 1 entry, returns `len(fruits)`.

### Complexity
- **Time:** O(n) — each element enters and leaves the window at most once.
- **Space:** O(1) — basket holds at most 3 entries before shrinking.

### Optimization Discussion
This is a direct application of the "at most K distinct" sliding window template. For K=2, the space is constant. The `while` loop for shrinking runs O(n) total across all iterations (amortized).

### Follow-up Variations
- **Longest Substring with At Most K Distinct Characters** (LC 340) — generalized version.
- **Longest Substring with At Most Two Distinct Characters** (LC 159) — string version of this exact problem.
- **Subarrays with K Different Integers** (LC 992) — exact K (use "at most K" minus "at most K-1").

### Common Traps
- Forgetting to `del` entries from the map when count hits 0 — `len(basket)` will be wrong.
- Using a set instead of a frequency map — you can't efficiently determine which element to remove from the set when shrinking.
- Misunderstanding the problem as "pick any 2 types from anywhere" — it must be a **contiguous** subarray.
