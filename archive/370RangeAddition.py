# coding=utf-8
'''
Created on 2017å¹?1æœ?11æ—?

@author: Administrator
'''


class Solution(object):

    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        for st, end, value in updates:
            res[st] += value
            if end + 1 < length:
                res[end + 1] -= value
        s = 0
        for i in xrange(len(res)):
            s += res[i]
            res[i] = s
        return res

