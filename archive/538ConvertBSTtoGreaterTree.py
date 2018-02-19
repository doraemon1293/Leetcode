# coding=utf-8
'''
Created on 2017å¹?4æœ?18æ—?

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

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.inorder_nodes_arr = []
        self.total = 0

        def inorder(node):
            if node:
                inorder(node.left)
                self.inorder_nodes_arr.append(node)
                self.total += node.val
                inorder(node.right)

        inorder(root)
        for node in self.inorder_nodes_arr:
            self.total -= node.val
            node.val += self.total
        return root


root = list_to_tree([5, 5, 5])
print tree_to_list(Solution().convertBST(root))

