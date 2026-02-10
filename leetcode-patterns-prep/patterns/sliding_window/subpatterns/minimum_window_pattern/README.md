# Minimum Window Pattern

## What This Subpattern Means

- You need the **smallest** (shortest) window that satisfies a condition.
- This is the opposite of "longest" window problems: you **shrink aggressively** once the window is valid.
- Think of it as: "find the tightest rubber band that still holds all the required items."

---

## The Trigger (How You Recognize It)

- "**Minimum** window substring containing all characters of T"
- "**Minimum size** subarray with sum **at least** K"
- "**Shortest** subarray with sum at least K"
- The word "minimum" or "shortest" + a validity condition on the window

---

## Template

```python
def minimum_window(arr, target):
    left = 0
    best = float("inf")
    window_state = 0  # e.g., sum, count, etc.

    for right in range(len(arr)):
        # EXPAND
        window_state += arr[right]

        # SHRINK while valid (try to minimize)
        while window_is_valid(window_state, target):
            best = min(best, right - left + 1)   # ← update INSIDE
            window_state -= arr[left]
            left += 1

    return best if best != float("inf") else -1
```

---

## Mistakes

- **Updating `best` OUTSIDE the while loop.** For minimum window, update INSIDE the shrink loop (you want the smallest valid window).
- **Using `if` instead of `while` for shrinking.** You need to keep shrinking as long as the window stays valid.
- **Stopping too early.** Even after finding a valid window, keep expanding right — there might be a smaller valid window later.
- **Shortest Subarray with Sum at Least K** with negative numbers: standard sliding window doesn't work — need a deque (monotonic queue). Don't apply this template blindly.

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Minimum Window Substring | Minimum Window Pattern | | |
| Minimum Size Subarray Sum | Minimum Window Pattern | | |
| Shortest Subarray with Sum at Least K | Minimum Window Pattern | | |

---

## TL;DR

- Same as variable window, but you want the SMALLEST valid window
- Update answer INSIDE the shrink loop (not outside)
- Keep shrinking while the window is still valid
- Watch out for problems with negative numbers — they may need a deque, not a simple window
