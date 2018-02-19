# coding=utf-8
'''
Created on 2017�?6�?15�?

@author: Administrator
'''


class Solution(object):

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 枚举�?后一个爆�?
        # 那么dp[st,en]=max( dp[st,i-1]+nums[st-1]*nums[i]*nums[en+1]+dp[i+1,en] )
        # 递推
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in xrange(n)]
        for length in xrange(1, n - 1):
            for st in xrange(1, n - length):
                # dp[st][st + length - 1] = max([dp[st][i - 1] + nums[st - 1] * nums[i] * nums[st + length] + dp[i + 1][st + length - 1] for i in xrange(st, st + length)])
                for i in xrange(st, st + length):
                    dp[st][st + length - 1] = max(dp[st][st + length - 1], dp[st][i - 1] + nums[st - 1] * nums[i] * nums[st + length] + dp[i + 1][st + length - 1])
        return dp[1][n - 2]


nums = [42, 23, 62, 2, 89, 97, 26, 82, 47, 23, 9, 2, 9, 11, 53, 49, 40, 3, 88, 76, 63, 11, 79, 37, 52, 91, 5, 44, 71, 69, 20, 5, 74, 41, 70, 68, 26, 16, 62, 53, 47, 46, 26, 27, 99, 72, 4, 40, 77, 74, 89, 19, 26, 7, 30, 79, 49, 75, 51, 28, 47, 26, 55, 81, 82, 15, 21, 89, 51, 10, 0, 50, 31, 32, 38, 7, 99, 13, 23, 98, 68, 9, 54, 15, 34, 52, 58, 48, 66, 75, 6, 15, 91, 33, 15, 37, 25, 98, 98, 77, 60, 16, 82, 89, 48, 43, 1, 85, 39, 99, 95, 86, 45, 90, 73, 45, 93, 99, 39, 57, 32, 47, 35, 79, 25, 54, 98, 34, 60, 90, 38, 40, 5, 5, 96, 21, 18, 93, 69, 38, 85, 49, 15, 77, 84, 70, 52, 87, 73, 15, 65]
# nums = [2, 2, 2]
print Solution().maxCoins(nums)

# 递归
#         memo = {}
#         nums = [1] + nums + [1]
#         def foo(st, en):
#             if st > en:
#                 return 0
#             if (st, en) in memo:
#                 return memo[(st, en)]
#
#             temp = max([foo(st, i - 1) + nums[st - 1] * nums[i] * nums[en + 1] + foo(i + 1, en) for i in xrange(st, en + 1)])
#             memo[(st, en)] = temp
#             #print st, en, temp
#             return temp
#
#         ans = foo(1, len(nums) - 2)
#         #print memo
#         return ans
