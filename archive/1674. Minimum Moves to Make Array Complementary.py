import collections
from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        nums = [sorted([nums[i], nums[len(nums) - i - 1]]) for i in range(len(nums) // 2)]
        arr = collections.defaultdict(int)
        for a, b in nums:
            arr[a + 1] -= 1
            arr[a + b] -= 1
            arr[a + b + 1] += 1
            arr[b + limit + 1] += 1
        arr = sorted([(k, v) for k, v in arr.items()])
        ans = temp = 2 * len(nums)
        for _, inc in arr:
            temp += inc
            ans = min(ans, temp)
        return ans