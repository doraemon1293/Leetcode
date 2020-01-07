# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution:
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        self.ans = {}

        def solve(root, x, y):
            if root:
                self.ans.setdefault(x, {})
                self.ans[x].setdefault(y, [])
                self.ans[x][y].append(root.val)
                solve(root.left, x - 1, y + 1)
                solve(root.right, x + 1, y + 1)

        ans = []
        solve(root, 0, 0)
        for x in sorted(self.ans.keys()):
            temp = []
            for y in sorted(self.ans[x].keys()):
                temp += sorted(self.ans[x][y])
            ans.append(temp)
        return ans
