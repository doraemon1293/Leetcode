# coding=utf-8
'''
Created on 2017å¹?5æœ?7æ—?

@author: Administrator
'''


class Solution(object):

    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """

        total = len(candies)
        kinds = len(set(candies))
        if kinds <= total - kinds:
            return kinds
        else:
            return total / 2

