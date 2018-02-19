# coding=utf-8
'''
Created on 2016å¹?11æœ?16æ—?

@author: Administrator
'''


class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        roman = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        for k, v in enumerate(s):
            if k == len(s) - 1 or roman[v] >= roman[s[k + 1]]:
                ans += roman[v]
            else:
                ans -= roman[v]
        return ans
