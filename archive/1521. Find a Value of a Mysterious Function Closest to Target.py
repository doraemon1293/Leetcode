from typing import List


class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        dp=set()
        ans = float("inf")
        for i in range(len(arr)):
            dp = set([x & arr[i] for x in dp]) | {arr[i]}
            for x in dp:
                ans = min(ans, abs(target - x))
        return ans


arr = [9, 12, 3, 7, 15]
target = 5

print(Solution().closestToTarget(arr,target))