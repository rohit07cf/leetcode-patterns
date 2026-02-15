# Smallest Range Covering Elements from K Lists

**Difficulty:** Hard
**Pattern:** Top K Elements
**Subpattern:** Max Heap for K Smallest
**Link:** https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

Given `k` sorted lists of integers, find the **smallest range** `[a, b]` such that at least one element from each list falls within the range. "Smallest" means `b - a` is minimized; ties broken by smaller `a`.

### 2. Clarification Questions

- **Input constraints?** k = len(nums), 1 <= k <= 3500, 1 <= list length <= 50, -10^5 <= element <= 10^5, lists are sorted ascending.
- **Edge cases?** k = 1 (range is [min, min] of that list), all lists share a common element.
- **Expected output?** A list `[a, b]` representing the smallest range.
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** For every combination of one element per list, compute the range `[min, max]`. Track the smallest range.
- **Time:** O(n1 * n2 * ... * nk) — exponential in k.
- **Space:** O(k)

### 4. Optimized Approach

- 💡 **Core Insight:** This is a **k-way merge with a sliding window**. Maintain a min heap of size k (one element per list). The current range is `[heap_min, current_max]`. Pop the minimum, push the next element from that list, update the max. Track the best range. This directly mirrors "Merge K Sorted Lists" but instead of building a merged list, we track the range spanned by the k current pointers.
- **Time:** O(N log k) where N = total elements across all lists
- **Space:** O(k)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| All combinations | Exponential | O(k) | Completely impractical |
| Min heap k-way merge | O(N log k) | O(k) | Optimal, elegant |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Seed the heap with the first element from each list. Track `current_max`.
- At each step, range = `[heap[0][0], current_max]`. Update best if smaller.
- Pop the min, advance that list's pointer. If a list is exhausted, stop — we can no longer cover all k lists.

```python
import heapq

class Solution:
    def smallestRange(self, nums):
        # Heap: (value, list_index, element_index)
        heap = []
        current_max = float('-inf')

        # Seed with first element of each list
        for i, lst in enumerate(nums):
            heapq.heappush(heap, (lst[0], i, 0))
            current_max = max(current_max, lst[0])

        best = [float('-inf'), float('inf')]

        while True:
            current_min, list_idx, elem_idx = heapq.heappop(heap)

            # Update best range if current is smaller
            if current_max - current_min < best[1] - best[0]:
                best = [current_min, current_max]

            # Advance pointer in the list that had the minimum
            if elem_idx + 1 == len(nums[list_idx]):
                break  # One list exhausted — can't cover all k lists

            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            # Only the new element can increase current_max
            current_max = max(current_max, next_val)

        return best
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]`

- Init: heap=[(0,1,0), (4,0,0), (5,2,0)], max=5
- Range [0,5], best=[0,5]
- Pop 0 (list 1), push 9 → heap=[(4,0,0), (9,1,1), (5,2,0)], max=9
- Range [4,9], width=5, best=[0,5] (tie, keep smaller a)... actually 5 == 5, keep [0,5]
- Pop 4 (list 0), push 10 → max=10, range [5,10], width=5, keep [0,5]
- Pop 5 (list 2), push 18 → max=18, range [9,18], width=9, skip
- Pop 9 (list 1), push 12 → max=18, range [10,18], width=8, skip
- Pop 10 (list 0), push 15 → max=18, range [12,18], width=6, skip
- Pop 12 (list 1), push 20 → max=20, range [15,20], width=5, update best=[15,20]? No, 5 == 5 and 0 < 15, keep [0,5]... wait, problem says smallest range then smaller a. So [0,5] is better.

Hmm, expected answer is **[20, 24]** with width 4. Let me continue:
- Pop 15, push 24 → max=24, range [18,24]=6, skip
- Pop 18, push 22 → max=24, range [20,24]=4 → **best=[20,24]** ✓

### Edge Case Testing

- **Empty input:** Not possible per constraints (each list has >= 1 element).
- **Single element:** k=1 → range is [list[0][0], list[0][0]].
- **Typical case:** Multiple lists with overlapping ranges — works as shown.
- **Extreme values:** Negative numbers — no special handling needed.

### Complexity

- **Time:** O(N log k) — each of N total elements is pushed/popped once, O(log k) per operation.
- **Space:** O(k) — heap stores exactly k entries.

### Optimization Discussion

An alternative is to **merge all lists** into one sorted list (tagging each element with its source list), then use a sliding window with a frequency map. This is O(N log N) time but may be simpler to reason about.

### Follow-up Variations

- What if lists aren't sorted? → Sort each first, then apply the same algorithm.
- Minimum window substring (LC 76) — similar sliding window with coverage constraint.

### ⚠️ Common Traps

- **Stopping condition** — must stop when ANY list is exhausted, not when ALL are. Once one list runs out, no range can cover all k lists.
- **Forgetting to update current_max** — only needs updating when a new element is pushed (not on pop).
- **Range comparison** — compare `b - a`, and break ties by smaller `a`.
