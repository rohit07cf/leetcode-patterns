# Sliding Window

> **Sliding window = a window on a train.** You're looking at the scenery through a fixed (or stretchy) window, and the train keeps moving forward. You never look backwards — you just slide the view.

---

## When to Use

- The problem asks about a **contiguous subarray** or **substring**
- You need to find the **max/min/count** of something within a window of elements
- The brute force would check every possible subarray — O(N^2) or worse
- The window has a **fixed size** (easy) or a **variable size** based on a condition (medium)
- Keywords: "subarray of size k", "longest substring", "minimum window"

---

## How to Spot It Fast

- "Maximum sum of subarray of size **k**" → fixed window
- "**Longest** substring without repeating characters" → variable window
- "**Minimum** window containing all characters of T" → minimum window pattern
- "Subarray with sum **at most/at least** K" → variable window
- "**Permutation** in string" → fixed window + HashMap
- "Count **distinct** elements in every window" → sliding window + HashMap
- The constraint mentions contiguous elements
- You can express the answer as: "find the best window [i..j] where..."

---

## Core Idea

- Maintain a "window" defined by two pointers: `left` and `right`
- **Expand** the window by moving `right` forward (add element to window)
- **Shrink** the window by moving `left` forward (remove element from window)
- At each step, update your answer based on the current window state
- Key: you never move backwards — each element enters and leaves the window at most once → O(N)

```
Array:  [2, 1, 5, 1, 3, 2]
Window:     [1, 5, 1]
            L        R

Slide right:
            [5, 1, 3]
               L        R
              ↑ removed   ↑ added
```

---

## Template (Python)

```python
def fixed_window(arr, k):
    """Fixed-size window of size k."""
    window_sum = sum(arr[:k])
    best = window_sum

    for right in range(k, len(arr)):
        window_sum += arr[right]        # add new element
        window_sum -= arr[right - k]    # remove old element
        best = max(best, window_sum)

    return best


def variable_window(arr, condition):
    """Variable-size window: expand right, shrink left when invalid."""
    left = 0
    best = 0
    # window state variables here

    for right in range(len(arr)):
        # expand: add arr[right] to window state

        while not valid():  # ← your condition
            # shrink: remove arr[left] from window state
            left += 1

        best = max(best, right - left + 1)

    return best
```

---

## Common Pitfalls

1. **Off-by-one with window size.** Window `[left..right]` has size `right - left + 1`.
2. **Forgetting to update window state when shrinking.** When you move `left`, remove that element's contribution!
3. **Variable window: shrinking too much or too little.** The `while` condition must match exactly what makes the window invalid.
4. **Fixed window: starting the loop at the wrong index.** First window is `arr[0..k-1]`, loop starts at index `k`.
5. **Confusing "longest" vs "shortest" window.** For longest: update answer outside the shrink loop. For shortest: update answer inside the shrink loop.
6. **HashMap windows: not cleaning up entries with count 0.** A key with count 0 is NOT the same as a missing key in some problems.
7. **Sliding window on strings: forgetting that strings are immutable in Python.** Use a dict/Counter for character counts.
8. **Not handling edge case: window size > array length.**
9. **Thinking the window can shrink from the right.** It can't — `right` only moves forward.
10. **Applying sliding window to non-contiguous problems.** Sliding window ONLY works for contiguous subarrays/substrings.

---

## Practice Problems (from Excel)

| Problem | Subpattern | Status | Notes |
|---------|-----------|--------|-------|
| Max Sum Subarray of Size K | Fixed Window | DONE | |
| Average of Subarrays | Fixed Window | DONE | |
| First Negative Number in Window | Fixed Window | DONE | |
| Longest Substring Without Repeating Chars | Variable Window | DONE | |
| Longest Repeating Character Replacement | Variable Window | | |
| Subarray Sum <= K | Variable Window | | |
| Longest Substring Without Repeating Chars | Sliding Window + HashMap | | |
| Permutation in String | Sliding Window + HashMap | | |
| Minimum Window Substring | Sliding Window + HashMap | | |
| Count Distinct Elements in Every Window | Sliding Window + HashMap | | |
| Minimum Window Substring | Minimum Window Pattern | | |
| Minimum Size Subarray Sum | Minimum Window Pattern | | |
| Shortest Subarray with Sum at Least K | Minimum Window Pattern | | |

---

## TL;DR

- Fixed window: precompute first window, then slide by adding right and removing left
- Variable window: expand right always, shrink left when window becomes invalid
- Each element enters and leaves the window at most once → O(N) total
- "Longest" → update outside shrink loop. "Shortest" → update inside shrink loop.
- Always ask: what's in my window? What makes it valid/invalid?
