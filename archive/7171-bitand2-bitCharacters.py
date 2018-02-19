# coding=utf-8
'''
Created on 2017å¹?10æœ?30æ—?

@author: Administrator
'''


class Solution(object):

    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if bits == [0]: return True
        ind = 0
        while ind < len(bits):
            if bits[ind] == 0:
                ind += 1
                if ind == len(bits) - 1:
                    return True
            elif bits[ind] == 1:
                ind += 2
                if ind == len(bits) - 1:
                    return True
        return False
