# coding=utf-8
'''
Created on 2017å¹?10æœ?1æ—?

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

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d = {}
        self.ans = 0

        def foo(root):
            if root in d:
                return d[root]
            if root.left and root.right and  root.val == root.left.val == root.right.val:
                self.ans = max(self.ans, 2 + foo(root.left) + foo(root.right))
            res = 0
            if root.left and root.val == root.left.val:
                res = max(res, 1 + foo(root.left))
            if root.right and root.val == root.right.val:
                res = max(res, 1 + foo(root.right))
            d[root] = res
            self.ans = max(self.ans, res)
            return res

        if root == None: return 0

        def inorder(node):
            if node:
                foo(node)
                inorder(node.left)
                inorder(node.right)

        inorder(root)
        return self.ans


root = list_to_tree([1, 4, 5, 4, 4, 5])
root = list_to_tree([26, 26, 26, 26, 26, 24, 26, 25, 25, 25, 27, 23, 25, 25, 27, 24, 26, 24, 26, 24, 24, None, 28, None, None, 26, None, None, 26, 26, 28, 25, None, 25, 27, None, None, None, None, None, 23, None, None, 29, 27, None, None, None, None, 25, None, 27, 27, 24, 26, 24, 26, 26, 26, None, 22, 28, None, 26, 26, None, None, 26, None, 28, 28, 25, None, None, None, 25, 25, 25, 27, 25, 25, 27, 25, None, None, None, None, None, None, None, 27, 27, 27, None, None, 27, 29, 24, 26, 26, 26, None, 26, None, 26, None, None, None, 24, 24, 24, None, 26, 24, 26, None, None, None, 26, None, None, None, 28, None, 30, None, 23, 27, None, None, None, None, None, None, None, None, None, None, None, 23, 25, 25, 25, 27, 25, 23, 25, None, None, None, None, None, None, 29, None, None, None, 26, None, 22, None, None, 26, 24, 26, None, 26, 28, None, None, 26, 22, None, None, None, None, None, None, None, None, None, None, 25, 23, None, None, None, None, 27])
print Solution().longestUnivaluePath(root)

