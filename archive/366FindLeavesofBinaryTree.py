# coding=utf-8
'''
Created on 2016å¹?12æœ?13æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []

        def height(node):
            if node == None:
                return -1
            h = max(height(node.left), height(node.right)) + 1
            if h >= len(ans):
                ans.append([])
            ans[h].append(node.val)
            return h

        height(root)
        return ans

