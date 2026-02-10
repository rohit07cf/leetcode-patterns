# Opposite Direction Two Pointers

## What This Subpattern Means

- You place one pointer at the **start** and one at the **end** of a sorted array (or string).
- They move **toward each other** until they meet — like two people walking from opposite ends of a hallway.

---

## The Trigger (How You Recognize It)

- "Find a pair in a **sorted** array that sums to X"
- "Is this string a **palindrome**?"
- "**Container** with most water" — maximize area between two lines
- Any problem where you're comparing **first vs last**, then **second vs second-to-last**, etc.

---

## Template

```python
def opposite_direction(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]

        if current == target:
            return [left, right]
        elif current < target:
            left += 1    # need bigger
        else:
            right -= 1   # need smaller

    return []
```

---

## Mistakes

- **Using `<=` in the while loop.** `left < right` is correct — if they're equal, you're comparing an element to itself.
- **Forgetting the array must be sorted.** If it's not sorted, sort it first or use a hash map.
- **Moving the wrong pointer.** If sum is too small, move the LEFT pointer (to get a bigger value). If too big, move RIGHT.
- **Not handling the "equal values" edge case.** Two elements can have the same value but different indices — that's still a valid pair.

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Valid Palindrome | Opposite Direction | DONE | |
| Two Sum (Sorted Array) | Opposite Direction | DONE | |
| Two Sum II – Input Array Is Sorted | Opposite Direction | DONE | |
| Container with Most Water | Opposite Direction | DONE | |

---

## TL;DR

- Start at both ends, squeeze inward
- Move the pointer that improves your condition
- Always `while left < right` — never `<=`
- Sorted array is the prerequisite
