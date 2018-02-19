# coding=utf-8
'''
Created on 2016å¹?11æœ?22æ—?

@author: Administrator
'''


class Solution(object):

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        from copy import copy
        ans = []

        def dfs(k, n, comb):
            if k == 0 and n == 0:
                ans.append(comb)
            if k > 0 and n > 0:
                for i in range(comb[-1] + 1 if comb else 1, min(n + 1, 10)):
                    dfs(k - 1, n - i, copy(comb) + [i])

        dfs(k, n, [])
        return ans


k = 4
n = 15
print Solution().combinationSum3(k, n)
