# coding=utf-8
'''
Created on 2016å¹?11æœ?16æ—?

@author: Administrator
'''


class Solution(object):

    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        import re
        return bool(re.match(r"^([a-z]+)\1+$", str))


s = "aabaabaab"
print Solution().repeatedSubstringPattern(s)
