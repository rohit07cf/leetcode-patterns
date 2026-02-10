# Binary Search

> **Binary search = "the answer is monotonic" detector.** If you can split the search space into "yes" and "no" with a clear boundary, binary search finds that boundary in O(log N).

---

## When to Use

- The input is **sorted** (or has a monotonic property)
- You need to **find a target** in O(log N) time
- You need to find the **first/last** element satisfying a condition
- The problem has a **rotated sorted array**
- You're searching for the **answer itself** (not an element) and can write a `check(mid)` function that's monotonic
- The brute force would be linear scan but the search space is huge (10^9)

---

## How to Spot It Fast

- "Search in a **sorted** array" → classic binary search
- "Find **first/last** occurrence" → boundary binary search
- "Search in **rotated** sorted array" → modified binary search
- "**Minimum/maximum** value that satisfies a condition" → binary search on answer
- "**Koko eating bananas**" / "ship packages within D days" → binary search on answer
- The constraint is N ≤ 10^5 but the answer space is up to 10^9 → binary search on answer
- "The answer is between **lo and hi**, and if X works, then X+1 also works" → monotonic → binary search

---

## Core Idea

- Divide the search space in half at each step
- Compare `mid` with your target/condition
- Eliminate the half that can't contain the answer
- Repeat until the search space has one element

```
Array: [1, 3, 5, 7, 9, 11, 13]    target = 7

Step 1: mid = 7, found!

But the real power is:
Answer space: [1, 2, 3, ..., 1000000000]
              can you do it with speed 500000000? yes → try smaller
              can you do it with speed 250000000? yes → try smaller
              ...
              can you do it with speed 4? no → try bigger
              can you do it with speed 5? yes → answer is 5!

  Only ~30 steps to search 10^9 values!
```

---

## Template (Python)

```python
def binary_search(arr, target):
    """Classic: find target in sorted array."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # avoid overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # not found


def binary_search_on_answer(lo, hi, check):
    """
    Find minimum value where check(mid) is True.
    Assumes: if check(x) is True, then check(x+1) is also True (monotonic).
    """
    while lo < hi:
        mid = lo + (hi - lo) // 2

        if check(mid):
            hi = mid        # mid might be the answer, search left
        else:
            lo = mid + 1    # mid too small, search right

    return lo  # lo == hi == answer
```

---

## Common Pitfalls

1. **Off-by-one errors.** The #1 bug. Use `left <= right` for classic search, `left < right` for boundary/answer search.
2. **Integer overflow with `(left + right) / 2`.** Use `left + (right - left) // 2` instead (Python handles big ints, but it's a good habit for interviews in other languages).
3. **Wrong `lo`/`hi` bounds in answer-space search.** Make sure the answer is within `[lo, hi]`. Too narrow → miss the answer. Too wide → still works, just slightly slower.
4. **Forgetting that rotated arrays have TWO sorted halves.** Identify which half is sorted, then check if target is in that half.
5. **Boundary search: updating `right = mid` vs `right = mid - 1`.** When searching for "first true", use `right = mid` (mid could be the answer). When searching for exact match, use `right = mid - 1`.
6. **Infinite loop when `lo == hi - 1`.** If `mid = lo`, and you set `lo = mid`, you're stuck. Make sure `lo` always increases: `lo = mid + 1`.
7. **Not defining the `check()` function clearly** for answer-space problems. Write it on paper first.
8. **Applying binary search when the property isn't monotonic.** Binary search on answer REQUIRES: if check(x) is True, check(x+1) is True (or the reverse).
9. **Confusing "find minimum that works" vs "find maximum that works."** Minimum → search left when check passes. Maximum → search right when check passes.
10. **Returning the wrong value.** After the loop, `lo == hi` — that's your answer (not `mid`).

---

## Practice Problems (from Excel)

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Binary Search | Classic | | |
| Search Insert Position | Classic | | |
| First Bad Version | Boundary (First/Last) | | |
| Find First and Last Position | Boundary (First/Last) | | |
| Lower Bound / Upper Bound | Boundary (First/Last) | | |
| Search in Rotated Sorted Array | Modified (Rotated) | | |
| Find Minimum in Rotated Sorted Array | Modified (Rotated) | | |
| Peak Element | Modified (Rotated) | | |
| Koko Eating Bananas | Binary Search on Answer | | |
| Capacity to Ship Packages | Binary Search on Answer | | |
| Minimum Speed to Arrive on Time | Binary Search on Answer | | |
| Split Array Largest Sum | Binary Search on Answer | | |

---

## TL;DR

- Classic binary search: `while left <= right`, return when found
- Boundary search: `while left < right`, narrow to first/last occurrence
- Binary search on answer: define `check(mid)`, search the answer space
- The #1 skill: recognizing that a problem has a monotonic `check()` function
- Off-by-one is your enemy — practice the template until it's muscle memory
