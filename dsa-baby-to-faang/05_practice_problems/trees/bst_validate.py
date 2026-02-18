"""
Problem: Validate Binary Search Tree (LeetCode #98)
Pattern: DFS with Range (min, max bounds)
Difficulty: Medium

Baby Explanation:
    A valid BST means every node on the left is smaller and every node on the
    right is bigger. We pass down allowed min/max bounds as we go deeper.
    If any node breaks the rules, the tree is NOT a valid BST.

Example:
    Input: root = [5, 1, 4, None, None, 3, 6]
    Output: False
    Explanation: The root is 5, but the right child 4 is less than 5. Invalid!

Approach:
    1. Start with the root and bounds of (-infinity, +infinity).
    2. If the node is None, return True (empty tree is valid).
    3. Check if the node's value is within the allowed (low, high) range.
    4. Recurse left with updated upper bound (must be less than current).
    5. Recurse right with updated lower bound (must be greater than current).

Time Complexity: O(n) - we visit every node once
Space Complexity: O(h) - recursion stack depth
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        def validate(node, low, high):
            # Step 1: Base case - empty node is always valid
            if not node:
                return True

            # Step 2: Check if current node violates the range
            if node.val <= low or node.val >= high:
                return False

            # Step 3: Left child must be less than current node
            # Step 4: Right child must be greater than current node
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        # Start with the widest possible range
        return validate(root, float('-inf'), float('inf'))


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Valid BST
    #       5
    #      / \
    #     3   7
    #    / \
    #   1   4
    root1 = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(7))
    assert sol.isValidBST(root1) == True

    # Test 2: Invalid BST (right child 4 < root 5)
    #       5
    #      / \
    #     1   4
    #        / \
    #       3   6
    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert sol.isValidBST(root2) == False

    # Test 3: Edge case - single node is always valid
    assert sol.isValidBST(TreeNode(1)) == True

    # Test 4: Tricky case - value equal to parent is NOT valid
    #     2
    #    / \
    #   2   2
    root4 = TreeNode(2, TreeNode(2), TreeNode(2))
    assert sol.isValidBST(root4) == False

    print("All tests passed!")
