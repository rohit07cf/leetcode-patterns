# Two Pointers

> **Two pointers = two hands moving on an array.** You place two fingers on the data and move them according to a rule until they meet or cross.

---

## When to Use

- The input is a **sorted array** (or can be sorted)
- You need to find a **pair** that satisfies a condition (sum, difference, etc.)
- You need to **compare elements from both ends** (palindromes, container problems)
- You need to **remove/modify elements in-place** without extra space
- You need to **partition** an array into groups (e.g., Sort Colors)
- You need to **detect a cycle** or find the **middle** of a linked list

---

## How to Spot It Fast

- "Find two elements that..." → opposite direction pointers
- "Remove duplicates" or "remove element in-place" → same direction (read/write pointers)
- "Is it a palindrome?" → opposite direction, shrink inward
- "Container with most water" / "trapping rain water" → opposite direction
- "3Sum" or "4Sum" → fix one element, two-pointer the rest
- "Sort an array with only 2-3 distinct values" → partition-style (Dutch National Flag)
- "Detect cycle in linked list" → fast & slow pointers
- The constraint says **O(1) extra space** → strong two-pointer signal

---

## Core Idea

- Instead of checking every pair (O(N^2)), two pointers let you skip impossible pairs
- In a sorted array, if `arr[left] + arr[right] < target`, moving `left` right increases the sum
- If `arr[left] + arr[right] > target`, moving `right` left decreases the sum
- This "squeeze" eliminates an entire row/column of possibilities per step → O(N)

```
Sorted array: [1, 3, 5, 7, 9]
              L              R

  sum too small? → move L right
  sum too big?   → move R left
  sum just right? → found it!
```

---

## Template (Python)

```python
def two_pointer_opposite(arr, target):
    """Opposite direction: find pair with given sum in sorted array."""
    left, right = 0, len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]

        if current == target:
            return [left, right]       # found
        elif current < target:
            left += 1                  # need bigger sum
        else:
            right -= 1                # need smaller sum

    return []  # no pair found


def two_pointer_same_direction(arr):
    """Same direction: remove duplicates / in-place modify."""
    write = 0  # slow pointer (where to write)

    for read in range(len(arr)):       # fast pointer (what to read)
        if should_keep(arr[read]):
            arr[write] = arr[read]
            write += 1

    return write  # new length
```

---

## Common Pitfalls

1. **Forgetting to sort first.** Two pointers on an unsorted array won't give correct results for sum-type problems.
2. **Using `<=` instead of `<` in `while left < right`.** If `left == right`, you're comparing an element with itself.
3. **Not handling duplicates.** In 3Sum, skip duplicate values: `while left < right and arr[left] == arr[left-1]: left += 1`
4. **Off-by-one in same-direction pointer.** The `write` pointer is the next position to write, not the last written position.
5. **Modifying the array when you shouldn't.** Some problems want a new result, not in-place modification. Read carefully.
6. **Forgetting the edge case: empty array or single element.** Always check `len(arr) < 2` for pair problems.
7. **Moving both pointers at once.** Only move ONE pointer per iteration (unless you found a match).
8. **Not returning to the right pointer position after skipping duplicates.** Keep track of where you are.
9. **Assuming sorted input.** If the problem doesn't say "sorted," you need to sort first (or use a hash map instead).
10. **Using two pointers when a hash map is simpler.** If the array isn't sorted and you can't sort it, a hash map might be O(N) vs O(N log N).

---

## Practice Problems (from Excel)

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Valid Palindrome | Opposite Direction | DONE | |
| Two Sum (Sorted Array) | Opposite Direction | DONE | |
| Two Sum II – Input Array Is Sorted | Opposite Direction | DONE | |
| Container with Most Water | Opposite Direction | DONE | |
| Valid Palindrome II | Opposite Direction + Skip Logic | DONE | |
| Reverse Vowels of a String | Opposite Direction + Skip Logic | DONE | |
| Remove Element | Same Direction | DONE | |
| Remove Duplicates from Sorted Array | Same Direction | DONE | |
| Move Zeroes | Same Direction | DONE | |
| Merge Sorted Array | Merge-Style | | |
| Merge Two Sorted Lists | Merge-Style | | |
| Squares of a Sorted Array | Merge-Style | | |
| 3Sum | Fix One + Two Pointers | DONE | |
| 3Sum Closest | Fix One + Two Pointers | DONE | |
| 4Sum | Fix One + Two Pointers | | |
| Sort Colors | Partition-Style | DONE | |
| Sort Array By Parity | Partition-Style | DONE | |
| Sort an Array (partition logic) | Partition-Style | | |
| Linked List Cycle | Fast & Slow | | |
| Middle of the Linked List | Fast & Slow | | |
| Happy Number | Fast & Slow | | |

---

## TL;DR

- Two pointers shrink the search space from O(N^2) to O(N) by exploiting sorted order
- **Opposite direction**: start at both ends, squeeze inward
- **Same direction**: read pointer scouts ahead, write pointer builds the result
- Always check: is the array sorted? Do I need to handle duplicates?
- When in doubt, draw the two pointers on paper and simulate 3 steps
