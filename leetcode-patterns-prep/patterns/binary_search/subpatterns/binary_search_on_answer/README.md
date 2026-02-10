# Binary Search on Answer Space (Most Important)

## What This Subpattern Means

- You're not searching an array — you're searching the **answer itself**.
- The answer lies in a range `[lo, hi]`. You binary search this range using a `check(mid)` function.
- 💡 **This is the most important binary search subpattern.** It shows up in medium/hard problems constantly.
- Think of it as: "can I do it with budget X? If yes, try with less. If no, try with more."

---

## The Trigger (How You Recognize It)

- "**Minimum** speed / capacity / time to do something"
- "**Maximum** value such that a condition holds"
- You can write a function `check(x)` that returns True/False
- If `check(x)` is True, then `check(x+1)` is also True (or vice versa) — **monotonic**
- The answer space is HUGE (up to 10^9) but checking each candidate is O(N) → total O(N log(answer_range))
- Keywords: "at most", "at least", "within D days", "minimum maximum"

---

## Template

```python
def binary_search_on_answer(lo, hi):
    """Find minimum value where check(mid) is True."""
    while lo < hi:
        mid = lo + (hi - lo) // 2

        if check(mid):
            hi = mid        # mid works, try smaller
        else:
            lo = mid + 1    # mid doesn't work, try bigger

    return lo  # lo == hi == smallest valid answer


def check(candidate):
    """
    Return True if `candidate` is a valid answer.
    MUST be monotonic: if check(x) is True, check(x+1) is True.
    (Or the reverse — then swap hi=mid and lo=mid+1.)
    """
    # Problem-specific logic here
    pass
```

---

## Mistakes

- **Not identifying the `check()` function.** Before coding, write on paper: "check(x) = can I do it with x?" and verify it's monotonic.
- **Wrong bounds for lo and hi.** lo should be the smallest possible answer, hi the largest. Being too conservative is fine (slightly wider range), but too narrow means you miss the answer.
- **Infinite loop: `lo = mid` instead of `lo = mid + 1`.** When `lo == hi - 1`, `mid == lo`, and `lo = mid` doesn't advance. Always use `lo = mid + 1`.
- **Searching for maximum instead of minimum:** flip the logic — `if check(mid): lo = mid + 1` and `hi = mid`. Or search for the minimum that FAILS and subtract 1.
- ⚠️ **Not verifying monotonicity.** If `check()` isn't monotonic, binary search gives wrong answers. Test with a few examples on paper.

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Koko Eating Bananas | Binary Search on Answer | | |
| Capacity to Ship Packages | Binary Search on Answer | | |
| Minimum Speed to Arrive on Time | Binary Search on Answer | | |
| Split Array Largest Sum | Binary Search on Answer | | |

---

## TL;DR

- You're searching the ANSWER, not an array element
- Write `check(mid)` → is this candidate valid?
- Verify monotonicity: True/False boundary exists
- `lo = mid + 1` (not `lo = mid`) to avoid infinite loops
- This subpattern solves 80% of medium/hard binary search problems
