# coding=utf-8
'''
Created on 2016å¹?11æœ?18æ—?

@author: Administrator
'''


# Definition for an interval.
class Interval(object):

    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e


class Solution(object):

    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        import bisect
        start_index = sorted([[interval.start, i] for i, interval in enumerate(intervals)])
        ans = []
        for interval in intervals:
            index = bisect.bisect(start_index, [interval.end])
            if index < len(start_index):
                ans.append(start_index[index][1])
            else:
                ans.append(-1)
        return ans

