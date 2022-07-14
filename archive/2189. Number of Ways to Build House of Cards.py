import functools


class Solution:
    def houseOfCards(self, n: int) -> int:
        @functools.lru_cache(None)
        def foo(n, k):  # n card left below row has k triangle
            if n == 0 and k > 0:
                return 1
            res = 0
            for k1 in range(1,k):
                if n-(3*k1-1)>=0:
                    res += foo(n - (3*k1-1), k1)
                else:
                    break
            return res

        ans = 0
        for k in range(1,n):
            if 3*k-1>n:
                break
            ans += foo(n-(3*k-1), k)
        return ans
n=500
print(Solution().houseOfCards(n))