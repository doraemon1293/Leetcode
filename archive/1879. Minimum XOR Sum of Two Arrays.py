from typing import List
import functools


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)

        @functools.lru_cache(None)
        def dp(mask, cur):  # mask[i]==0 => unused
            if cur == N:
                return 0
            res = float("inf")
            for i in range(N):
                if mask & (1 << i) == 0:
                    temp = (nums1[cur] ^ nums2[i]) + dp(mask | (1 << i), cur + 1)
                    res = min(temp, res)
            return res

        return dp(0, 0)


nums1 = [72,97,8,32,15]
nums2=[63,97,57,60,83]
print(Solution().minimumXORSum(nums1, nums2))
