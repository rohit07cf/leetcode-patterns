# Furthest Building You Can Reach

**Difficulty:** Medium
**Pattern:** Top K Elements
**Subpattern:** Max Heap for K Smallest
**Link:** https://leetcode.com/problems/furthest-building-you-can-reach/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

You are given an array `heights`, a number of `bricks`, and a number of `ladders`. To move from building `i` to `i+1`, if the next building is taller, you need `heights[i+1] - heights[i]` bricks or one ladder. Return the furthest building index you can reach.

### 2. Clarification Questions

- **Input constraints?** 1 <= n <= 10^5, 1 <= heights[i] <= 10^6, 0 <= bricks <= 10^9, 0 <= ladders <= n.
- **Edge cases?** No climbs needed (descending), zero bricks and zero ladders, ladders >= number of climbs.
- **Expected output?** Integer — the furthest building index (0-indexed).
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Try all combinations of assigning bricks vs ladders to each climb. DFS/backtracking.
- **Time:** O(2^n) — exponential in number of climbs.
- **Space:** O(n) — recursion stack.

### 4. Optimized Approach

- 💡 **Core Insight:** **Ladders should cover the largest climbs, bricks cover the rest.** Use a **max heap of size = ladders** (but inverted: use a min heap to track the k smallest climbs that bricks handle). As you encounter each climb, push it into a min heap. If the heap size exceeds `ladders`, pop the smallest — that climb must be paid with bricks. If bricks run out, you're stuck. This is the "max heap for k smallest" pattern: the min heap of size `ladders` keeps the largest climbs for ladders, while the popped (smallest) climbs are paid with bricks.
- **Time:** O(n log L) where L = ladders
- **Space:** O(L)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force DFS | O(2^n) | O(n) | Exponential, useless |
| Min heap (greedy) | O(n log L) | O(L) | Optimal, elegant |
| Binary search + check | O(n log n) | O(n) | Also works, more complex |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Walk through buildings left to right. For each upward climb, push the height difference into a min heap.
- If heap size exceeds `ladders`, pop the smallest climb — pay for it with bricks.
- If bricks go negative, we can't reach this building — return previous index.

```python
import heapq

class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        # Min heap holds the climbs we plan to use ladders for
        # (the largest climbs stay in the heap)
        ladder_climbs = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]

            if diff <= 0:
                continue  # Descending or flat — no cost

            # Tentatively assign a ladder to this climb
            heapq.heappush(ladder_climbs, diff)

            # If we've used too many ladders, convert smallest to bricks
            if len(ladder_climbs) > ladders:
                smallest = heapq.heappop(ladder_climbs)
                bricks -= smallest

            # If bricks go negative, we can't make this jump
            if bricks < 0:
                return i

        # Reached the last building
        return len(heights) - 1
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`heights = [4, 2, 7, 6, 9, 14, 12]`, bricks = 5, ladders = 1

Climbs needed: (2→7)=5, (6→9)=3, (9→14)=5

- i=0: 2 < 4, descend, skip
- i=1: 7 > 2, diff=5, push 5, heap=[5], size=1=ladders, ok
- i=2: 6 < 7, descend, skip
- i=3: 9 > 6, diff=3, push 3, heap=[3,5], size=2 > 1 ladder → pop 3, bricks=5-3=2
- i=4: 14 > 9, diff=5, push 5, heap=[5,5], size=2 > 1 → pop 5, bricks=2-5=-3 < 0 → **return 4** ✓

### Edge Case Testing

- **Empty input:** n=1 → no jumps, return 0.
- **Single element:** Same as above.
- **Typical case:** Mix of ups and downs — handled correctly.
- **Extreme values:** ladders >= n → all climbs covered by ladders, reach the end. bricks = 0, ladders = 0 → stop at first upward climb.

### Complexity

- **Time:** O(n log L) — n buildings, each heap op is O(log L) where L = ladders.
- **Space:** O(L) — heap stores at most L elements.

### Optimization Discussion

**Binary search approach:** Binary search on the answer (furthest index). For a candidate index `mid`, sort the climbs up to `mid`, assign ladders to the top L climbs, sum the rest for bricks. Check feasibility. This is O(n log n) overall, slightly worse than the heap approach.

### Follow-up Variations

- What if ladders can cover a fixed height (not unlimited)? → Different greedy, possibly DP.
- What if you can also go backward? → BFS/shortest path problem.

### ⚠️ Common Traps

- **Using max heap instead of min heap** — we want the min heap so that the **smallest** climb gets evicted to bricks, leaving the **largest** climbs for ladders.
- **Forgetting to skip descents** — negative or zero differences cost nothing.
- **Off-by-one on return index** — when bricks go negative at step i, return `i` (the last building reached), not `i+1`.
