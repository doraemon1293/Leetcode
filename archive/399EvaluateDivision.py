# coding=utf-8
'''
Created on 2017å¹?6æœ?19æ—?

@author: Administrator
'''

from collections import defaultdict


class Solution(object):

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        d = defaultdict(dict)
        for i in xrange(len(equations)):
            a, b = equations[i]
            v = values[i]
            d[a][b] = v
            d[b][a] = 1 / v
            d[a][a] = 1.0
            d[b][b] = 1.0
        for k in d:
            for i in d[k]:
                for j in d[k]:
                    d[i][j] = d[i][k] * d[k][j]
        ans = []
        for a, b in queries:
            if a in d and b in d[a]:
                ans.append(d[a][b])
            else:
                ans.append(-1.0)
        return ans

