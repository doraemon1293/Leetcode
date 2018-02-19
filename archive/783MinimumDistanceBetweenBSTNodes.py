# coding=utf-8
'''
Created on 12 Feb 2018

@author: Administrator
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.lastNum = None
        self.ans = float("inf")

        def inorder(node):
            if node != None and self.ans != 0:
                inorder(node.left)
                if self.lastNum != None:
                    self.ans = min(self.ans, node.val - self.lastNum)
                self.lastNum = node.val
                inorder(node.right)

        inorder(root)
        return self.ans

