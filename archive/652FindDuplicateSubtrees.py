# coding=utf-8
'''
Created on 2017å¹?7æœ?30æ—?

@author: Administrator
'''
from Tkconstants import SOLID
from data_structure.Tree import list_to_tree, tree_to_list


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
#         def preorder_traversal(root):
#             arr = []
#             def preorder(node):
#                 if node:
#                     arr.append(node.val)
#                     preorder(node.left)
#                     preorder(node.right)
#             preorder(root)
#             return arr
#
#         def tree_to_list(root):
#             from collections import deque
#             if root == None: return []
#             ans = []
#             q = deque([root])
#             while len(q) != 0:
#                 node = q.popleft()
#                 ans.append(node.val if node else None)
#                 if node:
#                     q.append(node.left)
#                     q.append(node.right)
#             while ans[-1] == None:
#                 del ans[-1]
#             return ans
#
#
#
#         def equal(p, q):
#             if p == q == None: return True
#             if p == None and q != None or p != None and q == None: return False
#             if p.val == q.val:
#                 return equal(p.left, q.left) and equal(p.right, q.right)
#             else:
#                 return False
#
#         nodes = preorder_traversal(root)
#         ans = []
#         for i in xrange(len(nodes)):
#             for j in xrange(i + 1, len(nodes)):
#                 if equal(i, j):
#                     ans.append(nodes[i])
#         return ans

        def preorder_traversal(root):
            arr = []

            def preorder(node):
                if node:
                    arr.append(node)
                    preorder(node.left)
                    preorder(node.right)

            preorder(root)
            return arr

        def tree_to_list(root):
            from collections import deque
            if root == None: return []
            ans = []
            q = deque([root])
            while len(q) != 0:
                node = q.popleft()
                ans.append(node.val if node else None)
                if node:
                    q.append(node.left)
                    q.append(node.right)
            while ans[-1] == None:
                del ans[-1]
            return ans

        nodes = preorder_traversal(root)
        d = {}
        s = set()
        ans = []
        for node in nodes:
            t = tuple(tree_to_list(node))
            if t in d and t not in s:
                s.add(t)
                ans.append(d[t])
            else:
                d[t] = node
        return ans


root = list_to_tree([0, 0, 0, 0, None, None, 0, None, None, 0, 0])
print [tree_to_list(x) for x in Solution().findDuplicateSubtrees(root)]

