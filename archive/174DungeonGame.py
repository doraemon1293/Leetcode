# coding=utf-8
'''
Created on 2017å¹?10æœ?19æ—?

@author: Administrator
'''


class Solution(object):

    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if not(i == m - 1 and j == n - 1):
                    dp[i][j] = max(1, (min(dp[i + 1][j] if i + 1 < m else float("inf"), dp[i][j + 1] if j + 1 < n else float("inf")) - dungeon[i][j]))
        return dp[0][0]


dungeon = [[0, 0]]
print Solution().calculateMinimumHP(dungeon)
