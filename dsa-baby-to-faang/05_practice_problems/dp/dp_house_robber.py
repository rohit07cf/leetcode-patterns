"""
Problem: House Robber (LeetCode #198)
Pattern: 1D DP
Difficulty: Medium

Baby Explanation:
    You're a robber and there's a row of houses with money. You can't rob two
    houses next to each other (alarms will go off!). What's the maximum money
    you can steal? At each house, you decide: rob it (skip previous) or skip it.

Example:
    Input: nums = [2, 7, 9, 3, 1]
    Output: 12
    Explanation: Rob houses 0, 2, 4 (values 2 + 9 + 1 = 12).

Approach:
    1. dp[i] = max money we can rob from houses 0 to i.
    2. At each house: either rob it (dp[i-2] + nums[i]) or skip it (dp[i-1]).
    3. dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    4. Optimize space: only need previous two values.
    5. Return the final value.

Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - only two variables
"""


class Solution:
    def rob(self, nums):
        # Step 1: Handle edge cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Step 2: Initialize - prev2 is dp[i-2], prev1 is dp[i-1]
        prev2 = 0        # max money before the previous house
        prev1 = nums[0]  # max money including first house

        # Step 3: For each house, pick the better choice
        for i in range(1, len(nums)):
            # Rob this house (prev2 + nums[i]) OR skip it (prev1)
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current

        # Step 4: Return the maximum money
        return prev1


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Skip alternating houses
    assert sol.rob([2, 7, 9, 3, 1]) == 12  # Rob 2 + 9 + 1

    # Test 2: Two houses
    assert sol.rob([1, 2]) == 2

    # Test 3: Adjacent houses with varying values
    assert sol.rob([2, 1, 1, 2]) == 4  # Rob first and last

    # Test 4: Edge case - single house
    assert sol.rob([5]) == 5

    # Test 5: All same values
    assert sol.rob([3, 3, 3, 3]) == 6  # Rob 1st and 3rd (or 2nd and 4th)

    print("All tests passed!")
