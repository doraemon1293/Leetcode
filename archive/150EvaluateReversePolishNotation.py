# coding=utf-8
'''
Created on 2017å¹?2æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        import re
        p = re.compile(r"-?\d+")

        s = []
        for token in tokens:
            if re.match(p, token):
                s.append(int(token))
            else:
                b, a = s.pop(), s.pop()
                print a, b
                if token == "+":
                    s.append(a + b)
                if token == "-":
                    s.append(a - b)
                if token == "*":
                    s.append(a * b)
                if token == "/":
                    s.append(abs(a) / abs(b) * (-1 if a < 0 else 1) * (-1 if b < 0 else 1))
        return s[-1]

