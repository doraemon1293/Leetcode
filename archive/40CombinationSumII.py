# coding=utf-8
'''
Created on 2017å¹?6æœ?8æ—?

@author: Administrator
'''


class Solution(object):

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = set()
        candidates.sort()

        def dfs(candidates, st, target, seq):
            for i in xrange(st + 1, len(candidates)):
                if candidates[i] == target:
                    ans.add(tuple(seq + [candidates[i]]))
                elif candidates[i] < target:
                    dfs(candidates, i, target - candidates[i], seq + [candidates[i]])
                else:
                    break

        dfs(candidates, -1, target, [])
        return [list(x) for x in ans]


candidates = [3, 1, 3, 5, 1, 1]
target = 8
print Solution().combinationSum2(candidates, target)
