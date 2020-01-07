"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            ans = node.right
            while ans.left:
                ans = ans.left
            return ans
        else:
            ans=node
            while ans.parent and ans.parent.left!=ans:
                ans=ans.parent
            return ans.parent
