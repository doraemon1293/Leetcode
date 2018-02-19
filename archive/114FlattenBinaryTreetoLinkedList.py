# coding=utf-8
'''
Created on 2017å¹?7æœ?12æ—?

@author: Administrator
'''
from data_structure.Tree import list_to_tree, tree_to_list


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def flatten(root):
            if root.left and root.right:
                left_head, left_tail = flatten(root.left)
                right_head, right_tail = flatten(root.right)
                root.left = None
                root.right = left_head
                left_tail.right = right_head
                return root, right_tail
            elif root.left:
                left_head, left_tail = flatten(root.left)
                root.left = None
                root.right = left_head
                return root, left_tail
            elif root.right:
                right_head, right_tail = flatten(root.right)
                root.right = right_head
                return root, right_tail
            else:
                return root, root

        if root:
            flatten(root)


root = list_to_tree([1, 2, 5, 3, 4, None, 6])
root = list_to_tree([1, 2, None, 3])

Solution().flatten(root)
print tree_to_list(root)
