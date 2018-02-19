# coding=utf-8
'''
Created on 2017å¹?8æœ?11æ—?

@author: Administrator
'''


class Solution(object):

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
# 1 Scan the string from beginning to end.
# 2 If current character is '(',
# push its index to the stack. If current character is ')' and the
# character at the index of the top of stack is '(', we just find a
# matching pair so pop from the stack. Otherwise, we push the index of
# ')' to the stack.
# 3 After the scan is done, the stack will only
# contain the indices of characters which cannot be matched. Then
# let's use the opposite side - substring between adjacent indices
# should be valid parentheses.
# 4 If the stack is empty, the whole input
# string is valid. Otherwise, we can scan the stack to get longest
# valid substring as described in step 3.

        stack = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                if stack:
                    if s[stack[-1]] == "(":
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
        stack.append(len(s))
        ans = stack[0] - (-1) - 1
        print stack
        for i in xrange(0, len(stack) - 1):
            ans = max(ans, stack[i + 1] - stack[i] - 1)
        return ans


s = ")(()"
print Solution().longestValidParentheses(s)
