# coding=utf-8
'''
Created on 2016å¹?12æœ?1æ—?

@author: Administrator
'''


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.l = []
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.l.append(val)
        if len(self.l) >= self.size:
            del self.l[0]
        return float(sum(self.l)) / len(self.l)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
