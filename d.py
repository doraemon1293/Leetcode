import heapq
from typing import List


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        max_sum = sum([num for num in nums if num>=0])
        abs_nums=sorted(abs(num) for num in nums)[:k]
        max_heap = [max_sum]
        for num in abs_nums:
            for pre_sum in heap[:]:
                new_sum = pre_sum - num
                heapq.heappush(heap, new_sum)
                while len(heap) > k:
                    x = heapq.heappop(heap)
                    # print("x=", x)

        # print(len(heap))
        return heap[0]

nums=[-347135403,-741775723,349271195,967839234,822470265,-545249891,293401682,908306445,296832265,9392523,-84929173,-784997375,699878100,291656873,-910458294,547370160,584504507,977373244,-963031162,819184328]
k=473
print((Solution().kSum(nums,k)))

