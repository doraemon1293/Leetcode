# coding=utf-8
'''
Created on 2017å¹?6æœ?20æ—?

@author: Administrator
'''
from data_structure.Tree import list_to_tree


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d = {}

        def foo(node):
            if node == None: return True
            if node in d:
                return d[node]
            if (node.left and node.left.val == node.val or node.left == None) and (node.right and node.right.val == node.val or node.right == None):
                d[node] = foo(node.left) and foo(node.right)
                return d[node]
            else:
                foo(node.left)
                foo(node.right)
                d[node] = False
                return False

        foo(root)
        return d.values().count(True)


root = list_to_tree([5, 1, 5, 5, 5, None, 5])
root = list_to_tree([1])

print Solution().countUnivalSubtrees(root)

