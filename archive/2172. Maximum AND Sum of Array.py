from typing import List
import collections


class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        dp = collections.defaultdict(int)
        dp[0] = 0
        for num in nums:
            new_dp = collections.defaultdict(int)
            for bit in dp:
                for i in range(1, numSlots + 1):
                    temp = (bit >> (2 * (i - 1))) & 3
                    if temp == 0:
                        new_bit = bit | (1 << (2 * (i - 1)))
                        new_dp[new_bit] = max(new_dp[new_bit], dp[bit] + (i & num))
                    if temp == 1:
                        new_bit = bit | (3 << (2 * (i - 1)))
                        new_dp[new_bit] = max(new_dp[new_bit], dp[bit] + (i & num))

            dp = new_dp
            # print(dp, num)
        return max(new_dp.values())