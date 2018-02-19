# coding=utf-8
'''
Created on 2017å¹?11æœ?19æ—?

@author: Administrator
'''


class Solution(object):

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for num in range(left, right + 1):
            flag = True
            s = str(num)
            for ch in s:
                i = int(ch)
                if i == 0 or num % i != 0:
                    flag = False
                    break
            if flag:
                ans.append(num)
        return ans
