# coding=utf-8
'''
Created on 2016å¹?11æœ?25æ—?

@author: Administrator
'''


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from Queue import Queue
        q = Queue()
        ans = []
        if root:
            q.put((root, 0))
        current_level = -1
        while not q.empty():
            node, level = q.get()
            if level > current_level:
                ans.append(node.val)
                current_level = level
            if node.left:
                q.put((node.left, level + 1))
            if node.right:
                q.put((node.right, level + 1))
        return ans


root = TreeNode(1)
print Solution().rightSideView(root)

