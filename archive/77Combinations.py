# coding=utf-8
'''
Created on 2017�?6�?1�?

@author: Administrator
'''
from itertools import combinations


class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 迭代
        combs = [[]]
        if k == n:
            return [range(1, n + 1)]
        for _ in range(min(k, n - k)):
            combs = [c + [i] for c in combs for i in range(c[-1] + 1 if c else 1, n + 1)]
        if k > n - k:
            combs = [list(set(range(1, n + 1)) - set(x)) for x in combs]
        return combs

        # 递归
        if k == 0:
            return [[]]
        if n < k:
            return []
        return [pre + [i] for i in range(1, n + 1) for pre in self.combine(i - 1, k - 1)]


n, k = 5, 3
print Solution().combine(n, k)

