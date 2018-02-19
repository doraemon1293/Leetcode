# coding=utf-8
'''
Created on 2017å¹?5æœ?18æ—?

@author: Administrator
'''


class Solution(object):

    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        def countofNumbersWithPrefixAndLessThanN(prefix, n):
            count = 0
            interval = [prefix, prefix + 1]
            while interval[0] <= n:
                count += (min(n + 1, interval[1])) - interval[0]
                interval = [interval[0] * 10, interval[1] * 10]
            return count

        k -= 1
        prefix = 1

        while k:
            count = countofNumbersWithPrefixAndLessThanN(prefix, n)
            if k >= count:
                prefix += 1
                k -= count
            else:
                prefix *= 10
                k -= 1
        return prefix


n = 10000
k = 10000
print Solution().findKthNumber(n, k)

