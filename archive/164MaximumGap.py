# coding=utf-8
'''
Created on 2017å¹?9æœ?21æ—?

@author: Administrator
'''

import itertools
import random


class Solution(object):

    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # åŸºæ•°æ’åº
        max_len = max([len(str(num)) for num in nums] + [0])
        buckets = [[num] for num in nums]
        for ith in xrange(max_len):
            new_bucket = [[] for _ in xrange(10)]
            for bucket in buckets:
                for num in bucket:
                    digit = (num % (10 ** (ith + 1))) / (10 ** (ith))
                    new_bucket[digit].append(num)
            buckets = new_bucket
        ans = list(itertools.chain(*buckets))
        return max([abs(ans[i] - ans[i + 1]) for i in xrange(len(ans) - 1)] + [0])


a = range(10)
random.shuffle(a)
a = []
print Solution().maximumGap(a)

