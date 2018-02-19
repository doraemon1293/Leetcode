# coding=utf-8
'''
Created on 2017å¹?8æœ?31æ—?

@author: Administrator
'''


class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict, deque
        indegrees = {}
        edges = defaultdict(set)
        for i in xrange(numCourses):
            indegrees[i] = 0
        for a, b in prerequisites:
            indegrees[a] += 1
            edges[b].add(a)  # b->a
        zeroDegrees = deque([i for i in xrange(numCourses) if indegrees[i] == 0])
        learnt = []
        while zeroDegrees:
            v0 = zeroDegrees.popleft()
            learnt.append(v0)
            for v1 in edges[v0]:
                indegrees[v1] -= 1
                if indegrees[v1] == 0:
                    zeroDegrees.append(v1)
        if len(learnt) == numCourses:
            return learnt
        else:
            return []


numCourses = 2
prerequisites = [[1, 0]]
print Solution().findOrder(numCourses, prerequisites)
