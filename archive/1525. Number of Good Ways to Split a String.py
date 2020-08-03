import collections


class Solution:
    def numSplits(self, s: str) -> int:
        c1 = collections.defaultdict(int)
        c2 = collections.Counter(s)
        ans = 0
        for ch in s:
            c1[ch] += 1
            c2[ch] -= 1
            if c2[ch] == 0:
                del c2[ch]
            if len(c1) == len(c2):
                ans += 1
        return ans
