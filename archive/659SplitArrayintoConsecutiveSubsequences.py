# coding=utf-8
'''
Created on 2017å¹?8æœ?13æ—?

@author: Administrator
'''


class Solution(object):

    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3: return False
        import bisect
        from collections import defaultdict, deque
        tails = defaultdict(list)
        tails[nums[0]].append(1)
        for num in nums[1:]:
            if num - 1 in tails:
                length = tails[num - 1][0] + 1
                del tails[num - 1][0]
                if len(tails[num - 1]) == 0: del tails[num - 1]
                bisect.insort(tails[num], length)
            elif num in tails:
                bisect.insort(tails[num], 1)
            else:
                for key in tails.keys():
                    if tails[key][0] < 3:
                        return False
                    else:
                        del tails[key]
                bisect.insort(tails[num], 1)
        for key in tails.keys():
            if tails[key][0] < 3:
                return False
        return True


nums = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
print Solution().isPossible(nums)
