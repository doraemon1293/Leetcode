# coding=utf-8
'''
Created on 2016å¹?10æœ?31æ—?

@author: Administrator
'''


class Solution(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        prime = [True] * (n)
        prime[0] = prime[1] = False
        for x in range(2, n ** 0.5 + 1):
            if prime[x]:
                for temp in range(2 * x, n, x):
                    prime[temp] = False
        return sum(prime)


print Solution().countPrimes(1500000)

