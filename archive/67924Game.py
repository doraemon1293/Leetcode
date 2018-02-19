# coding=utf-8
'''
Created on 2017å¹?9æœ?17æ—?

@author: Administrator
'''
import itertools


class Solution(object):

    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = [float(x) for x in nums]
        ops = ["+", "-", "*", "/"]

        def foo(stack, nums, ops, n):
            if n == 3:
                if abs(stack[0] - 24) < 0.0000001:
                    return True
                else:
                    return False
            else:
                for i, num in enumerate(nums):
                    if foo(stack + [num], nums[:i] + nums[i + 1:], ops, n):
                        return True
                if len(stack) >= 2:
                    b, a = stack[-1], stack[-2]
                    for op in ops:
                        if op == "+":
                            if foo(stack[:-2] + [a + b], nums, ops, n + 1):
                                return True
                        if op == "-":
                            if foo(stack[:-2] + [a - b], nums, ops, n + 1):
                                return True
                        if op == "*":
                            if foo(stack[:-2] + [a * b], nums, ops, n + 1):
                                return True
                        if op == "/":
                            if b != 0:
                                if foo(stack[:-2] + [a / b], nums, ops, n + 1):
                                    return True
                return False

        return foo([], nums, ops, 0)


nums = [3, 3, 8, 8]
print Solution().judgePoint24(nums)

