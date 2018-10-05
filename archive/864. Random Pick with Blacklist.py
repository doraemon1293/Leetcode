import random


class Solution:

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.blacklist = sorted(blacklist)
        self.N = N

    def pick(self):
        """
        :rtype: int
        """
        k = random.randint(0, self.N - 1 - len(self.blacklist))
        lo, hi = 0, len(self.blacklist) - 1
        while lo < hi:
            mid = (lo + hi+1) // 2
            if self.blacklist[mid] - mid > k:
                hi = mid - 1
            else:
                lo = mid
        if lo == hi and self.blacklist[lo] - lo <= k:
            return k + lo + 1
        else:
            return k