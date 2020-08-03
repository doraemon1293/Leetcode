from typing import List
import collections


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        c = collections.Counter([x % k for x in arr])
        if c.get(0,0)%2==1:
            return False
        for i in range(1, k // 2):
            if c.get(i, 0) != c.get(k - i, 0):
                return False
        return True
