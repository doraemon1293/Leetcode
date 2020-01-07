# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.sum = 0

        def dfs(cur_val, node):
            cur_val = cur_val * 2 + node.val
            if node.left == node.right == None:
                self.sum += cur_val
            if node.left:
                dfs(cur_val, node.left)
            if node.right:
                dfs(cur_val, node.right)

        dfs(0, root)
        return self.sum
