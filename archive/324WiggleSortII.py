# coding=utf-8
'''
Created on 2017å¹?8æœ?22æ—?

@author: Administrator
'''
from random import shuffle


class Solution(object):

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def findKthSmallestNum(nums, st, end, k):
            i, j = st, end
            x = nums[i]
            while i < j:
                while i < j and nums[j] >= x:
                    j -= 1
                if i < j: nums[i] = nums[j]
                while i < j and nums[i] <= x:
                    i += 1
                if i < j: nums[j] = nums[i]
            nums[i] = x
            if i - st + 1 == k:
                return i
            elif i - st + 1 > k:
                return findKthSmallestNum(nums, st, i - 1, k)
            else:
                return findKthSmallestNum(nums, i + 1, end, k - (i - st + 1))

        def findMedian(nums):  # n=len(nums) if len(nums) is odd return median
                               #             if len(nums) is even return smaller median
            shuffle(nums)
            return findKthSmallestNum(nums, 0, len(nums) - 1, (len(nums) + 1) / 2)

        n = len(nums)
        if n == 0: return []
        median = nums[findMedian(nums)]
        print nums, median
        i = j = (n - 1) / 2 * 2
        k = 1
        for _ in xrange(n):
            if nums[j] < median:
                nums[i], nums[j] = nums[j], nums[i]
                i -= 2
                j -= 2
                if j < 0:
                    j = n / 2 * 2 - 1
            elif nums[j] > median:
                nums[j], nums[k] = nums[k], nums[j]
                k += 2
            else:
                j -= 2
                if j < 0:
                    j = n / 2 * 2 - 1


nums = range(10) + [6, 6, 6, 6]

print Solution().wiggleSort(nums)
print nums

