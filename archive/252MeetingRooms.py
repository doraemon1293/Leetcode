# coding=utf-8
'''
Created on 2016å¹?12æœ?1æ—?

@author: Administrator
'''


# Definition for an interval.
class Interval(object):

    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e


class Solution(object):

    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key = lambda x:x.start)
        e = intervals[0].end
        for interval in intervals:
            if interval.start < e:
                return False
            else:
                e = interval.end
        return True
