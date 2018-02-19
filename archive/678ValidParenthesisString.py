# coding=utf-8
'''
Created on 2017å¹?9æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
#         def foo(p, s):
#             if p < 0: return False
#             for i, ch in enumerate(s):
#                 if ch == "(":
#                     p += 1
#                 elif ch == ")":
#                     if p == 0:
#                         return False
#                     else:
#                         p -= 1
#                 else:
#                     return foo(p + 1, s[i + 1:]) or foo(p - 1, s[i + 1:]) or foo(p, s[i + 1:])
#             return p == 0
#         return foo(0, s)
#         stars = 0
#         left = 0
#         for ch in s:
#             if ch == "(":
#                 left += 1
#             elif ch == ")":
#                 if left == 0:
#                     return False
#                 else:
#                     left -= 1
#             else:
#                 left += 1
#                 stars += 1
#         if left > stars * 2:
#             return False
#         else:
#             return True
        stack = []
        stars = 0
        left = 0
        for i, ch in enumerate(s):
            if ch == "(":
                left += 1
                stack.append("(")
            elif ch == ")":
                if stack == []:
                    return False
                elif left == 0:
                    stars -= 1
                    stack.pop()
                else:
                    for i in xrange(len(stack) - 1, -1, -1):
                        if stack[i] == "(":
                            del stack[i]
                            left -= 1
                            break
            else:
                stack.append("*")
                stars += 1
        s = "".join(stack)
        stack = []
        for ch in s:
            if ch == "(":
                stack.append("(")
            else:
                if stack != []:
                    stack.pop()
        return stack == []


s = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
s = "***((**"
print Solution().checkValidString(s)

