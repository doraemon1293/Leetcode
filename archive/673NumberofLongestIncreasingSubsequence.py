# coding=utf-8
'''
Created on 2017å¹?9æœ?10æ—?

@author: Administrator
'''


class Solution(object):

    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1] * n
        last_ind = [set()] * n
        longest = 0
        for i in xrange(n):
            for j in xrange(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        last_ind[i] = set([j])
                    elif dp[j] + 1 == dp[i]:
                        last_ind[i].add(j)
            longest = max(longest, dp[i])

        def get_subq(ind):
            if last_ind[ind] == set():
                return 1
            else:
                res = 0
                for k in last_ind[ind]:
                    res += get_subq(k)
                return res

        ans = 0
        for i, length in enumerate(dp):
            if length == longest:
                ans += get_subq(i)
        return ans


nums = [2, 2, 2, 2, 2]
nums = [1, 3, 5, 4, 7]
nums = []
print Solution().findNumberOfLIS(nums)

