# coding=utf-8
'''
Created on 2016å¹?11æœ?14æ—?

@author: Administrator
'''


class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        import bisect
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        lo = 0
        for x in nums2:
            lo = bisect.bisect(nums1, x, lo = lo)
            nums1.insert(lo, x)

