# coding=utf-8
'''
Created on 2017å¹?8æœ?16æ—?

@author: Administrator
'''


class Solution(object):

    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        def foo(a, b, num):
            c = str(int(a) + int(b))
            if num == c:
                return True
            elif num.startswith(c):
                return foo(b, c, num[len(c):])
            else:
                return False

        n = len(num)
        for len1 in xrange(1, n / 2 + 1):
            a = num[:len1]
            if a == "0" or (not a.startswith("0")):
                for len2 in xrange(1, (n - len1) / 2 + 1):
                    b = num[len1:len1 + len2]
                    if b == "0" or (not b.startswith("0")):
                        if foo(a, b, num[len1 + len2:]):
                            return True
        return False


num = "1123581322"
num = "101"
num = "000"
print Solution().isAdditiveNumber(num)

