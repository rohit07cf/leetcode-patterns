# Classic Binary Search

## What This Subpattern Means

- The most basic form: find a **target value** in a **sorted array**.
- Halve the search space each step. O(log N) time.

---

## The Trigger (How You Recognize It)

- "Search for target in a **sorted** array"
- "Find the **insertion position**" for a target
- The array is sorted and you need O(log N)

---

## Template

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # not found (or return left for insertion position)
```

---

## Mistakes

- **Using `left < right` instead of `left <= right`.** Classic search needs `<=` because the target could be at the last remaining position.
- **Using `mid = (left + right) // 2` in other languages.** This can overflow. Use `left + (right - left) // 2`. (Python handles big ints, but build the habit.)
- **Returning `mid` after the loop.** After the loop, `mid` is stale. For "search insert position," return `left`.
- **Not handling empty array.** Check `if not arr: return -1` first.

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Binary Search | Classic | | |
| Search Insert Position | Classic | | |

---

## TL;DR

- `while left <= right` for exact match search
- `mid = left + (right - left) // 2` always
- Return `left` for insertion position after the loop
- This is the foundation — master it cold before moving on
