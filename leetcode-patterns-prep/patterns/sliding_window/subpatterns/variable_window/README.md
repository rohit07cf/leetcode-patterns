# Variable-Size Sliding Window

## What This Subpattern Means

- The window size **is not fixed** — it grows and shrinks based on a condition.
- Right pointer always moves forward (expand). Left pointer moves forward to shrink when the window becomes invalid.
- Think of it as: "a rubber band on the array — stretch it right, snap it left when it breaks the rule."

---

## The Trigger (How You Recognize It)

- "**Longest** substring/subarray satisfying condition X"
- "Subarray with sum **at most** / **at least** K"
- "Longest substring **without repeating** characters"
- "Longest repeating character replacement" (change at most k chars)
- The answer is the **maximum window size** where the window is valid

---

## Template

```python
def variable_window(s):
    left = 0
    best = 0
    window = {}  # track state (e.g., character frequencies)

    for right in range(len(s)):
        # EXPAND: add s[right] to window state
        window[s[right]] = window.get(s[right], 0) + 1

        # SHRINK: while window is INVALID
        while window_is_invalid():  # ← your condition
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

        # UPDATE: window [left..right] is now valid
        best = max(best, right - left + 1)

    return best
```

---

## Mistakes

- **Forgetting to update window state when shrinking.** Every time `left` moves, remove that element from your tracking (counter, sum, set, etc.).
- **Cleaning up the dict:** when a char count drops to 0, DELETE the key (don't just leave it as 0).
- **Mixing up "valid" vs "invalid" in the while condition.** The loop shrinks while the window is INVALID. After the loop, the window is VALID.
- **Using `if` instead of `while` for shrinking.** You might need to shrink multiple times.
- **Updating `best` in the wrong place.** For "longest" problems: update AFTER the shrink loop (window is valid). For "shortest": update INSIDE the shrink loop.

---

## Practice Problems

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Longest Substring Without Repeating Chars | Variable Window | DONE | |
| Longest Repeating Character Replacement | Variable Window | | |
| Subarray Sum <= K | Variable Window | | |

---

## TL;DR

- Right pointer always expands; left pointer shrinks when invalid
- Shrink with `while`, not `if`
- Clean up dict entries when count reaches 0
- For "longest" → update outside shrink. For "shortest" → update inside shrink.
- O(N) because each element enters and leaves the window at most once
