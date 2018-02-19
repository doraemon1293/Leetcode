# coding=utf-8
'''
Created on 2016å¹?10æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {"(":")", "[":"]", "{":"}"}
        for c in s:
            if c in d:
                stack.append(c)
            else:
                if stack and d.get(stack[-1], None) == c:
                    stack.pop()
                else:
                    return False
        return not bool(stack)


print Solution().isValid("[][([])]")

