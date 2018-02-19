# coding=utf-8
'''
Created on 2017å¹?8æœ?20æ—?

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

    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return False
        summ = {}

        def get_sum(node):
            if node == None:
                return 0
            if node in summ:
                return summ[node]
            summ[node] = get_sum(node.left) + get_sum(node.right) + node.val
            return summ[node]

        get_sum(root)
        summ_root = summ[root]
        del summ[root]
        s = set(summ.values())
        if summ_root % 2 == 0 and summ_root / 2 in s:
            return True
        else:
            return False


root = list_to_tree([0])
print Solution().checkEqualTree(root)
