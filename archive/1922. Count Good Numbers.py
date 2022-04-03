import functools


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = (n + 1) // 2
        odd = n // 2
        MOD = 10 ** 9 + 7
        @functools.lru_cache(None)
        def foo(x, y):
            if y == 1:
                return x
            elif y == 0:
                return 1
            else:
                return foo(x, y % 2) * (foo(x, y // 2) ** 2) % MOD

        return foo(5, even) * foo(4, odd) % MOD