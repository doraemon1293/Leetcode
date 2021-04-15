from typing import List
import bisect
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x:x[1])
        dp=[[(0,0)]]
        for tk in range(1,k+1):
            dp.append([(0,0)])
            for s,e,v in events:
                ind=bisect.bisect(dp[tk-1],(s-1,float("inf")))-1
                if dp[tk-1][ind][1]+v>dp[tk][-1][1]:
                    dp[tk].append((e,dp[tk-1][ind][1]+v))
            # print(dp[tk])
        return dp[k][-1][1]