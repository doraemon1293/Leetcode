# coding=utf-8
'''
Created on 2016�?11�?15�?

@author: Administrator
'''


class Solution(object):

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = filter(lambda x:x.isalnum(), s.lower())
        return s[:len(s) / 2] == s[len(s) / 2 + len(s) % 2::][::-1]


s = "abcdefg"
print Solution().isPalindrome(s)
