"""
Max Sum Subarray of Size K

WHY THIS PATTERN: "contiguous subarray of size k" + "maximum sum" = textbook fixed sliding window.
Instead of recomputing the sum for every window (O(N*k)), we slide in O(N).

KEY INVARIANT: window always contains exactly k elements.
When sliding: add the new right element, remove the old left element.

TIME:  O(N) — single pass after building first window
SPACE: O(1) — just tracking sum and best
"""

from typing import List


def max_sum_subarray(arr: List[int], k: int) -> int:
    if len(arr) < k:
        return -1

    # Build the first window
    window_sum = sum(arr[:k])
    best = window_sum

    # Slide the window
    for right in range(k, len(arr)):
        window_sum += arr[right]         # new element enters from right
        window_sum -= arr[right - k]     # old element leaves from left
        best = max(best, window_sum)

    return best


# --- Quick test ---
if __name__ == "__main__":
    print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # 9  (window [5,1,3])
    print(max_sum_subarray([2, 3, 4, 1, 5], 2))      # 7  (window [3,4])
