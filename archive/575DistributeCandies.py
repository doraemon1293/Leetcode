# coding=utf-8
'''
Created on 2017�?5�?7�?

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

