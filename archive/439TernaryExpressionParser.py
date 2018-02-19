# coding=utf-8
'''
Created on 2017å¹?2æœ?22æ—?

@author: Administrator
'''


class Solution(object):

    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        s = []
        pop_in_next = False
        for ch in expression[::-1]:
            if ch in ("T", "F") or ch.isdigit():
                s.append(ch)
            if pop_in_next:
                condition = s.pop()
                a, b = s.pop(), s.pop()
                s.append(a if condition == "T" else b)
                pop_in_next = False
            if ch == "?":
                pop_in_next = True
        return s[-1]


expression = "T?T:F?T?1:2:F?3:4"
print Solution().parseTernary(expression)
