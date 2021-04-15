from typing import List
import heapq
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N=len(nums)
        heap=[(-nums[0],0)]
        summ=nums[0]
        for i in range(1,N):
            while heap[0][1]<i-k:
                heapq.heappop(heap)
            temp,ind,=heap[0]
            temp=-temp
            summ=temp+nums[i]
            heapq.heappush(heap,(-summ,i))
        return summ