import heapq
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        buy_orders = []  # max heaap
        sell_orders = []  # min heap
        # ans=0
        for price, amount, orderType in orders:
            if orderType == 0:
                while sell_orders and price >= sell_orders[0][0] and amount:
                    sell_price, sell_amount = heapq.heappop(sell_orders)
                    if amount <= sell_amount:
                        sell_amount -= amount
                        # ans += amount
                        amount = 0
                        # ans %= MOD
                        if sell_amount:
                            heapq.heappush(sell_orders, (sell_price, sell_amount))
                    else:
                        amount -= sell_amount
                        # ans+=sell_amount
                        # ans%=MOD
                if amount:
                    heapq.heappush(buy_orders, (-price, amount))

            if orderType == 1:
                while buy_orders and price <= -buy_orders[0][0] and amount:
                    buy_price, buy_amount = heapq.heappop(buy_orders)
                    if amount <= buy_amount:
                        buy_amount -= amount
                        # ans+=amount
                        # ans%=MOD
                        amount=0
                        if buy_amount:
                            heapq.heappush(buy_orders, (buy_price, buy_amount))
                    else:
                        amount -= buy_amount
                        # ans+=buy_amount
                        # ans%=MOD
                if amount:
                    heapq.heappush(sell_orders, (price, amount))
        return sum([x[1] for x in buy_orders + sell_orders]) % MOD


print(Solution().getNumberOfBacklogOrders([[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]))
print(Solution().getNumberOfBacklogOrders([[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]))
