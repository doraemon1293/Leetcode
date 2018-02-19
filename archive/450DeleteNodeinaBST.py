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

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        def find(root, key):
            parent = None
            node = root
            while node:
                if key == node.val:
                    return parent, node
                elif key < node.val:
                    parent = node
                    node = node.left
                else:
                    parent = node
                    node = node.right
            return None, None

        parent, node = find(root, key)
        if (parent, node) != (None, None):
            if node.left:
                parent, p = node, node.left
                while p.right:
                    parent = p
                    p = p.right
                if parent != node:
                    parent.right = p.left
                else:
                    parent.left = p.left
                node.val = p.val
                return root

            elif node.right:
                parent, p = node, node.right
                while p.left:
                    parent = p
                    p = p.left
                if parent != node:
                    parent.left = p.right
                else:
                    parent.right = p.right
                node.val = p.val
                return root

            elif parent:
                if parent.left == node: parent.left = None
                if parent.right == node: parent.right = None
                return root
            else:
                return None
        else:
            return root


root = list_to_tree([5, 3, 6, 2, 4, None, 7])
root = list_to_tree([2, 1, 3])
root = list_to_tree([3, 2, 4, 1])

key = 3
root = Solution().deleteNode(root, key)
print tree_to_list(root)
