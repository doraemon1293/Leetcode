# coding=utf-8
'''
Created on 2017å¹?7æœ?11æ—?

@author: Administrator
'''


class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0: return 0
        visited = s = {amount}
        ans = 0
        while s:
            new_s = {x - coin for x in s for coin in coins if x >= coin} - visited
            ans += 1
            s = new_s
            visited |= s
            if 0 in s: return ans
        return -1
