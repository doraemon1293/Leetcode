# coding=utf-8
'''
Created on 2017å¹?8æœ?17æ—?

@author: Administrator
'''
from _collections import defaultdict


class Solution(object):

    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """

        indegree = defaultdict(int)
        edge = defaultdict(set)
        n = 0
        ans = []
        for seq in seqs:
            if len(seq) == 1:
                if seq[0] < 1:
                    return False
                n = max(n, seq[0])
            for i in xrange(len(seq) - 1):
                if seq[i] < 1 or seq[i + 1] < 1:
                    return False
                if seq[i + 1] not in edge[seq[i]]:
                    edge[seq[i]].add(seq[i + 1])
                    indegree[seq[i + 1]] += 1
                n = max(n, seq[i], seq[i + 1])
        print edge
        print n
        checkingVertex = xrange(1, n + 1)
        while len(ans) < n:
            zeroIndegree = 0
            for i in checkingVertex:
                if indegree[i] == 0:
                    zeroIndegree += 1
                    u = i
                    if zeroIndegree > 1:
                        break
            if zeroIndegree == 1:
                checkingVertex = set()
                for v in edge[u]:
                    checkingVertex.add(v)
                    indegree[v] -= 1
                ans.append(u)
            else:
                return False
        return ans == org
# org = [4, 1, 5, 2, 6, 3]
# seqs = [[5, 2, 6, 3], [4, 1, 5, 2]]
# org = [1]
# seqs = [[1]]


org = [5, 3, 2, 4, 1]
seqs = [[5, 3, 2, 4], [4, 1], [1], [3], [2, 4], [1000000000]]

print Solution().sequenceReconstruction(org, seqs)
