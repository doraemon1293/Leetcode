# coding=utf-8
'''
Created on 2017å¹?1æœ?3æ—?

@author: Administrator
'''


class Solution(object):

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = bin(x)[2:][::-1]
        bin_y = bin(y)[2:][::-1]
        ans = 0
        for i in xrange(max(len(bin_x), len(bin_y))):
            ix = bin_x[i] if i < len(bin_x) else '0'
            iy = bin_y[i] if i < len(bin_y) else '0'
            ans += int(ix != iy)
        return ans


x, y = 1, 4
print Solution().hammingDistance(x, y)
