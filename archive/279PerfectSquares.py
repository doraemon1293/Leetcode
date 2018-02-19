# coding=utf-8
'''
Created on 2017å¹?6æœ?29æ—?

@author: Administrator
'''


class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = set([0])
        x = int(n ** 0.5)
        ans = 0
        while True:
            ans += 1
            s = s | set([t + i ** 2 for t in s for i in xrange(1, x + 1)])
            if n in s:
                return ans


print Solution().numSquares(12)

