# coding=utf-8
'''
Created on 2016å¹?12æœ?9æ—?

@author: Administrator
'''
from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.d:
            v = self.d.pop(key)
            self.d[key] = v
            return v
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.d:
            self.d.pop(key)
            self.d[key] = value
        else:
            self.capacity -= 1
            if self.capacity < 0:
                self.d.popitem(last = False)
                self.capacity += 1
            self.d[key] = value

