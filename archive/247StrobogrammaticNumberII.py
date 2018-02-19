# coding=utf-8
'''
Created on 2017å¹?6æœ?21æ—?

@author: Administrator
'''


class Solution(object):

    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr1 = ["0", "1", "8"]
        arr2 = ["00", "11", "69", "88", "96"]

        def foo(n):
            if n == 0:
                return []
            if n == 1:
                return ["0", "1", "8"]
            if n == 2:
                return ["11", "69", "88", "96"]
            if n % 2 == 1:
                return [x[:len(x) / 2] + y + x[len(x) / 2:] for x in foo(n - 1) for y in arr1]
            if n % 2 == 0:
                return [x[:len(x) / 2] + y + x[len(x) / 2:] for x in foo(n - 2) for y in arr2]

        return foo(n)


print Solution().findStrobogrammatic(5)
