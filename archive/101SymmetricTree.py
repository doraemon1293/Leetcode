# coding=utf-8
'''
Created on 2016å¹?11æœ?8æ—?

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

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        from collections import deque
        temp = []
        if root:
            q = deque()
            current_level = 0
            q.append((root, current_level))
            while q:
                node, level = q.popleft()
                if level > current_level:
                    if temp == temp[::-1]:
                        temp = []
                        current_level += 1
                    else:
                        return False
                temp.append(node.val if node else None)
                if node:
                    q.append((node.left, current_level + 1) if node.left else (None, current_level + 1))
                    q.append((node.right, current_level + 1) if node.right else (None, current_level + 1))
        return temp == temp[::-1]


root = list_to_tree([1, 2, 2, None, 3, None, 3])
print Solution().isSymmetric(root)
