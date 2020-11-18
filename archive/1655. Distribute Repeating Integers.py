from typing import List
import collections


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        dp = set([0])
        seq = sorted(collections.Counter(nums).values())
        d = collections.defaultdict(int)
        for b in range(1, 2 ** len(quantity)):
            for t in range(len(quantity)):
                if b >> t & 1:
                    d[b] += quantity[t]
        def foo(i):
            res = []
            for b in range(1, 2 ** len(quantity)):
                if d[b] <= seq[i]:
                    res.append(b)
            return res

        for i in range(len(seq)):
            res = foo(i)
            new_dp = set(dp)
            for status in dp:
                for new_status in res:
                    new_dp.add(new_status | status)
            # print(dp)
            # print(res)
            # print(new_dp)
            if 2 ** len(quantity) - 1 in new_dp:
                return True
            dp = new_dp
        return False


nums = [1, 2, 3, 3]
quantity = [2]
print(Solution().canDistribute(nums, quantity))
