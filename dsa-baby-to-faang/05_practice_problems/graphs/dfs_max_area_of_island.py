"""
Problem: Max Area of Island (LeetCode #695)
Pattern: Grid DFS
Difficulty: Medium

Baby Explanation:
    We have a grid of 1's (land) and 0's (water). Each island is a group of
    connected 1's. We need to find the island with the biggest area (most cells).
    We DFS from each '1', counting cells, and track the largest area found.

Example:
    Input: grid = [
        [0,0,1,0,0],
        [0,0,1,1,0],
        [0,0,0,1,1]
    ]
    Output: 5
    Explanation: The connected group of 1's has 5 cells total.

Approach:
    1. Loop through every cell in the grid.
    2. When we find a '1', DFS to count the area of that island.
    3. During DFS, mark cells as 0 (visited) and count each cell.
    4. Track the maximum area across all islands.
    5. Return the maximum area found.

Time Complexity: O(m * n) - we visit every cell at most once
Space Complexity: O(m * n) - recursion stack in worst case
"""


class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            # Step 3: Base case - out of bounds or water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            # Mark as visited
            grid[r][c] = 0

            # Count this cell (1) plus all connected cells
            area = 1
            area += dfs(r - 1, c)  # up
            area += dfs(r + 1, c)  # down
            area += dfs(r, c - 1)  # left
            area += dfs(r, c + 1)  # right
            return area

        # Step 1: Scan every cell
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Step 2: DFS to get island area
                    area = dfs(r, c)
                    # Step 4: Track the maximum
                    max_area = max(max_area, area)

        # Step 5: Return the biggest island
        return max_area


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()

    # Test 1: One island with area 5
    grid1 = [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1]
    ]
    assert sol.maxAreaOfIsland(grid1) == 5

    # Test 2: Multiple islands, pick the largest
    grid2 = [
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 1]
    ]
    assert sol.maxAreaOfIsland(grid2) == 3

    # Test 3: Edge case - all water
    grid3 = [[0, 0], [0, 0]]
    assert sol.maxAreaOfIsland(grid3) == 0

    # Test 4: Edge case - single cell island
    grid4 = [[0, 1, 0]]
    assert sol.maxAreaOfIsland(grid4) == 1

    print("All tests passed!")
