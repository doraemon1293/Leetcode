from typing import List
import collections


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        dp = collections.defaultdict(set)
        dp[0] = set([tuple([0] * n)])
        ans=0
        for req in requests:
            s, t = req
            new_dp=collections.defaultdict(set)
            for reqs in dp:
                new_dp[reqs]|=dp[reqs]
                for state in dp[reqs]:
                    new_state=list(state)
                    new_state[s]-=1
                    new_state[t]+=1
                    new_state=tuple(new_state)
                    if all([x==0 for x in new_state]):
                        ans=max(ans,reqs+1)
                    new_dp[reqs+1].add(new_state)
            dp=new_dp
        return ans
