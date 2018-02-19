# coding=utf-8
'''
Created on 2017å¹?6æœ?23æ—?

@author: Administrator
'''


class Solution(object):

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        d = [[0] * (n + 1) for i in range(m + 1)]
        arr = [(x.count("0"), x.count("1")) for x in strs]
        print arr
        for k in xrange(len(strs)):
            for x in xrange(m, -1, -1):
                for y in xrange(n, -1, -1):
                    if x >= arr[k][0] and y >= arr[k][1]:
                        d[x][y] = max(d[x][y], d[x - arr[k][0]][y - arr[k][1]] + 1)
        return d[m][n]


strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print Solution().findMaxForm(strs, m, n)

