from typing import List
import bisect


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        ans = 0
        MOD = 10 ** 9 + 7
        N = len(nums)
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)
        print(pre)
        for i in range(1, N):
            # i+1,N
            x = max(bisect.bisect_left(pre, pre[i] * 2), i + 1)
            y = min(bisect.bisect_right(pre, (pre[N] + pre[i]) / 2), N)
            if y >= x:
                ans += y - x
        return ans % MOD


print(Solution().waysToSplit(nums=[1, 2, 2, 2, 5, 0]))
