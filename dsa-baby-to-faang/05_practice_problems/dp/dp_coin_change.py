"""
Problem: Coin Change (LeetCode #322)
Pattern: Unbounded Knapsack
Difficulty: Medium

Baby Explanation:
    You have coins of different values and a target amount. Find the fewest
    coins needed to make that exact amount. You can use each coin as many
    times as you want. If it's impossible, return -1.

Example:
    Input: coins = [1, 5, 10], amount = 12
    Output: 3
    Explanation: 10 + 1 + 1 = 12, using 3 coins.

Approach:
    1. Create dp array where dp[i] = fewest coins to make amount i.
    2. Initialize dp[0] = 0 (zero coins needed for amount 0).
    3. Fill all other values with infinity (not yet reachable).
    4. For each amount from 1 to target, try every coin:
       dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    5. If dp[target] is still infinity, return -1.

Time Complexity: O(amount * len(coins)) - nested loop
Space Complexity: O(amount) - the dp array
"""


class Solution:
    def coinChange(self, coins, amount):
        # Step 1: Create dp array, fill with "infinity"
        dp = [float('inf')] * (amount + 1)

        # Step 2: Base case - 0 coins needed for amount 0
        dp[0] = 0

        # Step 3: Fill dp for each amount from 1 to target
        for i in range(1, amount + 1):
            # Step 4: Try each coin
            for coin in coins:
                if coin <= i and dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # Step 5: If still infinity, it's impossible
        return dp[amount] if dp[amount] != float('inf') else -1


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Standard case
    assert sol.coinChange([1, 5, 10], 12) == 3  # 10 + 1 + 1

    # Test 2: Classic example
    assert sol.coinChange([1, 5, 11], 15) == 3  # 5 + 5 + 5

    # Test 3: Impossible case
    assert sol.coinChange([2], 3) == -1  # Can't make 3 with only 2s

    # Test 4: Edge case - amount is 0
    assert sol.coinChange([1], 0) == 0

    # Test 5: Single coin type
    assert sol.coinChange([1], 5) == 5  # 1+1+1+1+1

    print("All tests passed!")
