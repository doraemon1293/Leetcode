from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        memo = {}

        def solve(st, end):
            # print(st, end)
            if (st, end) in memo:
                return memo[st, end]
            res = float("inf")
            for cut in cuts:
                if st < cut < end:
                    temp = (end - st) + solve(st, cut) + solve(cut, end)
                    res = min(res, temp)
            if res == float("inf"):
                res = 0
            memo[st, end] = res
            return res

        return solve(0, n)
