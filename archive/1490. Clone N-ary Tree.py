"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        def clone(root):
            if root==None:
                return None
            clone_root=Node(root.val,[None]*len(root.children))
            if root.children:
                for i in range(len(clone_root.children)):
                    clone_root.children[i]=clone(root.children[i])
            return clone_root

        return clone(root)
