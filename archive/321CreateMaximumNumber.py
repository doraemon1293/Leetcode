# coding=utf-8
'''
Created on 2017å¹?10æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        def pickNbitMaxNumber(nums, n):
            st = 0
            arr = []
            while n:
                end = len(nums) - n
                maxValue = -1
                maxInd = -1
                for i in xrange(st, end + 1):
                    if nums[i] > maxValue:
                        maxValue = nums[i]
                        maxInd = i
                arr.append(maxValue)
                st = maxInd + 1
                n -= 1
            return arr

        def merge(arr1, arr2):
            i = j = 0
            arr = []
            while i < len(arr1) and j < len(arr2):
                if arr1[i:] > arr2[j:]:
                    arr.append(arr1[i])
                    i += 1
                else:
                    arr.append(arr2[j])
                    j += 1
            arr.extend(arr1[i:])
            arr.extend(arr2[j:])
            return arr

        ans = [0]
        for k1 in xrange(min(k + 1, len(nums1) + 1)):
            k2 = k - k1
            if k2 <= len(nums2):
                arr1 = pickNbitMaxNumber(nums1, k1)
                arr2 = pickNbitMaxNumber(nums2, k2)
                arr = merge(arr1, arr2)
                if int("".join([str(x) for x in ans])) < int("".join([str(x) for x in arr])):
                    ans = arr
        return ans


nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
print Solution().maxNumber(nums1, nums2, k)

