# coding=utf-8
'''
Created on 2017å¹?7æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        bin_m = bin(m)[2:].zfill(31)
        bin_n = bin(n)[2:].zfill(31)
        ans = ["0"] * 31
        for i in xrange(31):
            if bin_m[i] == bin_n[i]:
                ans[i] = bin_m[i]
            else:
                break
        return int("".join(ans), 2)


print Solution().rangeBitwiseAnd(5, 7)
