# coding=utf-8
'''
Created on 2017å¹?7æœ?23æ—?

@author: Administrator
'''


class Solution(object):

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        for mid_ind in xrange(0, n):
            # odd length
            ans += 1
            i = 1
            while mid_ind - i >= 0 and mid_ind + i < n and s[mid_ind - i] == s[mid_ind + i]:
                ans += 1
                i += 1
            # even length
            if mid_ind + 1 < n and s[mid_ind] == s[mid_ind + 1]:
                ans += 1
                i = 1
                while mid_ind - i >= 0 and mid_ind + 1 + i < n and s[mid_ind - i] == s[mid_ind + 1 + i]:
                    ans += 1
                    i += 1
        return ans


s = "abc"
print Solution().countSubstrings(s)

