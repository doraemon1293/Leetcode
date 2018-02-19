# coding=utf-8
'''
Created on 2017å¹?2æœ?24æ—?

@author: Administrator
'''


class Solution(object):

    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = [1, 2, 2]
        p = 1
        while len(s) < n:
            p += 1
            s += (3 - s[-1]) * int(s[p])
        return s[:n].count(1)


Solution().magicalString(10)

