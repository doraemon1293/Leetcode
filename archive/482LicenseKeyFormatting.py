# coding=utf-8
'''
Created on 2017å¹?5æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace("-", "")
        s1 = len(S) % K if len(S) % K != 0 else K

        ans = S[:s1]
        while s1 < len(S):
            ans += "-" + S[s1:s1 + K]
            s1 += K
        return ans
