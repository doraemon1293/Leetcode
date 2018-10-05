# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        from collections import defaultdict
        d = defaultdict(set)

        def dfs(node, depth):
            d[depth].add(node)
            if node.left:
                node.left.parent = node
                dfs(node.left, depth + 1)
            if node.right:
                node.right.parent = node
                dfs(node.right, depth + 1)

        dfs(root, 0)
        max_depth = max(d.keys())
        nodes = d[max_depth]
        while len(nodes) != 1:
            nodes = set([node.parent for node in nodes])
        return nodes.pop()
