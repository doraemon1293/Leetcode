# coding=utf-8
'''
Created on 16 Jan 2018

@author: Administrator
'''


class Solution:

    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        d = {}
        for i, x in enumerate(row):
            d[x] = i
        ans = 0
        for i in range(0, len(row), 2):
            target = (row[i] + 1) if row[i] % 2 == 0 else (row[i] - 1)
            ind = d[target]
            if ind != i + 1:
                d[target] = i + 1
                d[row[i + 1]] = ind
                row[i + 1], row[ind] = row[ind], row[i + 1]
                ans += 1
        return ans


row = [5, 4, 2, 6, 3, 1, 0, 7]
print(Solution().minSwapsCouples(row))
