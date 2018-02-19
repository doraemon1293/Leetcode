# coding=utf-8
'''
Created on 2017å¹?4æœ?18æ—?

@author: Administrator
'''


class Solution(object):

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        import re
        a1, b1 = [int(x) for x in re.match(r"(-?\d+)\+(-?\d+)i", a).groups()]
        a2, b2 = [int(x) for x in re.match(r"(-?\d+)\+(-?\d+)i", b).groups()]
        a3, b3 = a1 * a2 - b1 * b2, a1 * b2 + a2 * b1
        return str(a3) + "+" + str(b3) + "i"


a = "1+-1i"
b = "1+-1i"
print Solution().complexNumberMultiply(a, b)
