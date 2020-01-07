# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        ans = 0
        maxi = -float("inf")
        arr = [root]
        level = 0
        while arr:
            level += 1
            summ = sum([node.val for node in arr])
            if summ > maxi:
                ans = level
                maxi = summ
            new_arr = [node.left for node in arr if node.left] + [node.right for node in arr if node.right]
            arr = new_arr
        return ans
