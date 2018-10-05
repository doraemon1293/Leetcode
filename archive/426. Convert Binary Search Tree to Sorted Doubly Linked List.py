"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def solve(root):
            h=t=root
            if root.left:
                h1,t1=solve(root.left)
                t1.right=root
                root.left=t1
                h=h1
            if root.right:
                h2,t2=solve(root.right)
                root.right=h2
                h2.left=root
                t=t2
            return h,t
        if root:
            h,t=solve(root)
            h.left=t
            t.right=h
            return h
        else:
            return root


