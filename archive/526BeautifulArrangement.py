# coding=utf-8
'''
Created on 2017å¹?5æœ?9æ—?

@author: Administrator
'''


class Solution(object):

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        nums = tuple(range(1, N + 1))
        self.cache = {}

        def dfs(n, nums):
            if (n, nums) in self.cache:
                return self.cache[(n, nums)]
            res = 0
            for i, num in enumerate(nums):
                if num % n == 0 or n % num == 0:
                    if n == N:
                        res += 1
                    else:
                        res += dfs(n + 1, nums[:i] + nums[i + 1:])
            self.cache[(n, nums)] = res
            return res

        return dfs(1, nums)


print Solution().countArrangement(15)
