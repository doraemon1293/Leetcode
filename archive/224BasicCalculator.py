# coding=utf-8
'''
Created on 2017�?8�?15�?

@author: Administrator
'''


class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        import re

        def calc(a, op, b):
            if op == "+":
                return a + b
            else:
                return a - b

        s = [x for x in re.split(r"([\(\)\+\-\*/])", s.replace(" ", "")) if x != ""]
        s1 = []
        s2 = []
        for ch in s:
            if ch.isdigit():
                s2.append(int(ch))
            elif s1 == []:
                s1.append(ch)
            elif ch == "(":
                s1.append(ch)
            elif ch == ")":
                while s1[-1] != "(":
                    s2.append(s1.pop())
                s1.pop()
            else:
                while s1 and s1[-1] != "(":
                    s2.append(s1.pop())
                s1.append(ch)
        while s1:
            s2.append(s1.pop())
        s = s2
        stack = []
        print(s)
        for ch in s:
            if type(ch) == int:
                stack.append(ch)
            else:
                b, a = stack.pop(), stack.pop()
                stack.append(calc(a, ch, b))
        return stack[-1]


s = "1+2+(3+4-5)+6"
print(Solution().calculate(s))

