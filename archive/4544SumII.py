# coding=utf-8
'''
Created on 2016å¹?11æœ?25æ—?

@author: Administrator
'''


class Solution(object):

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import Counter
        AB = Counter([a + b for a in A for b in B])
        CD = Counter([c + d for c in C for d in D])
        ans = 0
        for x in AB:
            if -x in CD:
                ans += AB[x] * CD[-x]
        return ans

