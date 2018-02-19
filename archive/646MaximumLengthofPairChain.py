# coding=utf-8
'''
Created on 2017å¹?7æœ?23æ—?

@author: Administrator
'''


class Solution(object):

    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        n = len(pairs)
        if n == 0: return 0
        pairs.sort(key = lambda x:x[0])
        chain = [1] * n
        ans = 1
        for i in xrange(n - 2, -1, -1):
            chain[i] = max([chain[j] for j in xrange(i + 1, n) if pairs[i][1] < pairs[j][0]] + [0]) + 1
            ans = max(ans, chain[i])
        return ans


pairs = [[5, 24], [39, 60], [15, 28], [27, 40], [50, 90]]
print Solution().findLongestChain(pairs)
