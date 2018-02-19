# coding=utf-8
# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def foo(node, mini, maxi):
            if node == None: return False
            if mini < node.val < maxi:
                return foo(node.left, mini, node.val) and foo(node.right, node.val, maxi)
            else:
                return False

        foo(root, -float("inf"), float("inf"))
