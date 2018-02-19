# coding=utf-8
'''
Created on 2017å¹?7æœ?14æ—?

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

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None: return []
        from collections import deque, defaultdict
        lo = hi = 0
        ans = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            node, level = q.popleft()
            ans[level].append(node.val)
            if node.left:
                lo = min(lo, level - 1)
                q.append((node.left, level - 1))
            if node.right:
                hi = max(hi, level + 1)
                q.append((node.right, level + 1))
        return [ans[i] for i in xrange(lo, hi + 1)]


root = list_to_tree([3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5])
print Solution().verticalOrder(root)

