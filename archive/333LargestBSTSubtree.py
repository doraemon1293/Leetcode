# coding=utf-8
'''
Created on 2017å¹?8æœ?16æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def foo(node):
            if node.left == node.right == None:
                self.ans = max(self.ans, 1)
                return node.val, node.val, 1

            if node.left and node.right == None:
                left_max, left_min, left_nodes = foo(node.left)
                if left_nodes > 0 and left_max < node.val:
                    self.ans = max(self.ans, left_nodes + 1)
                    return node.val, left_min, left_nodes + 1
                else:
                    return -1, -1, -1
            if node.right and node.left == None:
                right_max, right_min, right_nodes = foo(node.right)
                if right_nodes > 0 and right_min > node.val:
                    self.ans = max(self.ans, right_nodes + 1)
                    return right_max, node.val, right_nodes + 1
                else:
                    return -1, -1, -1
            if node.left and node.right:
                left_max, left_min, left_nodes = foo(node.left)
                right_max, right_min, right_nodes = foo(node.right)
            if left_nodes > 0 and right_nodes > 0 and left_max < node.val < right_min:
                self.ans = max(self.ans, left_nodes + right_nodes + 1)
                return right_max, left_min, left_nodes + right_nodes + 1
            else:
                return -1, -1, -1

        if root:
            foo(root)
        return self.ans

