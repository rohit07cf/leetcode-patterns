"""
Problem: Maximum Depth of Binary Tree (LeetCode #104)
Pattern: DFS Postorder
Difficulty: Easy

Baby Explanation:
    We want to find how "tall" a binary tree is. The depth is the number
    of nodes along the longest path from the root down to the farthest leaf.
    We check both sides and pick the deeper one, then add 1 for the current node.

Example:
    Input: root = [3, 9, 20, None, None, 15, 7]
    Output: 3
    Explanation: The longest path is 3 -> 20 -> 15 (or 3 -> 20 -> 7), which has 3 nodes.

Approach:
    1. If the node is None, return 0 (no depth).
    2. Recursively find the max depth of the left subtree.
    3. Recursively find the max depth of the right subtree.
    4. Return the bigger of the two depths, plus 1 for the current node.

Time Complexity: O(n) - we visit every node once
Space Complexity: O(h) - recursion stack, where h is the height of the tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        # Step 1: Base case - empty node has depth 0
        if not root:
            return 0

        # Step 2: Get the max depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Step 3: Current depth = 1 (this node) + deeper subtree
        return 1 + max(left_depth, right_depth)


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Normal tree with depth 3
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.maxDepth(root1) == 3

    # Test 2: Skewed tree (like a linked list)
    root2 = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert sol.maxDepth(root2) == 3

    # Test 3: Edge case - empty tree
    assert sol.maxDepth(None) == 0

    # Test 4: Edge case - single node
    assert sol.maxDepth(TreeNode(1)) == 1

    print("All tests passed!")
