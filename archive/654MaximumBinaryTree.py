# coding=utf-8
'''
Created on 2017å¹?8æœ?6æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def foo(nums):
            if nums == []:
                return None
            maxv = -float("inf")
            for i, num in enumerate(nums):
                if num > maxv:
                    maxInd = i
                    maxv = num
            root = TreeNode(maxv)
            root.left = foo(num[:maxInd])
            root.right = foo(num[maxInd + 1:])
            return root

        return foo(nums)

                if
