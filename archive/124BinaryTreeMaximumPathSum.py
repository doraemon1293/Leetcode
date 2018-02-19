# coding=utf-8
'''
Created on 2017å¹?7æœ?7æ—?

@author: Administrator
'''
from data_structure.Tree import list_to_tree


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.d = {}
        self.ans = -float("inf")

        def pathSum(node):
            if node == None: return 0
            if node in self.d: return self.d[node]
            left = max(pathSum(node.left), 0)
            right = max(pathSum(node.right), 0)
            res = max(left, right) + node.val
            self.ans = max(self.ans, left + right + node.val)
            self.d[node] = res
            return res

        pathSum(root)
        # print self.d
        return self.ans


root = list_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
print Solution().maxPathSum(root)
