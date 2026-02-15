# Find the Duplicate Number

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Fast and Slow
**Link:** https://leetcode.com/problems/find-the-duplicate-number/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given an array of `n + 1` integers where each integer is in the range `[1, n]`, find the one repeated number. You must solve it without modifying the array and using only O(1) extra space.

### 2. Clarification Questions
- Input constraints? `1 <= n <= 10^5`, array length is `n + 1`, values in `[1, n]`. There is **exactly one** duplicate but it may appear more than twice.
- Edge cases? Duplicate at the start, at the end, appearing many times.
- Expected output? The duplicate integer value.
- Can input be modified? **No** (explicit constraint).

### 3. Brute Force Approach
- **Idea:** Sort the array and check adjacent elements, or use a hash set.
- **Time:** O(n log n) for sort, O(n) for hash set.
- **Space:** O(n) for hash set, O(1) for sort but sort modifies the array (violates constraint).

### 4. Optimized Approach
- **Core Insight:** Treat the array as a linked list where `nums[i]` points to index `nums[i]`. Since values are in `[1, n]` and the array has `n + 1` elements, there must be a cycle. The duplicate number is the **entry point** of that cycle. Apply Floyd's algorithm exactly like Linked List Cycle II.
- **Time:** O(n)
- **Space:** O(1)

**Why a cycle must exist:** By pigeonhole, a duplicate exists. Starting from index 0 (which is never pointed to since values are in `[1, n]`), following the "linked list" must eventually revisit a node — that revisited node is the duplicate value.

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Hash Set | O(n) | O(n) | Violates space constraint |
| Sort | O(n log n) | O(1) | Violates no-modify constraint |
| Floyd's Cycle Detection | O(n) | O(1) | Satisfies all constraints |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- **Phase 1:** Use fast/slow pointers to find meeting point inside the cycle.
- **Phase 2:** Reset one pointer to start (index 0). Advance both at speed 1 until they meet at the cycle entry — that index value is the duplicate.

```python
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Phase 1: Detect cycle (find meeting point)
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]             # one hop
            fast = nums[nums[fast]]       # two hops
            if slow == fast:
                break

        # Phase 2: Find cycle entry point (the duplicate value)
        entry = nums[0]
        while entry != slow:
            entry = nums[entry]
            slow = nums[slow]

        return entry
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `nums = [1, 3, 4, 2, 2]`

**Implicit linked list:** `0->1, 1->3, 2->4, 3->2, 4->2`

**Phase 1:**

| Step | slow | fast |
|------|------|------|
| start | 1 | 1 |
| 1 | 3 | 4 |
| 2 | 2 | 4 |
| 3 | 4 | 4 |

Hmm, let's trace more carefully:
- slow = nums[1] = 3, fast = nums[nums[1]] = nums[3] = 2
- slow = nums[3] = 2, fast = nums[nums[2]] = nums[4] = 2

Meet at 2.

**Phase 2:**
- entry = nums[0] = 1, slow = 2
- entry = nums[1] = 3, slow = nums[2] = 4
- entry = nums[3] = 2, slow = nums[4] = 2

Meet at **2**. Return `2`.

### Edge Case Testing
- **Empty input:** Not possible per constraints (n >= 1, array has at least 2 elements).
- **Single element:** `nums = [1, 1]` — slow and fast both become 1, meet immediately. Phase 2 returns 1.
- **Typical case:** Duplicate in the middle of the array — correctly found.
- **Extreme values:** Duplicate appearing many times (e.g., `[2, 2, 2, 2, 2]`) — still forms a cycle, entry is 2.

### Complexity
- **Time:** O(n) — each phase traverses at most O(n) steps.
- **Space:** O(1) — only pointer variables.

### Optimization Discussion
This is optimal given the constraints (no modification, O(1) space). Binary search on the value range is another O(n log n) approach that also uses O(1) space.

### Follow-up Variations
- **Find all duplicates** (LeetCode 442) — different technique needed (index marking).
- **What if the array is read-only AND we can't use Floyd's?** — Binary search on value range, counting elements <= mid.
- **First duplicate in a stream** — hash set is the only option.

### Common Traps
- Starting from index 0 is critical — index 0 is the "head" of the implicit linked list because no value maps to 0 (values are in `[1, n]`).
- Confusing array **indices** with array **values** — the "nodes" are values, and `nums[value]` gives the next "node."
- Returning the **index** instead of the **value** — the duplicate number is the value, not the index.
