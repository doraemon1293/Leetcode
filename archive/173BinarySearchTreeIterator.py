# coding=utf-8
'''
Created on 2017å¹?5æœ?3æ—?

@author: Administrator
'''


# Definition for a  binary tree node
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.to_left_most_node(root)

    def to_left_most_node(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.to_left_most_node(node)
        return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
