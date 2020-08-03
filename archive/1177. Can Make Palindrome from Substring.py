import copy
import collections


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        counters = [{}]
        d = collections.defaultdict(int)
        for i in range(len(s)):
            d[s[i]] += 1
            counters.append(copy.copy(d))

        def sub(d1, d2):
            return dict([(k, d1[k] - d2.get(k, 0)) for k in d1])
        ans=[]
        for query in queries:
            l, r, k = query
            counter = sub(counters[r + 1], counter[l])
            odd=len([v for v in counter.values() if v%2==1])
            if odd//2>k:
                ans.append(False)
            else:
                ans.append(True)
        return ans
