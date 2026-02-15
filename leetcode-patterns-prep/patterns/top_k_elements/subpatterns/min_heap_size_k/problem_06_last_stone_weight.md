# Last Stone Weight

**Difficulty:** Easy
**Pattern:** Top K Elements
**Subpattern:** Min Heap of Size K
**Link:** https://leetcode.com/problems/last-stone-weight/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

You have a collection of stones, each with a positive integer weight. Each turn, pick the **two heaviest** stones and smash them. If they're equal, both are destroyed. If not, the lighter is destroyed and the heavier loses weight equal to the lighter. Return the weight of the last remaining stone, or `0` if none remain.

### 2. Clarification Questions

- **Input constraints?** `1 <= stones.length <= 30`, `1 <= stones[i] <= 1000`.
- **Edge cases?** Single stone (return it); two equal stones (both destroyed, return 0); all stones identical.
- **Expected output?** A single integer — weight of last stone, or 0.
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Each turn, sort the array, take the two largest, compute the result, repeat until ≤ 1 stone.
- **Time:** O(n^2 log n) — up to n rounds, each with a sort.
- **Space:** O(1) in-place

### 4. Optimized Approach

- 💡 **Core Insight:** We always need the **two largest** elements. A **max heap** gives us O(log n) access to the maximum. Pop two, compute the difference, push it back if nonzero.
- **Time:** O(n log n)
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Repeated sorting | O(n^2 log n) | O(1) | Simple but slow |
| Max Heap | O(n log n) | O(n) | **Optimal — always access the largest efficiently** |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Build a max heap (negate values for Python's min heap).
- Repeatedly pop the two largest stones.
- If they differ, push the difference back.
- Return the last stone (or 0 if heap is empty).

```python
import heapq

def lastStoneWeight(stones):
    # Max heap via negation (Python only has min heap)
    heap = [-s for s in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Pop two heaviest stones
        first = -heapq.heappop(heap)   # Largest
        second = -heapq.heappop(heap)  # Second largest

        if first != second:
            # Remaining fragment goes back
            heapq.heappush(heap, -(first - second))

    return -heap[0] if heap else 0
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`stones = [2, 7, 4, 1, 8, 1]`

Heap (negated): `[-8, -7, -4, -1, -2, -1]`

1. Pop 8, 7 → diff 1 → push 1 → `[-4, -2, -1, -1, -1]`
2. Pop 4, 2 → diff 2 → push 2 → `[-2, -1, -1, -1]`
3. Pop 2, 1 → diff 1 → push 1 → `[-1, -1, -1]`
4. Pop 1, 1 → equal → destroyed → `[-1]`
5. Return `1` ✓

### Edge Case Testing

- **Empty input:** Not possible per constraints (length ≥ 1).
- **Single element:** Heap has one element, skip while loop, return it.
- **Typical case:** Covered in dry run.
- **Extreme values:** Two equal stones → both destroyed, heap might empty → return 0.

### Complexity

- **Time:** O(n log n) — at most n rounds, each with O(log n) heap operations.
- **Space:** O(n) — heap stores all stones initially.

### Optimization Discussion

- Given constraints (n ≤ 30), even brute force is fast enough. The heap solution is the right approach to demonstrate in an interview.
- This problem is a **simulation** problem where the heap is used as the data structure to efficiently fetch the max.

### Follow-up Variations

- **Last Stone Weight II** (LeetCode 1049) — DP problem, totally different approach (subset sum).
- **What if we smash the two smallest instead?** Use a min heap directly (no negation).
- **Return the number of rounds** — count iterations of the while loop.

### ⚠️ Common Traps

- **Forgetting to negate values for max heap.** Python's `heapq` is a min heap. Without negation, you'll pop the smallest stones.
- **Not handling the empty heap case.** If all stones cancel out, the heap is empty. Return 0, not an error.
- **Pushing the difference when stones are equal.** Only push back if `first != second`. Pushing 0 would add a ghost stone.
