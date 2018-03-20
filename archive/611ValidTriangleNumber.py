# coding=utf-8
'''
Created on 2017�?6�?11�?

@author: Administrator
'''

import bisect


class Solution(object):

    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = sorted([num for num in nums if num > 0])
        d = {}
        i = 0
        for num in xrange(2001):
            while i < len(nums) and nums[i] < num:
                i += 1
            d[num] = i

        if len(nums) < 3: return 0
        ans = 0
        for ia in xrange(len(nums)):
            for ib in xrange(ia + 1, len(nums)):
                ans += d[nums[ia] + nums[ib]] - 1 - ib
        return ans


nums = [79, 96, 49, 49, 59, 64, 44, 81, 24, 65, 61, 30, 86, 50, 12, 90, 32, 91, 61, 51, 90, 14, 74, 16, 46, 90, 90, 62, 83, 27, 55, 90, 88, 30, 94, 79, 62, 72, 73, 24, 82, 87, 78, 96, 67, 86, 34, 13, 76, 53, 99, 15, 29, 30, 69, 98, 25, 15, 42, 78, 78, 22, 49, 87, 69, 38, 37, 79, 75, 72, 24, 27, 87, 71, 25, 82, 13, 98, 90, 95, 13, 63, 76, 58, 52, 13, 61, 64, 18, 99, 82, 50, 12, 52, 94, 35, 15, 97, 76, 88, 45, 25, 37, 49, 82, 86, 32, 41, 45, 21, 31, 13, 43, 14, 87, 81, 40, 23, 43, 84, 15, 37, 17, 53, 90, 42, 12, 93, 52, 39, 19, 27, 82, 17, 32, 78, 84, 39, 31, 83, 30, 17, 32, 31, 65, 43, 87, 93, 69, 13, 85, 45, 79, 60, 27, 91, 10, 93, 27, 31, 52, 60, 74, 64, 30, 34, 72, 32, 69, 57, 56, 80, 17, 95, 79, 32, 29, 16, 98, 34, 68, 84, 88, 61, 48, 55, 83, 65, 76, 91, 34, 56, 15, 28, 76, 13, 45, 53, 14, 97, 94, 70, 71, 49, 69, 66, 46, 76, 75, 75, 26, 29, 35, 45, 27, 54, 73, 73, 78, 19, 79, 12, 20, 68, 26, 91, 16, 64, 10, 44, 81, 14, 98, 12, 57, 51, 19, 65, 91, 74, 73, 26, 20, 52, 70, 51, 36, 76, 26, 94, 80, 45, 96, 76, 56, 41, 80, 56, 37, 55, 76, 20, 35, 19, 60, 54, 85, 81, 94, 18, 48, 15, 16, 45, 23, 24, 81, 84, 85, 72, 37, 50, 12, 39, 79, 12, 73, 75, 82, 15, 88, 92, 35, 47, 54, 42, 84, 100, 15, 98, 44, 68, 73, 52, 67, 60, 74, 61, 53, 77, 16, 100, 40, 90, 37, 77, 52, 49, 23, 16, 43, 89, 83, 98, 90, 18, 37, 13, 90, 40, 14, 17, 71, 90, 94, 32, 78, 59, 15, 93, 46, 18, 55, 96, 45, 10, 79, 96, 46, 87, 99, 60, 79, 67, 24, 64, 86, 86, 70, 65, 72, 92, 64, 42, 33, 69, 98, 64, 69, 69, 75, 48, 45, 45, 28, 58, 81, 44, 21, 55, 98, 14, 99, 99, 48, 51, 78, 52, 99, 93, 16, 95, 40, 89, 34, 92, 27, 37, 17, 24, 26, 56, 18, 31, 55, 76, 41, 88, 70, 27, 55, 78, 93, 41, 65, 94, 50, 50, 33, 48, 57, 84, 24, 97, 51, 73, 47, 10, 86, 87, 41, 54, 24, 75, 38, 45, 50, 44, 92, 52, 93, 24, 34, 96, 30, 45, 20, 49, 42, 92, 44, 90, 91, 73, 73, 66, 97, 52, 27, 24, 90, 49, 45, 98, 40, 68, 81, 47, 56, 33, 64, 94, 82, 19, 46, 62, 30, 19, 89, 68, 40, 82, 27, 56, 81, 97, 72, 33, 39, 37, 93, 35, 72, 38, 13, 73, 55, 13, 33, 16, 85, 82, 39, 81, 60, 41, 56, 31, 23, 75, 88, 34, 91, 76, 46, 22, 15, 24, 45, 99, 30, 29, 96, 35, 86, 15, 43, 100, 85, 30, 71, 39, 57, 92, 37, 64, 56, 93, 67, 60, 22, 16, 88, 39, 89, 27, 50, 38, 12, 67, 24, 41, 97, 25, 45, 96, 100, 48, 16, 89, 27, 54, 30, 45, 97, 70, 58, 53, 19, 37, 43, 31, 64, 96, 41, 16, 28, 94, 21, 12, 55, 45, 64, 79, 96, 82, 41, 68, 84, 14, 15, 44, 68, 93, 77, 80, 25, 31, 30, 77, 13, 94, 61, 76, 27, 71, 57, 77, 61, 85, 79, 74, 20, 13, 96, 32, 70, 53, 58, 17, 51, 41, 23, 94, 40, 55, 84, 21, 53, 70, 64, 44, 34, 44, 99, 58, 67, 70, 74, 31, 20, 100, 41, 95, 69, 43, 42, 44, 18, 59, 93, 84, 89, 39, 28, 69, 71, 77, 100, 27, 96, 60, 99, 82, 90, 52, 98, 52, 65, 84, 29, 100, 39, 56, 22, 42, 13, 79, 90, 77, 30, 95, 100, 15, 35, 52, 86, 98, 33, 44, 99, 87, 23, 66, 91, 80, 56, 32, 34, 97, 48, 61, 19, 100, 78, 88, 34, 97, 69, 97, 57, 72, 43, 29, 24, 23, 65, 68, 26, 29, 18, 12, 60, 100, 92, 53, 72, 24, 62, 41, 99, 52, 61, 27, 71, 82, 68, 50, 29, 65, 27, 90, 70, 73, 99, 31, 96, 82, 95, 39, 44, 57, 92, 18, 25, 70, 90, 15, 49, 86, 45, 64, 100, 37, 66, 42, 13, 94, 96, 82, 83, 13, 38, 39, 18, 20, 16, 13, 18, 28, 82, 76, 25, 55, 36, 91, 85, 20, 12, 11, 40, 63, 95, 91, 41, 23, 41, 41, 86, 16, 80, 68, 22, 49, 100, 75, 98, 96, 49, 75, 67, 67, 97, 87, 81, 15, 31, 57, 97, 51, 17, 39, 80, 76, 62, 14, 55, 97, 99, 61, 50, 42, 26, 91, 78, 16, 83, 72, 55, 79, 89, 36, 87, 22, 17, 46, 50, 90, 53, 22, 26, 16, 89, 11, 57, 51, 70, 84, 81, 74, 64, 99, 10, 68, 59, 83, 57, 66, 31, 82, 14, 25, 12, 10, 57, 79, 15, 67, 76, 37, 37, 90, 17, 56, 97, 27, 29, 18, 98, 27, 94, 93, 69, 91, 37, 38, 78, 74, 81, 73, 28, 41, 45, 42, 78, 77, 25, 24, 28, 50, 53, 24, 46, 23, 25, 100, 83, 18, 46, 24, 56, 37, 98, 51, 69, 75, 21, 40, 97, 22, 26, 31, 92, 97, 21, 75, 48, 76, 65, 21, 50, 74, 37, 76, 10, 56, 25, 21, 98, 27, 56, 42, 71, 52, 37, 43, 37, 20, 96, 86, 63, 98, 84, 21, 51, 23, 78, 24, 37, 96, 53, 21, 37, 21, 66, 98, 26, 90, 28, 71, 78, 85, 34, 66, 66, 64, 49, 26, 89, 47, 75, 33, 41, 80, 19, 14, 43, 100, 13, 94]
print Solution().triangleNumber(nums)