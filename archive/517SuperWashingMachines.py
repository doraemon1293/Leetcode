# coding=utf-8
'''
Created on 2017å¹?9æœ?12æ—?

@author: Administrator
'''


class Solution(object):

    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        summ = sum(machines)
        n = len(machines)
        if summ % n != 0: return -1
        target = summ / n
        machines = [x - target for x in machines]
        ans = 0
        summ = 0
        for x in machines:
            summ += x
            ans = max(ans, abs(summ), x)
        return ans

