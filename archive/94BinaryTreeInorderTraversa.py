# coding=utf-8
'''
Created on 2016�?11�?17�?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []

        def inorder(node):
            if node:
                inorder(node.left)
                arr.append(node.val)
                inorder(node.right)

        inorder(root)
        return arr

