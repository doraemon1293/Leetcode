# coding=utf-8
'''
Created on 2016å¹?12æœ?9æ—?

@author: Administrator
'''


class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = [1] * n
        for i in xrange(1, m):
            last_ans = ans
            ans = []
            for j in xrange(n):
                ans.append = last_ans[j] + (ans[j - 1] if j - 1 >= 0 else 0)
        return ans[m - 1][n - 1]
