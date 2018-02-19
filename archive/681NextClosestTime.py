# coding=utf-8
'''
Created on 2017å¹?9æœ?24æ—?

@author: Administrator
'''

import datetime


class Solution(object):

    def nextClosestTime(self, time_s):
        """
        :type time: str
        :rtype: str
        """
        t0 = datetime.datetime.strptime(time_s, '%H:%M')
        selections = set()
        for ch in time_s:
            if ch.isdigit():
                selections.add(ch)
        delta = datetime.timedelta.max
        ans = None
        for s1 in selections:
            for s2 in selections:
                for s3 in selections:
                    for s4 in selections:
                        s = s1 + s2 + ":" + s3 + s4
                        try:
                            t1 = datetime.datetime.strptime(s, '%H:%M')
                        except ValueError:
                            pass
                        else:
                            if t1 != t0:
                                if t1 < t0:
                                    t1 += datetime.timedelta(days = 1)
                                if t1 - t0 < delta:
                                    delta = abs(t1 - t0)
                                    ans = s

        return ans if ans != None else time_s


time_s = "23:59"
# time_s = "19:34"
print Solution().nextClosestTime(time_s)
