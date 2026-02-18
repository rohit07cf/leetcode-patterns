"""
Problem: Number of Islands (LeetCode #200)
Pattern: Grid BFS / Flood Fill
Difficulty: Medium

Baby Explanation:
    We have a 2D grid of '1's (land) and '0's (water). An island is a group of
    connected '1's (up, down, left, right). We need to count how many separate
    islands exist. Each time we find a '1', we BFS to mark the entire island visited.

Example:
    Input: grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    Output: 3
    Explanation: There are 3 separate groups of connected '1's.

Approach:
    1. Loop through every cell in the grid.
    2. When we find an unvisited '1', that's a new island - increment count.
    3. BFS from that cell, marking all connected '1's as '0' (visited).
    4. Continue scanning for the next unvisited '1'.
    5. Return the total island count.

Time Complexity: O(m * n) - we visit every cell at most once
Space Complexity: O(m * n) - the queue can hold all cells in worst case
"""

from collections import deque


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            # Step 3: BFS to mark all connected land as visited
            queue = deque([(r, c)])
            grid[r][c] = '0'  # Mark as visited

            while queue:
                row, col = queue.popleft()
                # Check all 4 directions: up, down, left, right
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = row + dr, col + dc
                    # If in bounds and is land, mark visited and add to queue
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        queue.append((nr, nc))

        # Step 1: Scan every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # Step 2: Found a new island
                if grid[r][c] == '1':
                    bfs(r, c)
                    count += 1

        # Step 5: Return total number of islands
        return count


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Multiple islands
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert sol.numIslands(grid1) == 3

    # Test 2: One big island
    grid2 = [
        ["1", "1", "1"],
        ["1", "1", "1"]
    ]
    assert sol.numIslands(grid2) == 1

    # Test 3: Edge case - all water
    grid3 = [["0", "0"], ["0", "0"]]
    assert sol.numIslands(grid3) == 0

    print("All tests passed!")
