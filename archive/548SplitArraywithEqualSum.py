# coding=utf-8
'''
Created on 2017å¹?7æœ?11æ—?

@author: Administrator
'''


class Solution(object):

    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # TLE
#         from collections import defaultdict
#         sum_ind = []
#         pinv = defaultdict(list)
#         summ = 0
#         for num in nums:
#             summ += num
#             sum_ind.append(summ)
#             pinv[summ].append(len(sum_ind) - 1)
#         for j in xrange(3, len(nums) - 3):
#             for k in xrange(j + 1, len(nums) - 1):
#                 if sum_ind[-1] - sum_ind[k] == sum_ind[k - 1] - sum_ind[j]:
#                     temp = sum_ind[-1] - sum_ind[k]
#                     if sum_ind[j - 1] - temp in pinv:
#                         for i in pinv[sum_ind[j - 1] - temp]:
#                             if i >= j - 1:
#                                 break
#                             if sum_ind[i - 1] == temp:
#                                 return True
#         return False

        from collections import defaultdict
        p = []
        pinv = defaultdict(list)
        summ = 0
        for num in nums:
            summ += num
            p.append(summ)
            pinv[summ].append(len(p) - 1)
        for j in xrange(3, len(nums) - 3):
            for k in xrange(j + 2, len(nums) - 1):
                for i in pinv[p[-1] - p[k]]:
                    if i >= j - 2: break
                    if p[i] == p[j - 1] - p[i + 1] == p[k - 1] - p[j] == p[-1] - p[k]:
                        return True
        return False


nums = [1, 2, 1, 2, 1, 2, 1]
print Solution().splitArray(nums)
