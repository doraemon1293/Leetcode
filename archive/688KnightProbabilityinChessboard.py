# coding=utf-8
'''
Created on 2017å¹?10æœ?1æ—?

@author: Administrator
'''


class Solution(object):

    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        from collections import defaultdict
        q = {(r, c):1.0}
        for _ in xrange(K):
            new_q = defaultdict(float)
            for temp, p in q.items():
                r0, c0 = temp
                for dr, dc in ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)):
                    r1, c1 = r0 + dr, c0 + dc
                    if 0 <= r1 < N and 0 <= c1 < N:
                        new_q[(r1, c1)] += p / 8
            q = new_q
        return sum(q.values())


N, K, r, c = 3, 2, 0, 0
print Solution().knightProbability(N, K, r, c)
