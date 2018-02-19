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
        # 先转换为逆波兰表达式 然后计算
        import re

        def calc(a, op, b):
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "*":
                return a * b
            else:
                return a // b

        def higherPri(a, b):
            if a in ("-", "+") and b in ("*", "/"):
                return False
            else:
                return True

        s = re.split(r"([\+\-\*/])", s.replace(" ", ""))
        s1 = []
        s2 = []
        for ch in s:
            if ch.isdigit():
                s2.append(int(ch))
            elif s1 == []:
                s1.append(ch)
            else:
                while s1 and higherPri(s1[-1], ch):
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


s = "1+2*3/4-5"
print(Solution().calculate(s))
