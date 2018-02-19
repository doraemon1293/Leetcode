# coding=utf-8
'''
Created on 2016å¹?11æœ?9æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def depth(node):
            if node == None: return 0
            a = depth(node.left)
            b = depth(node.right)
            if a == -1 or b == -1 or abs(a - b) > 1:
                return -1
            else:
                return max(a, b) + 1

        return depth(root) != -1

