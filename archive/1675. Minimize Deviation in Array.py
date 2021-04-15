import heapq
from typing import List
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap=[]
        for num in nums:
            if num%2:
                heap.append((num,num*2))
            else:
                temp=num
                while temp%2==0:
                    temp//=2
                heap.append((temp,num))
        heapq.heapify(heap)
        mini=min(x[0] for x in heap)
        maxi=max(x[0] for x in heap)
        ans=maxi-mini
        while heap[0][0]<heap[0][1]:
            num,max_num=heapq.heappop(heap)
            maxi=max(maxi,num*2)
            heapq.heappush(heap,num*2)
            mini=heap[0][0]
            ans=min(maxi-mini)
        return ans


print(Solution().minimumDeviation(nums = [1,2,3,4]))
print(Solution().minimumDeviation(nums = [3,5]))