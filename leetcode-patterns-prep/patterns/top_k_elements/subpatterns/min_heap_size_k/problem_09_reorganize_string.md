# Reorganize String

**Difficulty:** Medium
**Pattern:** Top K Elements
**Subpattern:** Min Heap of Size K
**Link:** https://leetcode.com/problems/reorganize-string/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given a string `s`, rearrange its characters so that **no two adjacent characters are the same**. If impossible, return an empty string.

### 2. Clarification Questions

- **Input constraints?** `1 <= s.length <= 500`, lowercase English letters only.
- **Edge cases?** Single character (always valid); one character dominates more than `(n+1)/2` positions (impossible); two characters alternating.
- **Expected output?** A rearranged string, or `""` if impossible.
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Try all permutations and check if any has no adjacent duplicates.
- **Time:** O(n!) — completely impractical
- **Space:** O(n)

### 4. Optimized Approach

- 💡 **Core Insight:** Greedily place the **most frequent** character available that isn't the same as the last placed character. A **max heap** gives O(log u) access to the most frequent. After placing a character, temporarily hold it aside and restore it on the next iteration.
- **Time:** O(n log u) where u = unique characters (≤ 26)
- **Space:** O(u)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | O(n!) | O(n) | Impractical |
| Max Heap greedy | O(n log u) | O(u) | **Effectively O(n) since u ≤ 26** |
| Interleave fill | O(n) | O(u) | Fill even indices first, then odd |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Count character frequencies.
- Check feasibility: if any character's count > `(n + 1) // 2`, return `""`.
- Use a max heap (negate counts). Each step: pop the most frequent, append it, hold it aside. Push the previously held character back. Repeat.

```python
import heapq
from collections import Counter

def reorganizeString(s):
    freq = Counter(s)
    n = len(s)

    # Impossible if any char exceeds half the string (rounded up)
    if any(count > (n + 1) // 2 for count in freq.values()):
        return ""

    # Max heap: (-count, char)
    heap = [(-count, char) for char, count in freq.items()]
    heapq.heapify(heap)

    result = []
    prev_count, prev_char = 0, ''

    while heap:
        neg_count, char = heapq.heappop(heap)
        result.append(char)

        # Push back the previously used character (if it still has remaining count)
        if prev_count < 0:
            heapq.heappush(heap, (prev_count, prev_char))

        # Save current char as "previous" with decremented count
        prev_count = neg_count + 1  # +1 because count is negated
        prev_char = char

    return ''.join(result)
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`s = "aab"`

Frequencies: `{'a': 2, 'b': 1}`

1. Heap: `[(-2, 'a'), (-1, 'b')]`, prev = `(0, '')`
2. Pop `(-2, 'a')` → result: `['a']`, prev = `(-1, 'a')` (one 'a' left)
3. Pop `(-1, 'b')` → result: `['a','b']`, push back `(-1, 'a')`, prev = `(0, 'b')`
4. Pop `(-1, 'a')` → result: `['a','b','a']`, push back nothing (prev_count = 0)
5. Return `"aba"` ✓

### Edge Case Testing

- **Empty input:** Not possible per constraints.
- **Single element:** `s = "a"` → no adjacent duplicates, return `"a"`.
- **Typical case:** Covered in dry run.
- **Extreme values:** `s = "aaab"` → `a` count = 3 > `(4+1)//2 = 2` → return `""`.

### Complexity

- **Time:** O(n log u) — n iterations, each with O(log u) heap operations. Since u ≤ 26, this is effectively **O(n)**.
- **Space:** O(u) — heap holds at most 26 entries.

### Optimization Discussion

- **Interleave approach:** Sort characters by frequency. Place the most frequent at even indices (0, 2, 4...), then fill odd indices. O(n) time, no heap needed.
- The heap approach is more intuitive to explain in an interview and generalizes to similar problems.

### Follow-up Variations

- **Rearrange String K Distance Apart** (LeetCode 358) — same idea but no two same chars within distance k. Use a queue of size k to hold characters.
- **Task Scheduler** (LeetCode 621) — similar greedy + cooldown logic.
- **Return all valid rearrangements** — backtracking with frequency tracking.

### ⚠️ Common Traps

- **Forgetting the feasibility check.** If max frequency > `(n+1)//2`, no valid arrangement exists. Check before building.
- **Not holding the previous character aside.** If you push it back immediately, it could be popped again and placed adjacent to itself.
- **Off-by-one on the negated count.** When decrementing a negated count, add 1 (since `-2 + 1 = -1` means one fewer occurrence).
