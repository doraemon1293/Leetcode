"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        node=leaf
        def flip(node,_from):
            if node!=root:
                left,right,parent=node.left,node.right,node.parent
                if left and left!=_from:


