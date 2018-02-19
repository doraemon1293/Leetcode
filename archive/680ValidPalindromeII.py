# coding=utf-8
'''
Created on 2017å¹?9æœ?17æ—?

@author: Administrator
'''
from __builtin__ import True


class Solution(object):

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

#         if s == s[::-1]:
#             return True
#         else:
#             for i in xrange(len(s)):
#
#                 temp = s[:i] + s[i + 1:]
#                 if temp == temp[::-1]:
#                     print i, s[i]
#                     return True
#             return False

        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                temp = s[:i] + s[i + 1:]
                if temp == temp[::-1]:
                    return True
                temp = s[:j] + s[j + 1:]
                if temp == temp[::-1]:
                    return True
                return False
        return True


print Solution().validPalindrome("cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucu")

