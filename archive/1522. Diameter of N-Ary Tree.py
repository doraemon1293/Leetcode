"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.ans=0
        def max_depth(node):
            children_max_depths=sorted([max_depth(child) for child in node.children])
            if len(children_max_depths)==0:
                return 0
            elif len(children_max_depths)==1:
                self.ans=max(self.ans,children_max_depths[0]+1)
                return children_max_depths[0]+1
            else:
                self.ans=max(self.ans,children_max_depths[-1]+1+children_max_depths[-2]+1)
                return children_max_depths[-1]+1

        max_depth(root)
        return self.ans

