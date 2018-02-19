# coding=utf-8
'''
Created on 2017å¹?5æœ?2æ—?

@author: Administrator
'''

import itertools


class Solution(object):

    def matrixReshape(self, nums, r, c):

        def grouper(iterable, n):
            args = [iter(iterable)] * n
            return zip(*args)

        arr = list(itertools.chain(*nums))
        print arr
        if len(arr) == r * c:
            return grouper(arr, c)
        else:
            return nums


nums = [[1, 2], [3, 4]]
r = 1
c = 4
print Solution().matrixReshape(nums, r, c)
