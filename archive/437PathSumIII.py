# coding=utf-8
'''
Created on 2016å¹?11æœ?7æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def path_sum_from_node(self, node, sum):
            if node == None:
                return 0
            return (1 if node.val == sum else 0) + path_sum_from_node(node.left, sum - node.val) + path_sum_from_node(node.right, sum - node.val)

        if root == None:
            return 0
        else:
            return path_sum_from_node(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

