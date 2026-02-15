# Minimum Consecutive Cards to Pick Up

**Difficulty:** Medium
**Pattern:** Sliding Window
**Subpattern:** Minimum Window Pattern
**Link:** https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an integer array `cards`, find the minimum number of consecutive cards you must pick up to have a pair of matching cards. Return `-1` if no matching pair exists.

### 2. Clarification Questions
- Input constraints? `1 <= cards.length <= 10^5`, `0 <= cards[i] <= 10^6`.
- Edge cases? All unique cards (return -1), all same card (return 2), two elements.
- Expected output? Minimum length of a contiguous subarray containing at least one duplicate.
- Can input be modified? Yes.

### 3. Brute Force Approach
- **Idea:** For every pair of indices with matching values, compute the distance. Return the minimum.
- **Time:** O(n^2)
- **Space:** O(1)

### 4. Optimized Approach
- **Core Insight:** Track the **last seen index** of each card value in a hashmap. For each card, if we've seen it before, the window `[last_index, current_index]` has length `current - last + 1`. This is the minimum window containing a duplicate of this specific value. Track the global minimum.
- **Time:** O(n)
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n^2) | O(1) | Check all pairs |
| HashMap | O(n) | O(n) | Track last seen index |
| Sliding Window | O(n) | O(n) | Shrink on duplicate |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Maintain a dictionary mapping each card value to its most recent index.
- For each card at index `i`, if it was previously seen at index `j`, the consecutive pickup is `i - j + 1`.
- Update the minimum across all such pairs.
- Always update the last-seen index to the current position.

```python
def minimumCardPickup(cards: list[int]) -> int:
    last_seen = {}  # card_value -> most recent index
    min_pickup = float('inf')

    for i, card in enumerate(cards):
        if card in last_seen:
            # distance from last occurrence to current (inclusive)
            min_pickup = min(min_pickup, i - last_seen[card] + 1)

        # update last seen to current index (always want closest pair)
        last_seen[card] = i

    return min_pickup if min_pickup != float('inf') else -1
```

**Alternative: Sliding window approach**

```python
def minimumCardPickup(cards: list[int]) -> int:
    count = {}
    min_pickup = float('inf')
    left = 0

    for right in range(len(cards)):
        count[cards[right]] = count.get(cards[right], 0) + 1

        # shrink window while we have a duplicate
        while count[cards[right]] > 1:
            min_pickup = min(min_pickup, right - left + 1)
            count[cards[left]] -= 1
            left += 1

    return min_pickup if min_pickup != float('inf') else -1
```

---

## PHASE 3 — AFTER CODING

### Dry Run
**Input:** `cards = [3,4,2,3,4,7]`

**HashMap approach:**

| i | card | last_seen | min_pickup |
|---|------|-----------|------------|
| 0 | 3 | {3:0} | inf |
| 1 | 4 | {3:0, 4:1} | inf |
| 2 | 2 | {3:0, 4:1, 2:2} | inf |
| 3 | 3 | seen at 0 → 3-0+1=4, update {3:3} | 4 |
| 4 | 4 | seen at 1 → 4-1+1=4, update {4:4} | 4 |
| 5 | 7 | {3:3, 4:4, 2:2, 7:5} | 4 |

**Output:** `4`

### Edge Case Testing
- **Empty input:** Not possible per constraints (length >= 1).
- **Single element:** `cards = [5]` → no pair possible, return -1.
- **Typical case:** Shown in dry run.
- **Extreme values:** All cards identical → every adjacent pair matches, return 2.

### Complexity
- **Time:** O(n) — single pass through the array.
- **Space:** O(n) — hashmap storing up to `n` distinct card values.

### Optimization Discussion
- The **hashmap approach** is simpler and more direct than the sliding window for this problem.
- The sliding window approach works but is overkill — we only need the closest pair, not a full window state.
- Both are O(n) time and O(n) space.

### Follow-up Variations
- Find the minimum window containing at least `m` duplicates (not just one pair).
- Return the actual subarray, not just the length.
- What if you need the minimum pickup with at least one pair of **each** card value present?

### Common Traps
- **Not updating `last_seen` to the current index** — you must always move the stored index forward. An older occurrence is never useful once a newer one exists (we want the closest pair).
- **Returning 0 or 1** — minimum valid pickup is 2 (a pair). If no duplicate exists, return -1.
- **Confusing "consecutive" with "any two matching"** — the problem requires a contiguous subarray, not just any two matching indices.
