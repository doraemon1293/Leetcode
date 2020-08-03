# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        d1 = set()
        d2 = set()

        def inorder(r, d):
            if r:
                inorder(r.left, d)
                d.add(r.val)
                inorder(r.right, d)

        inorder(root1, d1)
        inorder(root2, d2)
        for x in d1:
            if target - x in d2:
                return True
        return False



