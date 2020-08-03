class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty=0
        while numBottles:
            empty+=numBottles
            numBottles=empty//3
            ans += numBottles
        return ans
