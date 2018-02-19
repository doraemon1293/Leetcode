# coding=utf-8
'''
Created on 2017å¹?6æœ?23æ—?

@author: Administrator
'''


# Definition for an interval.
class Interval(object):

    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e


class Solution(object):

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        # (x,0) at x time end
        # (y,1) at y time start
        def cmp(x, y):
            if x[0] != y[0]:
                return x[0] - y[0]
            else:
                return x[1] - y[1]

        arr = sorted([(interval.start, 1) for interval in intervals] + [(interval.end, 0) for interval in intervals], cmp = cmp)
        # print arr
        rooms = 0
        ans = 0
        for time, x in arr:
            if x == 1:
                rooms += 1
                ans = max(ans, rooms)
            else:
                rooms -= 1
        return ans


intervals = [Interval(2, 7)]
print Solution().minMeetingRooms(intervals)
