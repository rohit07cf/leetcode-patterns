"""
Problem: Lowest Common Ancestor of a Binary Tree (LeetCode #236)
Pattern: DFS Postorder
Difficulty: Medium

Baby Explanation:
    Given two nodes p and q in a tree, find their lowest common ancestor (LCA).
    The LCA is the deepest node that is an ancestor of both p and q.
    We search left and right; if we find one on each side, the current node is the LCA.

Example:
    Input: root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1
    Output: 3
    Explanation: Node 5 is in the left subtree, node 1 is in the right subtree,
                 so node 3 (the root) is their lowest common ancestor.

Approach:
    1. If the current node is None, or equals p, or equals q, return it.
    2. Recursively search for p and q in the left subtree.
    3. Recursively search for p and q in the right subtree.
    4. If both sides return non-null, current node is the LCA.
    5. Otherwise, return whichever side found something.

Time Complexity: O(n) - we visit every node once
Space Complexity: O(h) - recursion stack depth
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # Step 1: Base case - reached null, or found p or q
        if not root or root == p or root == q:
            return root

        # Step 2: Search in left subtree
        left = self.lowestCommonAncestor(root.left, p, q)

        # Step 3: Search in right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # Step 4: If both sides found something, this node is the LCA
        if left and right:
            return root

        # Step 5: Otherwise return whichever side found a result
        return left if left else right


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()

    # Test 1: LCA is the root
    #       3
    #      / \
    #     5   1
    #    / \
    #   6   2
    node5 = TreeNode(5, TreeNode(6), TreeNode(2))
    node1 = TreeNode(1)
    root1 = TreeNode(3, node5, node1)
    assert sol.lowestCommonAncestor(root1, node5, node1) == root1

    # Test 2: LCA is one of the nodes itself (p is ancestor of q)
    #       3
    #      /
    #     5
    #    /
    #   6
    node6 = TreeNode(6)
    node5 = TreeNode(5, node6)
    root2 = TreeNode(3, node5)
    assert sol.lowestCommonAncestor(root2, node5, node6) == node5

    # Test 3: Edge case - two nodes in a simple tree
    #     1
    #    / \
    #   2   3
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root3 = TreeNode(1, node2, node3)
    assert sol.lowestCommonAncestor(root3, node2, node3) == root3

    print("All tests passed!")
