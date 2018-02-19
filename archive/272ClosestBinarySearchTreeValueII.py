# coding=utf-8
'''
Created on 2017å¹?9æœ?4æ—?

@author: Administrator
'''
from data_structure.Tree import list_to_tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # O(n)
#         from collections import deque
#         q = deque()
#         def add(val):
#             if len(q) < k:
#                 q.append(val)
#             else:
#                 a = abs(q[0] - target)
#                 b = abs(q[-1] - target)
#                 if abs(target - val) < a or abs(target - val) < b:
#                     if abs(q[0] - target) < abs(q[-1] - target):
#                         q.pop()
#                     else:
#                         q.popleft()
#                     q.append(val)
#
#         def inorder(root):
#             if root:
#                 inorder(root.left)
#                 add(root.val)
#                 inorder(root.right)
#         inorder(root)
#         return list(q)

        # O(log(n)) if BST is banlanced
        pre = []
        succ = []

        def initStack(root, target):
            while root:
                if root.val <= target:
                    pre.append(root)
                    root = root.right
                else:
                    succ.append(root)
                    root = root.left

        def getPre():
            node = pre.pop()
            if node.left:
                node = node.left
                pre.append(node)
                while node.right:
                    node = node.right
                    pre.append(node)

        def getSucc():
            node = succ.pop()
            if node.right:
                node = node.right
                succ.append(node)
                while node.left:
                    node = node.left
                    succ.append(node)

        if root == None:
            return []
        initStack(root, target)
        ans = []
        while k:
            if pre == [] or succ != [] and abs(pre[-1].val - target) > abs(succ[-1].val - target):
                ans.append(succ[-1].val)
                getSucc()
            else:
                ans.append(pre[-1].val)
                getPre()
            k -= 1
        return ans


root = list_to_tree([2, 1])
target = 2147483648.0
k = 2
print Solution().closestKValues(root, target, k)

