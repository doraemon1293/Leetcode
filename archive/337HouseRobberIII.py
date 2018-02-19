# coding=utf-8
'''
Created on 2017å¹?5æœ?25æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        memo = {None:0}

        def rob(node):
            if node in memo:
                return memo[node]
            else:
                memo[node] = max((node.val + ((rob(node.left.left) + rob(node.left.right)) if node.left else 0) + \
                                           ((rob(node.right.left) + rob(node.right.right)) if node.right else 0)),
                                          rob(node.left) + rob(node.right)
                                          )

                return memo[node]

        return rob(root)

