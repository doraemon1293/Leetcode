# coding=utf-8
'''
Created on 2017å¹?9æœ?27æ—?

@author: Administrator
'''


class Solution(object):

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isValid(s):
            count = 0
            for ch in s:
                if ch == "(":
                    count += 1
                elif ch == ")":
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        candidate = {s}
        while True:
            valid = filter(isValid, candidate)
            if valid:
                return list(valid)
            else:
                candidate = {s[:i] + s[i + 1:] for i in xrange(len(s)) for s in candidate}


s = "(a)())()"
s = ")("
print Solution().removeInvalidParentheses(s)

