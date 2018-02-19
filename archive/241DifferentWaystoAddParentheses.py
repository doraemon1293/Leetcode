# coding=utf-8
'''
Created on 2016å¹?11æœ?22æ—?

@author: Administrator
'''


class Solution(object):

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        import re
        nums = [int(x) for x in re.split("\D", input)]
        ops = re.findall("\D", input)
        ans = []
        memo = {}

        def foo(st, en):
            if st == en:
                return [nums[st]]
            res = []
            if (st, en) in memo:
                return memo[(st, en)]
            for i in range(st, en):
                for x in foo(st, i):
                    for y in foo(i + 1, en):
                        if ops[i] == "+":
                            res.append(x + y)
                        if ops[i] == "-":
                            res.append(x - y)
                        if ops[i] == "*":
                            res.append(x * y)
            memo[(st, en)] = res
            return res

        return foo(0, len(nums) - 1)


input = "2*3-4*5"
print Solution().diffWaysToCompute(input)

