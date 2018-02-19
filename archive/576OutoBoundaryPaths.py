# coding=utf-8
'''
Created on 2017å¹?5æœ?7æ—?

@author: Administrator
'''
# DP


class Solution(object):

    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        ans_i, ans_j = i, j
        MOD = 10 ** 9 + 7
        dp = last_dp = [[0] * n for i in range(m)]
        dd = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for step in range(N):
            dp = [[0] * n for i in range(m)]
            # print last_dp
            for i in range(m):
                for j in range(n):
                    for x, y in dd:
                        # print i, j, i + x, j + y, last_dp[i + x][j + y] if (0 <= (i + x) < m and 0 <= (j + y) < n) else 1
                        dp[i][j] += last_dp[i + x][j + y] if 0 <= (i + x) < m and 0 <= (j + y) < n else 1
                        dp[i][j] %= MOD
            last_dp = dp
            # print last_dp
        return dp[ans_i][ans_j]


print Solution().findPaths(1,
3,
3,
0,
1)
