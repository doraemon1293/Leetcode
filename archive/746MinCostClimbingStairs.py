# coding=utf-8
'''
Created on 18 Dec 2017

@author: Administrator
'''


class Solution(object):

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * (len(cost) + 1)
        for i in range(len(dp) - 2, -1, -1):
            mini = min(dp[i + 1] if i + 1 < len(dp) else float("inf"), dp[i + 2] if i + 2 < len(dp) else float("inf"))
            dp[i] = mini + cost[i]
        return min(dp[0], dp[1])


cost = [0, 0, 1, 1]
print(Solution().minCostClimbingStairs(cost))
