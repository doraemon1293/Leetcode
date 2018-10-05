# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        def search(root, val):
            if root:
                if root.val == val:
                    return root
                elif val < root.val:
                    return search(root.left, val)
                else:
                    return search(root.right, val)
            else:
                return None

        return search(root, val)
