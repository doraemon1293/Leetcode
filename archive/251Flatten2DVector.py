# coding=utf-8
'''
Created on 2017å¹?6æœ?13æ—?

@author: Administrator
'''

from itertools import chain


class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.gen = chain(*vec2d)
        self._has_next = True
        self._next = None
        try:
            self._next = self.gen.next()
        except StopIteration:
            self._has_next = False

    def next(self):
        """
        :rtype: int
        """
        temp = self._next
        try:
            self._next = self.gen.next()
        except StopIteration:
            self._next = None
            self._has_next = False
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._has_next

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
