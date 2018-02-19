# coding=utf-8
'''
Created on 2016å¹?11æœ?3æ—?

@author: Administrator
'''


class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import operator
        return reduce(operator.xor, nums)


print Solution().singleNumber([2, 2, 1])
