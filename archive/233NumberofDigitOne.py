# coding=utf-8
'''
Created on 2017å¹?9æœ?19æ—?

@author: Administrator
'''


class Solution(object):

    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        n = str(n)
        d = {}

        def foo(n):
            if n in d:
                return d[n]
            elif len(n) == 1:
                return 1 if int(n) >= 1 else 0
            else:
                res = 0
                for x in xrange(int(n[0]) + 1):
                    if x == int(n[0]):
                        if x == 1:
                            res += int(n[1:]) + 1 + foo(n[1:])
                        else:
                            res += foo(n[1:])
                    else:
                        if x == 1:
                            res += 10 ** (len(n) - 1) + foo(str(10 ** (len(n) - 1) - 1))
                        else:
                            res += foo(str(10 ** (len(n) - 1) - 1))
                    print n, x, res
                d[n] = res
                return res

        res = foo(n)
        return res


print Solution().countDigitOne(999)

