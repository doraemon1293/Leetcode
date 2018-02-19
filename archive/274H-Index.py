# coding=utf-8
'''
Created on 2017å¹?1æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        arr = [0] * (len(citations) + 1)
        for x in citations:
            if x >= len(citations):
                arr[len(citations)] += 1
            else:
                arr[x] += 1
        print arr
        temp = 0
        ans = len(citations) + 1
        while temp < ans:
            ans -= 1
            temp += arr[ans]

        return ans


citations = [3, 0, 6, 1, 5]
print Solution().hIndex(citations)
