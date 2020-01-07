# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 0 root is not covered
        # 1 root is covered
        # 2 root has camera
        from functools import lru_cache
        @lru_cache(None)
        def solve(root, state):
            if root is None:
                if state == 0 or state == 1:
                    return 0
                else:
                    return float("inf")
            if state == 0:
                # put camera in root
                res = solve(root, 2) + 1
                # put camera on left
                res = min(res, solve(root.left, 2) + solve(root.right, 0) + 1)
                # put camera in right
                res = min(res, solve(root.left, 0) + solve(root.right, 2) + 1)
                return res
            elif state == 1:
                #put camera in root
                res=solve(root,2)+1
                #don't put camera in root
                res=min(res,solve(root.left, 0) + solve(root.right, 0))
                return res
            elif state == 2:
                return solve(root.left, 1) + solve(root.right, 1)

        return solve(root, 0)
