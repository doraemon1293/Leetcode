# coding=utf-8
'''
Created on 2016å¹?11æœ?7æ—?

@author: Administrator
'''


class Solution(object):

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        from itertools import chain

        return list(chain.from_iterable([ [k] * v for k, v in (Counter(nums1) & Counter(nums2)).items()]))


nums1 = [2, 1]
nums2 = [1, 2]
print Solution().intersect(nums1, nums2)

