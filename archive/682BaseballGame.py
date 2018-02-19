# coding=utf-8
'''
Created on 2017å¹?9æœ?24æ—?

@author: Administrator
'''


class Solution(object):

    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op == "C":
                if stack:
                    stack.pop()
            elif op == "+":
                stack.append(sum(stack[-2:]))
            elif op == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))
        return sum(stack)


ops = ["5", "2", "C", "D", "+"]
ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
print Solution().calPoints(ops)

