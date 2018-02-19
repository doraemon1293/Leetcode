# coding=utf-8
'''
Created on 2017å¹?7æœ?28æ—?

@author: Administrator
'''


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        def find_min_idx(nums):
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                if nums[lo] < nums[hi]:
                    return lo
                mid = (lo + hi) / 2
                if nums[mid] < nums[hi]:
                    hi = mid
                elif nums[mid] > nums[hi]:
                    lo = mid + 1
                else:
                    if nums[lo] < nums[mid]:
                        lo = mid + 1
                    elif nums[lo] > nums[mid]:
                        hi = mid
                    else:
                        while lo <= mid and nums[lo] == nums[mid]:
                            lo += 1
            return lo

        min_idx = find_min_idx(nums)
        print min_idx

        def search(nums, s, e, target):
            while s <= e:
                mid = (s + e) / 2
                if target < nums[mid]:
                    e = mid - 1
                elif target > nums[mid]:
                    s = mid + 1
                else:
                    return mid
            return None

        ans = search(nums, 0, min_idx - 1, target)
        if ans != None: return True
        ans = search(nums, min_idx, len(nums) - 1, target)
        if ans != None:
            return True
        else:
            return False


nums = [1, 1, 1]
target = 1
print Solution().search(nums, target)
