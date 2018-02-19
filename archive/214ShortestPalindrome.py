# coding=utf-8
'''
Created on 2017å¹?7æœ?6æ—?

@author: Administrator
'''


class Solution(object):

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

#         if s == s[::-1]: return s
#         rev_s = s[::-1]
#         for n in xrange(len(s) - 1, -1, -1):
#             if s.startswith(rev_s[len(s) - n:]):
#                 return rev_s[:len(s) - n] + s
        # kmp
        def get_next(p):
            next = [0] * len(p)
            for ind in range(1, len(p)):
                k = next[ind - 1]
                if p[ind] == p[k]:
                    next[ind] = k + 1
                else:
                    while k:
                        k = next[k - 1]
                        if p[k] == p[ind]:
                            next[ind] = k + 1
                            break
            return next

        ind = get_next(s + "#" + s[::-1])[-1]
        return s[ind:][::-1] + s


print Solution().shortestPalindrome("aacecaaazz")
