# coding=utf-8
'''
Created on 2017�?9�?7�?

@author: Administrator
'''


class Solution(object):

    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
# 每次遍历完第i-1个house的所有上色情况后，存下最小的cost (min1)和次小的cost(min2)，并记录�?小cost的颜色c。这样在考虑第i个house的时候，除了上颜色c以外，cost[i][c’] = min1 + cost[i-1][c’]；上颜色c的时候，cost[i][c] = min2 + cost[i-1][c]�?
        import heapq
        if costs == []:
            return 0
        n, k = len(costs), len(costs[0])
        dp0 = heapq.nsmallest(2, [(cost, i) for i, cost in enumerate(costs[0])])
        for indn in xrange(1, n):
            dp1 = [float("inf")] * k
            for indk in xrange(k):
                if indk != dp0[0][1]:
                    dp1[indk] = min(dp1[indk], dp0[0][0] + costs[indn][indk])
                else:
                    dp1[indk] = min(dp1[indk], dp0[1][0] + costs[indn][indk])
            dp0 = heapq.nsmallest(2, [(cost, i) for i, cost in enumerate(dp1)])
        return dp0[0][0]


costs = [[8]]
print Solution().minCostII(costs)
