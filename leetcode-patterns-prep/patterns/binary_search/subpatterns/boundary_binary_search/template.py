"""
Boundary Binary Search (First/Last Occurrence) — Template
"""


def find_first(arr, target):
    """Find leftmost index of target. Return -1 if not found."""
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1    # keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def find_last(arr, target):
    """Find rightmost index of target. Return -1 if not found."""
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1     # keep searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def first_bad_version(n, isBadVersion):
    """Find the first bad version in [1..n]."""
    left, right = 1, n

    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid        # mid could be first bad
        else:
            left = mid + 1     # mid is good, first bad is after

    return left
