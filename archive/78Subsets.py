# coding=utf-8
'''
Created on 2017å¹?5æœ?31æ—?

@author: Administrator
'''


class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from collections import Counter
        counter = Counter(nums)
        distinct_nums = sorted(counter.keys())
        self.ans = []

        def dfs(cur, st):
            self.ans.append(cur)
            # print cur

            for i in range(st + 1, len(distinct_nums)):
                for k in range(1, counter[distinct_nums[i]] + 1):
                    dfs(cur + [distinct_nums[i]] * k, i)

        dfs([], -1)
        self.ans = map(lambda x:list(x), self.ans)
        return self.ans


nums = [1, 2, 2, 2, 3, 3]
print Solution().subsets(nums)

