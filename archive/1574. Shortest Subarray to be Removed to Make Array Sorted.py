from typing import List
import bisect
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N=len(arr)
        left=0
        for i in range(1,N):
            if arr[i]>=arr[i-1]:
                left=i
            else:
                break
        if left==N-1:
            return 0
        right=N-1
        for i in range(N-2,-1,-1):
            if arr[i]<=arr[i+1]:
                right=i
            else:
                break
        ans=max(left,N-right)
        for i in range(left+1):
            ind=bisect.bisect_left(arr,arr[i],right,N)
            ans=max(ans,N-ind+(i+1))
        # print(ind)
        return N-ans