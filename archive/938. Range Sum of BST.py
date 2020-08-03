# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        def solve(root):
            res = 0
            if root:
                if L <= root.val <= R:
                    res += root.val
                if root.val > L and root.left:
                    res += solve(root.left)
                if root.val < R and root.right:
                    res += solve(root.right)
            return res

        return solve(root)
