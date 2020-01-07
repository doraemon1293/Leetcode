# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left = (root.left is None or root.val == root.left.val) and self.isUnivalTree(root.left)
        right = (root.right is None or root.val == root.right.val) and self.isUnivalTree(root.right)
        return left and right
