"""
Sliding Window — Master Template
Copy-paste friendly. Adapt the condition for your specific problem.
"""


# ─── FIXED-SIZE WINDOW ─────────────────────────────────────────────
def fixed_window(arr, k):
    """
    Use when: window size is given (e.g., "subarray of size k").
    Key invariant: window always has exactly k elements.
    """
    # Build first window
    window_sum = sum(arr[:k])
    best = window_sum

    for right in range(k, len(arr)):
        window_sum += arr[right]          # add new element entering window
        window_sum -= arr[right - k]      # remove element leaving window
        best = max(best, window_sum)

    return best


# ─── VARIABLE-SIZE WINDOW ──────────────────────────────────────────
def variable_window(s):
    """
    Use when: find longest/shortest subarray/substring satisfying a condition.
    Key invariant: window [left..right] is always valid after the shrink loop.
    """
    left = 0
    best = 0
    window = {}  # track window state (e.g., char counts)

    for right in range(len(s)):
        # EXPAND: add s[right] to window
        window[s[right]] = window.get(s[right], 0) + 1

        # SHRINK: while window is invalid, remove from left
        while len(window) > 2:  # ← adapt this condition
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

        # UPDATE: current window is valid
        best = max(best, right - left + 1)

    return best


# ─── MINIMUM WINDOW PATTERN ────────────────────────────────────────
def minimum_window(s, t):
    """
    Use when: find smallest window containing all required elements.
    Key difference: update answer INSIDE the shrink loop (we want shortest).
    """
    from collections import Counter

    need = Counter(t)
    missing = len(t)  # number of chars still needed
    left = 0
    best = (float("inf"), 0, 0)  # (length, start, end)

    for right in range(len(s)):
        # EXPAND
        if need[s[right]] > 0:
            missing -= 1
        need[s[right]] -= 1

        # SHRINK (when window is valid, try to make it smaller)
        while missing == 0:
            # UPDATE inside shrink loop — we want the smallest valid window
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right)

            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1

    return s[best[1]:best[2] + 1] if best[0] != float("inf") else ""
