# coding=utf-8
'''
Created on 2016å¹?10æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        import re
        return " ".join(re.findall("\s*(\S+)\s*", s)[::-1])


s = "aaa   bb  nn"
print repr(Solution().reverseWords(s))
