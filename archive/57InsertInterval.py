# coding=utf-8
'''
Created on 2017å¹?7æœ?5æ—?

@author: Administrator
'''


# Definition for an interval.
class Interval(object):

    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e


class Solution(object):

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        def merge(intervals, ind):
            p = ind + 1
            while p < len(intervals) and intervals[p].st <= intervals[ind].end:
                intervals[ind].end = max(intervals[ind].end, intervals[p].end)
                p += 1
            return intervals[:ind + 1] + intervals[p:]

        st, en = 0, len(intervals) - 1
        ind = None
        while st <= en:
            mid = (st + en) / 2
            if intervals[mid].start < newInterval.start:
                st = mid + 1
            elif intervals[mid].start > newInterval.start:
                en = mid - 1
            else:
                ind = mid
                break
        if ind != None:
            intervals[ind].end = max(intervals[ind].end, newInterval.end)
            return merge(intervals, ind)
        else:
            if en == -1 or newInterval.start > intervals[en].end:
                intervals.insert(st, newInterval)
                return merge(intervals, st)
            else:
                intervals[en].end = max(intervals[ind].end, newInterval.end)
                return merge(intervals, en)

