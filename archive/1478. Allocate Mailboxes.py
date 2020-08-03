from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        memo = {}
        memo_foo = {}

        def foo(left, right):
            if (left, right) in memo_foo:
                return memo_foo[left, right]
            else:
                median = houses[left + (right - left) // 2]
                memo_foo[left, right] = sum([abs(houses[i] - median) for i in range(left, right + 1)])
                return memo_foo[left, right]

        def dp(left, right, k):
            if k == 1:
                return foo(left, right)
            if (left, right, k) in memo:
                return memo[left, right, k]
            res = float("inf")
            for r in range(left, right - k+2):
                res = min(res, foo(left, r) + dp(r + 1, right, k - 1))
            memo[left, right, k] = res
            return res

        return dp(0, len(houses)-1, k)
        # print(memo_foo)
        # print(memo)
        # return memo[0, len(houses)-1, k]


houses = [1, 4, 8, 10, 20]
k = 5
houses=[7,4,6,1]
k = 1
houses = [2,3,5,12,18]
k = 2
print(Solution().minDistance(houses, k))
