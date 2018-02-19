# coding=utf-8
'''
Created on 2016å¹?12æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def find_kth_least_number(nums1, nums2, s1, e1, s2, e2, k):

            if len(nums1) == 0:
                return nums2[k - 1]
            if len(nums2) == 0:
                return nums1[k - 1]
            if k == 1:
                return min(nums1[s1] if s1 < len(nums1) else float("inf"), nums2[s2] if s2 < len(nums2) else float("inf"))
            if s1 == e1:
                if nums1[s1] < (nums2[s2 + k - 1] if s2 + k - 1 < len(nums2) else float("inf")):
                    return max(nums2[s2 + k - 2], nums1[s1])
                else:
                    return nums2[s2 + k - 1]
            if s2 == e2:
                if nums2[s2] < (nums1[s1 + k - 1] if s1 + k - 1 < len(nums1) else float("inf")):
                    return max(nums1[s1 + k - 2], nums2[s2])
                else:
                    return nums1[s1 + k - 1]
            mid1 = (s1 + e1) / 2
            l1 = (mid1 - s1) + 1
            mid2 = (s2 + e2) / 2
            l2 = (mid2 - s2) + 1
            if nums1[mid1] <= nums2[mid2]:
                if l1 + l2 >= k:
                    return find_kth_least_number(nums1, nums2, s1, e1, s2, mid2, k)
                else:
                    return find_kth_least_number(nums1, nums2, mid1 + 1, e1, s2, e2, k - l1)
            else:
                if l1 + l2 >= k:
                    return find_kth_least_number(nums1, nums2, s1, mid1, s2, e2, k)
                else:
                    return find_kth_least_number(nums1, nums2, s1, e1, mid2 + 1, e2, k - l2)

        if (len(nums1) + len(nums2)) % 2 == 0:
            a = find_kth_least_number(nums1, nums2, 0, len(nums1) - 1, 0, len(nums2) - 1, (len(nums1) + len(nums2)) / 2)
            b = find_kth_least_number(nums1, nums2, 0, len(nums1) - 1, 0, len(nums2) - 1, (len(nums1) + len(nums2)) / 2 + 1)
            return float(a + b) / 2
        else:
            return find_kth_least_number(nums1, nums2, 0, len(nums1) - 1, 0, len(nums2) - 1, (len(nums1) + len(nums2)) / 2 + 1)


nums1 = [3]
nums2 = [2]
print Solution().findMedianSortedArrays(nums1, nums2)

