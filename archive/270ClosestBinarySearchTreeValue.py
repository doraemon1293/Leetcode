# coding=utf-8
'''
Created on 2016å¹?12æœ?1æ—?

@author: Administrator
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root.val == target:
            return root.val
        elif target > root.val:
            if root.right:
                temp = self.closestValue(root.right, target)
                if abs(temp - target) < abs(target - root.val):
                    return temp
                else:
                    return root.val
            else:
                return root.val
        elif target < root.val:
            if root.left:
                temp = self.closestValue(root.left, target)
                if abs(temp - target) < abs(target - root.val):
                    return temp
                else:
                    return root.val
            else:
                return root.val
