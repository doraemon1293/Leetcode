from typing import List
import collections


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        temp1 = nums1[:]
        temp2 = nums2[:]

        nums1 = collections.Counter([num ** 2 for num in nums1])
        nums2 = collections.Counter(nums2)

        ans = 0

        # type1
        for x in nums1:
            for y in nums2:
                if x % y == 0:
                    z = x // y
                    if z in nums2:
                        if z >= y:
                            if z != y:
                                ans += nums1[x] * nums2[y] * nums2[z]
                            else:
                                ans += nums1[x] * nums2[y] * (nums2[z] - 1) // 2
        # type2
        nums1=temp1
        nums2 = temp2
        nums1 = collections.Counter(nums1)
        nums2 = collections.Counter([num ** 2 for num in nums2])
        for x in nums2:
            for y in nums1:
                if x % y == 0:
                    z = x // y
                    if z in nums1:
                        if z >= y:
                            if z != y:
                                ans += nums2[x] * nums1[y] * nums1[z]
                            else:
                                ans += nums2[x] * nums1[y] * (nums1[z] - 1) // 2

        return ans