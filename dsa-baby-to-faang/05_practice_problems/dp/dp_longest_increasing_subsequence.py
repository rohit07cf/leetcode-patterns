"""
Problem: Longest Increasing Subsequence (LeetCode #300)
Pattern: 1D DP / Binary Search
Difficulty: Medium

Baby Explanation:
    Given an array of numbers, find the longest subsequence where each number
    is bigger than the one before it. A subsequence doesn't have to be contiguous
    (you can skip elements). We show two approaches: simple DP and optimized.

Example:
    Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
    Output: 4
    Explanation: One LIS is [2, 3, 7, 18], which has length 4.

Approach (O(n^2) DP):
    1. dp[i] = length of LIS ending at index i (starts at 1).
    2. For each element, check all previous elements.
    3. If nums[j] < nums[i], we can extend that subsequence: dp[i] = max(dp[i], dp[j] + 1).
    4. Answer is max(dp).

Approach (O(n log n) Binary Search):
    1. Maintain a list 'tails' where tails[i] = smallest tail element for LIS of length i+1.
    2. For each number, binary search for its position in tails.
    3. If it's larger than all tails, append it (extend LIS).
    4. Otherwise, replace the first tail >= num (keeps tails as small as possible).
    5. Length of tails = length of LIS.

Time Complexity: O(n^2) for DP, O(n log n) for Binary Search
Space Complexity: O(n) for both approaches
"""


class Solution:
    def lengthOfLIS_dp(self, nums):
        """O(n^2) DP approach - easier to understand."""
        if not nums:
            return 0

        # Step 1: Each element is at least a subsequence of length 1
        dp = [1] * len(nums)

        # Step 2: For each element, check all previous elements
        for i in range(1, len(nums)):
            for j in range(i):
                # Step 3: If nums[j] < nums[i], we can extend
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # Step 4: Answer is the maximum in dp
        return max(dp)

    def lengthOfLIS(self, nums):
        """O(n log n) Binary Search approach - interview optimal."""
        # Step 1: tails[i] = smallest tail for increasing subsequence of length i+1
        tails = []

        for num in nums:
            # Step 2: Binary search for the position of num
            lo, hi = 0, len(tails)
            while lo < hi:
                mid = (lo + hi) // 2
                if tails[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid

            # Step 3: If num is larger than all tails, extend LIS
            if lo == len(tails):
                tails.append(num)
            else:
                # Step 4: Replace to keep tails as small as possible
                tails[lo] = num

        # Step 5: Length of tails = length of LIS
        return len(tails)


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()

    # Test both approaches
    for method in [sol.lengthOfLIS_dp, sol.lengthOfLIS]:
        # Test 1: Standard case
        assert method([10, 9, 2, 5, 3, 7, 101, 18]) == 4

        # Test 2: Already sorted (entire array is the LIS)
        assert method([1, 2, 3, 4, 5]) == 5

        # Test 3: Decreasing (each element alone is a LIS of length 1)
        assert method([5, 4, 3, 2, 1]) == 1

        # Test 4: Edge case - single element
        assert method([7]) == 1

        # Test 5: Duplicates (equal elements don't count as increasing)
        assert method([2, 2, 2]) == 1

    print("All tests passed!")
