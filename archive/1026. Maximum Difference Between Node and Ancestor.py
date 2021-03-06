# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = -float("inf")

        def foo(node, maxi, mini):
            if node == None:
                self.ans = max(self.ans, maxi - mini)
            else:
                maxi = max(maxi, node.val)
                mini = min(mini, node.val)
                foo(node.left, maxi, mini)
                foo(node.right, maxi, mini)

        foo(root, -float("inf"), float("inf"))
        return self.ans
