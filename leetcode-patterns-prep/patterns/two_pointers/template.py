"""
Two Pointers — Master Template
Copy-paste friendly. Adapt the condition for your specific problem.
"""


# ─── OPPOSITE DIRECTION ───────────────────────────────────────────
def two_pointer_opposite(arr, target):
    """
    Use when: sorted array, find pair, palindrome check, squeeze from ends.
    Key invariant: everything outside [left, right] is already processed.
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]  # ← adapt this condition

        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1

    return []


# ─── SAME DIRECTION (IN-PLACE MODIFY) ─────────────────────────────
def two_pointer_same_direction(arr):
    """
    Use when: remove duplicates, remove element, compact array in-place.
    Key invariant: arr[0..write-1] contains the "kept" elements.
    """
    write = 0

    for read in range(len(arr)):
        if True:  # ← replace with your keep-condition
            arr[write] = arr[read]
            write += 1

    return write  # new length of modified array


# ─── FIX ONE + TWO POINTERS (3SUM STYLE) ──────────────────────────
def three_sum(arr, target=0):
    """
    Use when: find triplets, 3Sum, 3Sum Closest.
    Key invariant: fix arr[i], then two-pointer on arr[i+1..n-1].
    """
    arr.sort()
    result = []

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue  # skip duplicate fixed element

        left, right = i + 1, len(arr) - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == target:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1  # skip duplicates
            elif total < target:
                left += 1
            else:
                right -= 1

    return result
