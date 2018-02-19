# coding=utf-8
'''
Created on 2017å¹?6æœ?23æ—?

@author: Administrator
'''
from django.contrib.gis.gdal.prototypes.srs import new_srs


class Solution(object):

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        summ = sum(nums)
        if summ % 2 == 1: return False
        target = summ / 2
        d = {0:True}

        def dfs(d, target, ind):
            if target in d:
                return d[target]
            if target > 0:
                d[target] = False
                for i in xrange(ind, len(nums)):
                    if dfs(d, target - nums[i], i + 1):
                        d[target] = True
                        break
                return d[target]
            else:
                return False

        return dfs(d, target, 0)
