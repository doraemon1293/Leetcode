# coding=utf-8
'''
Created on 2017å¹?7æœ?10æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        from collections import deque
        if root == None: return []
        q = deque([(root, 0)])
        ans = []
        summ = 0
        length = 0
        cur_level = 0
        while q:
            node, level = q.popleft()
            if level > cur_level:
                ans.append(float(summ) / length)
                cur_level = level
                summ = node.val
                length = 1
            else:
                summ += node.val
                length += 1
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        ans.append(float(summ) / length)
        return ans

