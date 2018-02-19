# coding=utf-8
'''
Created on 2016å¹?11æœ?14æ—?

@author: Administrator
'''


class Solution(object):

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        from collections import Counter
        b = sum((Counter(secret) & Counter(guess)).values())
        a = 0
        for i, x in enumerate(guess):

            if secret[i] == x:
                a += 1
                b -= 1
        return "%sA%sB" % (a, b)


secret = "1122"
guess = "1222"
print Solution().getHint(secret, guess)
