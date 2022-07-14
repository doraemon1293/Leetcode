from typing import List
import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        half=sum(nums)/2
        nums=[-num for num in nums]
        heapq.heapify(nums)
        diff=0
        ans=0
        while diff<half:
            x=-heapq.heappop(nums)
            diff+=x/2
            heapq.heappush(nums,-x/2)
            ans+=1
            # print(diff)
            # print(nums)
        return ans




nums=[5,19,8,1]
print(Solution().halveArray(nums))