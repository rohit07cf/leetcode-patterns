# Circular Array Loop

**Difficulty:** Medium
**Pattern:** Two Pointers
**Subpattern:** Fast and Slow
**Link:** https://leetcode.com/problems/circular-array-loop/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Given a circular array of non-zero integers `nums`, determine if there is a cycle where **all** movements follow the same direction (all positive or all negative) and the cycle length is greater than 1. Movement from index `i` goes to index `(i + nums[i]) % n`.

### 2. Clarification Questions
- Input constraints? `1 <= nums.length <= 5000`, `-1000 <= nums[i] <= 1000`, `nums[i] != 0`.
- Edge cases? Single element (self-loop, but length 1 so not valid), all same direction, mixed directions.
- Expected output? `True` if a valid cycle exists, `False` otherwise.
- Can input be modified? Yes, we can mark visited indices.

### 3. Brute Force Approach
- **Idea:** For each index, simulate the path using a visited set. Check if a same-direction cycle of length > 1 forms.
- **Time:** O(n^2) in the worst case.
- **Space:** O(n) for the visited set per starting index.

### 4. Optimized Approach
- **Core Insight:** For each unvisited index, use Floyd's fast/slow cycle detection. At each step, verify the direction stays consistent. If a direction change occurs or a self-loop is found, mark all nodes in that path as invalid (they can't be part of a valid cycle). This avoids revisiting dead-end paths.
- **Time:** O(n)
- **Space:** O(1) — by marking visited nodes in-place (set to 0).

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force per index | O(n^2) | O(n) | Simple but slow |
| Floyd's with marking | O(n) | O(1) | Each node visited at most twice total |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- For each index, run Floyd's cycle detection.
- At every step, verify direction consistency (sign of nums must match).
- Check for self-loops (cycle length must be > 1).
- Mark explored dead-end paths with 0 to avoid revisiting.

```python
class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def next_index(i: int) -> int:
            # Circular wrap — handles negative values correctly
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue  # already marked as dead end

            slow = i
            fast = i
            # Determine required direction for this path
            direction = nums[i] > 0

            while True:
                # Move slow one step — check direction
                next_slow = next_index(slow)
                if (nums[next_slow] > 0) != direction:
                    break
                slow = next_slow

                # Move fast two steps — check direction at each
                next_fast = next_index(fast)
                if (nums[next_fast] > 0) != direction:
                    break
                fast = next_fast

                next_fast = next_index(fast)
                if (nums[next_fast] > 0) != direction:
                    break
                fast = next_fast

                # Check for cycle
                if slow == fast:
                    # Ensure cycle length > 1 (not a self-loop)
                    if slow == next_index(slow):
                        break  # self-loop, invalid
                    return True

            # Mark all nodes in this failed path as dead ends
            j = i
            while (nums[j] > 0) == direction and nums[j] != 0:
                nxt = next_index(j)
                nums[j] = 0  # mark as visited/dead
                j = nxt

        return False
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `nums = [2, -1, 1, 2, 2]`

Starting at index 0 (direction: positive):
- Sequence: 0 -> 2 -> 3 -> 0 (cycle!)
- All values at indices 0, 2, 3 are positive. Direction consistent.
- Cycle length = 3 > 1.

**Floyd's trace:**

| Step | slow | fast |
|------|------|------|
| 0 | 0 | 0 |
| 1 | 2 | 3 |
| 2 | 3 | 2 |
| 3 | 0 | 0 |

`slow == fast == 0`. `next_index(0) = 2 != 0`, so not a self-loop. Return `True`.

### Edge Case Testing
- **Empty input:** Not possible (n >= 1).
- **Single element:** `nums = [1]` — next_index(0) = 0, self-loop. Length 1, so invalid. Returns `False`.
- **Typical case:** Mixed directions — only same-direction cycles count.
- **Extreme values:** `nums = [-1, -1, -1]` — all negative, cycle 0 -> 2 -> 1 -> 0. Length 3, same direction. Returns `True`.

### Complexity
- **Time:** O(n) — each index is visited at most a constant number of times. Once marked 0, it's never revisited.
- **Space:** O(1) — modifies the input array in-place for marking.

### Optimization Discussion
The in-place marking is key to achieving O(n). Without it, each starting index could potentially traverse O(n) nodes, giving O(n^2).

If modifying the input is not allowed, use a separate `visited` array for O(n) space.

### Follow-up Variations
- **Find the length of the cycle** — once detected, keep moving one pointer until it returns to the meeting point.
- **Find all valid cycles** — don't return early, collect all cycles.
- **Circular array with zeros allowed** — zeros would be "stuck" positions, filter them out.

### Common Traps
- Forgetting the **same direction** constraint — a cycle that alternates between positive and negative movement is invalid.
- Not checking for **self-loops** — a single element pointing to itself has cycle length 1, which is invalid.
- Incorrect modular arithmetic with negative numbers — Python's `%` operator handles negatives correctly (`-1 % 5 = 4`), but C++/Java do not.
- Not marking dead-end paths — leads to O(n^2) time instead of O(n).
