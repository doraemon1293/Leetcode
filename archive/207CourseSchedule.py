# coding=utf-8
'''
Created on 2017å¹?8æœ?30æ—?

@author: Administrator
'''


class Solution(object):

    def canFinish(self, numCourses, prerequisites):
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
        learnt = 0
        while zeroDegrees:
            learnt += 1
            v0 = zeroDegrees.popleft()
            for v1 in edges[v0]:
                indegrees[v1] -= 1
                if indegrees[v1] == 0:
                    zeroDegrees.append(v1)
        if learnt == numCourses:
            return True
        else:
            return False


numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print Solution().canFinish(numCourses, prerequisites)

