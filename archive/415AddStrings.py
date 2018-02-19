# coding=utf-8
'''
Created on 2016�?11�?7�?

@author: Administrator
'''


class Solution(object):

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = []
        add = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(max(len(num1), len(num2))):
            temp = (int(num1[i]) if i < len(num1) else 0) + (int(num2[i]) if i < len(num2) else 0) + add
            add = temp / 10
            ans.append(str(temp % 10))
        if add:
            ans.append("1")
        return "".join(ans[::-1])


print Solution().addStrings("19999999", "1111111")

