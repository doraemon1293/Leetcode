# coding=utf-8
'''
Created on 2017å¹?6æœ?22æ—?

@author: Administrator
'''


class Solution(object):

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n^2
        n = len(nums)
        lis = [1] * n
        ans = 0
        for i in xrange(n - 1, -1, -1):
            lis[i] = max([lis[j] for j in xrange(i, n) if nums[i] < nums[j]] or [0]) + 1
            ans = max(ans, lis[i])
        return ans

        # nlogn
        def lengthOfLIS(self, nums):
            tails = [0] * len(nums)
            size = 0
            for x in nums:
                i, j = 0, size
                while i != j:
                    m = (i + j) / 2
                    if tails[m] < x:
                        i = m + 1
                    else:
                        j = m
                tails[i] = x
                size = max(i + 1, size)
            return size


nums = [10, 9, 2, 5, 3, 7, 101, 18]

print Solution().lengthOfLIS(nums)
