# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def pre(root, parent):
            if root:
                if root.val == x:
                    self.x_node = root
                root.p = parent
                pre(root.left, root)
                pre(root.right, root)

        def dfs(root):
            if root:
                for node in (root.right, root.left, root.p):
                    if node and node != self.x_node and node not in self.visited:
                        self.visited.add(node)
                        dfs(node)

        pre(root, None)
        self.visited = set()
        dfs(self.x_node.p)
        p = len(self.visited)
        self.visited = set()
        dfs(self.x_node.left)
        left = len(self.visited)
        self.visited = set()
        dfs(self.x_node.right)
        right = len(self.visited)

        print(p, left, right)
        if max(p, left, right) > n // 2:
            return True
        else:
            return False
