# coding=utf-8
'''
Created on 2017å¹?7æœ?14æ—?

@author: Administrator
'''

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):


class Solution(object):

    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        for i in xrange(n):
            if knows(x, i):
                x = i
        if any(knows(x, i) for i in xrange(n) if i != x):
            return -1
        if not all(knows(i, x) for i in xrange(n) if i != x):
            return -1
        return x
