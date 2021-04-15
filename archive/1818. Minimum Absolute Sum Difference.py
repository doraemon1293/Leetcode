import bisect
from typing import List
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        cur_sum=sum([abs(a-b) for a,b in zip(nums1,nums2)])
        sorted_nums1=sorted(nums1)
        maxi=0
        for a,b in zip(nums1,nums2):
            A=abs(a-b)
            ind=bisect.bisect_left(sorted_nums1,b)
            if ind==len(sorted_nums1):
                temp=A-abs(b-sorted_nums1[ind-1])
            elif ind==0:
                temp=A-abs(b-sorted_nums1[ind])
            else:
                temp=A-min(abs(b-sorted_nums1[ind-1]),abs(b-sorted_nums1[ind]))
            maxi=max(temp,maxi)
        return (cur_sum-maxi) % (10**9+7)


