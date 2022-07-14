from typing import List
import heapq


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        h1 = [-num for num in nums[:n]]  # maxheap
        heapq.heapify(h1)
        summ = -sum(h1)
        sum1 = {n - 1: summ}

        for i in range(n, 2 * n):
            top = -h1[0]
            if nums[i] < top:
                summ -= top
                summ += nums[i]
                heapq.heappop(h1)
                heapq.heappush(h1, -nums[i])
            sum1[i] = summ

        h2 = nums[-n:]
        heapq.heapify(h2)
        summ = sum(h2)
        sum2 = {2 * n: summ}
        for i in range(2 * n - 1, n - 1, -1):
            top = h2[0]
            if nums[i] > top:
                summ -= top
                summ += nums[i]
                heapq.heappop(h2)
                heapq.heappush(h2, nums[i])
            sum2[i] = summ
        ans = float("inf")
        for i in range(n - 1, 2 * n):
            ans = min(ans, sum1[i] - sum2[i + 1])
        return ans