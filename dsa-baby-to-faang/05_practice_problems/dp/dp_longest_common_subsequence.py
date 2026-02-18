"""
Problem: Longest Common Subsequence (LeetCode #1143)
Pattern: 2D DP
Difficulty: Medium

Baby Explanation:
    Given two strings, find the length of their longest common subsequence.
    A subsequence is characters in order but not necessarily next to each other.
    For example, "ace" is a subsequence of "abcde". We build a 2D table comparing
    characters from both strings.

Example:
    Input: text1 = "abcde", text2 = "ace"
    Output: 3
    Explanation: The longest common subsequence is "ace", which has length 3.

Approach:
    1. Create a 2D table dp[i][j] = LCS length for text1[:i] and text2[:j].
    2. If characters match (text1[i-1] == text2[j-1]), take diagonal + 1.
    3. If they don't match, take the max of left cell or top cell.
    4. Fill the table row by row.
    5. dp[m][n] is the answer (bottom-right corner).

Time Complexity: O(m * n) - fill the entire table
Space Complexity: O(m * n) - the 2D table
"""


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)

        # Step 1: Create (m+1) x (n+1) table initialized to 0
        # Extra row/col of 0s for the base case (empty string)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Step 2: Fill the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Step 3: Characters match - extend the LCS
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Step 4: Don't match - take the best without one char
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Step 5: Answer is in the bottom-right corner
        return dp[m][n]


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard case
    assert sol.longestCommonSubsequence("abcde", "ace") == 3  # "ace"

    # Test 2: One string is subsequence of the other
    assert sol.longestCommonSubsequence("abc", "abc") == 3

    # Test 3: No common subsequence
    assert sol.longestCommonSubsequence("abc", "def") == 0

    # Test 4: Single character match
    assert sol.longestCommonSubsequence("a", "a") == 1

    # Test 5: Longer example
    assert sol.longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy") == 2

    # Test 6: Edge case - empty string
    assert sol.longestCommonSubsequence("", "abc") == 0

    print("All tests passed!")
