# coding=utf-8
'''
Created on 2017å¹?7æœ?6æ—?

@author: Administrator
'''
from collections import deque

from data_structure.Tree import list_to_tree


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def boundaryOfBinaryTree(self, root):
        if root == None: return[]
        leftBoundary = [root.val]
        # leftBoundary
        node = root.left
        while node and (node.left or node.right):
            leftBoundary.append(node.val)
            node = node.left if node.left else node.right
        print leftBoundary
        # leaves
        s = []
        leaves = []
        node = root
        while node or s:
            if node:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                if node.left == node.right == None and node != root:
                    leaves.append(node.val)
                node = node.right
        print leaves
        # right
        rightBoundary = []
        node = root.right
        while node and (node.left or node.right):
            rightBoundary.append(node.val)
            node = node.right if node.right else node.left
        print rightBoundary
        return leftBoundary + leaves + rightBoundary[::-1]


root = list_to_tree([1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10])
root = list_to_tree([1, 2, 7, 3, 5, None, 6, 4])
root = list_to_tree([1])

print Solution().boundaryOfBinaryTree(root)
