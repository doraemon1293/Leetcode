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
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        ancestors_p={p}
        ancestors_q={q}
        while p or q:
            if p and p.parent:
                p=p.parent
                ancestors_p.add(p)
            if q and q.parent:
                q=q.parent
                ancestors_q.add(q)
            if p in ancestors_q:
                return p
            if q in ancestors_p:
                return q