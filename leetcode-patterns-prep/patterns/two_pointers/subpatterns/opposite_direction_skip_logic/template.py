"""
Opposite Direction + Skip Logic — Template
"""


def palindrome_skip_non_alnum(s: str) -> bool:
    """Valid Palindrome: ignore non-alphanumeric, case-insensitive."""
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def palindrome_skip_one(s: str) -> bool:
    """Valid Palindrome II: can remove at most one character."""

    def is_palindrome(lo, hi):
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # try skipping left OR skipping right
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -= 1

    return True
