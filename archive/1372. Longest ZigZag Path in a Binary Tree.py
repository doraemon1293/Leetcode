# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        memo = {}

        def f(root, direction):
            if root == None:
                return 0
            if (root, direction) in memo:
                return memo[root,direction]
            if direction == "L":
                res = 1 + f(root.left, "R")
            if direction == "R":
                res = 1 + f(root.right, "L")
            memo[root,direction]=res
            f(root.left,direction)
            f(root.right,direction)
        f(root,"L")
        f(root,"R")
        return max(memo.values())

