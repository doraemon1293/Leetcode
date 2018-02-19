# coding=utf-8
'''
Created on 2017å¹?8æœ?6æ—?

@author: Administrator
'''


class Solution(object):

    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        if A[-1] == -1: return []

        N = len(A)
        paths = [[] for _ in xrange(N)]
        costs = [float("Inf")] * N
        paths[-1] = [[N]]
        costs[-1] = 0
        for i in xrange(N - 1, -1, -1):
            if A[i] != -1:
                for j in xrange(i + 1, min(i + B + 1, N)):
                    if costs[i] > A[i] + costs[j]:
                        costs[i] = A[i] + costs[j]
                        paths[i] = [[i + 1] + path for path in paths[j]]
                    elif costs[i] == A[i] + costs[j]:
                        for path in paths[j]:
                            paths.append([i + 1] + path)

        def myCmp(a1, a2):
            l1, l2 = len(a1), len(a2)
            for i in xrange(min(l1, l2)):
                if a1[i] < a2[i]:
                    return -1
                elif a1[i] > a2[i]:
                    return 1
            if l1 < l2:
                return -1
            elif l1 == l1:
                return 0
            else:
                return 1

        ans = sorted(paths[0])
        if ans == []:
            return []
        else:
            return ans[0]


A = [1, 2, 4, -1, 2]
B = 1
print Solution().cheapestJump(A, B)
