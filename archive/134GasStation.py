# coding=utf-8
'''
Created on 2017å¹?8æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        a = [gas[i] - cost[i] for i in xrange(n)]
        if sum(a) < 0: return -1
        mini = float("inf")
        summ = 0
        for i in xrange(n):
            summ += a[i]
            if summ < mini:
                mini = summ
                st = (i + 1) % n
        return st


gas = [5]
cost = [5]
print Solution().canCompleteCircuit(gas, cost)

