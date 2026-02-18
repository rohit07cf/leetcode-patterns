"""
Problem: Climbing Stairs (LeetCode #70)
Pattern: 1D DP (Fibonacci Variant)
Difficulty: Easy

Baby Explanation:
    You're climbing a staircase with n steps. Each time you can climb 1 or 2 steps.
    How many different ways can you reach the top? It's just like Fibonacci!
    The number of ways to reach step i = ways to reach (i-1) + ways to reach (i-2).

Example:
    Input: n = 4
    Output: 5
    Explanation: The 5 ways are: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2

Approach:
    1. Base cases: 1 way to reach step 0, 1 way to reach step 1.
    2. For each step from 2 to n, ways = ways(i-1) + ways(i-2).
    3. We only need the last two values, so use two variables instead of an array.
    4. After the loop, return the current value.

Time Complexity: O(n) - single loop from 2 to n
Space Complexity: O(1) - only two variables
"""


class Solution:
    def climbStairs(self, n):
        # Step 1: Base cases
        if n <= 1:
            return 1

        # Step 2: Track only the previous two values
        prev2 = 1  # ways to reach step 0
        prev1 = 1  # ways to reach step 1

        # Step 3: Build up from step 2 to step n
        for i in range(2, n + 1):
            current = prev1 + prev2  # ways(i) = ways(i-1) + ways(i-2)
            prev2 = prev1
            prev1 = current

        # Step 4: Return the answer for step n
        return prev1


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()

    # Test 1: n = 2 -> two ways: (1+1) or (2)
    assert sol.climbStairs(2) == 2

    # Test 2: n = 3 -> three ways: (1+1+1), (1+2), (2+1)
    assert sol.climbStairs(3) == 3

    # Test 3: n = 4 -> five ways
    assert sol.climbStairs(4) == 5

    # Test 4: Edge case - single step
    assert sol.climbStairs(1) == 1

    # Test 5: Larger input
    assert sol.climbStairs(10) == 89

    print("All tests passed!")
