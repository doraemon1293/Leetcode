# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        leaves = set()

        def postorder(root, parent):
            if root:
                root.p = parent
                if root.left == root.right == None:
                    leaves.add(root)
                postorder(root.left, root)
                postorder(root.right, root)
        postorder(root,None)
        print(leaves)
        visited = set()

        def dfs(node, dis):
            if node and node not in visited:
                if dis <= distance:
                    visited.add(node)
                    if dis > 0 and node in leaves:
                        self.ans += 1
                    for next_node in (node.p, node.left, node.right):
                        dfs(next_node, dis + 1)

        for node in leaves:
            visited = set()
            dfs(node, 0)
        return self.ans // 2
