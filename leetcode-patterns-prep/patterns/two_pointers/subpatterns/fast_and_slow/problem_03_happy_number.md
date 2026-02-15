# Happy Number

**Difficulty:** Easy
**Pattern:** Two Pointers
**Subpattern:** Fast and Slow
**Link:** https://leetcode.com/problems/happy-number/

---

## PHASE 1 — BEFORE CODING

### 1. Restate the Problem
Determine if a number is "happy." Starting with any positive integer, replace the number by the sum of the squares of its digits. Repeat until the number equals 1 (happy) or loops endlessly in a cycle (not happy).

### 2. Clarification Questions
- Input constraints? `1 <= n <= 2^31 - 1`.
- Edge cases? `n = 1` (already happy), `n = 7` (happy), small numbers that cycle quickly.
- Expected output? `True` if the number eventually reaches 1, `False` otherwise.
- Can input be modified? Yes, we work with derived values.

### 3. Brute Force Approach
- **Idea:** Use a hash set to track all numbers seen. If we see 1, return `True`. If we see a repeat, return `False`.
- **Time:** O(k) where k is the number of steps until cycle or reaching 1.
- **Space:** O(k) — storing all intermediate numbers.

### 4. Optimized Approach
- **Core Insight:** The sequence of digit-square-sums always either reaches 1 or enters a cycle — just like a linked list! Apply Floyd's cycle detection: slow computes one step, fast computes two steps. If they meet at 1, it's happy. If they meet elsewhere, it's not.
- **Time:** O(k)
- **Space:** O(1)

### 5. Trade-off Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (Hash Set) | O(k) | O(k) | Simple, stores all intermediates |
| Optimized (Floyd's) | O(k) | O(1) | No extra storage needed |

### 6. Ask: *"Should I proceed with the optimized approach?"*

---

## PHASE 2 — DURING CODING

- Define a helper to compute sum of squares of digits.
- Use slow (one step) and fast (two steps) until they converge.
- Check if they converge at 1.

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_square_sum(num: int) -> int:
            total = 0
            while num:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        slow = n
        fast = n

        # Floyd's cycle detection on the number sequence
        while True:
            slow = digit_square_sum(slow)             # one step
            fast = digit_square_sum(digit_square_sum(fast))  # two steps

            if slow == fast:
                break

        # If they met at 1, the number is happy
        return slow == 1
```

---

## PHASE 3 — AFTER CODING

### Dry Run
Input: `n = 19`

Sequence: 19 -> 82 -> 68 -> 100 -> 1 -> 1 -> ...

| Step | slow | fast |
|------|------|------|
| 0 | 19 | 19 |
| 1 | 82 | 68 |
| 2 | 68 | 1 |
| 3 | 100 | 1 |
| 4 | 1 | 1 |

`slow == fast == 1`. Return `True`.

### Edge Case Testing
- **Empty input:** N/A (constraint guarantees `n >= 1`).
- **Single element:** `n = 1` — slow becomes 1, fast becomes 1 after one iteration. Returns `True`.
- **Typical case:** `n = 19` returns `True`; `n = 2` returns `False` (cycles through 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4).
- **Extreme values:** Large numbers quickly reduce since max digit-square-sum for a 10-digit number is `9^2 * 10 = 810`.

### Complexity
- **Time:** O(k) — the sequence is bounded because numbers quickly shrink below ~810, so k is effectively O(log n) for the initial reduction plus a constant cycle length.
- **Space:** O(1) — only two integer variables.

### Optimization Discussion
Both approaches have similar time complexity. The Floyd's approach is superior in space. In practice, the hash set approach terminates just as fast and is easier to reason about.

**Key mathematical insight:** For any number with d digits, the digit-square-sum is at most `81d`. For numbers > 999, `81d < n`, so the sequence strictly decreases until it falls below ~1000, after which it cycles among a small set of numbers.

### Follow-up Variations
- **Find the cycle length** of unhappy numbers — continue after detection.
- **Count steps to reach 1** — modify to count iterations for happy numbers.
- **Generalize to sum of cubes** or other powers — same cycle detection applies.

### Common Traps
- Using `do-while` logic incorrectly — in Python, use `while True` with a break since slow and fast start equal.
- Forgetting that the fast pointer needs **two** applications of the function, not one application moving two "nodes."
- Integer overflow in other languages — not an issue in Python but relevant in C++/Java.
