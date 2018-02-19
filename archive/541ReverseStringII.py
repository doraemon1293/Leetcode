# coding=utf-8
'''
Created on 2017å¹?3æœ?28æ—?

@author: Administrator
'''


class Solution(object):

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)

        def reverse(s, st, en):
            s[st:en + 1] = s[st:en + 1][::-1]

        p = 0
        f = True
        while p < len(s):
            if f:
                reverse(s, p, p + k - 1)
            f = not f
            p += k
        return "".join(s)


print Solution().reverseStr("abcdefg", 2)
