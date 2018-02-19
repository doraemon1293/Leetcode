# coding=utf-8
'''
Created on 2017å¹?11æœ?27æ—?

@author: Administrator
'''

import bisect


class MyCalendarThree(object):

    def __init__(self):
        self.keys = []
        self.d = {}

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """

        if start not in self.d:
            bisect.insort(self.keys, start)
        self.d.setdefault(start, 0)
        self.d[start] += 1
        if end not in self.d:
            bisect.insort(self.keys, end)
        self.d.setdefault(end, 0)
        self.d[end] -= 1
        cur = 0
        res = 0
        for key in self.keys:
            cur += self.d[key]
            res = max(res, cur)
        return res

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
