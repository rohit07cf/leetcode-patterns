"""
Problem: Binary Tree Level Order Traversal (LeetCode #102)
Pattern: BFS with Deque
Difficulty: Medium

Baby Explanation:
    We want to visit the tree level by level, left to right. Think of it like
    reading a book line by line. We use a queue: process all nodes on the current
    level, then move to the next level. Each level becomes a list in our result.

Example:
    Input: root = [3, 9, 20, None, None, 15, 7]
    Output: [[3], [9, 20], [15, 7]]
    Explanation: Level 0 has [3], level 1 has [9, 20], level 2 has [15, 7].

Approach:
    1. Start with the root in a queue.
    2. For each level, count how many nodes are in the queue (that's the level size).
    3. Process exactly that many nodes, adding their values to the current level list.
    4. Add each node's children to the queue for the next level.
    5. Append the level list to our result.

Time Complexity: O(n) - we visit every node once
Space Complexity: O(n) - the queue can hold up to n/2 nodes (bottom level)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        # Step 1: Handle empty tree
        if not root:
            return []

        result = []
        queue = deque([root])

        # Step 2: Process level by level
        while queue:
            level_size = len(queue)
            current_level = []

            # Step 3: Process all nodes at this level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                # Step 4: Add children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Step 5: Add this level's values to result
            result.append(current_level)

        return result


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Normal tree
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.levelOrder(root1) == [[3], [9, 20], [15, 7]]

    # Test 2: Single node
    assert sol.levelOrder(TreeNode(1)) == [[1]]

    # Test 3: Edge case - empty tree
    assert sol.levelOrder(None) == []

    # Test 4: Left-skewed tree
    root4 = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert sol.levelOrder(root4) == [[1], [2], [3]]

    print("All tests passed!")
