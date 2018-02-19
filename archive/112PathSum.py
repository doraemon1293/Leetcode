# coding=utf-8
'''
Created on 2016å¹?11æœ?11æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        def dfs(node, sum):
            if node.left == None and node.right == None:
                if node.val == sum:
                    return True
                else:
                    return False
            else:
                return (dfs(node.left, sum - node.val) if node.left else False) or (dfs(node.right, sum - node.val) if node.right else False)

        if root:
            return dfs(root, sum)
        else:
            return False
