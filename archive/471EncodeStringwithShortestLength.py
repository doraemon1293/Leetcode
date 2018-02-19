# coding=utf-8
'''
Created on 2017å¹?5æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.dp = {}

        def helper(s):
            n = len(s)
            ans = s
            if n <= 1:
                self.dp[s] = ans
                return ans
            if s in self.dp: return self.dp[s]
            for x in xrange(n):
                left, right = s[:x], s[x:]
                temp = helper(left) + solve(right)
                if len(temp) < len(ans):
                    ans = temp
            self.dp[s] = ans
            return ans

        def solve(s):
            n = len(s)
            ans = s
            for x in xrange(1, n):
                if n % x == 0 and s[:x] * (n / x) == s:
                    temp = str(n / x) + "[" + helper(s[:x]) + "]"
                    if len(temp) < len(ans):
                        ans = temp
            return ans

        helper(s)
        return self.dp[s]


s = ""
print Solution().encode(s)
