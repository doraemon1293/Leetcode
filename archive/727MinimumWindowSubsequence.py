# coding=utf-8
'''
Created on 2017å¹?11æœ?12æ—?

@author: Administrator
'''


# dp[i] denotes the start index when i+1 chars of T are matched.
class Solution(object):

    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        d = {}
        for i, ch in enumerate(T):
            d.setdefault(ch, []).append(i)
        dp = [-1] * len(T)
        ansLen = float("inf")
        st = None
        for ind, ch in enumerate(S):
            arr = d.get(ch, [])
            for i in arr[::-1]:
                if i == 0:
                    dp[0] = ind
                else:
                    dp[i] = dp[i - 1]
                if i == len(T) - 1 and dp[i] >= 0 and ind - dp[i] + 1 < ansLen:
                    ansLen = ind - dp[i] + 1
                    st = dp[i]
        return S[st:st + ansLen] if st != None else ""


S = "abcdebdde"
T = "bde"
print Solution().minWindow(S, T)
