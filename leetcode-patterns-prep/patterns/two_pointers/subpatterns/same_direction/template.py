"""
Same Direction Two Pointers (In-Place Modify) — Template
"""


def remove_element(arr, val):
    """Remove all occurrences of val in-place. Return new length."""
    write = 0

    for read in range(len(arr)):
        if arr[read] != val:
            arr[write] = arr[read]
            write += 1

    return write


def remove_duplicates_sorted(arr):
    """Remove duplicates from sorted array in-place. Return new length."""
    if not arr:
        return 0

    write = 1  # first element is always kept

    for read in range(1, len(arr)):
        if arr[read] != arr[write - 1]:  # compare with last written
            arr[write] = arr[read]
            write += 1

    return write
