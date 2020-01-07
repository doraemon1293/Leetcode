# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        def dfs(node):
            if node==None:
                return 0
            left,right=dfs(node.left),dfs(node.right)
            self.ans+=abs(left)+abs(right)
            return left+right+node.val-1
        dfs(root)
        return self.ans
