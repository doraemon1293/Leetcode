import bisect
from typing import List
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(v,m):
            last=position[0]
            m-=1
            while m:
                x=bisect.bisect_left(position,last+v)
                if x<len(position):
                    last=position[x]
                    m-=1
                else:
                    break
            print(v,m)
            return m==0

        lo,hi=1,position[-1]-position[0]
        while lo<=hi:
            mid=(lo+hi)//2
            print(lo,hi,mid)
            if check(mid,m):
                lo=mid+1
            else:
                hi=mid-1
        return hi


position = [1,2,3,4,7]
m = 3
# position = [5,4,3,2,1,1000000000]
# m = 2
print(Solution().maxDistance(position,m))
