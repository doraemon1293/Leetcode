# coding=utf-8
'''
Created on 2017å¹?6æœ?16æ—?

@author: Administrator
'''


class Solution(object):

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [1] * len(ratings)
        for x in xrange(0, len(ratings) - 1):
            if ratings[x] < ratings[x + 1]:
                candies[x + 1] = candies[x] + 1
        print candies
        for x in xrange(len(ratings) - 1, 0, -1):
            if ratings[x - 1] > ratings[x]:
                candies[x - 1] = max(candies[x - 1], candies[x] + 1)
        print candies
        return sum(candies)


ratings = [1, 2, 3, 5, 4, 6]

print Solution().candy(ratings)

