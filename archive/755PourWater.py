# coding=utf-8
'''
Created on 8 Jan 2018

@author: Administrator
'''


class Solution:

    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        for _ in range(V):
            left = ind = K
            # left
            while left - 1 >= 0 and heights[left - 1] <= heights[left]:
                if heights[left - 1] < heights[left]:
                    ind = left - 1
                left -= 1
            if ind != K:
                heights[ind] += 1
            else:
                right = ind = K
            # left
                while right + 1 < len(heights) and heights[right + 1] <= heights[right]:
                    if heights[right + 1] < heights[right]:
                        ind = right + 1
                    right += 1
                if ind != K:
                    heights[ind] += 1
                else:
                    heights[K] += 1
        return heights


heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]
V = 5
K = 5
print(Solution().pourWater(heights, V, K))
