# coding=utf-8
'''
Created on 2017å¹?6æœ?18æ—?

@author: Administrator
'''
from collections import Counter, deque


class Solution(object):

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0: return len(tasks)
        counter = Counter(tasks)
        width = counter.most_common(1)[0][1]
        return max(len(tasks), (n + 1) * (width - 1) + len([x for x in counter.most_common() if x[1] == width]))


tasks = ['A', 'A', 'A', 'B', 'B', 'B', ]
n = 2
print Solution().leastInterval(tasks, n)
