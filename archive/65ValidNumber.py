# coding=utf-8
'''
Created on 2017å¹?5æœ?11æ—?

@author: Administrator
'''


class Solution(object):

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s = s.strip()
        p = r"\A[-+]?((\d*\.?\d+)|(\d+\.?\d*))(e[-+]?\d+)?\Z"
        return bool(re.match(p, s, re.I))
