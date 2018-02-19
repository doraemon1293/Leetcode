# coding=utf-8
'''
Created on 2017å¹?2æœ?13æ—?

@author: Administrator
'''


class Solution(object):

    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = []
        if num < 0:
            ans.append("-")
            num = -num
        ans.append(str(num % 7))
        num /= 7
        while num:
            ans.append(str(num % 7))
            num /= 7
        if ans[0] == "-":
            # print ans, ans[:0:-1]
            return "".join(["-"] + ans[:0:-1])
        else:
            return "".join(ans[::-1])


print Solution().convertToBase7(0)
