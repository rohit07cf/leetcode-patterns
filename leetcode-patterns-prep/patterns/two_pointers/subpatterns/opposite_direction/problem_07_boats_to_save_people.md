# Boats to Save People

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Opposite Direction
**Link:** https://leetcode.com/problems/boats-to-save-people/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Each boat can carry at most **2 people** with a combined weight not exceeding `limit`. Given an array of people's weights, find the **minimum number of boats** to carry everyone.

### 2. Clarification Questions
- Input constraints? 1 to 5 * 10^4 people. Each weight 1 to `limit`. Limit up to 3 * 10^4.
- Edge cases? Every person weighs exactly `limit` -> each needs their own boat. Two lightest people exceed limit -> everyone gets a solo boat.
- Expected output? Minimum number of boats (integer).
- Can input be modified? Yes — we can sort the array.

### 3. Brute Force Approach
- **Idea:** Try all possible pairings to minimize boats. This is essentially a matching problem.
- **Time:** O(n!) — trying all permutations of pairings.
- **Space:** O(n)

### 4. Optimized Approach
- 💡 **Core Insight:** **Sort by weight, then greedily pair the lightest with the heaviest.** If the lightest and heaviest can share a boat, pair them (this is optimal because the lightest person is the best candidate to pair with anyone). If they can't share, the heaviest must ride alone.
- **Time:** O(n log n)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n!) | O(n) | Impractical |
| Sort + Greedy Two Pointers | O(n log n) | O(1) | Optimal greedy |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Sort the weights array.
- Use `left` (lightest) and `right` (heaviest) pointers.
- If they fit together, move both inward (shared boat).
- If not, the heaviest goes alone (move `right` only).
- Count each boat.

```python
def numRescueBoats(people: list[int], limit: int) -> int:
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0

    while left <= right:
        # Heaviest person always boards this boat
        if people[left] + people[right] <= limit:
            left += 1  # lightest person fits too — pair them
        right -= 1  # heaviest person boards (always)
        boats += 1

    return boats
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `people = [3, 2, 2, 1]`, `limit = 3`

Sorted: `[1, 2, 2, 3]`

| Step | left | right | pair? | Action | boats |
|------|------|-------|-------|--------|-------|
| 1 | 0 | 3 | 1+3=4 > 3 | 3 goes alone, right-- | 1 |
| 2 | 0 | 2 | 1+2=3 <= 3 | Pair (1,2), left++, right-- | 2 |
| 3 | 1 | 1 | left==right | 2 goes alone, right-- | 3 |

Result: **3** boats

### Edge Case Testing
- **Empty input:** Not possible per constraints (length >= 1).
- **Single element:** `[3], limit=5` -> one boat. `left == right`, boats = 1. Correct.
- **Typical case:** `[3,2,2,1], limit=3` -> 3 boats. Correct.
- **Extreme values:** Everyone weighs `limit` -> each person gets their own boat (n boats). Everyone weighs 1, limit >= 2 -> ceil(n/2) boats.

### Complexity
- **Time:** O(n log n) — sorting dominates. The two-pointer scan is O(n).
- **Space:** O(1) — in-place sort, only pointer variables.

### Optimization Discussion
O(n log n) is optimal. The sort is necessary to enable greedy pairing. You can prove optimality via exchange argument: pairing lightest with heaviest is always at least as good as any alternative pairing.

### Follow-up Variations
- What if each boat can carry **k people** instead of 2? Two pointers alone won't work — need a more general greedy or bin-packing approach.
- What if boats have **different capacities**? Sort boats too, match greedily.
- What if we want to **minimize total weight per boat** variance? Different optimization objective.

### ⚠️ Common Traps
- Using `left < right` instead of `left <= right` — misses the case where one person is left in the middle and still needs a boat.
- Forgetting to sort — the greedy pairing only works on sorted input.
- Trying to fit **3+ people** per boat — the constraint says at most 2.
- Moving `left` even when the pair doesn't fit — only the heaviest boards when they can't pair.
