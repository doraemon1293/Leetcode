"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res=[]
        def postorder(root):
            if root==None:
                return
            for child in root.children:
                postorder(child)
            res.append(root.val)
        postorder(root)
        return res