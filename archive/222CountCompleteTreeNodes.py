# coding=utf-8
'''
Created on 2017å¹?7æœ?13æ—?

@author: Administrator
'''
from data_structure.Tree import list_to_tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def height(node):
            res = -1
            while node:
                node = node.left
                res += 1
            return res

        def count(root):
            if root == None: return 0
            left_height = height(root.left)
            right_height = height(root.right)
            if left_height == right_height:
                return 1 + 2 ** (left_height + 1) - 1 + count(root.right)
            else:
                return 1 + count(root.left) + 2 ** (right_height + 1) - 1

        return count(root)


root = list_to_tree([1, 2, 3, 4, 5, 6])
print Solution().countNodes(root)
