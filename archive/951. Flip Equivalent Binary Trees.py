# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def equal(root1, root2):
            if root1 == root2 == None:
                return True
            if root1 == None or root2 == None:
                return False
            if root1.val == root2.val:
                return equal(root1.left, root2.left) and equal(root1.right, root2.right) or \
                       equal(root1.left,root2.right) and equal(root1.right, root2.left)
            else:
                return False

        return equal(root1, root2)
