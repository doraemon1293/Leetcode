from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans=sum([piles[-2-x*2] for x in range(len(piles)//3)])
        return ans