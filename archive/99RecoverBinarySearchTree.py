# coding=utf-8
'''
Created on 2017å¹?10æœ?6æ—?

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

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.last = None
        self.first = self.second = None

        def inorder(root):
            if root:
                inorder(root.left)
                if self.last != None:
                    if self.first == None and self.last.val >= root.val :
                        self.first = self.last
                    if self.first != None and  self.last.val >= root.val:
                        self.second = root
                self.last = root
                print root.val
                inorder(root.right)

        inorder(root)
        print self.first.val, self.second.val
        self.first.val, self.second.val = self.second.val, self.first.val


root = list_to_tree([2, 3, 1])
Solution().recoverTree(root)
print inorder_traversal(root)
