import functools
from typing import List


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        @functools.lru_cache(None)
        def comb(x, y):
            if x == 0 or y == 0:
                return 1
            if x == y:
                return 1
            if x<y:
                return 0
            return comb(x - 1, y - 1) + comb(x - 1, y)

        def f(x, y, k):
            print(x,y,k,comb(x + y - 1, x - 1))
            if k > comb(x + y - 1, x - 1):
                return "V" + f(x, y - 1, k - comb(x + y - 1, x - 1))
            elif k==comb(x + y - 1, x - 1):
                return "H"+"V"*y+"H"*(x-1)
            else:
                return "H" + f(x - 1, y, k)

        y, x = destination
        ans = f(x, y, k)
        return ans