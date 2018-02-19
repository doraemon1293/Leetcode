# coding=utf-8
'''
Created on 2017å¹?7æœ?11æ—?

@author: Administrator
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        self.ans = 0
        self.memo = {}  # nodeä¸ºç»ˆç‚? (a,b) aä¸ºå‘çˆ¶èŠ‚ç‚¹æ–¹å‘é?’å¢çš„æœ€å¤§é•¿åº? bä¸ºé?’å‡

        def foo(node):
            res_0 = res_1 = 1
            if node.left:
                left_0, left_1 = self.memo(node.left) if node.left in self.memo else foo(node.left)
            else:
                left_0 = left_1 = 0
            if node.right:
                right_0, right_1 = self.memo(node.right) if node.right in self.memo else foo(node.right)
            else:
                right_0 = right_1 = 0

            if node.left:
                if node.left.val == node.val - 1:
                    res_0 = max(res_0, left_0 + 1)
                if node.left.val == node.val + 1:
                    res_1 = max(res_1, left_1 + 1)
            if node.right:
                if node.right.val == node.val - 1:
                    res_0 = max(res_0, right_0 + 1)
                if node.right.val == node.val + 1:
                    res_1 = max(res_1, right_1 + 1)

            self.ans = max(self.ans, res_0 + res_1 - 1)
            self.memo[node] = (res_0, res_1)
            return (res_0, res_1)

        foo(root)
#         for k, v in self.memo.items():
#             print k.val, v
#         print self.memo
        return self.ans
