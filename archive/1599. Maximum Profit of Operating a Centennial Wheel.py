from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        rotate = 0
        profit = 0
        maxi_profit = 0
        maxi_profit_rotate=-1
        while True:
            if rotate < len(customers):
                waiting += customers[rotate]
            rotate += 1
            ppl = min(4, waiting)
            waiting -= ppl
            profit += boardingCost * ppl - runningCost
            if profit>maxi_profit:
                maxi_profit = profit
                maxi_profit_rotate=rotate
            if waiting==0 and rotate >= len(customers):
                break

        return maxi_profit_rotate if maxi_profit else -1