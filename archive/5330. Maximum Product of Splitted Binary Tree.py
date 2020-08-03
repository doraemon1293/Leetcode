# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        summ = {}

        def foo(root):
            if root in summ:
                return summ[root]
            if root == None:
                return 0
            summ[root] = root.val + foo(root.left) + foo(root.right)
            return summ[root]

        foo(root)
        total = summ(root)
        ans = 0
        for node in summ:
            ans = max(ans, summ[node] * (total - summ[node]))
        return ans%(10**9 + 7)
