# coding=utf-8
'''
Created on 2016�?11�?7�?

@author: Administrator
'''


class Solution(object):

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = []
        if num < 0:
            num += 2 ** 32
        elif num == 0:
            return "0"
        while num:
            temp = num & 0b1111
            if temp > 9:
                temp = chr(ord('a') + temp - 10)
            else:
                temp = str(temp)
            num >>= 4
            ans.append(temp)
        return "".join(ans[::-1])


num = 0
# print num >> 4
print Solution().toHex(num)
