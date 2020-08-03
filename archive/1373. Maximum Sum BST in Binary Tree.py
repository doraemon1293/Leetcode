# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        memo = {}

        def foo(root):
            if root in memo:
                return memo[root]
            if root:
                lc_is_bst, lc_sum = foo(root.left)
                rc_is_bst, rc_sum = foo(root.right)
                if root.right and root.val >= root.right.val:
                    return False, 0
                if root.left and root.val <= root.left.val:
                    return False, 0
                if lc_is_bst and rc_is_bst:
                    summ = root.val + lc_sum + rc_sum
                    res = (True, summ)
                else:
                    res = (False, 0)
                memo[root] = res
                return res
            else:
                return True, 0

        foo(root)
        return max([x[1] for x in memo.values()]+[0])
