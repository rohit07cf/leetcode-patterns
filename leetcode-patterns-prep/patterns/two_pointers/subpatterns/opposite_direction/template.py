"""
Opposite Direction Two Pointers — Template
"""


def opposite_direction(arr, target):
    """
    Sorted array → find pair with target sum.
    Adapt the condition (==, <, >) for your problem.
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]

        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1

    return []


def is_palindrome(s):
    """
    String/array → check if it reads the same forwards and backwards.
    """
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
