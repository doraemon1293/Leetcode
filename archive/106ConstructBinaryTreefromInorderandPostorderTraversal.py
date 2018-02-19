# coding=utf-8
'''
Created on 2017å¹?7æœ?13æ—?

@author: Administrator
'''
from data_structure.Tree import tree_to_list


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if inorder and postorder:
            # print inorder, postorder
            root_val = postorder.pop()
            i = inorder.index(root_val)
            # rint root_val, i
            root = TreeNode(root_val)
            root.right = self.buildTree(inorder[i + 1:], postorder)
            root.left = self.buildTree(inorder[:i], postorder)
            return root
        else:
            return None


inorder = [2, 1, 3]
postorder = [2, 3, 1]

root = Solution().buildTree(inorder, postorder)
print tree_to_list(root)

