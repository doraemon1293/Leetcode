# coding=utf-8
'''
Created on 2016å¹?11æœ?8æ—?

@author: Administrator
'''


class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        add = 1
        for i in range(len(digits) - 1, -1, -1):
            temp = digits[i] + add
            digits[i] = temp % 10
            add = temp / 10
        if add:
            digits.insert(0, 1)
        return digits

