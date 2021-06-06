import functools
import sys


class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        sys.setrecursionlimit(10000)

        @functools.lru_cache(None)
        def foo(n, k):
            if n == k:
                return 1
            if k == 0:
                return 0
            return (foo(n - 1, k - 1) + (n - 1) * foo(n - 1, k)) % MOD  # longest at last

        return foo(n, k)