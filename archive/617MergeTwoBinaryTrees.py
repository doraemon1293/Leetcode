# coding=utf-8
'''
Created on 2017å¹?6æœ?11æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        def add(t1, t2):
            if t1 == None and t2 == None:
                return None
            if t1 == None and t2:
                root = TreeNode(t2.val)
                root.left = add(None, t2.left)
                root.right = add(None, t2.right)
            if t1 and t2 == None:
                root = TreeNode(t1.val)
                root.left = add(t1.left, None)
                root.right = add(t1.right, None)
            if t1 and t2:
                root = TreeNode(t1.val + t2.val)
                root.left = add(t1.left, t2.left)
                root.right = add(t1.right, t2.right)
            return root

        return add(t1, t2)
