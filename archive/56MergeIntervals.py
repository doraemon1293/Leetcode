# coding=utf-8
'''
Created on 2016å¹?12æœ?12æ—?

@author: Administrator
'''


# Definition for an interval.
class Interval(object):

    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []: return intervals
        intervals.sort(key = lambda x: x.start)
        ans = intervals[0]
        for i in intervals[1:]:
            if i.start <= ans[-1].end:
                if i.end > ans[-1].end:
                    ans[-1].end = i.end
            else:
                ans.append[i]
        return ans
