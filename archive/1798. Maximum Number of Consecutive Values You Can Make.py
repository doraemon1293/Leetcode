from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        ans = 0
        for coin in coins:
            if coin <= ans + 1:
                ans += coin
            else:
                return ans + 1
        return ans + 1
