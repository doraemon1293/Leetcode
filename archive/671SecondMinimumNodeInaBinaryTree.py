# coding=utf-8
'''
Created on 2017å¹?9æœ?3æ—?

@author: Administrator
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        q = deque([root])
        min_val = root.val
        second_min_val = float("inf")
        node = root
        while q:
            new_q = []
            for node in q:
                if node.left:
                    if node.left.val == min_val:
                        new_q.append(node.left)
                    elif node.left.val < second_min_val:
                        second_min_val = node.left.val
                if node.right:
                    if node.right.val == min_val:
                        new_q.append(node.right)
                    elif node.right.val < second_min_val:
                        second_min_val = node.right.val
            q = new_q
        if second_min_val == float("inf"):
            return -1
        else:
            return second_min_val

