# coding=utf-8
'''
Created on 2016å¹?11æœ?16æ—?

@author: Administrator
'''


class Solution(object):

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        max = -1 * float("inf")
        d = {}
        for i, j in people:
            d.setdefault(i, [])
            d[i].append(j)
        ans = []
        for k in sorted(d.keys(), reverse = True):
            for x in sorted(d[k]):
                ans.insert(x, [k, x])
        return ans


people = [[7, 0]]
print Solution().reconstructQueue(people)
