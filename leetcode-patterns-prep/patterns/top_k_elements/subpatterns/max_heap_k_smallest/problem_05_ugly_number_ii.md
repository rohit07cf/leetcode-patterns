# Ugly Number II

**Difficulty:** Medium
**Pattern:** Top K Elements
**Subpattern:** Max Heap for K Smallest
**Link:** https://leetcode.com/problems/ugly-number-ii/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

An **ugly number** is a positive integer whose prime factors are limited to 2, 3, and 5. Given an integer `n`, return the nth ugly number (1 is considered the first ugly number).

### 2. Clarification Questions

- **Input constraints?** 1 <= n <= 1690.
- **Edge cases?** n = 1 (return 1), large n (up to 1690).
- **Expected output?** A single integer — the nth ugly number.
- **Can input be modified?** N/A — single integer input.

### 3. Brute Force Approach

- **Idea:** Check every positive integer: divide out all 2s, 3s, 5s and see if it reduces to 1. Count until we reach the nth one.
- **Time:** O(n * max_ugly) — potentially checking very large numbers.
- **Space:** O(1)

### 4. Optimized Approach

- 💡 **Core Insight:** Use a **min heap** to generate ugly numbers in order. Start with 1; each time we pop the smallest, we push `2*val`, `3*val`, `5*val`. Use a set to avoid duplicates. This generates the k smallest ugly numbers using a heap. Alternatively, the **three-pointer DP** approach is O(n) time and O(n) space.
- **Time:** O(n log n) for heap approach, O(n) for DP approach
- **Space:** O(n)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force check | O(n * max_ugly) | O(1) | Very slow |
| Min heap + set | O(n log n) | O(n) | Demonstrates pattern, clean |
| Three-pointer DP | O(n) | O(n) | Optimal, no heap needed |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Start with 1 in the heap. Pop the smallest, multiply by 2, 3, 5 and push new values (if unseen).
- Repeat n times. The nth popped value is the answer.

**Heap approach** (demonstrates pattern):

```python
import heapq

class Solution:
    def nthUglyNumber(self, n):
        heap = [1]
        seen = {1}
        factors = [2, 3, 5]

        val = 1
        for _ in range(n):
            val = heapq.heappop(heap)
            # Generate next ugly numbers from current
            for f in factors:
                nxt = val * f
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return val
```

**Three-pointer DP** (optimal):

```python
class Solution:
    def nthUglyNumber(self, n):
        dp = [0] * n
        dp[0] = 1
        # Pointers for multiples of 2, 3, 5
        i2 = i3 = i5 = 0

        for i in range(1, n):
            next2, next3, next5 = dp[i2] * 2, dp[i3] * 3, dp[i5] * 5
            dp[i] = min(next2, next3, next5)
            # Advance ALL pointers that match (handles duplicates like 6=2*3)
            if dp[i] == next2: i2 += 1
            if dp[i] == next3: i3 += 1
            if dp[i] == next5: i5 += 1

        return dp[-1]
```

---

## PHASE 3 — AFTER CODING

### Dry Run

n = 10 → expected output: 12

Sequence: 1, 2, 3, 4, 5, 6, 8, 9, 10, **12**

Heap approach trace (first few pops):
- Pop 1, push 2, 3, 5 → heap: [2, 3, 5]
- Pop 2, push 4, 6, 10 → heap: [3, 4, 5, 6, 10]
- Pop 3, push 9, 15 (6 already seen) → heap: [4, 5, 6, 9, 10, 15]
- Pop 4, push 8, 12, 20 → ...continues to 10th pop = **12** ✓

### Edge Case Testing

- **Empty input:** Not applicable (n >= 1).
- **Single element:** n = 1 → return 1.
- **Typical case:** n = 10 → 12.
- **Extreme values:** n = 1690 → valid; heap grows but stays manageable.

### Complexity

- **Time:** O(n log n) heap, O(n) DP.
- **Space:** O(n) for both — heap + seen set, or DP array.

### Optimization Discussion

The DP approach is strictly better at O(n) time. The heap approach is valuable as a **pattern demonstration** — it shows how to generate the k smallest elements from a structured space using a heap.

### Follow-up Variations

- **Super Ugly Number (LC 313)** — same idea with arbitrary prime factors.
- **Nth Magical Number (LC 878)** — binary search + inclusion-exclusion.

### ⚠️ Common Traps

- **Duplicate generation** — 6 = 2*3 = 3*2. The heap approach needs a `seen` set; the DP approach must advance all matching pointers with `if` (not `elif`).
- **1 is an ugly number** — don't forget the base case.
- **Integer overflow** — not an issue in Python, but matters in Java/C++.
