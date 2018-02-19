# coding=utf-8
'''
Created on 16 Jan 2018

@author: Administrator
'''


class Solution:

    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x:x[1])
        ans = []
        for a, b in intervals:
            if len(ans) == 0 or ans[-1] < a:
                ans.extend([b - 1, b])
            else:
                if ans[-2] < a:
                    if ans[-1] == b:
                        ans.append(b - 1)
                    else:
                        ans.append(b)
        return len(ans)

