# coding=utf-8
'''
Created on 2017å¹?10æœ?31æ—?

@author: Administrator
'''


class Solution(object):

    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """

        def nearestPalindromeWithSameLength(n):
            firstHalf = int(n[:(len(n) + 1) / 2])
            candidates = [str(temp) + str(temp)[::-1] if len(n) % 2 == 0
                          else str(temp) + str(temp)[:-1][::-1]
                          for temp in (firstHalf - 1, firstHalf, firstHalf + 1)]
            minDiff = float("inf")
            res = None
            for candidate in candidates:
                if abs(int(candidate) - int(n)) != 0 and abs(int(candidate) - int(n)) < minDiff:
                    minDiff = abs(int(candidate) - int(n))
                    res = candidate
            return res

        def nearestPalindromeWithdifferentLength(n):
            a = "9"*(len(n) - 1)
            b = "1" + "0" * (len(n) - 1) + "1"
            if a and abs(int(n) - int(a)) <= abs(int(n) - int(b)):
                return a
            else:
                return b

        a = nearestPalindromeWithSameLength(n)
        b = nearestPalindromeWithdifferentLength(n)

        if abs(int(n) - int(a)) < abs(int(n) - int(b)):
            return a
        elif abs(int(n) - int(a)) > abs(int(n) - int(b)):
            return b
        else:
            return a if int(a) < int(b) else b


print Solution().nearestPalindromic("101")
