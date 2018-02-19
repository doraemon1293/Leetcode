# coding=utf-8
'''
Created on 2017å¹?7æœ?12æ—?

@author: Administrator
'''


class Solution(object):

    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 9
        lo = 10 ** (n - 1)
        hi = lo * 10 - 1
        for n in xrange(hi, lo - 1, -1):
            ans = int(str(n) + str(n)[::-1])
            for a in xrange(hi / 11, (lo + 1) / 11, -1):
                if (ans / (11 * a) > hi):
                    break
                if ((ans % (11 * a)) == 0):
                    return ans % 1337
#             else:
#                 for a in xrange(hi, lo - 1, -1):
#                     if ans / a > hi:
#                         break
#                     if ans % a == 0:
#                         return ans % 1337


n = 8
print Solution().largestPalindrome(n)

