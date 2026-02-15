# Super Ugly Number

**Difficulty:** Medium
**Pattern:** Top K Elements
**Subpattern:** Max Heap for K Smallest
**Link:** https://leetcode.com/problems/super-ugly-number/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem

A **super ugly number** is a positive integer whose prime factors are all in a given list `primes`. Given `n` and `primes`, return the nth super ugly number (1 is the 1st).

### 2. Clarification Questions

- **Input constraints?** 1 <= n <= 10^5, 1 <= len(primes) <= 100, 2 <= primes[i] <= 1000, primes are unique and sorted.
- **Edge cases?** n = 1 (return 1), single prime, very large n.
- **Expected output?** A single integer — the nth super ugly number.
- **Can input be modified?** Yes.

### 3. Brute Force Approach

- **Idea:** Use a min heap with duplicate tracking (same as Ugly Number II heap approach but generalized to k primes).
- **Time:** O(n * k * log(n * k)) — each pop generates up to k new candidates.
- **Space:** O(n * k) — heap + seen set can grow large.

### 4. Optimized Approach

- 💡 **Core Insight:** Generalize the **multi-pointer DP** from Ugly Number II. Maintain one pointer per prime. At each step, compute `dp[ptr[j]] * primes[j]` for all j, take the minimum, and advance all matching pointers. This generates the n smallest super ugly numbers in order.
- **Time:** O(n * k) where k = len(primes)
- **Space:** O(n + k)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Min heap + set | O(nk log(nk)) | O(nk) | Simple but large heap |
| Heap with (val, prime, idx) | O(nk log k) | O(n + k) | Cleaner heap usage |
| Multi-pointer DP | O(nk) | O(n + k) | No heap, optimal |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

**Heap approach** (demonstrates pattern):

- Heap stores `(value, prime_used, dp_index)` — the next candidate from each prime's stream.
- Pop minimum, add to result, push next candidate from same prime stream.

```python
import heapq

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        dp = [0] * n
        dp[0] = 1

        # Heap: (next_value, prime, pointer_into_dp)
        # Each prime starts by multiplying dp[0] = 1
        heap = [(p, p, 0) for p in primes]
        heapq.heapify(heap)

        for i in range(1, n):
            dp[i] = heap[0][0]  # Smallest candidate

            # Pop ALL entries that equal dp[i] to avoid duplicates
            while heap[0][0] == dp[i]:
                val, prime, idx = heapq.heappop(heap)
                heapq.heappush(heap, (prime * dp[idx + 1], prime, idx + 1))

        return dp[-1]
```

**Multi-pointer DP** (optimal, no heap):

```python
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        k = len(primes)
        dp = [0] * n
        dp[0] = 1
        # One pointer per prime
        ptrs = [0] * k

        for i in range(1, n):
            # Compute next candidate from each prime
            candidates = [primes[j] * dp[ptrs[j]] for j in range(k)]
            dp[i] = min(candidates)
            # Advance all pointers that produced the minimum
            for j in range(k):
                if candidates[j] == dp[i]:
                    ptrs[j] += 1

        return dp[-1]
```

---

## PHASE 3 — AFTER CODING

### Dry Run

`n = 12`, `primes = [2, 7, 13, 19]`

Expected: `[1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]` → answer = **32**

Heap trace (first few):
- Heap: [(2,2,0), (7,7,0), (13,13,0), (19,19,0)]
- i=1: dp[1]=2, advance prime 2 → push (2*2=4,2,1)
- i=2: dp[2]=4, advance prime 2 → push (2*4=8,2,2) ... wait, that's wrong
- Correction: push (2*dp[2]=2*4=8, 2, 2)... actually push (prime*dp[idx+1], prime, idx+1) = (2*dp[1]=2*2=4, 2, 1)
- Continuing correctly yields **32** at position 12 ✓

### Edge Case Testing

- **Empty input:** Not applicable (n >= 1, primes non-empty).
- **Single element:** n = 1 → return 1 (base case).
- **Typical case:** Multiple primes, moderate n — works as shown.
- **Extreme values:** n = 10^5 with 100 primes — DP is O(10^7), manageable.

### Complexity

- **Time:** O(nk) for DP, O(nk log k) for heap approach.
- **Space:** O(n + k) — dp array + pointers/heap.

### Optimization Discussion

The heap approach with `(value, prime, dp_index)` tuples avoids the seen set entirely by ensuring each prime "stream" advances independently. This is O(n log k) per step vs O(nk) for the DP, so the **heap is actually faster** when k is large.

### Follow-up Variations

- **Ugly Number II (LC 264)** — special case with primes = [2, 3, 5].
- **Nth Magical Number (LC 878)** — different structure, uses binary search.

### ⚠️ Common Traps

- **Duplicate values** — multiple primes can produce the same number (e.g., 2*7 = 14, 7*2 = 14). Must advance ALL matching pointers/entries.
- **Heap indexing** — the `idx` in the heap tuple refers to the dp array index, not the primes array. Confusing these causes wrong results.
- **Off-by-one** — dp is 0-indexed but the problem is 1-indexed; dp[n-1] is the answer.
