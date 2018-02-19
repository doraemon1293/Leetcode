# coding=utf-8
'''
Created on 2017å¹?6æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        pointers = [0] * len(primes)
        nums = [1]
        for i in xrange(1, n):
            nums.append(min([nums[pointers[j]] * primes[j] for j in xrange(len(primes))]))
            for j in xrange(len(primes)):
                if nums[pointers[j]] * primes[j] <= nums[-1]:
                    pointers[j] += 1
        return nums[-1]


n = 10
primes = [2, 3, 5]
print Solution().nthSuperUglyNumber(n, primes)
