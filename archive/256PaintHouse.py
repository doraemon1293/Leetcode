# coding=utf-8
'''
Created on 2017å¹?2æœ?1æ—?

@author: Administrator
'''


class Solution(object):

    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        from copy import copy
        if costs == []: return 0
        last = copy(costs[0][:])
        cur = copy(costs[0][:])
        for i in xrange(1, len(costs)):
            cur = [None] * 3
            for j in xrange(0, 3):
                cur[j] = min([last[x] for x in xrange(len(last)) if x != j]) + costs[i][j]
            last = cur
        return min(cur)


costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
print Solution().minCost(costs)
