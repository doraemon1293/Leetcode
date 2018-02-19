# coding=utf-8
'''
Created on 13 Feb 2018

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """

        def foo(node):
            if node == None:
                return None, None
            if node.val <= V:
                left, right = foo(node.right)
                node.right = left
                return node, right
            else:
                left, right = foo(node.left)
                node.left = right
                return left, node

        return foo(root)

