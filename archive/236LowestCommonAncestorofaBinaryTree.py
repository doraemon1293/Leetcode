# coding=utf-8
'''
Created on 2017å¹?7æœ?7æ—?

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

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.ans = None

        def has(node, p, q):
            if self.ans == None:
                left = right = False
                if node == None: return (False, False)
                if node == p:
                    left = True
                if node == q:
                    right = True
                a1, b1 = has(node.left, p, q)
                a2, b2 = has(node.right, p, q)
                res = (left or a1 or a2, right or b1 or b2)
                if self.ans == None and res == (True, True):
                    self.ans = node.val
                return res
            else:
                return (False, False)

        has(root, p, q)
        return self.ans


root = list_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print Solution().lowestCommonAncestor(root, 5, 4)

