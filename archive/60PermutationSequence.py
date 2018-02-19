# coding=utf-8
'''
Created on 2017å¹?7æœ?6æ—?

@author: Administrator
'''


class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import operator

        def factional(n):
            if n == 0: return 1
            return reduce(operator.mul, range(1, n + 1))

        arr = range(1, n + 1)
        ans = ""
        k -= 1
        while len(arr):
            first = k / factional(len(arr) - 1)
            k = k % factional(len(arr) - 1)
            ans += str(arr[first])
            del arr[first]
        return ans


n = 3
k = 5
print Solution().getPermutation(n, k)

