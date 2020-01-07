import math


class Solution:
    def minimizeError(self, prices: list, target: int) -> str:
        arr = []
        ce_sub_fe = []
        sum_fe = 0
        for price in prices:
            price = float(price)
            if math.floor(price) == price:
                target -= price
            else:
                arr.append(price)
                ce_sub_fe.append(abs(math.ceil(price) - price) - abs(math.floor(price) - price))
                sum_fe += abs(math.floor(price) - price)
                target-=math.floor(price)
        print(target)
        print(sum_fe)
        target=int(target)
        if target < 0:
            return "-1"
        elif target>len(ce_sub_fe):
            return "-1"
        elif target == 0:
            return str("{:.3f}".format(sum_fe))
        else:
            ce_sub_fe.sort()
            target = int(target)
            return str("{:.3f}".format(sum_fe + sum(ce_sub_fe[:target])))


prices = ["0.700", "2.800", "4.900"]
target = 8
prices = ["1.500","2.500","3.500"]
target = 10
print(Solution().minimizeError(prices, target))
