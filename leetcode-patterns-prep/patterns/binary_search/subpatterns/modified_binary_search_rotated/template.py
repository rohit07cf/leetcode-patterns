"""
Modified Binary Search (Rotated / Special Arrays) — Template
"""


def search_rotated(arr, target):
    """Search target in a rotated sorted array (no duplicates)."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        if arr[left] <= arr[mid]:
            # Left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def find_min_rotated(arr):
    """Find minimum element in rotated sorted array."""
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] > arr[right]:
            left = mid + 1      # min is in right half
        else:
            right = mid          # min could be mid

    return arr[left]


def find_peak_element(arr):
    """Find any peak element (greater than neighbors)."""
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1      # peak is to the right
        else:
            right = mid          # peak is at mid or to the left

    return left  # index of peak
