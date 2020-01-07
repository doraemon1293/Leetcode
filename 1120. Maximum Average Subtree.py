# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.ans = -float("inf")

        def foo(root):
            if root == None:
                return 0, 0
            # if root in d:
            #     return d[root]
            l_sum, l_nodes = foo(root.left)
            r_sum, r_nodes = foo(root.right)
            summ = l_sum + r_sum + root.val
            nodes = l_nodes + r_nodes + 1
            self.ans = max(self.ans, summ / nodes)
            return summ, nodes

        foo(root)
        return self.ans
