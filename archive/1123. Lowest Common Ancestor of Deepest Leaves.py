# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.deepest_nodes = []
        self.deepest = -1

        def pre(root, depth, parent):
            if root:
                if depth > self.deepest:
                    self.deepest = depth
                    self.deepest_nodes = []
                    self.deepest_nodes.append(root)
                elif depth == self.deepest:
                    self.deepest_nodes.append(root)
                root.parent = parent
                pre(root.left, depth + 1, root)
                pre(root.right, depth + 1, root)

        pre(root, 0, None)
        self.deepest_nodes = set(self.deepest_nodes)
        while len(self.deepest_nodes) > 1:
            self.deepest_nodes = set([node.parent for node in self.deepest_nodes])

        return self.deepest_nodes.pop()
