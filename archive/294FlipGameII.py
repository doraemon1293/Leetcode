# coding=utf-8
'''
Created on 2017å¹?6æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        memo = {}

        def dfs(s):
            if s in memo:
                return memo[s]
            for i in xrange(len(s) - 1):
                if s[i] == s[i + 1] == "+":
                    new_s = s[:i] + "--" + s[i + 2:]
                    if not dfs(new_s):
                        memo[s] = True
                        return True
            memo[s] = False
            return False

        return dfs(s)


s = "++++++++"
print Solution().canWin(s)
