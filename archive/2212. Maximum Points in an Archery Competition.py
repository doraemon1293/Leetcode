from typing import List
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        dp={0:0}
        path={0:[0]}
        for score in range(1,12):
            new_dp={0:0}
            new_path={0:[0]*(score+1)}
            for arrow in dp:
                if arrow not in new_dp or dp[arrow]>new_dp[arrow]:
                    new_dp[arrow]=dp[arrow]
                    new_path[arrow]=path[arrow]+[0]

                if arrow+aliceArrows[score]+1<=numArrows:
                    if arrow+aliceArrows[score]+1 not in new_dp or dp[arrow]+score>new_dp[arrow+aliceArrows[score]+1]:
                        new_dp[arrow+aliceArrows[score]+1]=dp[arrow]+score
                        new_path[arrow+aliceArrows[score]+1]=path[arrow]+[1]
            dp=new_dp
            path=new_path
        score=0
        final_path=[0]*12
        for k in dp:
            if dp[k]>score:
                score=dp[k]
                final_path=path[k]
        for i in range(1,12):
            final_path[i]=aliceArrows[i]+1 if final_path[i] else 0

        for i in range(11,-1,-1):
            if final_path[i]:
                final_path[i]=numArrows-(sum(final_path)-final_path[i])
                break


        return final_path


numArrows=9
aliceArrows=[1,1,0,1,0,0,2,1,0,1,2,0]
print(Solution().maximumBobPoints(numArrows,aliceArrows))