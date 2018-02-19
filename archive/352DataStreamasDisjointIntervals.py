# coding=utf-8
'''
Created on 2017å¹?5æœ?9æ—?

@author: Administrator
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s = 0, e = 0):
#         self.start = s
#         self.end = e


class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = [Interval(s = -2 ** 31, e = -2 ** 31), Interval(s = 2 ** 31 - 1, e = 2 ** 31 - 1)]

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        in_interval, ind = self.bisect(val)
        if in_interval == False:
            flag = True
            if self.intervals[ind].end == val - 1:
                self.intervals[ind].end = val
                flag = False
            if self.intervals[ind + 1].start == val + 1:
                self.intervals[ind + 1].start = val
                flag = False
            if self.intervals[ind].end == self.intervals[ind + 1].start:
                self.intervals[ind].end = self.intervals[ind + 1].end
                del self.intervals[ind + 1]
            if flag:
                self.intervals.insert(ind + 1, Interval(s = val, e = val))

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals[1:-1]

    def bisect(self, val):
        st, en = 0, len(self.intervals) - 1
        while st <= en:
            mid = (st + en) / 2
            if self.intervals[mid].start <= val <= self.intervals[mid].end:
                return True, mid
            elif val < self.intervals[mid].start:
                if val > self.intervals[mid - 1].end:
                    return False, mid - 1
                else:
                    en = mid - 1
            elif val > self.intervals[mid].end:
                if val < self.intervals[mid + 1].start:
                    return False, mid
                else:
                    st = mid + 1
        raise Exception("error")

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
