# coding=utf-8
'''
Created on 2017�?2�?9�?

@author: Administrator
'''


class Solution(object):

    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ans = 0
        for i in xrange(len(timeSeries)):
            if i + 1 < len(timeSeries) and timeSeries[i + 1] < timeSeries[i] + duration:
                ans += timeSeries[i + 1] - timeSeries[i]
            else:
                ans += duration

