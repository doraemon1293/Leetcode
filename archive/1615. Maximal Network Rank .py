import collections
from  typing import List
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d=collections.defaultdict(int)
        roads=set([tuple(sorted(t)) for t in roads])
        for s,t in roads:
            d[s]+=1
            d[t]+=1
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                ans=max(ans,d[i]+d[j]-(1 if (i,j) in roads else 0))
        return ans




