# coding=utf-8
'''
Created on 2016å¹?11æœ?11æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
# dfs
#         def dfs(node, depth):
#             if node.left == node.right == None:
#                 return depth
#             else:
#                 left_depth = float("inf")
#                 right_depth = float("inf")
#                 if node.left:
#                     dfs(node.left, depth + 1)
#                 if node.right:
#                     dfs(node.right, depth + 1)
#                 return min(left_depth, right_depth)
#         if root:
#             return dfs(root, 1)
#         else:
#             return 0

# bfs
        from Queue import Queue
        q = Queue()
        depth = 0
        if root:
            q.put((root, 1))
            while not q.empty():
                node, depth = q.get()
                if node.left == node.right == None:
                    return depth
                if node.left:
                    q.put((node.left, depth + 1))
                if node.right:
                    q.put((node.right, depth + 1))
        else:
            return 0

