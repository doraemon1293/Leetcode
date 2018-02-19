# coding=utf-8
'''
Created on 2017å¹?6æœ?13æ—?

@author: Administrator
'''


class Solution(object):

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k: return "0"
        s = []
        for c in num:
            while k and s and c < s[-1]:
                s.pop()
                k -= 1
            s.append(c)
        if k: s = s[:-k]
        ans = "".join(s).lstrip("0")
        if ans == "": ans = "0"
        return ans


num = "1"
k = 1
print Solution().removeKdigits(num, k)
