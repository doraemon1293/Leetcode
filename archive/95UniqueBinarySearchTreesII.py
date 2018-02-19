# coding=utf-8
'''
Created on 2017å¹?5æœ?10æ—?

@author: Administrator
'''
from data_structure.Tree import tree_to_list


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def trees(st, en):
            if st > en:
                return [None]
            if st == en:
                return [TreeNode(st)]
            res = []
            for i in range(st, en + 1):
                for left_tree in trees(st, i - 1):
                    for right_tree in trees(i + 1, en):
                        node = TreeNode(i)
                        node.left = left_tree
                        node.right = right_tree
                        res.append(node)
            return res

        if n:
            return trees(1, n)
        else:
            return []


print Solution().generateTrees(3)
