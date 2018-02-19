# coding=utf-8
'''
Created on 2017å¹?1æœ?25æ—?

@author: Administrator
'''
from math import sqrt, ceil


class Solution(object):

    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        l = int(ceil(sqrt(area)))
        while area % l:
            l += 1
        return [l, area / l]


print Solution().constructRectangle(100)
