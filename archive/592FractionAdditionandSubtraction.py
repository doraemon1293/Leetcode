# coding=utf-8
'''
Created on 2017å¹?5æœ?21æ—?

@author: Administrator
'''


class Solution(object):

    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        import re
        from fractions import Fraction
        ans = 0
        p = r"[-+]?\d+/\d+"
        m = re.match(p, expression)
        for m in re.finditer(p, expression):
            # print m.group(0)
            ans += Fraction(m.group(0))
            # print ans
        if ans.denominator == 1:
            return str(ans) + "/1"
        else:
            return str(ans)


expression = "1/2+1/2"
print Solution().fractionAddition(expression)
