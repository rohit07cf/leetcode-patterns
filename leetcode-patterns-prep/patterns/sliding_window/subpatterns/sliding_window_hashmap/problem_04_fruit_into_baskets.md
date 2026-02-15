# Fruit Into Baskets

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Sliding Window + Hashmap
**Link:** https://leetcode.com/problems/fruit-into-baskets/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an array `fruits` where `fruits[i]` is the type of fruit at tree `i`, find the **maximum number of fruits** you can collect if you can only carry **at most 2 types** of fruit. You must pick from a contiguous segment of trees.

This is equivalent to: **Longest subarray with at most 2 distinct values.**

### 2. Clarification Questions
- **Input constraints?** `1 <= fruits.length <= 10^5`, `0 <= fruits[i] < fruits.length`.
- **Edge cases?** All same type → return `len(fruits)`. Only 1 or 2 elements → return length.
- **Expected output?** An integer — the maximum number of fruits collected.
- **Can input be modified?** Yes, but not needed.

### 3. Brute Force Approach
- **Idea:** Check every subarray, count distinct types with a set, track the longest subarray with at most 2 types.
- **Time:** O(n^2)
- **Space:** O(1) — set holds at most n types but we can check inline.

### 4. Optimized Approach
- **Core Insight:** Classic sliding window — expand `right` to include fruits; when the window has **more than 2 distinct types**, shrink `left` until we're back to 2 types. A hashmap tracks the **count of each type** in the current window.
- **Time:** O(n)
- **Space:** O(1) — hashmap holds at most 3 entries before we shrink.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(n) | Check every subarray |
| Sliding Window + Hashmap | O(n) | O(1) | At most 3 keys in map |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Use a hashmap `basket` to track fruit type → count in the current window.
- Expand `right` pointer, adding fruits to `basket`.
- When `len(basket) > 2`, shrink from `left` until we have at most 2 types.
- Track `max_fruits` at each step.

```python
from collections import defaultdict

def totalFruit(self, fruits: list[int]) -> int:
    basket = defaultdict(int)  # fruit_type -> count in window
    left = 0
    max_fruits = 0

    for right in range(len(fruits)):
        basket[fruits[right]] += 1

        # Shrink window until we have at most 2 types
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `fruits = [1, 2, 3, 2, 2]`

| right | fruit | basket          | left | window        | max_fruits |
|-------|-------|-----------------|------|---------------|------------|
| 0     | 1     | {1:1}           | 0    | [1]           | 1          |
| 1     | 2     | {1:1, 2:1}      | 0    | [1,2]         | 2          |
| 2     | 3     | {1:1, 2:1, 3:1} | 0    | too many types|            |
|       |       | shrink → {2:1, 3:1} | 2 | [3]          |            |
|       |       | wait, remove 1 first | 1 | {2:1, 3:1}  | 2          |
| 3     | 2     | {2:2, 3:1}      | 1    | [2,3,2]       | 3          |
| 4     | 2     | {2:3, 3:1}      | 1    | [2,3,2,2]     | 4          |

**Output:** `4` (subarray `[2, 3, 2, 2]`)

### Edge Case Testing
- **Empty input:** Not possible per constraints (length >= 1).
- **Single element:** `[5]` → returns 1.
- **Typical case:** `[1,2,3,2,2]` → returns 4.
- **Extreme values:** All same type `[1,1,1,1]` → returns 4. Two types only `[1,2,1,2]` → returns 4.

### Complexity
- **Time:** O(n) — each element is added and removed from the window at most once.
- **Space:** O(1) — hashmap holds at most 3 entries.

### Optimization Discussion
- This is a specific case of "longest subarray with at most K distinct values" with K=2.
- Could generalize to K distinct by changing the `> 2` condition to `> k`.

### Follow-up Variations
- **Longest Substring with At Most K Distinct Characters** (LeetCode 340) — generalized version.
- **Longest Substring with At Most Two Distinct Characters** (LeetCode 159) — string version of same problem.
- **Subarrays with K Different Integers** (LeetCode 992) — exact K, uses atMost(K) - atMost(K-1).

### Common Traps
- Forgetting to delete zero-count entries from the hashmap — `len(basket)` will overcount types.
- Off-by-one when computing window size: it's `right - left + 1`, not `right - left`.
- Thinking this is about choosing any 2 types globally — it must be a **contiguous subarray**.
