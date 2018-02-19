# coding=utf-8
'''
Created on 2017å¹?3æœ?3æ—?

@author: Administrator
'''


class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()

        def dfs(candidates, st, target, seq):
            for i in xrange(st, len(candidates)):
                if candidates[i] == target:
                    ans.append(seq + [candidates[i]])
                elif candidates[i] < target:
                    dfs(candidates, i, target - candidates[i], seq + [candidates[i]])
                else:
                    break

        dfs(candidates, 0, target, [])
        return ans


candidates = [2, 3, 6, 7]
target = 7
print Solution().combinationSum(candidates, target)
