from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        children = set()

        def dfs(node):
            if node in children:
                return
            else:
                for child in node.children:
                    dfs(child)
                    children.add(child)

        for node in tree:
            dfs(node)
        for node in tree:
            if node not in children:
                return node
