# coding=utf-8
'''
Created on 2017�?9�?7�?

@author: Administrator
'''


class Solution(object):

    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
# 状�?�转移方程：

# dp[k][i] = min(dp[k][i], dp[k - 1][j] + min(abs(i - j), len(ring) - abs(i - j)))

# 其中k表示当前字符在key中的下标，i表示当前字符在ring中的下标，j表示上一个字符在ring中的下标�?

        n = len(key)
        d = {}
        for ind in xrange(n):
            d[ind] = [i for i in xrange(len(ring)) if ring[i] == key[ind]]
        dp0 = {0:0}
        dp1 = {}

        for ind in xrange(len(key)):
            for pos0, steps0 in dp0.items():
                for pos1 in d[ind]:
                    dp1[pos1] = min(dp1.get(pos1, float("inf")), steps0 + abs(pos0 - pos1) + 1, steps0 + len(ring) - abs(pos0 - pos1) + 1)
            dp0 = dp1
            dp1 = {}
        return min(dp0.values())


ring = "godding"
key = "gd"
ring = "abcde"
key = "ade"
print Solution().findRotateSteps(ring, key)
