# coding=utf-8
'''
Created on 2017å¹?6æœ?16æ—?

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

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # recursive
#         arr = []
#         def postorder(node):
#             if node:
#                 postorder(node.left)
#                 postorder(node.right)
#                 arr.append(node.val)
#         postorder(root)
#         return arr
        # iterative
        if root == None: return []
        left_viewed = set()
        right_viewed = set()
        s = [root]
        ans = []
        while s:
            node = s[-1]
            if node.left and (not node in left_viewed):
                s.append(node.left)
                left_viewed.add(node)
            elif node.right and (not node in right_viewed):
                s.append(node.right)
                right_viewed.add(node)
            else:
                node = s.pop()
                ans.append(node.val)
        return ans


root = list_to_tree([1, 2, 3, None, 4, None, 5])
print Solution().postorderTraversal(root)

