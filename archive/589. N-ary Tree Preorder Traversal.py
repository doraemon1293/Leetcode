"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []

        def preorder(root):
            if root is None:
                return
            else:
                res.append(root.val)
                for child in root.children:
                    preorder(child)

        preorder(root)
        return res
