"""
Problem: Diameter of Binary Tree (LeetCode #543)
Pattern: Tree DP / DFS Postorder
Difficulty: Easy

Baby Explanation:
    The diameter is the longest path between ANY two nodes in the tree.
    This path may or may not pass through the root. At each node, the longest
    path through it equals left height + right height. We track the global max.

Example:
    Input: root = [1, 2, 3, 4, 5]
    Output: 3
    Explanation: The longest path is 4 -> 2 -> 1 -> 3 (or 5 -> 2 -> 1 -> 3),
                 which has length 3 (edges, not nodes).

Approach:
    1. Use a variable to track the maximum diameter seen so far.
    2. For each node, compute the height of its left and right subtrees.
    3. The diameter through this node = left_height + right_height.
    4. Update the global max if this diameter is bigger.
    5. Return the height of this node (1 + max of children) to the parent.

Time Complexity: O(n) - we visit every node once
Space Complexity: O(h) - recursion stack depth
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):
        # Step 1: Track the best diameter we've found
        self.max_diameter = 0

        def height(node):
            # Step 2: Base case - null node has height 0
            if not node:
                return 0

            # Step 3: Get heights of left and right subtrees
            left_h = height(node.left)
            right_h = height(node.right)

            # Step 4: Diameter through this node = left + right heights
            self.max_diameter = max(self.max_diameter, left_h + right_h)

            # Step 5: Return this node's height to its parent
            return 1 + max(left_h, right_h)

        height(root)
        return self.max_diameter


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Diameter passes through root
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert sol.diameterOfBinaryTree(root1) == 3

    # Test 2: Diameter does NOT pass through root
    #       1
    #      /
    #     2
    #    / \
    #   3   4
    #  /     \
    # 5       6
    left = TreeNode(2, TreeNode(3, TreeNode(5)), TreeNode(4, None, TreeNode(6)))
    root2 = TreeNode(1, left)
    assert sol.diameterOfBinaryTree(root2) == 4

    # Test 3: Edge case - single node (diameter = 0)
    assert sol.diameterOfBinaryTree(TreeNode(1)) == 0

    print("All tests passed!")
