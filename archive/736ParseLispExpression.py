# coding=utf-8
'''
Created on 2017å¹?11æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        from copy import copy
        expression = expression.replace("(", "( ")
        expression = expression.replace(")", " )")
        exp = expression.split(" ")

        def solve(st, args):
            i = st + 1
            if exp[i] == "let":
                i += 1
                readingName = True  # Flase=>reading Value
                while True:
                    if readingName:
                        # exp[i] is the last exp
                        if exp[i + 1] == ")":
                            v = args[exp[i]] if "a" <= exp[i][0] <= "z" else int(exp[i])
                            exp[st:i + 2] = [v]
                            return v
                        elif exp[i] == "(":
                            v = solve(i, copy(args))
                            exp[st:i + 2] = [v]
                            return v
                        else:
                            name = exp[i]
                            i += 1
                            readingName = not readingName
                    else:
                        if exp[i] == "(":
                            v = solve(i, copy(args))
                            args[name] = int(v)
                            i += 1
                            readingName = not readingName
                        else:
                            args[name] = args[exp[i]] if "a" <= exp[i][0] <= "z" else int(exp[i])
                            i += 1
                            readingName = not readingName

            elif exp[i] == "add" or exp[i] == "mult":
                op = exp[i]
                i += 1
                v1 = v2 = None
                while v1 == None or v2 == None:
                    if exp[i] == "(":
                        v = solve(i, copy(args))
                    else:
                        v = args[exp[i]] if "a" <= exp[i][0] <= "z" else int(exp[i])
                    if v1 == None:
                        v1 = v
                    else:
                        v2 = v
                    i += 1
                v = (v1 + v2) if op == "add" else (v1 * v2)
                exp[st:i + 1] = [v]
                return v

        return solve(0, {})


expression = "(add 1 2)"
expression = "(let x 1 y 2 x (add x y) (add x y))"
expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
expression = "(let x 7 -12)"
print Solution().evaluate(expression)

