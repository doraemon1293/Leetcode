# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        memo = {0: [None], 1: [TreeNode(0)]}

        def trees(n):
            if n%2==0:
                return []
            if n in memo:
                return memo[n]
            else:
                res=[]
                for left_n in range(1, n, 2):
                    right_n = n - 1 - left_n
                    left_nodes = trees(left_n)
                    right_nodes = trees(right_n)
                    for left_node in left_nodes:
                        for right_node in right_nodes:
                            root = TreeNode(0)
                            root.left = left_node
                            root.right = right_node
                            res.append(root)
                return res

        return trees(N)


print(Solution().allPossibleFBT(3))
