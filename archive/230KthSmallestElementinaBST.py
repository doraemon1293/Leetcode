# coding=utf-8
'''
Created on 2017�?1�?8�?

@author: Administrator
'''
from data_structure.Tree import list_to_tree


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.nodes_num = None


class Solution(object):

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # inorder_traversal recursive

#         def helper(self, node):
#             if not node:
#                 return
#             self.helper(node.left)
#             self.k -= 1
#             if self.k == 0:
#                 self.res = node.val
#                 return
#             self.helper(node.right)
#         self.k = k
#         self.res = None
#         self.helper(root)
#         return self.res

        # inorder_traversal iterative
#         s = []
#         while root or s:
#             while root:
#                 s.append(root)
#                 root = root.left
#             root = s.pop()
#             k -= 1
#             if k == 0:
#                 return root.val
#             root = root.right

# 记录节点左子树的结点个数
# The optimal runtime complexity is O(height of BST).
# But pre-process is neccesary
        def get_nodes_num(node):
            if node.left: get_nodes_num(node.left)
            if node.right: get_nodes_num(node.right)
            node.nodes_num = (node.left.nodes_num if node.left else 0) + (node.right.nodes_num if node.right else 0) + 1

        get_nodes_num(root)
        node = root
        while True:
            left_count = node.left.nodes_num if node.left else 0
            # print "**", node.val, left_count
            if k == left_count + 1:
                return node.val
            if k < left_count + 1:
                node = node.left
            if k >= left_count + 1:
                k -= left_count + 1
                node = node.right


arr = [4, 2, 6, 1, 3, 5, 7]
root = list_to_tree(arr)
print Solution().kthSmallest(root, 2)
