# coding=utf-8
'''
Created on 2016å¹?11æœ?16æ—?

@author: Administrator
'''


class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import operator
        xor = reduce(operator.xor, nums)
        # xor &= -xor
        temp = 1
        while xor & 1 == 0:
            temp <<= 1
            xor >>= 1

        xor1 = xor2 = 0
        for num in nums:
            if temp & num:
                xor1 ^= num
            else:
                xor2 ^= num
        return xor1, xor2


nums = [-253415037, 1320283273]
print Solution().singleNumber(nums)
print bin(nums[0] ^ nums[1])
