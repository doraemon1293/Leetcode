# coding=utf-8
'''
Created on 2017å¹?1æœ?10æ—?

@author: Administrator
'''


class Solution(object):

    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int("".join(["0" if x == "1" else "1" for x in bin(num)[2:]]), 2)
