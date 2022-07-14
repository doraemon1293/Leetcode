import heapq
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            x=heapq.heappop(nums)
            heapq.heappush(nums,x+1)
        res=1
        MOD=10**9 + 7
        for num in nums:
            res=(res*num)%MOD
        return res
