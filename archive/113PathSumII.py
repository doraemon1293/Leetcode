# coding=utf-8
'''
Created on 2016å¹?12æœ?22æ—?

@author: Administrator
'''
from data_structure.Tree import list_to_tree, inorder_traversal


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        from copy import copy

        def dfs(node, sum, path):
            path.append(node.val)
            sum -= node.val
            if node.left == node.right == None and sum == 0:
                ans.append(copy(path))
            else:
                if node.left:
                    dfs(node.left, sum, path)
                if node.right:
                    dfs(node.right, sum, path)
            path.pop()

        ans = []
        if root:
            dfs(root, sum, [])
        return ans


root = list_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
sum = 22
print Solution().pathSum(root, sum)
