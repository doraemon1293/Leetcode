class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        memo = {}

        def dp(x, y):
            if x > y:
                return 0
            if x == y:
                return 1
            if s[x] == s[y]:
                res = dp(x + 1, y - 1)
                memo[x, y] = res
                return res
            res = max(dp(x + 1, y), dp(x, y - 1))
            memo[x, y] = res
            return res

        longest=dp(0,len(s)-1)
        return longest+k>len(s)