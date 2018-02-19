# coding=utf-8
'''
Created on 2016å¹?11æœ?9æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        ans = []
        if root:
            from collections import deque
            current_level = 0
            q = deque()
            q.append((root, 0))
            temp = []
            while q:
                node, level = q.popleft()
                if level > current_level:
                    ans.append(temp)
                    temp = []
                    current_level += 1
                temp.append(node.val)
                if node.left:
                    q.append((node.left, current_level + 1))
                if node.right:
                    q.append((node.right, current_level + 1))
            ans.append(temp)
        return ans

