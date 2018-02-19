# coding=utf-8
'''
Created on 2016å¹?11æœ?23æ—?

@author: Administrator
'''


class Solution(object):

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        num = ""
        chars = ""
        for i in xrange(len(s) + 1):
            if i < len(s):
                x = s[i]
                if x.isdigit():
                    if chars:
                        stack.append(chars)
                    num += x
                    chars = ""
                if x == "[":
                    if num:
                        stack.append(int(num))
                    num = ""
                if x.isalpha():
                    chars += x
                if x == "]":
                    while type(stack[-1]) != int:
                        chars = stack.pop() + chars
                    stack.append(stack.pop() * chars)
                    chars = ""
                print stack, num, chars, s[i], i
            else:
                return "".join(stack) + chars


s = "2[l3[e4[c5[t]]]]"
s = "2[2[2[b]]]"
print Solution().decodeString(s)

