# coding=utf-8
'''
Created on 2017å¹?6æœ?26æ—?

@author: Administrator
'''
import heapq


class Solution(object):

    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key = lambda x:x[1])
        st = 0
        ans = 0
        q = []
        for dur, end in courses:
            st += dur
            ans += 1
            heapq.heappush(q, -dur)
            while st > end:
                temp = -heapq.heappop(q)
                st -= temp
                ans -= 1
        return ans

