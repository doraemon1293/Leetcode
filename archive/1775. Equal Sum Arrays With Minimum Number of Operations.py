from typing import List
import math
import collections
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1=sum(nums1)
        sum2=sum(nums2)
        d=collections.defaultdict(int)
        if sum1==sum2:
            return 0
        if sum1>sum2:
            larger=nums1
            smaller=nums2
        else:
            larger=nums2
            smaller=nums1
        for num in larger:
            d[num-1]+=1

        for num in smaller:
            d[6-num]+=1
        diff=abs(sum1-sum2)
        ans=0
        for k in range(5,0,-1):
            if d[k]*k>=diff:
                ans+=math.ceil(diff/k)
                return ans
            else:
                diff-=d[k]*k
                ans+=d[k]
        return -1
