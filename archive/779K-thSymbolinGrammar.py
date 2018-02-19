# coding=utf-8
'''
Created on 12 Feb 2018

@author: Administrator
'''


class Solution(object):

    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        self.memo = {}

        def foo(n, k):
            if k == 1 or n == 1:
                return 0
            if (n, k) in self.memo:
                return self.memo[(n, k)]
            last = foo(n - 1, (k + 1) // 2)
            if last == 0:
                self.memo[(n, k)] = 0 if k % 2 == 1 else 1
            if last == 1:
                self.memo[(n, k)] = 1 if k % 2 == 1 else 0
            return self.memo[(n, k)]

        return foo(N, K)


N = 3
K = 3
print(Solution().kthGrammar(N, K))
