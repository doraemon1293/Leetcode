# coding=utf-8
'''
Created on 2016å¹?11æœ?15æ—?

@author: Administrator
'''


class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = ""
        a = a[::-1]
        b = b[::-1]
        add = 0
        for i in range(max(len(a), len(b))):
            digit_a = int(a[i] if i < len(a) else 0)
            digit_b = int(b[i] if i < len(b) else 0)
            digit_sum = (digit_a + digit_b + add) % 2
            add = (digit_a + digit_b + add) / 2
            ans += str(digit_sum)
        if add:
            ans += str(add)
        return ans[::-1]
