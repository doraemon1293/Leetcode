import collections
from typing import List
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD=10**9+7
        counter=collections.Counter(inventory)
        counter[0]=0
        keys=collections.deque(sorted(counter.keys(),reverse=True))
        keys.append(0)
        values=0
        while orders:
            k0,k1=keys[0],keys[1]
            if orders>=(k0-k1)*counter[k0]:
                values=(values+(k1+1+k0)*(k0-k1)//2*counter[k0])%MOD
                orders-=(k0-k1)*counter[k0]
                counter[k1]+=counter[k0]
                del counter[k0]
                keys.popleft()
            else:
                div=orders//counter[k0]
                remain=orders%counter[k0]
                values = (values + (k0 + (k0 - div + 1)) * div// 2*counter[k0]) % MOD
                values=(values+(k0-div)*remain)%MOD
                orders=0
            #     print(div,remain)
            # print(k0,k1,counter,keys,values,orders)
        return values