# coding=utf-8
'''
Created on 2016å¹?10æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        pat = re.compile(p + "$")
        if pat.match(s):
            return True
        else:
            return False


s = "aa"
p = "a"
print Solution().isMatch(s, p)
import re
print re.match("123", "123123")
