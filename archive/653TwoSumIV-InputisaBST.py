# coding=utf-8
'''
Created on 2017å¹?8æœ?6æ—?

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

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        def inorder_traversal(root):
            arr = []

            def inorder(node):
                if node:
                    inorder(node.left)
                    arr.append(node.val)
                    inorder(node.right)

            inorder(root)
            return arr

        arr = inorder_traversal(root)
        d = {}
        for num in arr:
            d.setdefault(num, 0)
            d[num] += 1
        for num in arr:
            if k - num != num and k - num in d:
                return True
            if k - num == num and k - num in d and d[k - num] > 1:
                return True
        return False


root = list_to_tree([1])
k = 2
print Solution().findTarget(root, k)
