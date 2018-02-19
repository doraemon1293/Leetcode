# coding=utf-8
'''
Created on 2017å¹?11æœ?20æ—?

@author: Administrator
'''
from bisect import bisect_left, bisect_right


class MyCalendar(object):

    def __init__(self):
        self.range = [-float('inf'), float('inf')]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        li = bisect_right(self.range, start)
        ri = bisect_left(self.range, end)
        if not(li == ri and li % 2 == 1):
            return False
        else:
            li = bisect_left(self.range, start)
            ri = bisect_right(self.range, end)
            if li % 2 == 0:
                li = li - 1
                start = self.range[li]
            if ri % 2 == 0:
                end = self.range[ri]
                ri += 1
            self.range[li:ri] = [start, end]
            return True
