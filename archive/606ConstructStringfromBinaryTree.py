# coding=utf-8
'''
Created on 2017å¹?6æœ?5æ—?

@author: Administrator
'''
from data_structure.Tree import tree_to_list, list_to_tree


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """

        def foo(node):
            if node:
                if node.right:
                    return str(node.val) + "(" + foo(node.left) + ")" + "(" + foo(node.right) + ")"
                if node.left and (not node.right):
                    return str(node.val) + "(" + foo(node.left) + ")"
                if (not node.left) and (not node.right):
                    return str(node.val)
            else:
                return ""

        return foo(t)


t = list_to_tree([1, 2, 3, None, 4])
print Solution().tree2str(t)
