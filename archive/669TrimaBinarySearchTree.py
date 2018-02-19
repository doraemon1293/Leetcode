# coding=utf-8
'''
Created on 2017å¹?9æœ?3æ—?

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

    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        def trim(root):
            if root:
                left = trim(root.left)
                right = trim(root.right)
                root.left = left
                root.right = right
                if root.val < L:
                    return root.right
                if root.val > R:
                    return root.left
                else:
                    return root
            else:
                return root

        root = trim(root)
        return root


root = list_to_tree([3, 0, 4, None, 2, None, None, 1])
L = 1
R = 3
print tree_to_list(Solution().trimBST(root, L, R))

