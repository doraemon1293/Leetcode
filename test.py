import heapq
from typing import List


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        max_sum = sum([num for num in nums if num >= 0])
        abs_nums = sorted(abs(num) for num in nums)[:k]
        max_heap = [(-max_sum,-1)]
        while k>1:
            pre_sum,i=heapq.heappop(max_heap)
            pre_sum=-pre_sum


        for num in abs_nums:
            for pre_sum in heap[:]:
                new_sum = pre_sum - num
                if len(heap) == k:
                    if new_sum > heap[0]:
                        heapq.heappushpop(heap, new_sum)
                else:
                    heapq.heappush(heap, new_sum)

        # print(len(heap))
        return heap[0]