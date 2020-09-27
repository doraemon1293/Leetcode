from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        self.bst = TreeNode(nums[0])
        N = len(nums)
        MOD = 10 ** 9 + 7

        def insert(num, bst):
            if num < bst.val:
                if bst.left == None:
                    bst.left = TreeNode(num)
                else:
                    insert(num, bst.left)
            if num > bst.val:
                if bst.right == None:
                    bst.right = TreeNode(num)
                else:
                    insert(num, bst.right)

        for num in nums:
            insert(num, self.bst)

        combination = {}

        def c(m, n):
            if n == 0:
                return 1
            if m == n:
                return 1
            if (m, n) in combination:
                return combination[m, n]
            res = c(m - 1, n - 1) + c(m - 1, n)
            combination[m, n] = res
            return res

        def f(m, n, node):
            if m == n:
                return 1
            prod = 1
            v = node.val
            lc, rc = node.left, node.right
            if lc:
                prod *= f(m, v - 1, lc)
                prod %= MOD
            if rc:
                prod *= f(v + 1, n, rc)
                prod %= MOD
            prod *= c(n - m, v - m)
            prod %= MOD
            # print(m,n,node.val,prod)
            return prod
        return (f(1, N, self.bst)-1)%MOD