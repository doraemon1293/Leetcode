# coding=utf-8
'''
Created on 2017å¹?6æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
            return False
        memo = {}

        nums = range(1, maxChoosableInteger + 1)

        def dfs(nums, total):
            k = tuple(nums)
            if k in memo:
                return memo[k]
            if nums[-1] >= total:
                return True
            for i in xrange(len(nums)):
                if not dfs(nums[:i] + nums[i + 1:], total - nums[i]):
                    memo[k] = True
                    return True
            memo[k] = False
            return False

        return dfs(nums, desiredTotal)


maxChoosableInteger = 19
desiredTotal = 190
print Solution().canIWin(maxChoosableInteger, desiredTotal)
