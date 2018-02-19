# coding=utf-8
'''
Created on 2017å¹?4æœ?24æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def postorder(node):
            if node == None:
                return 0
            left_sum = postorder(node.left)
            right_sum = postorder(node.right)
            self.ans += abs(left_sum - right_sum)
            return left_sum + right_sum + node.val

        postorder(root)
        return self.ans
