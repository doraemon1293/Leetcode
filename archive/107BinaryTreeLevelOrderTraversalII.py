# coding=utf-8
'''
Created on 2016å¹?11æœ?8æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if root:
            from Queue import Queue
            q = Queue()
            q.put((root, 0))
            current_level = -1
            while not q.empty():
                p, level = q.get()
                if level > current_level:
                    ans.append([])
                    current_level = level
                ans[level].append(p.val)
                if p.left:
                    q.put((p.left, level + 1))
                if p.right:
                    q.put((p.right, level + 1))
        return ans[::-1]

