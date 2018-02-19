# coding=utf-8
'''
Created on 2017å¹?3æœ?7æ—?

@author: Administrator
'''
from Tkconstants import SOLID

from data_structure.Tree import list_to_tree


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.last_num = None
        self.ans = float("inf")

        def inorder(node):
            if node != None and self.ans != 0:
                inorder(node.left)
                if self.last_num != None:
                    self.ans = min(self.ans, abs(node.val - self.last_num))
                    self.last_num = node.val
                else:
                    self.last_num = node.val

                inorder(node.right)

        inorder(root)
        return self.ans


root = list_to_tree([1, None, 2, 3])
print Solution().getMinimumDifference(root)

