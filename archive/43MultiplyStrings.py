# coding=utf-8
'''
Created on 2016å¹?10æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        add = 0
        ans = [0] * (len(num1) + len(num2))
        num1 = [int(x) for x in num1[::-1]]
        num2 = [int(x) for x in num2[::-1]]
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                add, remain = num1[i] * num2[j] / 10, num1[i] * num2[j] % 10
                ans[i + j] += remain
                ans[i + j + 1] += add
        print ans
        for i in xrange(len(ans) - 1):
            temp = ans[i]
            ans[i] = temp % 10
            ans[i + 1] += temp / 10
        print ans
        ans = "".join([str(x) for x in ans[::-1]]).lstrip("0")
        if ans == "":
            return "0"
        else:
            return ans


num1 = "9999"
num2 = "9999"
print Solution().multiply(num1, num2)
