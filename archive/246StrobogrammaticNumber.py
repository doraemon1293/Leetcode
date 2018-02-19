# coding=utf-8
'''
Created on 2016å¹?12æœ?1æ—?

@author: Administrator
'''


class Solution(object):

    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        i, j = 0, len(num) - 1
        while i <= j:
            if (int(num[i]), int(num[j])) not in ((0, 0), (1, 1), (6, 9), (9, 6), (8, 8)):
                return False
            else:
                i += 1
                j -= 1
        return True
