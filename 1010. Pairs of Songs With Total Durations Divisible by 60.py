from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d=defaultdict(int)
        for t in time:
            d[t%60]+=1
        ans=0
        for k in d:
            if 0<k<30:
                ans+=d[k]*d[60-k]
            else:
                ans+=(d[k]*d[k]-1)//2
        return ans

