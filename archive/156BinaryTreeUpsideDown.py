# coding=utf-8
'''
Created on 2017å¹?5æœ?25æ—?

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

    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None : return None

        def get_sibling_and_parent(node):
            if node.left:
                node.left.sibling = node.right
                node.left.parent = node
                get_sibling_and_parent(node.left)

        get_sibling_and_parent(root)

        node = root
        while node.left:
            node = node.left
        new_root = node
        while node != root:
            node.left = node.sibling
            node.right = node.parent
            node = node.parent
        node.left = node.right = None

        return new_root


root = list_to_tree ([1, 2, 3, 4, 5])
root = list_to_tree([])
new_root = Solution().upsideDownBinaryTree(root)
print tree_to_list(new_root)
