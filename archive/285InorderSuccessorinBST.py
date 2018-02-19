# coding=utf-8
'''
Created on 2017�?7�?13�?

@author: Administrator
'''
from lib2to3.fixes.fix_print import parend_expr


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # 如果大于等于根节�? 那么后继肯定在右子树
        # 如果小于根节�? 那么后继就是当前节点
        succ = None
        while root:
            if root.val > p.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ

