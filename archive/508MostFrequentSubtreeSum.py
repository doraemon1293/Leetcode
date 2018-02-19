# coding=utf-8
'''
Created on 2017å¹?2æœ?10æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d = {}

        def foo(node):
            if node == None:
                return 0
            s = foo(node.left) + foo(node.right) + node.val
            d.setdefault(s, 0)
            d[s] += 1
            return s

        maxi = 0
        ans = []
        foo(root)
        for k, v in d.items():
            if v > maxi:
                ans = [k]
                maxi = v
            elif v == maxi:
                ans.append(k)
        return ans

