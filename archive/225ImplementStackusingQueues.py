# coding=utf-8
'''
Created on 2016å¹?11æœ?14æ—?

@author: Administrator
'''


class Stack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        temp = []
        while not self.empty():
            x = self.s.pop(0)
            if not self.empty():
                temp.append(x)
        self.s = temp

    def top(self):
        """
        :rtype: int
        """
        temp = []
        while not self.empty():
            x = self.s.pop(0)
            temp.append(x)
        self.s = temp
        return x

    def empty(self):
        """
        :rtype: bool
        """
        return not bool(self.s)


stack = Stack()
print stack.top()
