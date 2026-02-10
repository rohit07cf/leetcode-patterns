"""
Binary Search — Master Template
Copy-paste friendly. Three variants for different problem types.
"""


# ─── CLASSIC BINARY SEARCH ─────────────────────────────────────────
def binary_search_classic(arr, target):
    """
    Use when: find exact target in sorted array.
    Key: while left <= right (inclusive bounds).
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ─── BOUNDARY BINARY SEARCH (FIRST TRUE) ──────────────────────────
def first_true(arr, condition):
    """
    Use when: find first element where condition is True.
    Key: while left < right (converging bounds).
    """
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if condition(arr[mid]):
            right = mid         # mid could be the answer
        else:
            left = mid + 1      # mid is too small

    return left  # left == right == first True


# ─── BINARY SEARCH ON ANSWER SPACE ────────────────────────────────
def binary_search_on_answer(lo, hi, check):
    """
    Use when: searching for minimum value that satisfies check().
    Requires: check is monotonic (False, False, ..., True, True, ...).
    """
    while lo < hi:
        mid = lo + (hi - lo) // 2

        if check(mid):
            hi = mid        # mid works, try smaller
        else:
            lo = mid + 1    # mid doesn't work, try bigger

    return lo  # lo == hi == answer
