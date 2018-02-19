# coding=utf-8
'''
Created on 2017å¹?7æœ?21æ—?

@author: Administrator
'''


class Solution(object):

    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        # dp[w][c] the max value in w-th week in c -city
        # dp[w][c]=max(dp[w-1][from_city])+days[w][c] if flights[from_city][c]==1
        # initial dp[w][c]=-1 dp[w][0]=0
        n, k = len(days), len(days[0])  # n cities k weeks
        dp = [-1] * n
        dp[0] = 0
        for week in xrange(k):
            new_dp = []
            for to_city in xrange(n):
                new_dp.append(max([dp[from_city] + days[to_city][week] for from_city in xrange(n) if dp[from_city] >= 0 and (flights[from_city][to_city] == 1 or from_city == to_city)] + [-1]))
            dp = new_dp
        return max(dp)


flights = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
days = [[1, 1, 1], [7, 7, 7], [7, 7, 7]]
flights = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
days = [[1, 3, 1], [6, 0, 3], [3, 3, 3]]
print Solution().maxVacationDays(flights, days)

