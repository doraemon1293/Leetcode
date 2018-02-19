# coding=utf-8
'''
Created on 23 Jan 2018

@author: Administrator
'''


class Solution:

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        def lowerPriority(op1, op2):
            """True if op1 has lower prior than op2
            """
            if op1 == "(" or (op1 in ("+", "-") and op2 in ("*", "/")):
                return True
            else:
                return False

        def cal(exp):
            stack = []
            for i in range(len(exp)):
                ch = exp[i]
                if ch.isdigit():
                    stack.append(int(ch))
                else:
                    b, a = stack.pop(), stack.pop()
                    if ch == "+":
                        stack.append(a + b)
                    if ch == "-":
                        stack.append(a - b)
                    if ch == "*":
                        stack.append(a * b)
                    if ch == "/":
                        stack.append(a // b)
            return stack[-1]

        def convertInfixToPostfix(s):
            ind = 0
            stack = []
            exp = []
            cur = ""
            while ind < len(s):
                ch = s[ind]
                if ch == " ":
                    pass
                elif ch.isdigit():
                    cur += ch
                else:
                    if cur != "":
                        exp.append(cur)
                        cur = ""
                    if ch == "(":
                        stack.append(ch)
                    elif ch == ")":
                        while stack[-1] != "(":
                            exp.append(stack.pop())
                        stack.pop()
                    else:  # +-*/
                        while stack and not lowerPriority(stack[-1], ch):
                            exp.append(stack.pop())
                        stack.append(ch)
                ind += 1
            if cur != "": exp.append(cur)
            while stack:
                exp.append(stack.pop())
            return exp

        exp = convertInfixToPostfix(s)
        return cal(exp)


s = "(2+6* 3+5- (3*14/7+2)*5)+3"
s = "2*(5+5*2)/3+(6/2+8)"
s = "1+1"
print(Solution().calculate(s))

