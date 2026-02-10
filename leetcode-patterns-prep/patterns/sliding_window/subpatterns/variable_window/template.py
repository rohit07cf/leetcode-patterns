"""
Variable-Size Sliding Window — Template
"""


def longest_substring_no_repeat(s):
    """Longest substring without repeating characters."""
    left = 0
    best = 0
    seen = {}  # char → last index (or use a set + counter)

    for right in range(len(s)):
        # EXPAND: add s[right]
        seen[s[right]] = seen.get(s[right], 0) + 1

        # SHRINK: while window has a duplicate
        while seen[s[right]] > 1:
            seen[s[left]] -= 1
            if seen[s[left]] == 0:
                del seen[s[left]]
            left += 1

        # UPDATE: valid window
        best = max(best, right - left + 1)

    return best


def subarray_sum_at_most_k(arr, k):
    """Longest subarray with sum <= k (all positive numbers)."""
    left = 0
    best = 0
    window_sum = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        while window_sum > k:
            window_sum -= arr[left]
            left += 1

        best = max(best, right - left + 1)

    return best
