# coding=utf-8
'''
Created on 2017�?6�?16�?

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

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        self.ans = 0
        self.memo = {}

        def foo(node):
            res = 1
            if node.left:
                left = self.memo(node.left) if node.left in self.memo else foo(node.left)
            else:
                left = 0
            if node.right:
                right = self.memo(node.right) if node.right in self.memo else foo(node.right)
            else:
                right = 0
            if left and node.left.val == node.val + 1:
                res = max(res, left + 1)
            if right and node.right.val == node.val + 1:
                res = max(res, right + 1)
            self.ans = max(self.ans, res)
            self.memo[node] = res
            return res

        foo(root)
#         for k, v in self.memo.items():
#             print k.val, v
#         print self.memo
        return self.ans


root = list_to_tree([1, None, 3, 2, 4, None, None, None, 5])
print Solution().longestConsecutive(root)

