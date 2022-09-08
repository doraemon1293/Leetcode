import collections
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        pre_sum = [0]
        for t in travel:
            pre_sum.append(pre_sum[-1] + t)
        m = []
        p = []
        g = []
        for i, s in enumerate(garbage):
            s = collections.Counter(s)
            for ch in s:
                if ch=='M':
                    m.append((i, s[ch]))
                if ch=='P':
                    p.append((i, s[ch]))
                if ch=='G':
                    g.append((i, s[ch]))
        ans = 0

        for arr in (m, p, g):
            # print(arr)
            cur = 0
            for x, y in arr:
                ans += pre_sum[x] - pre_sum[cur]
                ans += y
                cur = x
        return ans
