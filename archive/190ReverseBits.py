# coding=utf-8
'''
Created on 2016�?10�?31�?

@author: Administrator
'''


class Solution:

    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], 2)


print int(bin(0)[2:].zfill(32)[::-1], 2)
