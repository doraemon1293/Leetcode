# coding=utf-8
'''
Created on 2016å¹?10æœ?27æ—?

@author: Administrator
'''


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mini = float("inf")

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if x < self.mini:
            self.mini = x

    def pop(self):
        """
        :rtype: void
        """
        temp = self.stack.pop()
        if temp == self.mini:
            if self.stack:
                self.mini = min(self.stack)
            else:
                self.mini = float("inf")

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini
