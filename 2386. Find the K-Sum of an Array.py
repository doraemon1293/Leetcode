import heapq
from typing import List


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        max_sum = sum([num for num in nums if num >= 0])
        abs_nums = sorted(abs(num) for num in nums)[:k]
        heap = [(-(max_sum - abs_nums[0]), 0)]
        ans = max_sum
        # print(ans)
        for _ in range(k - 1):
            summ, i = heapq.heappop(heap)
            summ = -summ
            if i + 1 < len(abs_nums):
               heapq.heappush(heap,(-(summ - abs_nums[i + 1]), i + 1))
               heapq.heappush(heap,(-(summ + abs_nums[i] - abs_nums[i + 1]), i + 1))
            ans = summ
            # print(ans)
        return ans

print(Solution().kSum([1,-2,3,4,-10,12],
16))