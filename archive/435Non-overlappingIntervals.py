# coding=utf-8
'''
Created on 2016å¹?11æœ?25æ—?

@author: Administrator
'''


# Definition for an interval.
class Interval(object):

    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e


class Solution(object):

    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key = lambda x:x.start)
        s = intervals[0].start
        e = intervals[0].end
        ans = 0
        for interval in intervals[1:]:
            if interval.start < e:
                ans += 1
                e = min(e, interval.end)
            else:
                e = interval.end
        return ans

