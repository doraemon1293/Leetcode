from typing import List
import bisect
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        d=dict([(x,i) for i,x in enumerate(target)])
        arr=[d[ch] for ch in arr if ch in d]
        print(arr)
        B=[float("inf")]*len(arr)
        lis=[1]*len(arr)
        for i, num in enumerate(arr):
            x=bisect.bisect_left(B,num)
            B[x]=min(B[x],num)
            lis[i]=x+1
        return len(target)-max(lis)



print(Solution().minOperations(target = [5,1,3], arr = [9,4,2,3,4]))