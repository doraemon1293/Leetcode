# coding=utf-8
'''
Created on 2017å¹?2æœ?1æ—?

@author: Administrator
'''
import collections


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import Counter
        d = {}

        def traversal(node):
            if node:
                traversal(node.left)
                d.setdefault(node.val, 0)
                d[node.val] += 1
                traversal(node.right)

        traversal(root)
        ans = []
        maxi = -1
        for k, v in d.items():
            if v > maxi:
                ans = [k]
                maxi = v
            elif v == maxi:
                ans.append(k)
        return ans

