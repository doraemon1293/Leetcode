# coding=utf-8
'''
Created on 2016�?11�?16�?

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
