# coding=utf-8
'''
Created on 2017å¹?10æœ?10æ—?

@author: Administrator
'''


class Solution(object):

    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "": return 0
        temp = []
        last_ch = s[0]
        for cur_ch in list(s[1:]) + [None]:
            if cur_ch != last_ch:
                temp.append(last_ch)
                last_ch = cur_ch
        s = temp
        memo = {}

        def dp(i, j):
            if i > j: return 0
            if (i, j) in memo:
                return memo[i, j]
            res = dp(i + 1, j) + 1
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    res = min(res, dp(i, k - 1) + dp(k + 1, j))
            memo[i, j] = res
            return res

        return dp(0, len(s) - 1)


s = "aaabb"
print Solution().strangePrinter(s)

