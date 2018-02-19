# coding=utf-8
'''
Created on 2017å¹?8æœ?15æ—?

@author: Administrator
'''


class Solution(object):

    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        length = 0
        d = {}  # the maximium length of valid substring end with c equals to d[c]
        for i, ch in enumerate(p):
            if i == 0:
                length = 1
            elif ord(p[i - 1]) + 1 == ord(ch) or p[i - 1] == "z" and ch == "a":
                length += 1
            else:
                length = 1
            d[ch] = max(d.get(ch, 0), length)
        return sum(d.values())


p = "abcdefghijklmnopqrstuvwxyzabc"
print Solution().findSubstringInWraproundString(p)

