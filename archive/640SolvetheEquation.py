# coding=utf-8
'''
Created on 2017å¹?7æœ?10æ—?

@author: Administrator
'''


class Solution(object):

    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        coeff = 0
        const = 0
        left, right = equation.split("=")
        n = ""
        for ch in left:
            if ch == "x":
                if n == "" or n == "+":
                    t_coeff = 1
                elif n == "-":
                    t_coeff = -1
                else:
                    t_coeff = int(n)
                coeff += t_coeff
                n = ""
            elif ch == "+" or ch == "-":
                t_const = int(n) if n != "" else 0
                const -= t_const
                n = ch
            else:
                n += ch
        t_const = int(n) if n != "" else 0
        const -= t_const
        n = ""

        for ch in right:
            if ch == "x":
                if n == "" or n == "+":
                    t_coeff = 1
                elif n == "-":
                    t_coeff = -1
                else:
                    t_coeff = int(n)
                coeff -= t_coeff
                n = ""
            elif ch == "+" or ch == "-":
                t_const = int(n) if n != "" else 0
                const += t_const
                n = ch
            else:
                n += ch
        t_const = int(n) if n != "" else 0
        const += t_const
        n = ""
        if const == coeff == 0:
            return "Infinite solutions"
        elif coeff == 0 and const != 0:
            return "No solution"
        else:
            return "x=" + str(const / coeff)


equation = "2=-x"
print Solution().solveEquation(equation)
