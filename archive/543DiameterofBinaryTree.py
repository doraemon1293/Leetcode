# coding=utf-8
'''
Created on 2017å¹?3æœ?28æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1

        def depth(node):
            if node == None:
                return 0
            depth_left = depth(node.left)
            depth_right = depth(node.right)
            self.ans = max(self.ans, depth_left + depth_right + 1)
            return max(depth_left, depth_right) + 1

        depth(root)
        return self.ans - 1
