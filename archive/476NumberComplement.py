# coding=utf-8
'''
Created on 2017�?1�?10�?

@author: Administrator
'''


class Solution(object):

    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int("".join(["0" if x == "1" else "1" for x in bin(num)[2:]]), 2)
