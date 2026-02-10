"""
Quick Sort — Template
Focus: the partition step (the most interview-relevant part).
"""

import random


def quicksort(arr, lo=None, hi=None):
    """Sort arr in-place using quicksort."""
    if lo is None:
        lo, hi = 0, len(arr) - 1

    if lo < hi:
        pivot_idx = partition(arr, lo, hi)
        quicksort(arr, lo, pivot_idx - 1)
        quicksort(arr, pivot_idx + 1, hi)


def partition(arr, lo, hi):
    """
    Lomuto partition with random pivot.
    After partition: arr[lo..i-1] <= pivot, arr[i] = pivot, arr[i+1..hi] > pivot.
    """
    # Random pivot to avoid O(N^2) on sorted input
    rand_idx = random.randint(lo, hi)
    arr[rand_idx], arr[hi] = arr[hi], arr[rand_idx]

    pivot = arr[hi]
    i = lo  # next position for elements <= pivot

    for j in range(lo, hi):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Place pivot in its final position
    arr[i], arr[hi] = arr[hi], arr[i]
    return i


def quickselect(arr, k, lo=None, hi=None):
    """
    Find Kth smallest element (0-indexed) in O(N) average.
    Uses partition to narrow down to the Kth position.
    """
    if lo is None:
        lo, hi = 0, len(arr) - 1

    pivot_idx = partition(arr, lo, hi)

    if pivot_idx == k:
        return arr[k]
    elif pivot_idx < k:
        return quickselect(arr, k, pivot_idx + 1, hi)
    else:
        return quickselect(arr, k, lo, pivot_idx - 1)
