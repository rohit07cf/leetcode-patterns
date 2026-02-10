# Boundary Binary Search (First/Last Occurrence)

## What This Subpattern Means

- Instead of finding ANY occurrence of target, find the **first** or **last** one.
- Equivalent to finding the **boundary** between "too small" and "big enough" (lower bound / upper bound).

---

## The Trigger (How You Recognize It)

- "Find **first** bad version"
- "Find **first and last** position of target"
- "**Lower bound** / **upper bound**"
- Any time you need the leftmost or rightmost occurrence, not just any occurrence

---

## Template

```python
def find_first(arr, target):
    """Find first (leftmost) occurrence of target."""
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid       # found one, but keep searching LEFT
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def find_last(arr, target):
    """Find last (rightmost) occurrence of target."""
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid       # found one, but keep searching RIGHT
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
```

---

## Mistakes

- **Returning immediately when `arr[mid] == target`.** That's classic binary search. For first/last, you must KEEP SEARCHING after finding a match.
- **First occurrence:** when found, search LEFT (`right = mid - 1`).
- **Last occurrence:** when found, search RIGHT (`left = mid + 1`).
- **First Bad Version:** the "isBadVersion" API replaces the `arr[mid] == target` check — same logic applies.

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| First Bad Version | Boundary | | |
| Find First and Last Position | Boundary | | |
| Lower Bound / Upper Bound | Boundary | | |

---

## TL;DR

- Same as classic, but DON'T return when you find a match
- First occurrence: save result, keep going left
- Last occurrence: save result, keep going right
- This is the building block for range queries and counting
