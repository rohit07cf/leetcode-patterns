"""
Merge Sort — Template
Focus: the merge step (the most interview-relevant part).
"""


def merge_sort(arr):
    """Sort array using merge sort. Returns new sorted array."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """Merge two sorted arrays into one sorted array."""
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= for stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_count_inversions(arr):
    """
    Sort + count inversions (pairs where i < j but arr[i] > arr[j]).
    Returns (sorted_array, inversion_count).
    """
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = merge_sort_count_inversions(arr[:mid])
    right, right_inv = merge_sort_count_inversions(arr[mid:])

    merged = []
    inversions = left_inv + right_inv
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i  # all remaining left elements are > right[j]
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions
