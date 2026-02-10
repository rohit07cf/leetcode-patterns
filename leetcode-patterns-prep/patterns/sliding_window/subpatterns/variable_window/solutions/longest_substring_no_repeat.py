"""
Longest Substring Without Repeating Characters (LeetCode 3)

WHY THIS PATTERN: "longest substring" + "without repeating" = variable sliding window.
We expand right to explore new chars, shrink left when we find a duplicate.

KEY INVARIANT: window [left..right] always contains unique characters.
The dict tracks character counts in the current window.

TIME:  O(N) — each char enters and leaves the window at most once
SPACE: O(min(N, 26)) — at most 26 lowercase letters (or full charset)
"""


def length_of_longest_substring(s: str) -> int:
    left = 0
    best = 0
    char_count = {}

    for right in range(len(s)):
        # EXPAND: add the new character
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1

        # SHRINK: while we have a duplicate (count > 1)
        while char_count[char] > 1:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        # UPDATE: window is valid (all unique)
        best = max(best, right - left + 1)

    return best


# --- Quick test ---
if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3 ("abc")
    print(length_of_longest_substring("bbbbb"))      # 1 ("b")
    print(length_of_longest_substring("pwwkew"))     # 3 ("wke")
