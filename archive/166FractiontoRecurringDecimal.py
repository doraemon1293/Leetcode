# coding=utf-8
'''
Created on 2017å¹?7æœ?3æ—?

@author: Administrator
'''


class Solution(object):

    def fractionToDecimal(self, a, b):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if a < 0 and b > 0 or a > 0 and b < 0:
            sign = "-"
        else:
            sign = ""
        a = abs(a)
        b = abs(b)
        if a % b == 0:
            return sign + str(a / b)

        integer = str(a / b) + "."
        fraction = []
        a = a % b
        d = {}
        i = 0
        while a:
            if a in d:
                break
            d[a] = i
            i += 1
            a *= 10
            fraction.append(str(a / b))
            a = a % b
        if a == 0:
            return sign + integer + "".join(fraction)
        else:
            print a, d
            fraction.insert(d[a], "(")
            fraction.append(")")
            return sign + integer + "".join(fraction)


print Solution().fractionToDecimal(-50, 8)
