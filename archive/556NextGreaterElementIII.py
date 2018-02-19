# coding=utf-8
'''
Created on 2017å¹?8æœ?10æ—?

@author: Administrator
'''


class Solution(object):

    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = list(str(n))
        for i in xrange(len(n) - 2, -1, -1):
            if n[i] < n[i + 1]:
                maxi = n[i + 1]
                k = i + 1
                for j in xrange(i + 1, len(n)):
                    if n[i] < n[j] < maxi:
                        k = j
                        maxi = n[j]

                n[i], n[k] = n[k], n[i]
                n = n[:i + 1] + sorted(n[i + 1:])
                ans = int("".join([str(x) for x in n]))
                if ans > 2 ** 31 - 1:
                    return -1
                else:
                    return ans

        return -1


n = 202
print Solution().nextGreaterElement(n)
