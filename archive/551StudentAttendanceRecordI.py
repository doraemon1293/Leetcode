# coding=utf-8
'''
Created on 2017å¹?4æœ?16æ—?

@author: Administrator
'''


class Solution(object):

    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import collections
        c = collections.Counter(s)
        if c["A"] > 1:
            return False
        if "LLL" in s:
            return False
        return True


s = "PPALLL"
print Solution().checkRecord(s)
