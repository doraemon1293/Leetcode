# coding=utf-8
'''
Created on 3 Dec 2017

@author: Administrator
'''


class Solution(object):

    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0
        maxi = max(nums)
        dp = [0] * (maxi + 1)
        a = [0] * (maxi + 1)
        for num in nums:
            a[num] += num
        nums = sorted(set(nums))
        for num in xrange(maxi + 1):
            dp[num] = max(dp[num - 1], dp[num - 2] + a[num])
        return dp[maxi]


nums = [1, 1, 1, 2, 4, 5, 5, 5, 6]
# nums = [3, 1]
print Solution().deleteAndEarn(nums)
