# Revision Checklists

> Go through these before interviews. If you can't check every box from memory, revisit that pattern.

---

## Two Pointers

- [ ] I know when to use opposite-direction vs same-direction pointers
- [ ] I can write the opposite-direction template from memory
- [ ] I know to use `while left < right` (not `<=`) for most cases
- [ ] I understand the "skip logic" variant (e.g., Valid Palindrome II)
- [ ] I can handle the 3Sum pattern (fix one, two-pointer the rest)
- [ ] I know how to partition in-place (Sort Colors / Dutch National Flag)
- [ ] I know the fast & slow pointer technique for cycle detection
- [ ] I remember to sort the array first when the problem allows it

---

## Sliding Window

- [ ] I can distinguish fixed-window from variable-window problems
- [ ] I can write the fixed-window template from memory
- [ ] I can write the variable-window template (expand right, shrink left)
- [ ] I know when to use a HashMap inside the window
- [ ] I remember to update the window state when shrinking (not just expanding)
- [ ] I know the "minimum window" variant (shrink to find smallest valid window)
- [ ] I don't confuse window size with array indices

---

## Binary Search

- [ ] I can write classic binary search without off-by-one errors
- [ ] I know when to use `left < right` vs `left <= right`
- [ ] I can find first/last occurrence using boundary binary search
- [ ] I can binary search on rotated sorted arrays
- [ ] I understand "binary search on answer space" — the most important variant
- [ ] I can define the `check(mid)` function for answer-space problems
- [ ] I know the monotonicity condition: if `check(x)` is true, `check(x+1)` is also true (or vice versa)
- [ ] I remember to think about integer overflow with `mid = (left + right) // 2`

---

## Top K Elements

- [ ] I know to use a min-heap of size K for "Kth largest" problems
- [ ] I can explain why a min-heap works (smallest in heap = Kth largest overall)
- [ ] I know to use a max-heap (negate values) for "Kth smallest" problems
- [ ] I can use `heapq` in Python (it's a min-heap by default)
- [ ] I remember that heap operations are O(log K), total is O(N log K)
- [ ] I know when bucket sort or quickselect might be better than a heap

---

## Sorting

- [ ] I can write quicksort's partition logic from memory
- [ ] I know quicksort is O(N log N) average, O(N^2) worst case
- [ ] I can write merge sort from memory
- [ ] I know merge sort is O(N log N) always, but uses O(N) extra space
- [ ] I understand when to use each sorting approach in interview problems
- [ ] I know the Dutch National Flag partition (3-way partition)
