# coding=utf-8
'''
Created on 2017å¹?9æœ?26æ—?

@author: Administrator
'''
from collections import defaultdict


class Solution(object):

    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dp = defaultdict(set)
        valid_stones = set(stones)
        dp[0].add(1)
        for stone in stones:
            for jump in dp[stone]:
                next_stone = stone + jump
                if next_stone in valid_stones:
                    if jump - 1 > 0: dp[next_stone].add(jump - 1)
                    dp[next_stone].add(jump)
                    dp[next_stone].add(jump + 1)
#         for stone in stones:
#             print stone, dp[stone]
        return len(dp[stones[-1]]) != 0


stones = [0, 1, 3, 5, 6, 8, 12, 17]
print Solution().canCross(stones)

