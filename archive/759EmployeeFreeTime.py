# coding=utf-8
'''
Created on 16 Jan 2018

@author: Administrator
'''


# Definition for an interval.
class Interval:

    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e


class Solution:

    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        import bisect
        intervals = [-float("inf"), float("inf")]

        def removeInterval(intervals, left, right):
            # [lb,rb]=[L(or blank),R(or bland)]
            interval = []
            lb = bisect.bisect_left(intervals, left)
            if lb % 2 == 0:
                pass
            else:
                interval.append(left)
            rb = bisect.bisect_right(intervals, right)
            if rb % 2 == 0:
                pass
            else:
                interval.append(right)
            intervals[lb:rb] = interval

        for arr in schedule:
            for interval in arr:
                removeInterval(intervals, interval.start, interval.end)

        ans = []
        for i in range(0, len(intervals), 2):
            a = intervals[i]
            b = intervals[i + 1]
            if a != -float("inf") and b != float("inf"):
                ans.append(Interval(a, b))
        return ans


schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
temp = []
for arr in schedule:
    temp1 = []
    for x in arr:
        temp1.append(Interval(x[0], x[1]))
    temp.append(temp1)
schedule = temp
intervals = Solution().employeeFreeTime(schedule)
for interval in intervals:
    print(interval.start, interval.end)
