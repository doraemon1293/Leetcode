# coding=utf-8
'''
Created on 2017�?5�?28�?

@author: Administrator
'''


class Solution(object):

    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        # f(n) -- n bit int无连�?1的个�?
        # 假设num是n bit int
        # 如果num�?11�?�? 那么 return f(n) (n位无连续11的肯定都比num�?)
        # 如果num�?10�?�? 对于0�?头情�? �?�?0+(n-1)都符合条件既f(n-1)
        #                对于1�?头情�? 前两位必�?10 那么个数为findIntegers(num{2:])
        fib = []
        fib.extend([-1, 2, 3])
        for _ in range(29):
            fib.append(fib[-1] + fib[-2])

        ans = 0
        arr = bin(num)[2:]

        def helper(arr):
            while len(arr) > 1 and arr[0] == "0": arr = arr[1:]
            if arr == "0": return 1
            if arr == "1": return 2
            if arr[:2] == "11": return fib[len(arr)]
            if arr[:2] == "10": return fib[len(arr) - 1] + helper(arr[1:])

        return helper(bin(num)[2:])


num = 59034207
print Solution().findIntegers(num)

