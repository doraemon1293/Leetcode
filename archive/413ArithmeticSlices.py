# coding=utf-8
'''
Created on 2016å¹?11æœ?16æ—?

@author: Administrator
'''


class Solution(object):

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        i = 0
        start = True
        length = 1
        ans = 0
        while i + 1 <= len(A):
            print i, ans
            if start:
                if i + 1 == len(A):
                    break
                diff = A[i + 1] - A[i]
                start = False
                length = 2
                i += 1
            else:
                if i + 1 < len(A) and A[i + 1] - A[i] == diff:
                    length += 1
                    i += 1
                else:
                    if length >= 3:
                        ans += (length ** 2 - 3 * length + 2) / 2
                    start = True

        return ans


A = [1, 2, 3, 4, 5]
print Solution().numberOfArithmeticSlices(A)

