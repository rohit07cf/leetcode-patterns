"""
Fixed-Size Sliding Window — Template
"""


def max_sum_subarray_of_size_k(arr, k):
    """Find max sum of any contiguous subarray of size k."""
    if len(arr) < k:
        return -1

    window_sum = sum(arr[:k])
    best = window_sum

    for right in range(k, len(arr)):
        window_sum += arr[right]
        window_sum -= arr[right - k]
        best = max(best, window_sum)

    return best


def averages_of_subarrays(arr, k):
    """Find averages of all contiguous subarrays of size k."""
    result = []
    window_sum = sum(arr[:k])
    result.append(window_sum / k)

    for right in range(k, len(arr)):
        window_sum += arr[right]
        window_sum -= arr[right - k]
        result.append(window_sum / k)

    return result
